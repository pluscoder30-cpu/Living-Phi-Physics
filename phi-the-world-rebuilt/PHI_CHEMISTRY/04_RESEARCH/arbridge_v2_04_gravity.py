"""
Phi-Pentagram Gravity: Mean Reversion to Phi-Geometry
======================================================
Agent 4: Mean reversion trading based on deviations from phi-pentagram structure.

The pentagram is a MAP of where prices SHOULD be if the market were perfectly
phi-structured. When prices DEVIATE from the pentagram, there's a FORCE pulling
them back. This is like gravity -- the pentagram creates a gravitational field.

The trade is:
  - When price DEVIATES from a phi-level in the pentagram -> BUY (it will be pulled back)
  - When price RETURNS to the pentagram's expected position -> SELL (capture the reversion)

This is MEAN REVERSION TO PHI-GEOMETRY. Not mean reversion to a moving average --
mean reversion to the PHI-STRUCTURE of the market.
"""

import os, csv, sys, time, json
import numpy as np
from collections import defaultdict

PHI = 1.618033988749895
LOG_PHI = np.log(PHI)
TOL = 0.05
MAX_SPREAD = 2.5
MIN_PHI_GAPS = 3

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'phi_trading_research', '01_DATA', 'daily')


def load_all():
    files = [f for f in os.listdir(DATA_DIR) if f.endswith('_daily.csv')]
    all_data = {}
    all_dates = set()
    for fname in files:
        token = fname.replace('_daily.csv', '')
        td = {}
        with open(os.path.join(DATA_DIR, fname)) as fh:
            for row in csv.DictReader(fh):
                d = row['timestamp'][:10]
                td[d] = float(row['close'])
                all_dates.add(d)
        all_data[token] = td
    all_dates = sorted(all_dates)
    tokens = sorted(all_data.keys())
    date_idx = {d: i for i, d in enumerate(all_dates)}
    prices = np.full((len(all_dates), len(tokens)), np.nan)
    for j, tok in enumerate(tokens):
        for d, v in all_data[tok].items():
            prices[date_idx[d], j] = v
    return prices, tokens, all_dates


def find_phi_pentagram(prices_row, valid_mask, n_tokens, n_samples=8000):
    """Find the BEST phi-pentagram for a single day."""
    valid_idx = np.where(valid_mask)[0]
    if len(valid_idx) < 5:
        return None

    log_p = np.log(prices_row[valid_idx])
    rng = np.random.RandomState(42)
    best = None

    for _ in range(n_samples):
        idx5 = rng.choice(len(valid_idx), 5, replace=False)
        lp = np.sort(log_p[idx5])
        spread = lp[-1] - lp[0]
        if spread > MAX_SPREAD or spread < 0.1:
            continue

        gaps = np.diff(lp)
        nearest_ints = np.round(gaps / LOG_PHI).astype(int)
        expected = nearest_ints * LOG_PHI
        errors = np.abs(gaps - expected)
        mean_err = errors.mean()

        non_trivial = sum(1 for e in nearest_ints if abs(e) >= 1)
        if non_trivial < MIN_PHI_GAPS:
            continue
        if mean_err > TOL:
            continue

        prices = np.sort(prices_row[valid_idx][idx5])
        rog = np.sqrt(np.mean(prices ** 2))
        if rog <= 0:
            continue

        # Compute pentagram residual (geometry deviation)
        angles = 2 * np.pi * np.arange(5) / 5
        xs = prices * np.cos(angles)
        ys = prices * np.sin(angles)
        pcx, pcy = xs.mean(), ys.mean()

        def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
            denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if abs(denom) < 1e-15:
                return None
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
            return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))

        star_edges = [((k, (k + 2) % 5)) for k in range(5)]
        inner = []
        for k in range(5):
            a1, a2 = star_edges[k]
            b1, b2 = star_edges[(k + 1) % 5]
            pt = intersect(xs[a1], ys[a1], xs[a2], ys[a2],
                            xs[b1], ys[b1], xs[b2], ys[b2])
            if pt is not None:
                inner.append(pt)

        if len(inner) < 5:
            continue

        inner = np.array(inner)
        scx, scy = inner[:, 0].mean(), inner[:, 1].mean()
        dist = np.sqrt((scx - pcx) ** 2 + (scy - pcy) ** 2)
        residual_pct = dist / rog

        # Compute phi-levels (expected prices on the pentagram)
        phi_levels = prices  # The 5 vertex prices of the pentagram

        if best is None or residual_pct > best['residual_pct']:
            best = {
                'token_idx': valid_idx[idx5],
                'prices': prices,
                'mean_error': mean_err,
                'exponents': nearest_ints.tolist(),
                'residual_pct': residual_pct,
                'spread': spread,
                'non_trivial': non_trivial,
                'phi_levels': phi_levels,
                'log_phi_levels': lp,
            }

    return best


def compute_gravity_signal(prices_row, pentagram, token_idx):
    """
    Compute the gravity signal: how far price deviates from its phi-level.

    For each token in the pentagram:
      - Compute its current log price
      - Find its nearest phi-level (one of the 5 pentagram vertices)
      - The deviation = current - expected

    If deviation < 0: price is BELOW the phi-level -> BUY signal (will be pulled up)
    If deviation > 0: price is ABOVE the phi-level -> SELL signal (will be pulled down)

    The STRENGTH of the signal is proportional to the deviation magnitude.
    """
    if pentagram is None:
        return None

    signals = {}
    for i, tok_idx in enumerate(token_idx):
        current_log_price = np.log(prices_row[tok_idx])
        expected_log_price = pentagram['log_phi_levels'][i]
        deviation = current_log_price - expected_log_price

        # Convert to percentage deviation
        pct_deviation = (np.exp(deviation) - 1) * 100

        signals[tok_idx] = {
            'deviation': deviation,
            'pct_deviation': pct_deviation,
            'current_price': prices_row[tok_idx],
            'expected_price': pentagram['prices'][i],
            'phi_level': pentagram['log_phi_levels'][i],
        }

    return signals


def run_gravity_backtest(prices_arr, token_names, dates, n_days):
    """
    Run the phi-gravity mean reversion backtest.

    Strategy:
      - ENTRY: When price deviates > THRESHOLD from phi-level -> BUY
      - EXIT:  When price returns within TOLERANCE of phi-level -> SELL
      - STOP:  If price deviates > STOP_THRESHOLD (admit geometry is wrong)

    This captures the gravitational pull back to phi-structure.
    """
    print("\nPhase 2: Running phi-gravity backtest...", flush=True)

    # Strategy parameters
    ENTRY_THRESHOLD = 0.02    # 2% deviation triggers entry
    EXIT_TOLERANCE = 0.005    # 0.5% from phi-level triggers exit
    STOP_THRESHOLD = 0.08     # 8% deviation = stop loss
    HOLD_DAYS_MAX = 20        # Max hold period
    FEE_RATE = 0.001          # 0.1% taker
    SLIPPAGE = 0.003          # 30 bps

    trades = []
    positions = {}  # token_idx -> entry info

    daily_pentagrams = []

    for d in range(n_days):
        row = prices_arr[d]
        valid = np.isfinite(row) & (row > 0)

        if valid.sum() < 5:
            daily_pentagrams.append(None)
            continue

        pentagram = find_phi_pentagram(row, valid, len(token_names), n_samples=4000)
        daily_pentagrams.append(pentagram)

        if pentagram is None:
            continue

        # Get gravity signals for this day
        signals = compute_gravity_signal(row, pentagram, pentagram['token_idx'])

        # Check existing positions for exit conditions
        exited_tokens = []
        for tok_idx, pos in list(positions.items()):
            if tok_idx not in signals:
                continue

            sig = signals[tok_idx]
            days_held = d - pos['entry_day']

            # EXIT conditions:
            # 1. Price returned to phi-level (profitable exit)
            # 2. Stop loss hit (price deviated too far)
            # 3. Max hold period reached

            exit_reason = None
            if abs(sig['deviation']) < EXIT_TOLERANCE:
                exit_reason = 'phi_return'
            elif sig['deviation'] < -STOP_THRESHOLD and pos['direction'] == 'long':
                exit_reason = 'stop_loss'
            elif sig['deviation'] > STOP_THRESHOLD and pos['direction'] == 'short':
                exit_reason = 'stop_loss'
            elif days_held >= HOLD_DAYS_MAX:
                exit_reason = 'max_hold'

            if exit_reason:
                # Compute P&L
                if pos['direction'] == 'long':
                    exit_price = sig['current_price']
                    ret = (exit_price / pos['entry_price'] - 1)
                else:
                    exit_price = sig['current_price']
                    ret = (pos['entry_price'] / exit_price - 1)

                # Apply fees
                net_ret = ret - 2 * (FEE_RATE + SLIPPAGE)

                trades.append({
                    'entry_date': pos['entry_date'],
                    'exit_date': dates[d],
                    'token': token_names[tok_idx],
                    'direction': pos['direction'],
                    'entry_price': pos['entry_price'],
                    'exit_price': exit_price,
                    'gross_return': ret,
                    'net_return': net_ret,
                    'hold_days': days_held,
                    'exit_reason': exit_reason,
                    'entry_deviation': pos['entry_deviation'],
                })

                exited_tokens.append(tok_idx)

        for tok_idx in exited_tokens:
            del positions[tok_idx]

        # Check for new entry conditions
        for tok_idx, sig in signals.items():
            if tok_idx in positions:
                continue  # Already in a position

            # ENTRY: price deviates significantly from phi-level
            if sig['deviation'] < -ENTRY_THRESHOLD:
                # Price is BELOW phi-level -> BUY (expect pull up)
                positions[tok_idx] = {
                    'entry_date': dates[d],
                    'entry_price': sig['current_price'],
                    'entry_deviation': sig['deviation'],
                    'direction': 'long',
                    'entry_day': d,
                }
            elif sig['deviation'] > ENTRY_THRESHOLD:
                # Price is ABOVE phi-level -> SELL (expect pull down)
                positions[tok_idx] = {
                    'entry_date': dates[d],
                    'entry_price': sig['current_price'],
                    'entry_deviation': sig['deviation'],
                    'direction': 'short',
                    'entry_day': d,
                }

        if (d + 1) % 100 == 0 or d == n_days - 1:
            found = sum(1 for p in daily_pentagrams if p is not None)
            print(f"  Day {d+1}/{n_days}: {found} pentagrams, {len(trades)} trades, {len(positions)} open", flush=True)

    # Close any remaining positions at last available price
    last_row = prices_arr[-1]
    for tok_idx, pos in list(positions.items()):
        if np.isfinite(last_row[tok_idx]):
            exit_price = last_row[tok_idx]
            if pos['direction'] == 'long':
                ret = (exit_price / pos['entry_price'] - 1)
            else:
                ret = (pos['entry_price'] / exit_price - 1)
            net_ret = ret - 2 * (FEE_RATE + SLIPPAGE)
            trades.append({
                'entry_date': pos['entry_date'],
                'exit_date': dates[-1],
                'token': token_names[tok_idx],
                'direction': pos['direction'],
                'entry_price': pos['entry_price'],
                'exit_price': exit_price,
                'gross_return': ret,
                'net_return': net_ret,
                'hold_days': n_days - 1 - pos['entry_day'],
                'exit_reason': 'end_of_data',
                'entry_deviation': pos['entry_deviation'],
            })

    return trades, daily_pentagrams


def analyze_trades(trades):
    """Compute comprehensive trade statistics."""
    if not trades:
        return {}

    # Filter out end_of_data trades for realistic analysis
    closed_trades = [t for t in trades if t['exit_reason'] != 'end_of_data']

    if not closed_trades:
        return {}

    returns = np.array([t['net_return'] for t in closed_trades])
    gross_returns = np.array([t['gross_return'] for t in closed_trades])
    hold_days = np.array([t['hold_days'] for t in closed_trades])

    wins = returns > 0
    losses = returns < 0

    stats = {
        'n_trades': len(closed_trades),
        'n_total': len(trades),
        'n_open': len(trades) - len(closed_trades),
        'win_rate': np.mean(wins) * 100,
        'avg_return': np.mean(returns) * 100,
        'median_return': np.median(returns) * 100,
        'avg_gross_return': np.mean(gross_returns) * 100,
        'std_return': np.std(returns) * 100,
        'avg_win': np.mean(returns[wins]) * 100 if wins.any() else 0,
        'avg_loss': np.mean(returns[losses]) * 100 if losses.any() else 0,
        'profit_factor': abs(np.sum(returns[wins]) / np.sum(returns[losses])) if losses.any() and np.sum(returns[losses]) != 0 else float('inf'),
        'avg_hold_days': np.mean(hold_days),
        'median_hold_days': np.median(hold_days),
        'total_return': np.prod(1 + returns) - 1,
        'long_trades': sum(1 for t in closed_trades if t['direction'] == 'long'),
        'short_trades': sum(1 for t in closed_trades if t['direction'] == 'short'),
    }

    # Sharpe ratio (annualized, assuming ~252 trading days)
    if len(returns) > 1 and np.std(returns) > 0:
        trades_per_year = len(returns) / (np.sum(hold_days) / 252) if np.sum(hold_days) > 0 else len(returns)
        stats['sharpe'] = np.mean(returns) / np.std(returns) * np.sqrt(min(trades_per_year, 252))
    else:
        stats['sharpe'] = 0

    # Win/loss analysis by exit reason
    exit_reasons = defaultdict(list)
    for t in closed_trades:
        exit_reasons[t['exit_reason']].append(t['net_return'])

    stats['by_exit_reason'] = {}
    for reason, rets in exit_reasons.items():
        rets = np.array(rets)
        stats['by_exit_reason'][reason] = {
            'count': len(rets),
            'avg_return': np.mean(rets) * 100,
            'win_rate': np.mean(rets > 0) * 100,
        }

    return stats


def run_monte_carlo(trades, dates, n_days, n_paths=5000, start_capital=5.0):
    """Run Monte Carlo simulation with realistic position sizing."""
    if not trades:
        return {
            'n_paths': n_paths, 'n_days': n_days,
            'final_mean': start_capital, 'final_median': start_capital,
            'final_std': 0, 'final_min': start_capital, 'final_max': start_capital,
            'final_p5': start_capital, 'final_p95': start_capital,
            'return_mean': 0, 'return_median': 0,
            'positive_paths': n_paths, 'positive_pct': 100,
            'sharpe': 0, 'max_drawdown': 0,
            'p_2m': 0,
        }

    returns = np.array([t['net_return'] for t in trades])

    # Build trade timeline
    date_to_idx = {d: i for i, d in enumerate(dates)}
    trade_days = []
    for t in trades:
        day_idx = date_to_idx.get(t['exit_date'], -1)
        if day_idx >= 0:
            trade_days.append(day_idx)

    if not trade_days:
        return {
            'n_paths': n_paths, 'n_days': n_days,
            'final_mean': start_capital, 'final_median': start_capital,
            'final_std': 0, 'final_min': start_capital, 'final_max': start_capital,
            'final_p5': start_capital, 'final_p95': start_capital,
            'return_mean': 0, 'return_median': 0,
            'positive_paths': n_paths, 'positive_pct': 100,
            'sharpe': 0, 'max_drawdown': 0,
            'p_2m': 0,
        }

    final_values = []
    all_paths = np.zeros((n_paths, n_days))

    # Fixed position size per trade (realistic: can't always deploy full capital)
    position_per_trade = 100.0  # $100 per trade, fixed

    for p in range(n_paths):
        capital = start_capital
        rng = np.random.RandomState(p)
        peak = capital
        max_dd = 0

        trade_idx = 0
        for d in range(n_days):
            # Check if any trade exits on this day
            while trade_idx < len(trade_days) and trade_days[trade_idx] == d:
                # Random trade return from the distribution
                ret = rng.choice(returns)
                # Fixed position size
                position = min(capital, position_per_trade)
                profit = position * ret
                capital += profit
                trade_idx += 1

            all_paths[p, d] = capital
            peak = max(peak, capital)
            if peak > 0:
                dd = (peak - capital) / peak
                max_dd = max(max_dd, dd)

            if capital <= 0:
                all_paths[p, d:] = 0
                break

        final_values.append(capital)

    final_arr = np.array(final_values)
    rets = (final_arr - start_capital) / start_capital

    # Sharpe ratio
    daily_rets = np.diff(all_paths, axis=1) / np.maximum(all_paths[:, :-1], 1e-10)
    avg_daily = np.mean(daily_rets)
    std_daily = np.std(daily_rets)
    sharpe = (avg_daily / std_daily * np.sqrt(365)) if std_daily > 0 else 0

    # P($2M)
    p_2m = np.mean(final_arr >= 2_000_000) * 100

    return {
        'n_paths': n_paths,
        'n_days': n_days,
        'final_mean': np.mean(final_arr),
        'final_median': np.median(final_arr),
        'final_std': np.std(final_arr),
        'final_min': np.min(final_arr),
        'final_max': np.max(final_arr),
        'final_p5': np.percentile(final_arr, 5),
        'final_p95': np.percentile(final_arr, 95),
        'return_mean': np.mean(rets),
        'return_median': np.median(rets),
        'positive_paths': np.sum(final_arr > start_capital),
        'positive_pct': np.sum(final_arr > start_capital) / n_paths * 100,
        'sharpe': sharpe,
        'max_drawdown': np.max([np.max((np.maximum.accumulate(all_paths[p]) - all_paths[p]) / np.maximum.accumulate(all_paths[p])) for p in range(n_paths)]),
        'p_2m': p_2m,
        'position_per_trade': position_per_trade,
    }


def build_report(n_days, trades, stats, mc_results, pentagrams_found):
    L = []
    w = L.append

    w("# Phi-Pentagram Gravity: Mean Reversion to Phi-Geometry")
    w("## Agent 4: Gravitational Pull Back to Phi-Structure")
    w("")
    w("---")
    w("")
    w("## Core Insight")
    w("")
    w("The pentagram is a MAP of where prices SHOULD be if the market were perfectly")
    w("phi-structured. When prices DEVIATE from the pentagram, there's a FORCE pulling")
    w("them back. This is like gravity -- the pentagram creates a gravitational field.")
    w("")
    w("```")
    w("  The trade:")
    w("    - When price DEVIATES from a phi-level -> BUY (it will be pulled back)")
    w("    - When price RETURNS to the phi-level -> SELL (capture the reversion)")
    w("")
    w("  This is MEAN REVERSION TO PHI-GEOMETRY.")
    w("  Not mean reversion to a moving average --")
    w("  mean reversion to the PHI-STRUCTURE of the market.")
    w("```")
    w("")
    w("---")
    w("")
    w("## Backtest Results")
    w("")

    if stats:
        w("### Trade Statistics")
        w("")
        w("| Metric | Value |")
        w("|--------|-------|")
        w(f"| Total trades entered | {stats['n_total']} |")
        w(f"| Closed trades | {stats['n_trades']} |")
        w(f"| Still open | {stats['n_open']} |")
        w(f"| Win rate | {stats['win_rate']:.1f}% |")
        w(f"| Avg net return | {stats['avg_return']:.4f}% |")
        w(f"| Median net return | {stats['median_return']:.4f}% |")
        w(f"| Avg gross return | {stats['avg_gross_return']:.4f}% |")
        w(f"| Std dev | {stats['std_return']:.4f}% |")
        w(f"| Avg win | {stats['avg_win']:.4f}% |")
        w(f"| Avg loss | {stats['avg_loss']:.4f}% |")
        w(f"| Profit factor | {stats['profit_factor']:.2f} |")
        w(f"| Sharpe ratio | {stats['sharpe']:.4f} |")
        w(f"| Avg hold days | {stats['avg_hold_days']:.1f} |")
        w(f"| Long trades | {stats['long_trades']} |")
        w(f"| Short trades | {stats['short_trades']} |")
        w("")

        # Exit reason analysis
        w("### Exit Reason Analysis")
        w("")
        w("| Reason | Count | Avg Return | Win Rate |")
        w("|--------|-------|------------|----------|")
        for reason, data in stats['by_exit_reason'].items():
            w(f"| {reason} | {data['count']} | {data['avg_return']:.4f}% | {data['win_rate']:.1f}% |")
        w("")

        # Sample trades
        w("### Sample Trades")
        w("")
        w("| Entry Date | Exit Date | Token | Dir | Entry | Exit | Return | Hold | Reason |")
        w("|------------|-----------|-------|-----|-------|------|--------|------|--------|")
        for t in trades[:15]:
            w(f"| {t['entry_date']} | {t['exit_date']} | {t['token'][:10]} | {t['direction'][:1]} | "
              f"${t['entry_price']:.2f} | ${t['exit_price']:.2f} | {t['net_return']*100:.2f}% | "
              f"{t['hold_days']}d | {t['exit_reason']} |")
        w("")
    else:
        w("**No trades generated.** The phi-gravity signals may not have been triggered.")
        w("")

    w("---")
    w("")
    w("## Monte Carlo Simulation")
    w("")
    w(f"| Parameter | Value |")
    w(f"|------------|-------|")
    w(f"| Starting capital | $5.00 |")
    w(f"| Paths | {mc_results['n_paths']} |")
    w(f"| Days simulated | {mc_results['n_days']} |")
    w(f"| Position per trade | ${mc_results.get('position_per_trade', 100):.0f} |")
    w("")
    w("### Final Portfolio Value")
    w("")
    w("| Statistic | Value |")
    w("|-----------|-------|")
    w(f"| Mean | ${mc_results['final_mean']:.2f} |")
    w(f"| Median | ${mc_results['final_median']:.2f} |")
    w(f"| Std | ${mc_results['final_std']:.2f} |")
    w(f"| Min | ${mc_results['final_min']:.2f} |")
    w(f"| Max | ${mc_results['final_max']:.2f} |")
    w(f"| p5 | ${mc_results['final_p5']:.2f} |")
    w(f"| p95 | ${mc_results['final_p95']:.2f} |")
    w("")
    w("### Return")
    w("")
    w("| Statistic | Value |")
    w("|-----------|-------|")
    w(f"| Mean | {mc_results['return_mean']*100:.2f}% |")
    w(f"| Median | {mc_results['return_median']*100:.2f}% |")
    w(f"| Positive paths | {mc_results['positive_paths']}/{mc_results['n_paths']} ({mc_results['positive_pct']:.1f}%) |")
    w(f"| Sharpe ratio | {mc_results['sharpe']:.4f} |")
    w(f"| Max drawdown | {mc_results['max_drawdown']*100:.2f}% |")
    w(f"| P($2M) | {mc_results['p_2m']:.2f}% |")
    w("")

    w("---")
    w("")
    w("## Comparison with Previous Approaches")
    w("")
    w("| Approach | Win Rate | Avg Return | Sharpe | P($2M) | Verdict |")
    w("|----------|----------|------------|--------|--------|---------|")
    w("| v2.01 Static Capture | ~50% | < 0 | - | 0% | NOT TRADEABLE |")
    w("| v2.02 Fill Rate | 1.8% fill | - | - | - | NEGATIVE EV |")
    w("| v2.03 Rotation | ~50% | ~0 | ~0 | ~0% | FEES EAT IT |")
    if stats:
        w(f"| **v2.04 Gravity** | **{stats['win_rate']:.1f}%** | **{stats['avg_return']:.4f}%** | **{stats['sharpe']:.4f}** | **{mc_results['p_2m']:.2f}%** | **{'PROFITABLE' if stats['avg_return'] > 0 else 'NOT PROFITABLE'}** |")
    else:
        w("| v2.04 Gravity | N/A | N/A | N/A | N/A | NO TRADES |")
    w("")

    w("---")
    w("")
    w("## The Gravity Mechanism")
    w("")
    w("1. **Map**: Compute the phi-pentagram (5 vertices at phi-ratio log prices)")
    w("2. **Measure**: Calculate deviation of each token from its phi-level")
    w("3. **Enter**: When deviation exceeds threshold -> BUY (expect gravitational pull)")
    w("4. **Exit**: When price returns to phi-level -> SELL (capture reversion)")
    w("5. **Stop**: If deviation exceeds max -> STOP (geometry is wrong)")
    w("")

    w("### Why Gravity Works (If It Does)")
    w("")
    w("- The pentagram is a MAP of phi-structure in the market")
    w("- Prices DEVIATE from the map due to noise, emotion, short-term flow")
    w("- But the phi-structure PERSISTS -> there's a FORCE pulling prices back")
    w("- This force is the gravitational pull of phi-geometry")
    w("- We trade the DEVIATION and capture the RETURN")
    w("")

    w("---")
    w("")
    w("## Bottom Line")
    w("")
    if stats:
        avg_net = stats['avg_return']
        win_rate = stats['win_rate']
        sharpe = stats['sharpe']
        p2m = mc_results['p_2m']

        w(f"| Metric | Value |")
        w(f"|--------|-------|")
        w(f"| Trades | {stats['n_trades']} |")
        w(f"| Win rate | {win_rate:.1f}% |")
        w(f"| Avg net return | {avg_net:.4f}% |")
        w(f"| Sharpe | {sharpe:.4f} |")
        w(f"| P($2M) | {p2m:.2f}% |")
        w(f"| MC mean final | ${mc_results['final_mean']:.2f} |")
        w("")

        if avg_net > 0.001 and win_rate > 55:
            w("**VERDICT: PHI-GRAVITY IS PROFITABLE.** The mean reversion to phi-geometry")
            w("generates positive expected value with a >55% win rate. The gravitational")
            w("pull of phi-structure creates a tradeable edge.")
        elif avg_net > 0:
            w("**VERDICT: PHI-GRAVITY IS MARGINALLY PROFITABLE.** Positive EV but the edge")
            w("is thin. May not survive real-world execution costs.")
        else:
            w("**VERDICT: PHI-GRAVITY IS NOT PROFITABLE.** The gravitational pull is too")
            w("weak or the entry/exit thresholds are wrong. The phi-structure may not")
            w("create sufficient mean reversion pressure.")
    else:
        w("**No trades generated.** The phi-gravity approach needs different parameters")
        w("or the market data does not exhibit the expected gravitational behavior.")

    w("")
    w("---")
    w("")
    w(f"*Generated by phi-gravity analyzer v2.04 -- Agent 4 -- {time.time():.0f}*")

    return '\n'.join(L)


def main():
    t_start = time.time()
    print("=" * 70)
    print("PHI-PENTAGRAM GRAVITY: MEAN REVERSION TO PHI-GEOMETRY")
    print("Agent 4: Gravitational pull back to phi-structure")
    print("=" * 70)
    print()

    print("Loading price data...", flush=True)
    prices_arr, token_names, dates = load_all()
    n_days, n_tokens = prices_arr.shape
    print(f"  {n_tokens} tokens, {n_days} days ({time.time()-t_start:.1f}s)", flush=True)

    # Run gravity backtest
    trades, pentagrams = run_gravity_backtest(prices_arr, token_names, dates, n_days)

    # Analyze trades
    print("\nPhase 3: Analyzing trades...", flush=True)
    stats = analyze_trades(trades)

    if stats:
        print(f"\n  Total trades: {stats['n_trades']}")
        print(f"  Win rate: {stats['win_rate']:.1f}%")
        print(f"  Avg net return: {stats['avg_return']:.4f}%")
        print(f"  Sharpe: {stats['sharpe']:.4f}")
    else:
        print("  No trades generated!")

    # Monte Carlo
    print("\nPhase 4: Monte Carlo Simulation (5000 paths)...", flush=True)
    # Use only closed trades for MC (not end_of_data)
    closed_trades = [t for t in trades if t['exit_reason'] != 'end_of_data']
    mc_results = run_monte_carlo(closed_trades, dates, n_days, n_paths=5000)

    print(f"\n  MC Mean: ${mc_results['final_mean']:.2f}")
    print(f"  MC P($2M): {mc_results['p_2m']:.2f}%")

    # Generate report
    print("\nPhase 5: Generating report...", flush=True)
    pentagrams_found = sum(1 for p in pentagrams if p is not None)
    report = build_report(n_days, closed_trades, stats, mc_results, pentagrams_found)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'arbridge_v2_04_gravity.md')
    with open(out, 'w') as f:
        f.write(report)
    print(f"  Report saved: {out}", flush=True)

    elapsed = time.time() - t_start
    print(f"\nTotal time: {elapsed:.0f}s", flush=True)

    key_finding = f"{stats['n_trades']} closed trades, {stats['win_rate']:.1f}% win, {stats['avg_return']:.4f}% avg, P($2M)={mc_results['p_2m']:.2f}%" if stats else "No trades"
    print(f"\nAgent 4 complete. {key_finding}")


if __name__ == '__main__':
    main()

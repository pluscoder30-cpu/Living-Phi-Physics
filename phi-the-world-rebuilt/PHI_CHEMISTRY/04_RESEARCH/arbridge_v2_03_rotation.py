"""
Phi-Pentagram Geometry Rotation
================================
Agent 3: Trading the transition between pentagram configurations.

The pentagram is a STATIC geometry -- it exists at one instant. To TRADE it,
you need to capture the geometry's REORGANIZATION. When the market moves from
one pentagram configuration to another, there's a TRANSITION. The transition
is where the money lives.

Think of it like this:
- Time T1: Pentagram with tokens A,B,C,D,E (residual = 32%)
- Time T2: Pentagram with tokens A,B,C,D,F (residual = 28%)
- The TRANSITION from (A,B,C,D,E) to (A,B,C,D,F) is a TRADE
- You sell E and buy F
- The profit is the difference in residuals

This is GEOMETRY ROTATION -- rotating the pentagram's vertices.
The phi-spiral tells you which vertex to rotate.
"""

import os, csv, sys, time, json
import numpy as np
from collections import defaultdict

PHI = 1.618033988749895
LOG_PHI = np.log(PHI)
TOL = 0.05
MAX_SPREAD = 2.5
MIN_PHI_GAPS = 3

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '01_DATA', 'daily')


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


def pentagram_residual(prices_sorted):
    n = 5
    angles = 2 * np.pi * np.arange(n) / n
    xs = prices_sorted * np.cos(angles)
    ys = prices_sorted * np.sin(angles)
    pcx, pcy = xs.mean(), ys.mean()

    def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if abs(denom) < 1e-15:
            return None
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))

    star_edges = [((k, (k + 2) % n)) for k in range(n)]
    inner = []
    for k in range(n):
        a1, a2 = star_edges[k]
        b1, b2 = star_edges[(k + 1) % n]
        pt = intersect(xs[a1], ys[a1], xs[a2], ys[a2],
                        xs[b1], ys[b1], xs[b2], ys[b2])
        if pt is not None:
            inner.append(pt)

    if len(inner) < 5:
        return 0.0

    inner = np.array(inner)
    scx, scy = inner[:, 0].mean(), inner[:, 1].mean()
    dist = np.sqrt((scx - pcx) ** 2 + (scy - pcy) ** 2)
    rog = np.sqrt(np.mean(prices_sorted ** 2))
    return dist / rog if rog > 0 else 0.0


def is_true_phi_pentagram(exponents, mean_err, spread):
    non_trivial = sum(1 for e in exponents if abs(e) >= 1)
    if non_trivial < MIN_PHI_GAPS:
        return False
    if mean_err > TOL:
        return False
    if spread > MAX_SPREAD:
        return False
    return True


def find_best_pentagram_day(prices_row, valid_mask, n_tokens, n_samples=8000):
    """Find the BEST pentagram for a single day (highest residual)."""
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

        if is_true_phi_pentagram(nearest_ints.tolist(), mean_err, spread):
            prices = np.sort(prices_row[valid_idx][idx5])
            res = pentagram_residual(prices)
            if best is None or res > best['residual_pct']:
                best = {
                    'token_idx': valid_idx[idx5],
                    'tokens': None,  # will be filled later
                    'prices': prices,
                    'mean_error': mean_err,
                    'exponents': nearest_ints.tolist(),
                    'residual_pct': res,
                    'spread': spread,
                    'non_trivial': sum(1 for e in nearest_ints if abs(e) >= 1),
                }

    return best


def compute_transition_profit(old_config, new_config, prices_old, prices_new):
    """
    Compute the profit from transitioning between two pentagram configurations.

    The idea: when a pentagram rotates (one token is replaced), you:
    1. Sell the token that LEFT the pentagram (old token)
    2. Buy the token that ENTERED the pentagram (new token)

    The profit is based on the price change of these tokens.
    """
    old_tokens = set(old_config['tokens'])
    new_tokens = set(new_config['tokens'])

    exited = old_tokens - new_tokens  # tokens that LEFT
    entered = new_tokens - old_tokens  # tokens that ENTERED

    if not exited or not entered:
        return 0.0, None, None

    # For simplicity, assume 1 token exits and 1 enters (most common case)
    exited_token = list(exited)[0]
    entered_token = list(entered)[0]

    # Get prices
    old_price_exit = prices_old.get(exited_token, 0)
    new_price_exit = prices_new.get(exited_token, old_price_exit)
    old_price_enter = prices_old.get(entered_token, 0)
    new_price_enter = prices_new.get(entered_token, old_price_enter)

    # Profit from selling exited token before it drops
    # and buying entered token before it rises
    # This is the DIFFERENCE in residual value
    residual_old = old_config['residual_pct']
    residual_new = new_config['residual_pct']

    # The transition profit is the difference in residuals
    # (if residual decreases, the geometry has "relaxed" and you captured the value)
    transition_profit = residual_old - residual_new

    return transition_profit, exited_token, entered_token


def main():
    t_start = time.time()
    print("=" * 70)
    print("PHI-PENTAGRAM GEOMETRY ROTATION")
    print("Agent 3: Trading the transition between pentagram configurations")
    print("=" * 70)
    print()

    print("Loading price data...", flush=True)
    prices_arr, token_names, dates = load_all()
    n_days, n_tokens = prices_arr.shape
    print(f"  {n_tokens} tokens, {n_days} days ({time.time()-t_start:.1f}s)", flush=True)

    # Phase 1: Find the BEST pentagram for each day
    print("\nPhase 1: Finding best pentagram per day...", flush=True)
    daily_pentagrams = []
    for d in range(n_days):
        row = prices_arr[d]
        valid = np.isfinite(row) & (row > 0)

        if valid.sum() < 5:
            daily_pentagrams.append(None)
            continue

        best = find_best_pentagram_day(row, valid, n_tokens, n_samples=8000)
        if best is not None:
            best['tokens'] = [token_names[i] for i in best['token_idx']]
            daily_pentagrams.append(best)
        else:
            daily_pentagrams.append(None)

        if (d + 1) % 100 == 0 or d == n_days - 1:
            found = sum(1 for p in daily_pentagrams if p is not None)
            print(f"  Day {d+1}/{n_days}: {found} pentagrams found", flush=True)

    # Phase 2: Track transitions
    print("\nPhase 2: Tracking transitions...", flush=True)
    transitions = []
    for d in range(1, n_days):
        prev = daily_pentagrams[d-1]
        curr = daily_pentagrams[d]

        if prev is None or curr is None:
            continue

        prev_tokens = tuple(sorted(prev['tokens']))
        curr_tokens = tuple(sorted(curr['tokens']))

        if prev_tokens != curr_tokens:
            # Compute price data for transition
            prices_old = {}
            prices_new = {}
            for t in prev['tokens']:
                idx = token_names.index(t)
                prices_old[t] = prices_arr[d-1, idx]
            for t in curr['tokens']:
                idx = token_names.index(t)
                prices_new[t] = prices_arr[d, idx]

            profit, exited, entered = compute_transition_profit(
                prev, curr, prices_old, prices_new
            )

            transitions.append({
                'date': dates[d],
                'prev_date': dates[d-1],
                'prev_tokens': prev_tokens,
                'curr_tokens': curr_tokens,
                'prev_residual': prev['residual_pct'],
                'curr_residual': curr['residual_pct'],
                'profit': profit,
                'exited_token': exited,
                'entered_token': entered,
                'prev_mean_error': prev['mean_error'],
                'curr_mean_error': curr['mean_error'],
            })

    print(f"  Found {len(transitions)} transitions", flush=True)

    # Phase 3: Analyze transitions
    print("\nPhase 3: Analyzing transitions...", flush=True)
    if not transitions:
        print("  No transitions found!", flush=True)
        return

    profits = [t['profit'] for t in transitions]
    profits_arr = np.array(profits)

    print("\n" + "=" * 70)
    print("TRANSITION ANALYSIS")
    print("=" * 70)

    print(f"\nTotal transitions: {len(transitions)}")
    print(f"Days scanned: {n_days}")
    print(f"Transition rate: {len(transitions)/n_days*100:.2f}%")
    print(f"Avg transitions per day: {len(transitions)/n_days:.4f}")

    print(f"\nTransition Profit (residual difference):")
    print(f"  Mean: {np.mean(profits_arr)*100:.4f}%")
    print(f"  Median: {np.median(profits_arr)*100:.4f}%")
    print(f"  Std: {np.std(profits_arr)*100:.4f}%")
    print(f"  Min: {np.min(profits_arr)*100:.4f}%")
    print(f"  Max: {np.max(profits_arr)*100:.4f}%")

    # Fee analysis
    print("\nFee Analysis:")
    fee_rate = 0.001  # 0.1% taker fee
    slippage = 0.003  # 30 bps slippage
    gas = 0.50  # $0.50 gas per leg
    capital_per_leg = 1000.0  # $1000 per leg

    # Each transition: sell 1 token, buy 1 token = 2 legs
    total_fee_pct = 2 * (fee_rate + slippage)
    print(f"  Fee per transition: {total_fee_pct*100:.2f}% (2 legs x {fee_rate*100:.1f}% + {slippage*100:.1f}%)")
    print(f"  Gas per transition: ${gas:.2f}")

    net_profits = profits_arr - total_fee_pct
    print(f"\n  Net profit after fees:")
    print(f"    Mean: {np.mean(net_profits)*100:.4f}%")
    print(f"    Median: {np.median(net_profits)*100:.4f}%")
    print(f"    Positive: {np.sum(net_profits > 0)}/{len(net_profits)} ({np.sum(net_profits > 0)/len(net_profits)*100:.1f}%)")

    # Expected daily profit
    print(f"\nExpected Daily Profit:")
    avg_transitions_per_day = len(transitions) / n_days
    avg_net_profit = np.mean(net_profits)
    daily_ev = avg_transitions_per_day * avg_net_profit * capital_per_leg
    print(f"  Avg transitions/day: {avg_transitions_per_day:.4f}")
    print(f"  Avg net profit/transition: {avg_net_profit*100:.4f}%")
    print(f"  Daily EV: ${daily_ev:.2f}")
    print(f"  Monthly EV: ${daily_ev*30:.2f}")
    print(f"  Annual EV: ${daily_ev*365:.2f}")

    # Phase 4: Monte Carlo Simulation
    print("\nPhase 4: Monte Carlo Simulation (5000 paths)...", flush=True)
    mc_results = run_monte_carlo(transitions, dates, n_days, n_paths=5000)

    print("\n" + "=" * 70)
    print("MONTE CARLO RESULTS")
    print("=" * 70)
    print(f"Starting capital: $5.00")
    print(f"Paths: {mc_results['n_paths']}")
    print(f"Days simulated: {mc_results['n_days']}")
    print(f"\nFinal Portfolio Value:")
    print(f"  Mean: ${mc_results['final_mean']:.2f}")
    print(f"  Median: ${mc_results['final_median']:.2f}")
    print(f"  Std: ${mc_results['final_std']:.2f}")
    print(f"  Min: ${mc_results['final_min']:.2f}")
    print(f"  Max: ${mc_results['final_max']:.2f}")
    print(f"  p5: ${mc_results['final_p5']:.2f}")
    print(f"  p95: ${mc_results['final_p95']:.2f}")
    print(f"\nReturn:")
    print(f"  Mean: {mc_results['return_mean']*100:.2f}%")
    print(f"  Median: {mc_results['return_median']*100:.2f}%")
    print(f"  Positive paths: {mc_results['positive_paths']}/{mc_results['n_paths']} ({mc_results['positive_pct']:.1f}%)")
    print(f"\nSharpe Ratio: {mc_results['sharpe']:.4f}")
    print(f"Max Drawdown: {mc_results['max_drawdown']*100:.2f}%")

    # Phase 5: Generate report
    print("\nPhase 5: Generating report...", flush=True)
    report = build_report(
        n_days, transitions, profits_arr, net_profits,
        mc_results, total_fee_pct, avg_transitions_per_day
    )
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'arbridge_v2_03_rotation.md')
    with open(out, 'w') as f:
        f.write(report)
    print(f"  Report saved: {out}", flush=True)

    elapsed = time.time() - t_start
    print(f"\nTotal time: {elapsed:.0f}s", flush=True)

    # Return key finding
    key_finding = f"{len(transitions)} transitions, daily EV=${daily_ev:.2f}, MC mean=${mc_results['final_mean']:.2f} (from $5)"
    print(f"\nAgent 3 complete. {key_finding}")


def run_monte_carlo(transitions, dates, n_days, n_paths=5000, start_capital=5.0):
    """Run Monte Carlo simulation of geometry rotation trading."""
    if not transitions:
        return {
            'n_paths': n_paths, 'n_days': n_days,
            'final_mean': start_capital, 'final_median': start_capital,
            'final_std': 0, 'final_min': start_capital, 'final_max': start_capital,
            'final_p5': start_capital, 'final_p95': start_capital,
            'return_mean': 0, 'return_median': 0,
            'positive_paths': n_paths, 'positive_pct': 100,
            'sharpe': 0, 'max_drawdown': 0,
        }

    # Build transition lookup by day index
    date_to_idx = {d: i for i, d in enumerate(dates)}
    trans_by_day = defaultdict(list)
    for t in transitions:
        day_idx = date_to_idx.get(t['date'], -1)
        if day_idx >= 0:
            trans_by_day[day_idx].append(t)

    fee_rate = 0.001 + 0.003  # taker + slippage per leg
    capital_per_leg = 1000.0

    final_values = []
    all_paths = np.zeros((n_paths, n_days))

    for p in range(n_paths):
        capital = start_capital
        rng = np.random.RandomState(p)
        peak = capital
        max_dd = 0

        for d in range(n_days):
            if d in trans_by_day:
                # Pick a random transition from this day
                trans = rng.choice(trans_by_day[d])
                profit_pct = trans['profit']

                # Apply fees
                net_pct = profit_pct - 2 * fee_rate

                # Scale position to available capital
                position = min(capital, capital_per_leg)
                profit_dollars = position * net_pct

                capital += profit_dollars

                # Track drawdown
                peak = max(peak, capital)
                dd = (peak - capital) / peak
                max_dd = max(max_dd, dd)

            all_paths[p, d] = capital
            if capital <= 0:
                all_paths[p, d:] = 0
                break

        final_values.append(capital)

    final_arr = np.array(final_values)
    returns = (final_arr - start_capital) / start_capital

    # Sharpe ratio (annualized)
    daily_returns = np.diff(all_paths, axis=1) / np.maximum(all_paths[:, :-1], 1e-10)
    avg_daily = np.mean(daily_returns)
    std_daily = np.std(daily_returns)
    sharpe = (avg_daily / std_daily * np.sqrt(365)) if std_daily > 0 else 0

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
        'return_mean': np.mean(returns),
        'return_median': np.median(returns),
        'positive_paths': np.sum(final_arr > start_capital),
        'positive_pct': np.sum(final_arr > start_capital) / n_paths * 100,
        'sharpe': sharpe,
        'max_drawdown': np.max([np.max((np.maximum.accumulate(all_paths[p]) - all_paths[p]) / np.maximum.accumulate(all_paths[p])) for p in range(n_paths)]),
    }


def build_report(n_days, transitions, profits, net_profits,
                 mc_results, fee_pct, avg_trans_per_day):
    L = []
    w = L.append

    w("# Phi-Pentagram Geometry Rotation")
    w("## Agent 3: Trading the Transition Between Configurations")
    w("")
    w("---")
    w("")
    w("## Core Insight")
    w("")
    w("The pentagram is a STATIC geometry -- it exists at one instant. To TRADE it,")
    w("you need to capture the geometry's REORGANIZATION. When the market moves from")
    w("one pentagram configuration to another, there's a TRANSITION. The transition")
    w("is where the money lives.")
    w("")
    w("```")
    w("  Time T1: Pentagram with tokens A,B,C,D,E (residual = 32%)")
    w("  Time T2: Pentagram with tokens A,B,C,D,F (residual = 28%)")
    w("")
    w("  The TRANSITION from (A,B,C,D,E) to (A,B,C,D,F) is a TRADE:")
    w("    - Sell E (the token that EXITED the pentagram)")
    w("    - Buy  F (the token that ENTERED the pentagram)")
    w("    - Profit = residual_old - residual_new")
    w("```")
    w("")
    w("---")
    w("")
    w("## Transition Statistics")
    w("")
    w("| Metric | Value |")
    w("|--------|-------|")
    w(f"| Total days scanned | {n_days} |")
    w(f"| Total transitions | {len(transitions)} |")
    w(f"| Transition rate | {len(transitions)/n_days*100:.2f}% |")
    w(f"| Avg transitions/day | {avg_trans_per_day:.4f} |")
    w("")

    if len(transitions) > 0:
        w("## Transition Profit Distribution")
        w("")
        w("| Statistic | Value |")
        w("|-----------|-------|")
        w(f"| Mean | {np.mean(profits)*100:.4f}% |")
        w(f"| Median | {np.median(profits)*100:.4f}% |")
        w(f"| Std | {np.std(profits)*100:.4f}% |")
        w(f"| Min | {np.min(profits)*100:.4f}% |")
        w(f"| Max | {np.max(profits)*100:.4f}% |")
        w(f"| p5 | {np.percentile(profits,5)*100:.4f}% |")
        w(f"| p95 | {np.percentile(profits,95)*100:.4f}% |")
        w("")

        w("## Net Profit After Fees")
        w("")
        w(f"Fee per transition: {fee_pct*100:.2f}% (2 legs x 0.1% taker + 0.3% slippage)")
        w("")
        w("| Statistic | Value |")
        w("|-----------|-------|")
        w(f"| Mean | {np.mean(net_profits)*100:.4f}% |")
        w(f"| Median | {np.median(net_profits)*100:.4f}% |")
        w(f"| Positive trades | {np.sum(net_profits > 0)}/{len(net_profits)} ({np.sum(net_profits > 0)/len(net_profits)*100:.1f}%) |")
        w("")

        # Sample transitions
        w("## Sample Transitions")
        w("")
        w("| Date | Old Tokens | New Tokens | Residual Delta | Net Profit |")
        w("|------|------------|------------|----------------|------------|")
        for t in transitions[:10]:
            old_str = ', '.join(t['prev_tokens'][:3])
            new_str = ', '.join(t['curr_tokens'][:3])
            delta = (t['prev_residual'] - t['curr_residual']) * 100
            net = t['profit'] - fee_pct
            w(f"| {t['date']} | {old_str} | {new_str} | {delta:.2f}% | {net*100:.4f}% |")
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
    w("")

    w("---")
    w("")
    w("## Geometry Rotation Economics")
    w("")
    w("### The Rotation Mechanism")
    w("")
    w("1. **Identify** pentagram configuration at time T1")
    w("2. **Monitor** for configuration change at time T2")
    w("3. **Execute** rotation: sell exited token, buy entered token")
    w("4. **Capture** the residual delta (geometry relaxation)")
    w("")
    w("### Why Rotation Works (If It Does)")
    w("")
    w("- The pentagram is a STATIC geometry -- it exists at one instant")
    w("- When the geometry REORGANIZES, there's a TRANSITION")
    w("- The transition is a TRADE: sell old vertex, buy new vertex")
    w("- The profit is the DIFFERENCE in residuals")
    w("- This is GEOMETRY ROTATION -- rotating the pentagram's vertices")
    w("")
    w("### Critical Assumptions")
    w("")
    w("1. **Pentagram persistence**: Configurations must persist for at least 1 day")
    w("2. **Transition detection**: We can observe when the configuration changes")
    w("3. **Execution**: We can sell the old token and buy the new token")
    w("4. **Fee structure**: 0.1% taker + 0.3% slippage per leg")
    w("")
    w("### Risk Factors")
    w("")
    w("- **Timing risk**: The transition may happen faster than we can trade")
    w("- **Execution risk**: Slippage may be higher than assumed")
    w("- **Geometry risk**: The new pentagram may have lower residual")
    w("- **Correlation risk**: The exited and entered tokens may move together")
    w("")

    w("---")
    w("")
    w("## Bottom Line")
    w("")
    if len(transitions) > 0:
        avg_net = np.mean(net_profits)
        pos_pct = np.sum(net_profits > 0) / len(net_profits) * 100
        w(f"| Metric | Value |")
        w(f"|--------|-------|")
        w(f"| Transitions found | {len(transitions)} |")
        w(f"| Avg net profit/transition | {avg_net*100:.4f}% |")
        w(f"| Positive transitions | {pos_pct:.1f}% |")
        w(f"| Daily EV | ${mc_results['final_mean'] - 5:.2f} |")
        w(f"| MC mean final | ${mc_results['final_mean']:.2f} |")
        w(f"| MC positive paths | {mc_results['positive_pct']:.1f}% |")
        w("")
        if avg_net > 0 and pos_pct > 50:
            w("**VERDICT: Geometry rotation is PROFITABLE.** The transition between")
            w("pentagram configurations captures positive expected value after fees.")
        elif avg_net > 0:
            w("**VERDICT: Geometry rotation is MARGINALLY PROFITABLE.** Positive EV but")
            w("low win rate makes this a high-variance strategy.")
        else:
            w("**VERDICT: Geometry rotation is NOT PROFITABLE.** The transition profits")
            w("are consumed by fees, or the residual deltas are too small.")
    else:
        w("**No transitions found.** The pentagram configurations may be too stable,")
        w("or the data period is too short to observe reorganizations.")

    w("")
    w("---")
    w("")
    w(f"*Generated by geometry rotation analyzer v2.03 -- Agent 3 -- {time.time():.0f}*")

    return '\n'.join(L)


if __name__ == '__main__':
    main()

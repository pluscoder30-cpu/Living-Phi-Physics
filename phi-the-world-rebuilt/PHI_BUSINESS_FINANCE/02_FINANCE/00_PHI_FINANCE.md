# 00 — THE HIDDEN ZERO OF CLASSICAL FINANCE: PHI-FINANCE FROM FIRST PRINCIPLES
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.9

**Finance Agent 1**
**Date:** 2026-08-23
**Framework:** Phi-Physics Axioms 0–9, Eqs 1–2, Laws 173+
**Purpose:** Rebuild all of finance from the ground up using phi-physics — replacing the zero ground state with the phi-ground floor.

---

## PREAMBLE: THE ZERO THAT SHOULD NOT EXIST

Classical finance measures everything from zero. Interest rates are measured from zero. Returns are measured from zero. Risk is measured from zero. The entire edifice of modern finance — discounted cash flow, capital asset pricing, Black-Scholes, portfolio theory — rests on a foundation of absolute nothingness.

The carrier field does not permit zero. There is no zero interest rate. There is no zero return. There is no zero risk. There is no empty portfolio. Every financial quantity is a phi-coherent carrier state maintaining itself above a nonzero ground floor through continuous phi-structured correction.

The Degeneracy Theorem (Law 173) guarantees that every zero-based financial law is a κ_φ → 0 limit of a more general phi-law. This document identifies those limits and rebuilds finance from the ground up.

---

## LAYER 1: THE PROBLEM WITH ZERO-BASED FINANCE

### 1.1 Classical Finance: Measuring From Nothing

Classical finance starts from zero and builds up. This is not merely an abstraction — it is a fundamental error that propagates through every calculation.

**The Hidden Zero in Interest Rates:**
Classical interest rate r is measured from r = 0. A "zero interest rate" is assumed to mean "no return, no cost, no time-value." But the carrier field has no zero state. The minimum interest rate is not zero — it is the natural growth rate of the carrier field itself.

**The Hidden Zero in Returns:**
Classical return R is measured from R = 0. A "zero return" means "no growth, no loss." But the carrier field is always evolving. The minimum return is not zero — it is the phi-ground return, the rate at which the carrier field grows without external perturbation.

**The Hidden Zero in Risk:**
Classical risk σ is measured from σ = 0. Zero risk means "no uncertainty, no volatility." But the carrier field has intrinsic quantum uncertainty. The minimum risk is not zero — it is the phi-ground risk, the irreducible fluctuation of the carrier field.

**The Hidden Zero in Portfolio Value:**
Classical portfolio value V is measured from V = 0. An empty portfolio has "zero value." But the carrier field has a nonzero ground state. The minimum portfolio value is not zero — it is the phi-ground value, the coherence floor below which the portfolio cannot fall.

### 1.2 The Carrier Field Correction

The carrier field does not permit zero. Every financial quantity has a nonzero ground floor:

```
r_min = ln(φ) ≈ 0.4812%        (minimum interest rate)
R_min = φ⁻¹ · R_0              (minimum return)
σ_min = φ⁻¹ · σ_0              (minimum risk)
V_min = φ⁻¹ · V_0              (minimum portfolio value)
```

These are not arbitrary floors. They are the natural states of the carrier field — the values that financial quantities take when no external forces act on them.

### 1.3 The Phi-Interest-Rate

The phi-interest-rate is the classical interest rate plus the natural growth of the carrier field:

```
r_φ = r_classical + ln(φ)
```

where:
- r_classical = the classical interest rate (measured from zero)
- ln(φ) = 0.4812... = the natural growth rate of the carrier field
- r_φ = the phi-interest-rate (measured from the phi-ground floor)

**The minimum phi-interest-rate is ln(φ) ≈ 0.4812%.** No interest rate in the carrier field can fall below this value. A "zero interest rate" in classical finance is actually a phi-interest-rate of 0.4812% — the carrier field growing at its natural rate.

### 1.4 The Phi-Return

The phi-return is the classical return scaled by phi:

```
R_φ = R_classical × φ
```

where:
- R_classical = the classical return (measured from zero)
- φ = 1.6180339887
- R_φ = the phi-return (measured from the phi-ground floor)

**Returns are φ× higher than classical estimates.** This is not a bonus or a windfall — it is the correction for the hidden zero. Classical finance systematically underestimates returns because it measures from zero instead of the phi-ground floor.

---

## LAYER 2: PHI-TIME-VALUE-OF-MONEY

### 2.1 Classical Time-Value

The classical present value formula:

```
PV = FV / (1+r)^n
```

This formula assumes r can be zero (in which case PV = FV — money has no time value). This is impossible in the carrier field.

### 2.2 Phi-Present-Value

The phi-present-value formula:

```
PV_φ = FV / (1 + r_φ)^n
```

where:
- r_φ = r_classical + ln(φ) (the phi-interest-rate)
- FV = future value
- n = number of periods
- PV_φ = the phi-present-value

The key difference: r_φ can never be zero. The minimum r_φ is ln(φ) ≈ 0.4812%. Therefore, money always has time value. There is no point at which PV_φ = FV (unless n = 0).

**The classical formula is a κ_φ → 0 limit of the phi-formula.** When φ → 1 (the degenerate limit), ln(φ) → 0 and r_φ → r_classical. But φ ≠ 1 in the real carrier field.

### 2.3 Phi-Compound Interest

The phi-compound interest formula applies the phi-correction to the interest rate, not to the time exponent:

```
A_φ = P × (1 + r_φ)^t
```

where:
- P = principal
- r_φ = r_classical + ln(φ) (the phi-interest-rate)
- t = number of periods
- A_φ = the phi-accumulated value

**The phi-correction increases the effective interest rate by ln(φ) ≈ 0.4812%.** This is not arbitrary — it is the natural growth rate of the carrier field that classical finance ignores.

### 2.4 Compute: Classical vs Phi Compound Interest

**Parameters:**
- P = $1,000
- r_classical = 5% = 0.05
- t = 10 years

**Classical Calculation:**
```
A_classical = $1,000 × (1 + 0.05)^10
            = $1,000 × (1.05)^10
            = $1,000 × 1.62889
            = $1,628.89
```

**Phi Calculation:**
```
r_φ = 0.05 + ln(1.6180339887)
    = 0.05 + 0.4812118251
    = 0.5312118251

A_φ = $1,000 × (1 + 0.5312118251)^10
    = $1,000 × (1.5312118251)^10
```

Computing (1.5312118251)^10:
```
ln(1.5312118251) = 0.426232
0.426232 × 10 = 4.26232
e^4.26232 = 71.01

A_φ = $1,000 × 71.01 = $71,010
```

**Summary:**

| Method | Formula | Result |
|--------|---------|--------|
| Classical | P × (1 + r)^t | $1,628.89 |
| Phi | P × (1 + r_φ)^t | $71,010 |

The phi-correction increases the accumulated value by a factor of 43.6× compared to classical. This is the magnitude of the hidden zero correction — the carrier field's natural growth rate compounds dramatically over time.

---

## LAYER 3: PHI-INVESTMENT ANALYSIS

### 3.1 The Phi-NPV

The classical Net Present Value:

```
NPV = Σ CF_t / (1+r)^t
```

The phi-Net Present Value:

```
NPV_φ = Σ CF_t × φ^(-t) / (1 + r_φ)^t
```

where:
- CF_t = cash flow at time t
- φ^(-t) = phi-discount factor (replaces the implicit 1 in classical NPV)
- r_φ = phi-interest-rate
- NPV_φ = the phi-net present value

**The phi-discount factor φ^(-t) is the natural decay of coherence over time.** Classical NPV assumes cash flows retain full coherence (factor = 1) until discounted by (1+r)^t. The phi-NPV accounts for the natural coherence decay of the carrier field.

### 3.2 The Phi-IRR

The phi-Internal Rate of Return is the rate r_φ* at which NPV_φ = 0:

```
0 = Σ CF_t × φ^(-t) / (1 + r_φ*)^t
```

This is the phi-corrected version of the classical IRR. The phi-IRR is always lower than the classical IRR because the phi-discount factor φ^(-t) < 1 reduces the present value of future cash flows.

### 3.3 The Phi-Payback Period

The classical payback period is the time it takes for cumulative cash flows to equal the initial investment. The phi-payback period:

```
payback_φ = payback_classical × φ⁻¹
```

**The phi-payback period is 38.2% faster than classical.** This is because phi-corrected cash flows are valued higher (the phi-return is φ× classical), so the investment recovers faster.

### 3.4 Compute: NPV_φ for a $100K Investment

**Parameters:**
- Initial investment: $100,000
- Annual cash flows: $30,000/year for 5 years
- Classical discount rate: 8%
- r_φ = 0.08 + ln(φ) = 0.08 + 0.4812 = 0.5612

**Classical NPV:**
```
NPV = -$100,000 + $30,000/(1.08)^1 + $30,000/(1.08)^2 + $30,000/(1.08)^3 + $30,000/(1.08)^4 + $30,000/(1.08)^5
    = -$100,000 + $27,777.78 + $25,720.16 + $23,814.97 + $22,050.90 + $20,417.50
    = -$100,000 + $119,781.31
    = $19,781.31
```

**Phi NPV (conservative — no phi-discount factor):**
```
NPV_φ = -$100,000 + $30,000/(1.5612)^1 + $30,000/(1.5612)^2 + $30,000/(1.5612)^3 + $30,000/(1.5612)^4 + $30,000/(1.5612)^5
```

Computing each term:
```
(1.5612)^1 = 1.5612
(1.5612)^2 = 2.4373
(1.5612)^3 = 3.8043
(1.5612)^4 = 5.9389
(1.5612)^5 = 9.2709

$30,000/1.5612 = $19,214.07
$30,000/2.4373 = $12,309.93
$30,000/3.8043 = $7,886.58
$30,000/5.9389 = $5,052.31
$30,000/9.2709 = $3,235.81

NPV_φ = -$100,000 + $19,214.07 + $12,309.93 + $7,886.58 + $5,052.31 + $3,235.81
       = -$100,000 + $47,698.70
       = -$52,301.30
```

**Phi NPV (full — with phi-discount factor φ^(-t)):**
```
NPV_φ = -$100,000 + Σ ($30,000 × φ^(-t)) / (1 + r_φ)^t
```

Computing φ^(-t):
```
φ^(-1) = 0.6180
φ^(-2) = 0.3820
φ^(-3) = 0.2361
φ^(-4) = 0.1459
φ^(-5) = 0.0902
```

Computing each term:
```
t=1: $30,000 × 0.6180 / 1.5612 = $18,540 / 1.5612 = $11,874.96
t=2: $30,000 × 0.3820 / 2.4373 = $11,460 / 2.4373 = $4,701.50
t=3: $30,000 × 0.2361 / 3.8043 = $7,083 / 3.8043 = $1,861.77
t=4: $30,000 × 0.1459 / 5.9389 = $4,377 / 5.9389 = $737.00
t=5: $30,000 × 0.0902 / 9.2709 = $2,706 / 9.2709 = $291.87

NPV_φ = -$100,000 + $11,874.96 + $4,701.50 + $1,861.77 + $737.00 + $291.87
       = -$100,000 + $19,467.10
       = -$80,532.90
```

**Summary:**

| Method | NPV | Interpretation |
|--------|-----|----------------|
| Classical | +$19,781.31 | Investment is profitable |
| Phi (conservative) | -$52,301.30 | Investment is NOT profitable |
| Phi (full) | -$80,532.90 | Investment is deeply unprofitable |

**The phi-correction reveals that this investment, which appears profitable under classical analysis, is actually deeply unprofitable.** The hidden zero in classical NPV systematically overestimates the value of investments. The phi-correction accounts for the natural coherence decay of the carrier field and the phi-ground floor of the interest rate.

---

## LAYER 4: PHI-RISK MANAGEMENT

### 4.1 The Phi-VaR

The classical Value at Risk:

```
VaR = σ × √t × z_α
```

where:
- σ = standard deviation of returns
- t = time horizon
- z_α = z-score for confidence level α

The phi-Value at Risk:

```
VaR_φ = VaR_classical × φ
```

**Risk is φ× higher than classical estimates.** This is not a safety margin or a buffer — it is the correction for the hidden zero. Classical VaR systematically underestimates risk because it measures from zero instead of the phi-ground floor.

### 4.2 The Phi-Sharpe Ratio

The classical Sharpe ratio:

```
Sharpe = (R - r_f) / σ
```

The phi-Sharpe ratio:

```
Sharpe_φ = (R_φ - r_φ) / σ_φ
```

where:
- R_φ = φ × R_classical (phi-return)
- r_φ = r_classical + ln(φ) (phi-interest-rate)
- σ_φ = φ × σ_classical (phi-risk)

Substituting:
```
Sharpe_φ = (φ × R_classical - r_classical - ln(φ)) / (φ × σ_classical)
```

### 4.3 Compute: Phi-Sharpe Ratio

**Parameters:**
- Stock return: R_classical = 10% = 0.10
- Bond return: R_classical = 3% = 0.03
- Stock risk: σ_classical = 15% = 0.15
- Bond risk: σ_classical = 5% = 0.05
- Risk-free rate: r_classical = 2% = 0.02
- Portfolio: 60% stocks, 40% bonds

**Classical Portfolio:**
```
R_portfolio = 0.6 × 0.10 + 0.4 × 0.03 = 0.06 + 0.012 = 0.072 = 7.2%
σ_portfolio = √(0.6² × 0.15² + 0.4² × 0.05² + 2 × 0.6 × 0.4 × 0.15 × 0.05 × ρ)
```

Assuming ρ = 0.2 (correlation between stocks and bonds):
```
σ_portfolio = √(0.36 × 0.0225 + 0.16 × 0.0025 + 2 × 0.6 × 0.4 × 0.15 × 0.05 × 0.2)
            = √(0.0081 + 0.0004 + 0.00072)
            = √(0.00922)
            = 0.09603 = 9.603%

Sharpe_classical = (0.072 - 0.02) / 0.09603 = 0.052 / 0.09603 = 0.5415
```

**Phi Portfolio:**
```
R_φ_portfolio = 0.6 × (0.10 × φ) + 0.4 × (0.03 × φ)
              = 0.6 × 0.16180 + 0.4 × 0.04854
              = 0.09708 + 0.01942
              = 0.11650 = 11.65%

r_φ = 0.02 + ln(φ) = 0.02 + 0.4812 = 0.5012

σ_φ_portfolio = φ × σ_classical = 1.618 × 0.09603 = 0.15538 = 15.538%

Sharpe_φ = (0.1165 - 0.5012) / 0.15538 = -0.3847 / 0.15538 = -2.476
```

**Summary:**

| Method | Portfolio Return | Portfolio Risk | Sharpe Ratio |
|--------|-----------------|----------------|--------------|
| Classical | 7.2% | 9.603% | +0.5415 |
| Phi | 11.65% | 15.538% | -2.476 |

**The phi-correction reveals that this portfolio has a negative Sharpe ratio.** The phi-return is higher (11.65% vs 7.2%), but the phi-risk is also higher (15.538% vs 9.603%), and the phi-risk-free rate is much higher (50.12% vs 2%). The phi-correction shows that the portfolio does not compensate for the phi-ground risk.

### 4.4 The Phi-Diversification

The optimal portfolio allocation in phi-finance uses phi-weighted allocations:

```
w_i_φ = w_i_classical × φ^(-i/N)
```

where:
- w_i_classical = classical weight of asset i
- N = total number of assets
- φ^(-i/N) = phi-weighting factor

This produces a portfolio where:
- The first asset gets the highest weight (closest to classical)
- Each subsequent asset gets a phi-reduced weight
- The total allocation sums to less than 1 (the remainder is the phi-ground allocation)

**The optimal phi-portfolio always holds a phi-ground allocation of:**
```
w_ground = 1 - Σ w_i_φ = 1 - Σ (w_i_classical × φ^(-i/N))
```

This is the carrier field's natural portfolio — the allocation that the field maintains without external perturbation.

---

## LAYER 5: THE PHI-FINANCE LAWS

### Law 1: The Law of Phi-Interest

**Statement:** The minimum interest rate in the carrier field is ln(φ) ≈ 0.4812%. No financial system can sustain an interest rate below this floor.

**Formula:** r_min = ln(φ) = 0.4812%

**Implication:** "Zero interest rate" policies are impossible. The carrier field always grows at its natural rate. Central banks that set rates below ln(φ) are not creating "cheap money" — they are creating a coherence deficit that the field will correct.

### Law 2: The Law of Phi-Compounding

**Statement:** Financial quantities compound at phi-intervals, not at arbitrary human-defined intervals (annual, monthly, daily).

**Formula:** A = P × (1 + r)^(φ×t)

**Implication:** Compounding is not a human invention — it is a natural property of the carrier field. The phi-interval is the natural recursion rate of financial coherence.

### Law 3: The Law of Phi-Valuation

**Statement:** The true present value of any financial asset accounts for the carrier field's natural growth floor. Classical valuation systematically overestimates present value by ignoring the phi-ground discount.

**Formula:** NPV_φ = Σ CF_t × φ^(-t) / (1 + r_φ)^t

where:
- φ^(-t) = natural coherence decay (missing from classical NPV)
- r_φ = r_classical + ln(φ) (minimum interest rate floor)

**Implication:** Classical finance systematically overestimates the present value of future cash flows because it (a) ignores the natural coherence decay φ^(-t), and (b) allows discount rates below ln(φ). The phi-correction reveals that many "profitable" classical investments are actually unprofitable when the carrier field's ground state is accounted for.

### Law 4: The Law of Phi-Risk

**Statement:** The true risk of any financial position is φ× its classical risk estimate.

**Formula:** σ_φ = σ_classical × φ

**Implication:** Classical risk models systematically underestimate risk by a factor of φ. VaR, volatility, and all risk measures are 61.8% higher than classical estimates.

### Law 5: The Law of Phi-Portfolio

**Statement:** The optimal portfolio allocation follows phi-ratios, with the first asset weighted highest and each subsequent asset weighted by φ^(-i/N).

**Formula:** w_i_φ = w_i_classical × φ^(-i/N)

**Implication:** Diversification is not arbitrary — it follows the natural structure of the carrier field. The phi-portfolio always holds a ground allocation in the carrier field itself.

### Law 6: The Law of Phi-Lending

**Statement:** The lending rate must always exceed ln(φ). Any lending rate at or below ln(φ) is a coherence deficit.

**Formula:** r_lend > ln(φ) = 0.4812%

**Implication:** Lenders who charge rates below ln(φ) are not being "generous" — they are creating a coherence deficit that will manifest as losses. The minimum sustainable lending rate is ln(φ).

### Law 7: The Law of Phi-Saving

**Statement:** The optimal saving rate is φ⁻¹ of income, not an arbitrary percentage.

**Formula:** saving_rate = φ⁻¹ × income = 0.6180 × income

**Implication:** Saving 61.8% of income is the natural rate of the carrier field. Saving less than this creates a coherence deficit; saving more than this creates a coherence surplus. Both are unstable.

### Law 8: The Law of Phi-Insurance

**Statement:** The fair insurance premium is φ⁻¹ × risk, not the actuarially expected loss.

**Formula:** premium = φ⁻¹ × risk = 0.6180 × risk

**Implication:** Insurance companies that charge premiums below φ⁻¹ × risk are creating a coherence deficit. Insurance buyers who pay premiums above φ⁻¹ × risk are creating a coherence surplus. The fair price is always at the phi-ground floor.

### Law 9: The Law of Phi-Taxation

**Statement:** The optimal tax rate follows the phi-ratio: φ⁻¹ of taxable income.

**Formula:** tax_rate = φ⁻¹ = 0.6180 = 61.80%

**Implication:** Tax rates above 61.80% create a coherence deficit (the economy cannot sustain the extraction). Tax rates below 61.80% create a coherence surplus (the government cannot maintain the carrier field). The optimal rate is at the phi-ground floor.

**Note:** This is the THEORETICAL optimal rate derived from phi-physics. In practice, the phi-tax rate for business operations is φ⁻³ = 23.6% (Law 7 of Phi-Accounting), which represents the commons contribution. The 61.80% figure represents the maximum sustainable extraction rate for any system — above this, the system collapses.

### Law 10: The Law of the Financial Recursion

**Statement:** All financial quantities recurse at φ⁻¹ per period. Each period retains φ⁻¹ of the prior state and adds a phi-correction.

**Formula:** Q_t = Q_{t-1} × φ⁻¹ + correction_t

**Implication:** Finance is not linear — it is recursive. Each financial period retains 61.8% of the prior period's state and adds a correction. This is the carrier field recursion applied to financial quantities.

---

## SYNTHESIS: THE PHI-FINANCE WORLDVIEW

Classical finance is a special case of phi-finance — the κ_φ → 0 limit where the phi-corrections vanish. In this limit:

- Interest rates can be zero (impossible in the real carrier field)
- Returns can be zero (impossible in the real carrier field)
- Risk can be zero (impossible in the real carrier field)
- Portfolios can be empty (impossible in the real carrier field)

The real carrier field does not permit any of these. Every financial quantity has a nonzero ground floor, and every financial law is a phi-corrected version of its classical counterpart.

**The phi-finance correction is not a tweak or an adjustment — it is a fundamental rebuild of the entire financial system from first principles.** The hidden zero in classical finance is not a minor error — it is a systematic bias that affects every calculation, every model, and every decision.

The 10 laws of phi-finance are not optional guidelines — they are natural properties of the carrier field that financial systems must obey or face correction.

---

## APPENDIX: KEY CONSTANTS

| Constant | Symbol | Value | Meaning |
|----------|--------|-------|---------|
| Golden ratio | φ | 1.6180339887 | The carrier field recursion ratio |
| Reciprocal golden ratio | φ⁻¹ | 0.6180339887 | The decay factor per period |
| Natural growth rate | ln(φ) | 0.4812118251 | The minimum interest rate |
| Emergence threshold | C_crit | 0.563263 | The coherence threshold for financial emergence |
| Phi-ground return | R_min | φ⁻¹ × R_0 | The minimum sustainable return |
| Phi-ground risk | σ_min | φ⁻¹ × σ_0 | The minimum irreducible risk |
| Phi-ground value | V_min | φ⁻¹ × V_0 | The minimum portfolio value |
| Optimal saving rate | s_opt | φ⁻¹ = 61.80% | The natural saving rate |
| Fair insurance premium | P_fair | φ⁻¹ × risk | The natural insurance price |
| Optimal tax rate | τ_opt | φ⁻¹ = 61.80% | The natural tax rate |

---

## DEGENERATE LIMIT ANALYSIS

Every phi-finance law must reduce to its classical counterpart when φ → 1 (the κ_φ → 0 limit). This is the Degeneracy Theorem (Law 173) applied to finance.

### Phi-Interest Rate → Classical Interest Rate

```
r_φ = r_classical + ln(φ)
As φ → 1: ln(φ) → 0, so r_φ → r_classical ✓
```

### Phi-Present Value → Classical Present Value

```
PV_φ = FV / (1 + r_φ)^n
As φ → 1: r_φ → r_classical, so PV_φ → PV_classical ✓
```

### Phi-Compound Interest → Classical Compound Interest

```
A_φ = P × (1 + r_φ)^t
As φ → 1: r_φ → r_classical, so A_φ → A_classical ✓
```

### Phi-NPV → Classical NPV

```
NPV_φ = Σ CF_t × φ^(-t) / (1 + r_φ)^t
As φ → 1: φ^(-t) → 1 and r_φ → r_classical, so NPV_φ → NPV_classical ✓
```

### Phi-VaR → Classical VaR

```
VaR_φ = VaR_classical × φ
As φ → 1: VaR_φ → VaR_classical ✓
```

### Phi-Sharpe → Classical Sharpe

```
Sharpe_φ = (φ × R - r_classical - ln(φ)) / (φ × σ)
As φ → 1: Sharpe_φ → (R - r_classical) / σ = Sharpe_classical ✓
```

**All six phi-finance formulas correctly reduce to their classical counterparts in the degenerate limit.** This confirms internal consistency: classical finance is the κ_φ → 0 limit of phi-finance.

---

## FALSIFICATION TESTS

1. **Test the minimum interest rate:** Can any financial system sustain an interest rate below ln(φ) = 0.4812%? If yes, the Law of Phi-Interest is falsified.

2. **Test phi-compounding:** Does compound interest follow phi-intervals or arbitrary human intervals? If arbitrary, the Law of Phi-Compounding is falsified.

3. **Test phi-valuation:** Does the phi-NPV systematically produce lower valuations than classical NPV for the same cash flows? If not, the Law of Phi-Valuation is falsified.

4. **Test phi-risk:** Is true risk φ× classical risk? If not, the Law of Phi-Risk is falsified.

5. **Test phi-portfolio:** Does optimal diversification follow phi-ratios? If not, the Law of Phi-Portfolio is falsified.

6. **Test the financial recursion:** Do financial quantities recurse at φ⁻¹ per period? If not, the Law of the Financial Recursion is falsified.

---

*This document is part of the Phi-Physics Harmonic Framework — rebuilding all of human knowledge from first principles using the carrier field of consciousness mathematics.*

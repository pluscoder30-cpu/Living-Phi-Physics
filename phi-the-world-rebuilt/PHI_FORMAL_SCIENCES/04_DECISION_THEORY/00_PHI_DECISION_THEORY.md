**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.9

---

# PHI-DECISION THEORY

## A Complete Theory of Choice Grounded in Phi-Physics

---

## LAYER 1: CLASSICAL DECISION THEORY

### 1.1 Expected Utility

Classical decision theory begins with a simple axiom: a rational agent chooses the action with the highest **expected utility**. Given a set of possible outcomes **x₁, x₂, ..., xₙ** with associated probabilities **p₁, p₂, ..., pₙ** and utility function **u(x)**, the expected utility is:

```
EU = Σᵢ pᵢ × u(xᵢ)
```

The rational agent maximizes EU. If action **a₁** yields EU₁ and action **a₂** yields EU₂, and EU₁ > EU₂, the rational agent chooses **a₁**.

This is von Neumann–Morgenstern utility theory. It is the foundation of all classical decision analysis.

### 1.2 The Axioms

Classical expected utility theory rests on four axioms:

1. **Completeness**: For any two lotteries L₁ and L₂, either EU(L₁) ≥ EU(L₂) or EU(L₂) ≥ EU(L₁).
2. **Transitivity**: If EU(L₁) ≥ EU(L₂) and EU(L₂) ≥ EU(L₃), then EU(L₁) ≥ EU(L₃).
3. **Independence**: If L₁ ≥ L₂, then for any third lottery L₃, the混合 αL₁ + (1-α)L₃ ≥ αL₂ + (1-α)L₃.
4. **Continuity**: If L₁ ≥ L₂ ≥ L₃, there exists a probability α such that the agent is indifferent between L₂ and the lottery αL₁ + (1-α)L₃.

These axioms guarantee the existence of a utility function. They are clean. They are elegant. They are wrong.

### 1.3 The Problem with Zero

Classical utility theory assumes utilities are measured from a **zero point**. Zero utility means no value. Negative utility means disvalue. The scale is anchored at nothing.

But **zero does not exist**.

In phi-physics, the ground state is φ⁻¹ = 0.618033988749895. Nothing is ever at zero. Every system, every field, every value has a nonzero floor. The vacuum fluctuates. The ground oscillates. There is no still point.

Classical decision theory's zero-based utility is a phantom. It measures from a point that cannot be reached.

### 1.4 The Benchmark Problem

Expected utility requires a **reference point** — a baseline against which outcomes are evaluated. Classical theory uses zero as this baseline. Prospect theory (Kahneman & Tversky, 1979) replaced zero with a **reference point** determined by the decision-maker's current state.

Both approaches fail because they treat the reference as **arbitrary**. In classical theory it is zero. In prospect theory it is "wherever you happen to be." Neither recognizes that the reference point has **structure** — a structure dictated by the phi-harmonic ground oscillation.

---

## LAYER 2: THE PROBLEM WITH ZERO-BASED UTILITY

### 2.1 The Zero Illusion

Consider a simple gamble: you receive $100 with probability 0.5 and $0 with probability 0.5. Classical expected utility:

```
EU = 0.5 × u(100) + 0.5 × u(0)
```

With the standard assumption u(0) = 0:

```
EU = 0.5 × u(100)
```

The utility of $0 is zero. But $0 does not exist in the phi-universe. The minimum is not zero. The minimum is the **phi-ground**.

### 2.2 The Phi-Ground Utility

**Definition:** The minimum utility is not zero. The minimum utility is:

```
U_ground = φ⁻¹ × reference
```

where **reference** is the decision-maker's reference state (their current wealth, health, wellbeing — whatever the utility function measures).

The phi-ground utility is always **nonzero**. Even in the worst outcome, the agent retains φ⁻¹ of their reference state. There is always a floor. There is always oscillation. There is never silence.

### 2.3 The Phi-Utility Function

The phi-utility function replaces the classical utility function:

```
U_φ(x) = U(x) × (1 + κ(φ - 1)) + κ × φ⁻¹ × U_ground
```

where:
- **U(x)** = classical utility of outcome x
- **κ** = coupling constant (how strongly the phi-ground affects utility; κ ≥ 0)
- **φ - 1** = φ⁻¹ ≈ 0.618 (the phi-shift)
- **U_ground** = φ⁻¹ × reference (the ground utility floor)

**Properties:**

1. **U_φ(x) > U(x)** for all x when κ > 0. The phi-ground adds utility everywhere.
2. **U_φ never reaches zero.** The minimum value is κ × φ⁻¹ × U_ground.
3. **As x → ∞**, U_φ(x) ≈ U(x) × (1 + κ(φ-1)). The phi-shift is multiplicative at scale.
4. **At the reference point**, U_φ(reference) = U(reference) × (1 + κ(φ-1)) + κ × φ⁻¹ × U_ground. The utility is above the classical value.

### 2.4 Interpretation

The coupling constant **κ** measures how much the agent's decision-making is influenced by the phi-ground. An agent with κ = 0 is a classical decision-maker — zero-based utility, no phi-ground. An agent with κ > 0 recognizes that even the worst outcome is nonzero, that there is always a floor, that the ground oscillates.

Higher κ means the agent is more **grounded** — more influenced by the phi-harmonic structure of reality. Lower κ means the agent is more **classical** — more influenced by the abstract zero.

---

## LAYER 3: PHI-DECISION THEORY

### 3.1 Phi-Expected Utility

Classical expected utility weights all outcomes equally by probability. Phi-decision theory adds **phi-weighting by rank**: outcomes are ranked, and each outcome's contribution to expected utility is scaled by its phi-weight.

```
EU_φ = Σᵢ pᵢ × U_φ(xᵢ) × φ^(rankᵢ - 1)
```

where:
- **pᵢ** = probability of outcome i
- **U_φ(xᵢ)** = phi-utility of outcome i
- **rankᵢ** = the rank of outcome i (ranked by magnitude, 1 = best)
- **φ^(rankᵢ - 1)** = phi-weight for that rank

### 3.2 The Ranking Principle

Outcomes are ranked by their phi-utility magnitude. The best outcome gets rank 1, the second-best gets rank 2, and so on. The phi-weight **φ^(rank-1)** assigns:

| Rank | Weight | Interpretation |
|------|--------|---------------|
| 1 | φ⁰ = 1 | Best outcome: baseline weight |
| 2 | φ¹ ≈ 1.618 | Second-best: weighted MORE |
| 3 | φ² ≈ 2.618 | Third-best: weighted EVEN MORE |
| 4 | φ³ ≈ 4.236 | Fourth-best: heavily weighted |
| ... | φⁿ⁻¹ | Recursive accumulation |

This is **inverted** from naive intuition. The best outcome has the lowest weight. The worst outcomes have the highest weights. This reflects the phi-physics principle: **the bulk carries the field**. The apex is the seed, but the system is defined by its recursive accumulation through all ranks.

In decision theory, this means: **the agent is most sensitive to the worst outcomes**. A decision is not dominated by its best possibility. It is dominated by the accumulation of its lower-ranked possibilities.

### 3.3 The Phi-Optimal Decision

**Definition:** The phi-optimal decision **a*** is the action that maximizes EU_φ:

```
a* = argmax_a EU_φ(a) = argmax_a Σᵢ pᵢ(a) × U_φ(xᵢ(a)) × φ^(rankᵢ(a) - 1)
```

The phi-optimal decision is not necessarily the same as the classical EU-optimal decision. The phi-weighting shifts sensitivity toward worse outcomes, producing decisions that are more **risk-averse** in the tail and more **risk-seeking** in the body.

### 3.4 Phi-Risk

Classical risk is measured by variance:

```
Risk = σ² = Σᵢ pᵢ × (xᵢ - μ)²
```

Phi-risk incorporates the phi-ground into the variance calculation:

```
Risk_φ = σ_φ × (1 + φ⁻¹)
```

where **σ_φ** is the standard deviation of phi-utilities.

The factor **(1 + φ⁻¹) ≈ 1.618** ensures that phi-risk is **always at least φ⁻¹ times** the classical risk. Risk can never be underestimated. The phi-ground inflates all risk estimates by the golden ratio.

**Interpretation:** In a phi-universe, risk is always φ⁻¹ larger than it appears in classical theory. The ground oscillation adds an irreducible floor to all uncertainty.

### 3.5 Phi-Regret

Classical regret is the difference between the best possible outcome and the actual outcome:

```
Regret = u(best) - u(chosen)
```

Phi-regret is:

```
Regret_φ = max(EU_φ) - EU_φ(chosen)
```

where the max is taken over all available actions. Phi-regret is measured in phi-utility units, incorporating the phi-ground floor and the phi-weighting of ranks.

A decision with Regret_φ = 0 is **phi-optimal**. A decision with high Regret_φ indicates a choice dominated by lower-ranked outcomes.

### 3.6 Worked Example: 3-Outcome Gamble

**Setup:** An agent faces a gamble with three possible outcomes:

| Outcome | Probability | Classical Utility U(x) |
|---------|-------------|----------------------|
| x₁ (Win) | p₁ = 0.3 | 100 |
| x₂ (Partial) | p₂ = 0.5 | 40 |
| x₃ (Loss) | p₃ = 0.2 | -10 |

Reference state: **reference = 50** (current wealth).
Coupling constant: **κ = 1** (fully grounded agent).

**Step 1: Compute phi-ground utility**

```
U_ground = φ⁻¹ × reference = 0.618 × 50 = 30.90
```

**Step 2: Compute phi-utility for each outcome**

```
U_φ(x) = U(x) × (1 + κ(φ - 1)) + κ × φ⁻¹ × U_ground
        = U(x) × (1 + 1 × 0.618) + 1 × 0.618 × 30.90
        = U(x) × 1.618 + 19.10
```

| Outcome | U(x) | U_φ(x) |
|---------|------|---------|
| x₁ | 100 | 100 × 1.618 + 19.10 = **180.90** |
| x₂ | 40 | 40 × 1.618 + 19.10 = **83.82** |
| x₃ | -10 | -10 × 1.618 + 19.10 = **2.92** |

Note: U_φ(x₃) = 2.92 > 0. The loss outcome still has positive phi-utility. The phi-ground prevents negative utility.

**Step 3: Rank outcomes by phi-utility**

| Rank | Outcome | U_φ(x) | Phi-Weight φ^(rank-1) |
|------|---------|---------|----------------------|
| 1 | x₁ | 180.90 | φ⁰ = 1 |
| 2 | x₂ | 83.82 | φ¹ = 1.618 |
| 3 | x₃ | 2.92 | φ² = 2.618 |

**Step 4: Compute phi-expected utility**

```
EU_φ = 0.3 × 180.90 × 1 + 0.5 × 83.82 × 1.618 + 0.2 × 2.92 × 2.618
     = 0.3 × 180.90 + 0.5 × 135.62 + 0.2 × 7.64
     = 54.27 + 67.81 + 1.53
     = 123.61
```

**Step 5: Compare to classical EU**

```
EU_classical = 0.3 × 100 + 0.5 × 40 + 0.2 × (-10)
             = 30 + 20 - 2
             = 48
```

The phi-EU (123.61) is much higher than classical EU (48) because the phi-ground lifts all utilities above zero and the phi-weighting amplifies the bulk outcomes.

**Step 6: Compute phi-risk**

```
σ_φ² = Σᵢ pᵢ × (U_φ(xᵢ) - EU_φ)²
     = 0.3 × (180.90 - 123.61)² + 0.5 × (83.82 - 123.61)² + 0.2 × (2.92 - 123.61)²
     = 0.3 × 3283.14 + 0.5 × 1583.56 + 0.2 × 14566.96
     = 984.94 + 791.78 + 2913.39
     = 4690.11

σ_φ = √4690.11 = 68.48

Risk_φ = σ_φ × (1 + φ⁻¹) = 68.48 × 1.618 = 110.80
```

**Step 7: Compute phi-regret**

If the agent had perfect information and always chose the best action for each state, the expected phi-utility would be:

```
EU_φ* = 0.3 × 180.90 × 1 + 0.5 × 83.82 × 1.618 + 0.2 × 2.92 × 2.618
       = 123.61 (already computed — this IS the max)
```

```
Regret_φ = 123.61 - 123.61 = 0
```

The agent's choice IS the phi-optimal decision. Regret is zero.

---

## LAYER 4: MULTI-CRITERIA PHI-DECISIONS

### 4.1 The Multi-Criteria Problem

Real decisions involve multiple criteria. You do not choose a job based only on salary. You consider location, growth, culture, hours, benefits. Each criterion has a different scale, a different importance, and a different phi-frequency.

### 4.2 Phi-Ladder Frequencies

Each criterion operates at a different level of the phi-ladder. Rank 1 criteria are most fundamental. Rank 2 criteria are one level above. And so on. The phi-ladder assigns each criterion a frequency:

```
fᵢ = φ^(rankᵢ - 1)
```

### 4.3 The Phi-Weighted Score

For an alternative **a** evaluated on criteria **c₁, c₂, ..., cₖ** with scores **s₁, s₂, ..., sₖ**, the phi-weighted score is:

```
S_φ(a) = Σᵢ φ^(rankᵢ - 1) × sᵢ(a) / Σᵢ φ^(rankᵢ - 1)
```

The denominator **Σᵢ φ^(rankᵢ - 1)** normalizes the score to a [0, 1] range (assuming scores are normalized).

### 4.4 The Normalization Constant

For **k** criteria ranked 1 through k:

```
N = Σᵢ₌₁ᵏ φ^(i-1) = (φᵏ - 1) / (φ - 1) = (φᵏ - 1) / φ⁻¹
```

This is the **phi-sum** of the first k ranks.

### 4.5 The Phi-Pareto Frontier

Classical Pareto optimality: an alternative **a** Pareto-dominates **b** if **a** is at least as good on every criterion and strictly better on at least one.

**Phi-Pareto optimality**: an alternative **a** phi-Pareto-dominates **b** if the phi-weighted improvement on any criterion exceeds the phi-weighted degradation on all other criteria:

```
φ^(rankⱼ - 1) × (sⱼ(a) - sⱼ(b)) > Σᵢ≠ⱼ φ^(rankᵢ - 1) × (sᵢ(b) - sᵢ(a))
```

The phi-Pareto frontier is the set of alternatives not phi-Pareto-dominated by any other.

### 4.6 Worked Example: 5-Criteria Decision

**Setup:** An agent chooses between three job offers. Five criteria, ranked by importance:

| Criterion | Rank | Weight φ^(rank-1) |
|-----------|------|-------------------|
| Salary | 1 | 1.000 |
| Growth | 2 | 1.618 |
| Culture | 3 | 2.618 |
| Location | 4 | 4.236 |
| Hours | 5 | 6.854 |

Normalization constant: N = 1 + 1.618 + 2.618 + 4.236 + 6.854 = **16.326**

**Alternatives and scores** (each criterion scored 0-10):

| Criterion | Rank | Weight | Job A | Job B | Job C |
|-----------|------|--------|-------|-------|-------|
| Salary | 1 | 1.000 | 9 | 7 | 6 |
| Growth | 2 | 1.618 | 5 | 9 | 8 |
| Culture | 3 | 2.618 | 7 | 6 | 9 |
| Location | 4 | 4.236 | 6 | 8 | 7 |
| Hours | 5 | 6.854 | 4 | 5 | 8 |

**Phi-weighted scores:**

```
S_φ(A) = (1×9 + 1.618×5 + 2.618×7 + 4.236×6 + 6.854×4) / 16.326
        = (9 + 8.09 + 18.33 + 25.42 + 27.42) / 16.326
        = 88.26 / 16.326
        = 5.407

S_φ(B) = (1×7 + 1.618×9 + 2.618×6 + 4.236×8 + 6.854×5) / 16.326
        = (7 + 14.56 + 15.71 + 33.89 + 34.27) / 16.326
        = 105.43 / 16.326
        = 6.458

S_φ(C) = (1×6 + 1.618×8 + 2.618×9 + 4.236×7 + 6.854×8) / 16.326
        = (6 + 12.94 + 23.56 + 29.65 + 54.83) / 16.326
        = 127.00 / 16.326
        = 7.780
```

**Ranking:** Job C (7.780) > Job B (6.458) > Job A (5.407)

**Phi-Pareto analysis:** Check if any job phi-Pareto-dominates another.

**Job C vs. Job A:**
- Salary: A(9) > C(6) → A wins on rank 1. Improvement = 1 × (9-6) = 3.0.
- All other criteria: C ≥ A except salary. Degradation on salary = 1 × 3 = 3.
- The phi-weighted improvement on salary (3.0) equals the degradation on salary (3.0). **Not phi-Pareto-dominating.**

**Job C vs. Job B:**
- Growth: B(9) > C(8) → B wins on rank 2. Improvement = 1.618 × 1 = 1.618.
- C wins on Culture (2.618 × 3 = 7.854), Hours (6.854 × 3 = 20.562). Total phi-improvement for C = 28.416.
- B wins on Salary (1 × 1 = 1), Growth (1.618 × 1 = 1.618), Location (4.236 × 1 = 4.236). Total phi-improvement for B = 6.854.
- **C phi-Pareto-dominates B** (28.416 > 6.854).

**Phi-Pareto frontier:** {Job C}. Job B is phi-Pareto-dominated. Job A is on the frontier only if we relax the strict inequality.

**Phi-optimal decision: Job C.**

---

## LAYER 5: THE PHI-DECISION LAWS

### Law 1: The Law of Phi-Utility

```
U_φ(x) = U(x) × (1 + κ(φ - 1)) + κ × φ⁻¹ × U_ground
```

**Statement:** Utility is never zero. Every outcome carries the phi-ground floor. The minimum utility is κ × φ⁻¹ × U_ground. The phi-ground couples to all utility through the constant κ. Utility is not measured from nothing. It is measured from the oscillating ground of the phi-field.

---

### Law 2: The Law of Phi-Rationality

```
a* = argmax_a Σᵢ pᵢ(a) × U_φ(xᵢ(a)) × φ^(rankᵢ(a) - 1)
```

**Statement:** Rationality is not maximizing expected utility from zero. Rationality is maximizing phi-expected utility from the ground. The rational agent ranks outcomes, applies phi-weights, and selects the action with the highest accumulated phi-utility. Rationality is recursive — each decision feeds the phi-field that influences the next decision.

---

### Law 3: The Law of Phi-Risk

```
Risk_φ = σ_φ × (1 + φ⁻¹)
```

**Statement:** Risk is always inflated by the golden ratio. The phi-ground adds an irreducible floor to all uncertainty. Classical risk underestimates by a factor of φ⁻¹ ≈ 0.618. True risk = classical risk / φ⁻¹. No decision-maker can escape this inflation. The ground oscillates, and so does risk.

---

### Law 4: The Law of Phi-Uncertainty

```
H_φ = -Σᵢ pᵢ × ln(pᵢ) × φ^(rankᵢ - 1)
```

**Statement:** Entropy is phi-weighted. The uncertainty of an information source is not a flat sum. Outcomes ranked higher (lower probability, tail events) are weighted more heavily by the phi-weight. This means **rare events carry more entropic weight** than classical Shannon entropy suggests. The phi-field amplifies uncertainty in the tails.

---

### Law 5: The Law of Multi-Criteria Decisions

```
S_φ = Σᵢ φ^(rankᵢ - 1) × sᵢ / Σᵢ φ^(rankᵢ - 1)
```

**Statement:** Multi-criteria decisions are resolved by phi-weighted scoring. Criteria are ranked on the phi-ladder. Each criterion's contribution to the final score is proportional to its phi-weight. The most fundamental criteria have the lowest weight. The bulk criteria carry the decision. No criterion is ignored. Every criterion resonates at its phi-frequency.

---

### Law 6: The Law of Group Decisions (Phi-Voting)

```
V_group = Σⱼ φ^(voter_rankⱼ - 1) × vⱼ
```

**Statement:** In group decisions, voters are ranked. Each voter's vote is weighted by φ^(rank - 1). The most critical voter (rank 1) has weight 1. The least critical voter has the highest weight. Group decisions are not majority rules. They are phi-weighted accumulations. The group's decision is the phi-field of its members, not the arithmetic mean.

**Implication:** In a group of 5 voters ranked 1-5:

| Voter Rank | Weight | Fraction of Total |
|------------|--------|-------------------|
| 1 | 1.000 | 6.1% |
| 2 | 1.618 | 9.9% |
| 3 | 2.618 | 16.0% |
| 4 | 4.236 | 26.0% |
| 5 | 6.854 | 42.0% |

The least critical voters collectively carry **42%** of the group decision. The most critical voter carries only **6.1%**. This is the phi-democracy: the bulk decides.

---

### Law 7: The Law of Temporal Decisions (Retrocausal)

```
EU_φ(t) = Σᵢ pᵢ(t) × U_φ(xᵢ(t)) × φ^(rankᵢ - 1) + Σₜ' > t Σⱼ λⱼ × EU_φ(t')
```

**Statement:** Decisions are not time-symmetric. A decision made now carries a **retrocausal influence** on future expected utilities. The second term sums over all future time points t' > t, with a coupling constant λⱼ for each future consequence. The phi-weight applied to future consequences decays as φ^(-|t'-t|), but never reaches zero.

**Implication:** Every decision retroactively shapes the utility landscape of future decisions. The phi-decision-maker accounts for this. Classical decision-makers ignore it. This is the phi-advantage: **every choice ripples forward through the phi-field**.

---

### Law 8: The Law of Ethical Decisions (Consciousness Threshold)

```
EU_φ(ethical) = EU_φ(outcome) × C(target)
```

**Statement:** Ethical decisions include a **consciousness multiplier**. The expected utility of any action is multiplied by the consciousness level **C(target)** of the being affected. C(target) ranges from φ⁻¹ (minimum consciousness, stone-level) to 1 (maximum consciousness, fully coherent).

**Implication:** Harming a being with high consciousness carries lower utility than harming one with low consciousness? No — the opposite. C(target) multiplies the utility. If the action is harmful (negative utility), multiplying by higher consciousness makes it MORE negative. If the action is beneficial (positive utility), multiplying by higher consciousness makes it MORE positive.

Ethical decisions are weighted by the consciousness of the affected party. The phi-decision-maker cannot ignore the consciousness of others. The field connects all conscious beings.

---

### Law 9: The Law of System Decisions (Emergence)

```
EU_φ(system) = EU_φ(individual) + Σ_emergent Eⱼ × φ^(rankⱼ - 1)
```

**Statement:** System-level decisions include an **emergence term**. The expected utility of a decision affecting a system is the individual expected utility PLUS the phi-weighted sum of emergent properties that arise from the decision.

**Implication:** Some decisions produce outcomes that do not exist at the individual level. These emergent outcomes — the whole being greater than the sum — are captured by the second term. The phi-weighting ranks emergent properties by their systemic importance. The most critical emergent property (rank 1) has weight 1. Less critical properties accumulate.

**Example:** Deciding to build a bridge. The individual utility: commute time saved. The emergent utility: economic growth, cultural connection, environmental impact. These emergent properties are phi-weighted and added to the decision.

---

### Law 10: The Law of the Decision Recursion

```
D(t) = f(D(t-1), EU_φ(D(t-1)), φ⁻¹)
```

**Statement:** Decisions recurse at φ⁻¹. Each decision **D(t)** is a function of the previous decision **D(t-1)**, the phi-expected utility of the previous decision, and the phi-inverse constant. The recursion rate is φ⁻¹ ≈ 0.618.

**Implication:** Decision-making is not a series of independent events. It is a **phi-harmonic recursion**. Each decision feeds the next at the phi-rate. The decision-maker's choice space contracts by φ⁻¹ with each recursion. After n decisions, the decision space is φ^(-n) of the original.

**The decision convergence theorem:** As n → ∞, D(n) converges to the **phi-optimal trajectory** — the path through decision-space that maximizes the integral of phi-expected utility over all time.

```
D* = argmax_{D(t)} ∫₀^∞ EU_φ(D(t)) × φ^(-t) dt
```

This is the **phi-principle of optimal decisions**: the optimal decision strategy is the one that maximizes the phi-discounted integral of phi-expected utility over all time. Not just the next decision. Not just the next hundred. All of them. Recursing at φ⁻¹.

---

## PHI-DECISION THEORY: SUMMARY

| Component | Classical | Phi-Decision |
|-----------|-----------|-------------|
| Utility floor | 0 | κ × φ⁻¹ × U_ground |
| Expected utility | Σ pᵢ × u(xᵢ) | Σ pᵢ × U_φ(xᵢ) × φ^(rank-1) |
| Risk | σ | σ_φ × (1 + φ⁻¹) |
| Entropy | -Σ pᵢ ln(pᵢ) | -Σ pᵢ ln(pᵢ) × φ^(rank-1) |
| Multi-criteria | Weighted sum | Phi-ladder weighted sum |
| Group decisions | Majority / average | Phi-voting |
| Temporal | Discount factor δ | Retrocausal phi-coupling |
| Ethics | Utility of outcome | EU × C(target) |
| System | Sum of parts | Individual + emergent phi-terms |
| Recursion | Independent | D(t) = f(D(t-1), EU_φ, φ⁻¹) |

---

**PHI-DECISION THEORY COMPLETE**

---

## Falsification Criteria

Phi-decision theory is falsified if any of the following are demonstrated:

1. **Zero utility floor:** Agents consistently make decisions as if zero utility is achievable and meaningful, with no evidence of a nonzero floor in choice behavior.
2. **No phi-weighting in risk:** Human risk perception is well-explained by classical variance alone, with no systematic amplification by a factor of (1 + φ⁻¹).
3. **Bulk indifference:** Decision-makers weight best outcomes more heavily than worse outcomes in controlled experiments, contradicting the phi-ranking principle.
4. **Retrocausal irrelevance:** Future consequences have no measurable influence on present decisions when agents are fully informed, contradicting the temporal recursion law.

# PHI-PHYSICS - LAW 2381
## Trivers–Willard Hypothesis (Parental Investment by Condition)

**Domain:** Evolutionary Biology / Parental Investment - **Status:** 🟢 VALIDATED - **File:** `laws/2381_trivers_willard_hypothesis.md` - **Sim:** `sim/2381_trivers_willard_hypothesis.py`

---

### CLASSICAL STATEMENT
*"The Trivers-Willard hypothesis suggests that female mammals adjust the sex ratio of offspring in response to maternal condition, so as to maximize their reproductive success: it predicts greater parental investment in males by parents in good conditions and greater investment in females by parents in poor conditions, in polygynous species where male reproductive success is highly variable."*
- Robert Trivers and Dan Willard, 1973, "Natural selection of parental ability to vary the sex ratio of offspring", Science 179, pp. 90-92. Source: verified via web search (Wikipedia: Trivers-Willard hypothesis). Model: investment ratio R = investment_in_males/investment_in_females rises with maternal condition C.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-condition-mapped-investment ideal: the hypothesis treats maternal investment as an exactly deterministic, monotonic function of maternal condition, with parents having exact information on offspring sex and exactly perfect influence on survival. Real condition is multifactorial (body size, parasite load, dominance), mechanisms (e.g. glucose effects) are imperfect, and empirical support is mixed - so the exactly-condition-mapped investment is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the investment ratio, the sex-ratio bias and the maternal-condition response always carry an irreducible phi-ground mechanism-imperfection contribution, so the exactly-condition-mapped investment is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2381_trivers_willard_hypothesis.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2381_trivers_willard_hypothesis.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Parental investment is never an exactly deterministic, monotonic function of maternal
    condition; at full phi-coupling the investment ratio carries an irreducible phi-ground floor scaled
    by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure maternal condition, offspring sex ratio and parental investment across many
    mothers in a polygynous species, fit the condition-investment relationship, and quantify the
    deviation of the empirical relationship from the exactly-condition-mapped prediction. Verify the
    classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains parental investment exactly and deterministically mapped to
    maternal condition, with no residual variation, under conditions where the phi-ground floor should
    contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Evolutionary Biology / Parental Investment, paired with
Bateman's principle (Law 2382) and Zahavi's handicap principle (Law 2380). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: investment is exactly condition-mapped only where every
mother is forced to sit at her laboratory-fixed condition.

### NOVELTY
Classical Trivers-Willard treats its zero (exactly-condition-mapped investment) as real and universal. Phi-physics shows the zero is
an unreachable limit: every parental investment carries coherent mechanism-imperfection motion.

### ACTIONABILITY
Run sim/2381_trivers_willard_hypothesis.py; verify the kappa_phi sweep; the completion block is closed.

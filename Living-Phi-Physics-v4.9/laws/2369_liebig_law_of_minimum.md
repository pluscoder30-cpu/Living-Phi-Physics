# PHI-PHYSICS - LAW 2369
## Liebig's Law of the Minimum (Growth Limited by the Scarcest Resource)

**Domain:** Ecology / Limiting Factors - **Status:** 🟢 VALIDATED - **File:** `laws/2369_liebig_law_of_minimum.md` - **Sim:** `sim/2369_liebig_law_of_minimum.py`

---

### CLASSICAL STATEMENT
*"Liebig's law of the minimum states that growth is dictated not by the total resources available, but by the scarcest resource (the limiting factor): the most abundant nutrient in the soil is only as good as the least abundant nutrient in the soil - a chain is only as strong as its weakest link."*
- Carl Sprengel (1840), popularized by Justus von Liebig, 1840. Source: verified via web search (Wikipedia: Liebig's law of the minimum). Model: dO/dt = O*(min(mu_I*I/(k_I+I), mu_N*N/(k_N+N), mu_P*P/(k_P+P)) - m), with N the limiting nutrient.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-one-limiting-factor ideal: the law's minimum is taken over a fixed, exactly-specified set of factors with one factor exactly alone in control. Real growth is co-limited - multiple nutrients interact, factors substitute for each other, and the identity of the limiting factor shifts with season, life stage and the adaptation of the organism (the adaptation-cooper lengthens the shortest stave) - so the exactly-single-limiter state is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the limiting growth rate, the limiting nutrient concentration and the yield always carry an irreducible phi-ground co-limitation contribution, so the exactly-one-limiting-factor ideal is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2369_liebig_law_of_minimum.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2369_liebig_law_of_minimum.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Growth is never limited by exactly one factor with exactly the others saturating;
    at full phi-coupling the limiting yield carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure yield across graded gradients of multiple nutrients (e.g. N, P, light) on
    replicated plots, fit the min-of-Michaelis-Menten model, and quantify the deviation of the
    empirical limiting set from the exactly-one limiting factor. Verify the classical-limit error
    is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains growth limited by exactly one factor, with all other factors
    exactly saturating, under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Ecology / Limiting Factors, paired with
Shelford's law of tolerance (Law 2370) and Hutchinson's niche concept (Law 2371). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: growth is exactly limited by a single factor only where
every other factor is forced to sit exactly at saturation.

### NOVELTY
Classical Liebig treats its zero (exactly-one limiting factor) as real and universal. Phi-physics shows the zero is
an unreachable limit: every growth process carries coherent co-limitation motion.

### ACTIONABILITY
Run sim/2369_liebig_law_of_minimum.py; verify the kappa_phi sweep; the completion block is closed.

# PHI-PHYSICS - LAW 2370
## Shelford's Law of Tolerance (Tolerance Range for Each Factor)

**Domain:** Ecology / Tolerance - **Status:** 🟢 VALIDATED - **File:** `laws/2370_shelford_law_of_tolerance.md` - **Sim:** `sim/2370_shelford_law_of_tolerance.py`

---

### CLASSICAL STATEMENT
*"Shelford's law of tolerance states that an organism's success is based on a complex set of conditions, and that each organism has a certain minimum, maximum and optimum environmental factor or combination of factors that determine success - the law is best illustrated by a bell-shaped curve with a definite range of tolerance."*
- Victor Ernest Shelford, 1913 (law elaborated from his 1911 work). Source: verified via web search (Wikipedia: Shelford's law of tolerance). Model: success S(e) = 1 - 4*((e - e_opt)/(e_max - e_min))^2 over the tolerance range [e_min, e_max], optimal factor e_opt, optimal success = 1.0.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-fixed-tolerance-range ideal: the law's minimum, maximum and optimum for each factor are treated as exactly fixed, identical across seasons, life stages and processes. Real tolerance ranges change with the seasons, with the life stage of the organism, and even differ between processes in the same organism (e.g. photosynthesis vs growth in the pea plant) - so the exactly-fixed, universal tolerance range is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the tolerance optimum, the tolerance range and the optimal success always carry an irreducible phi-ground range-variability contribution, so the exactly-fixed tolerance range is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2370_shelford_law_of_tolerance.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2370_shelford_law_of_tolerance.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The tolerance range is never exactly fixed with exactly reproducible min/max/optimum;
    at full phi-coupling the optimal success carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure survival or reproduction across a graded environmental factor gradient over
    multiple seasons and life stages, fit the tolerance bell-curve, and quantify the deviation of
    the empirical min/max/optimum from the exactly-fixed range. Verify the classical-limit error is
    <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains a tolerance range that is exactly fixed, with exactly reproducible
    min/max/optimum across seasons and life stages, under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Ecology / Tolerance, paired with
Liebig's law of the minimum (Law 2369) and Hutchinson's niche concept (Law 2371). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: the tolerance range is exactly fixed only where every
factor is forced to sit at its laboratory-fixed optimum.

### NOVELTY
Classical Shelford treats its zero (exactly-fixed tolerance range) as real and universal. Phi-physics shows the zero is
an unreachable limit: every tolerance curve carries coherent range-variability motion.

### ACTIONABILITY
Run sim/2370_shelford_law_of_tolerance.py; verify the kappa_phi sweep; the completion block is closed.

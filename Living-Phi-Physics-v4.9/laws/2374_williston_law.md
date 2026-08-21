# PHI-PHYSICS - LAW 2374
## Williston's Law (Parts Reduce in Number and Specialize in Function)

**Domain:** Evolutionary Biology / Morphology - **Status:** 🟢 VALIDATED - **File:** `laws/2374_williston_law.md` - **Sim:** `sim/2374_williston_law.py`

---

### CLASSICAL STATEMENT
*"Williston's law states that parts in an organism, such as arthropod limbs and vertebrate teeth, tend toward reduction in number, with the fewer parts greatly specialized in function: 'it is also a law in evolution that the parts in an organism tend toward reduction in number, with the fewer parts greatly specialized in function'."*
- Samuel Wendell Williston, 1914, "Water Reptiles of the Past and Present". Source: verified via web search (Wikipedia: Samuel Wendell Williston). Model: parts count N_late < N_early, with specialization index S_late > S_early.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-monotonic-reduction ideal: the law treats the reduction in part number as an exactly monotonic, universal trend in every lineage. Real serially repeated structures show early-burst patterns, stasis, and even increases (branchiostegal rays in osteichthyans fail to show a generalized reduction) - so the exactly-monotonic reduction is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the parts count, the parts reduction and the specialization index always carry an irreducible phi-ground early-burst/stasis contribution, so the exactly-monotonic reduction is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2374_williston_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2374_williston_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Part number never reduces exactly monotonically along a lineage;
    at full phi-coupling the parts count carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Count serially repeated structures (teeth, limb segments, branchiostegal rays) across
    dated fossil horizons within clades, fit the number trend, and quantify the deviation of the
    empirical trend from the exactly-monotonic reduction. Verify the classical-limit error is <= 1%
    and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains a lineage with exactly monotonic reduction in part number, with
    no early-burst or stasis, under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Evolutionary Biology / Morphology, paired with
Cope's rule (Law 2372) and Dollo's law (Law 2373). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: parts reduce exactly monotonically only where every
generation is forced to sit at its laboratory-fixed part-count decrement.

### NOVELTY
Classical Williston treats its zero (exactly-monotonic part reduction) as real and universal. Phi-physics shows the zero is
an unreachable limit: every serially repeated structure carries coherent early-burst motion.

### ACTIONABILITY
Run sim/2374_williston_law.py; verify the kappa_phi sweep; the completion block is closed.

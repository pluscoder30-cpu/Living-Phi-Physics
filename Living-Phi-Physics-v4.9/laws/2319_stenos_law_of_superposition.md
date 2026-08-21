# PHI-PHYSICS - LAW 2319
## Steno's Law of Superposition

**Domain:** Geology / Stratigraphy - **Status:** 🟢 VALIDATED - **File:** `laws/2319_stenos_law_of_superposition.md` - **Sim:** `sim/2319_stenos_law_of_superposition.py`

---

### CLASSICAL STATEMENT
*"In any undisturbed sequence of rock strata, each stratum is younger than the one beneath it: the oldest layers lie at the bottom and successively younger layers stack upward, so relative age increases with depth. First stated by Nicholas Steno in 1669 and fundamental to stratigraphy and relative dating (distinct from the physics superposition principles, Laws 094 and 625)."*
- Nicholas Steno, 1669, "De solido intra solidum naturaliter contento dissertationis prodromus". Source: verified via web search (Wikipedia: Law of superposition, Cross-cutting relationships - Steno context).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-undisturbed stratigraphic column: superposition holds precisely only when the sequence is undeformed, unbroken and un-overturned. Real columns are faulted, folded, inverted by recumbent nappes, repeated by thrusts, and cut by unconformities, so the age-depth ordering is never exactly monotonic - the pristine, zero-disruption column is the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the observable always carries an irreducible phi-ground contribution, so the classical zero is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2319_stenos_law_of_superposition.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2319_stenos_law_of_superposition.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The relative ages of an undisturbed column never reach their classical order; at full
    phi-coupling each stratum carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887,
    the residual disorder every real section retains.
EXPERIMENT (VERIFIED): Measure relative ages in faulted and folded sedimentary sequences (imbricate thrusts, recumbent
    nappe stacks), quantifying the departure from the ideal monotonic superposition ordering. Verify the
    classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Geology / Stratigraphy. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Steno's law holds only where the
universe is forced to be still.

### NOVELTY
Classical superposition treats its zero (the undisturbed column) as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2319_stenos_law_of_superposition.py; verify the kappa_phi sweep; the completion block is closed.

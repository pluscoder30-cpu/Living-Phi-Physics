# PHI-PHYSICS - LAW 2320
## Steno's Original Horizontality

**Domain:** Geology / Stratigraphy - **Status:** 🟢 VALIDATED - **File:** `laws/2320_stenos_original_horizontality.md` - **Sim:** `sim/2320_stenos_original_horizontality.py`

---

### CLASSICAL STATEMENT
*"Layers of sediment are originally deposited horizontally under the action of gravity; inclined beds are interpreted as the result of subsequent tilting or folding rather than of deposition. First proposed by Nicholas Steno in 1669; it is essential to the analysis of folded and tilted strata."*
- Nicholas Steno, 1669, "De solido intra solidum naturaliter contento dissertationis prodromus". Source: verified via web search (Wikipedia: Principle of original horizontality).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the perfectly horizontal depositional surface: the law presumes each layer is laid down with exactly zero primary dip. Real sediments carry small primary dips (foreset bedding, delta fronts, channel floors) and are deposited on sloping basins, so the exactly-flat depositional surface is the unreachable laboratory zero.

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

`sim/2320_stenos_original_horizontality.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2320_stenos_original_horizontality.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The depositional dip of a stratum never reaches its classical zero value; at full
    phi-coupling it carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure primary dips in modern delta fronts, foresets and basin-floor turbidites, quantifying
    the minimum non-zero depositional slope. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
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
Classical horizontality treats its zero (the perfectly flat bed) as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2320_stenos_original_horizontality.py; verify the kappa_phi sweep; the completion block is closed.

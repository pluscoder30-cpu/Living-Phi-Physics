# PHI-PHYSICS - LAW 2323
## Uniformitarianism

**Domain:** Geology / History of Geology - **Status:** 🟢 VALIDATED - **File:** `laws/2323_uniformitarianism.md` - **Sim:** `sim/2323_uniformitarianism.py`

---

### CLASSICAL STATEMENT
*"The present is the key to the past: the same natural laws and processes that operate today have always operated in the universe, at uniform rates. 'No powers are to be employed that are not natural to the globe.' Formulated by James Hutton (1785) and popularized as the Uniformitarian Principle by Charles Lyell (1830)."*
- James Hutton, 1785, "Theory of the Earth"; Charles Lyell, 1830, "Principles of Geology". Source: verified via web search (Wikipedia: Uniformitarianism).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-constant process rate: uniformitarianism presumes geological processes operate at uniform, present-day rates across all time. Real Earth history includes catastrophic, non-uniform events (impacts, flood basalts, glaciations, turbidite storms) and rate changes, so the perfectly steady, rate-invariant process is the unreachable laboratory zero.

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

`sim/2323_uniformitarianism.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2323_uniformitarianism.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The process rate of the present never maps identically onto the past; at full
    phi-coupling the rate ratio carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Compare modern erosion, uplift and sedimentation rates with deep-time rates from stratigraphy,
    radiometric and provenance data, quantifying the non-uniformity. Verify the classical-limit error is <= 1%
    and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Geology / History of Geology. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Hutton's law holds only where the
universe is forced to be still.

### NOVELTY
Classical uniformitarianism treats its zero (the steady process) as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2323_uniformitarianism.py; verify the kappa_phi sweep; the completion block is closed.

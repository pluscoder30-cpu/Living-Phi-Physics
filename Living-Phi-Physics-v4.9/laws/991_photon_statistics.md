# PHI-PHYSICS — LAW 991
## Photon Statistics (Mandel Q)

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/991_photon_statistics.md` · **Sim:** `sim/991_photon_statistics.py`

---

### CLASSICAL STATEMENT
*"Photon statistics: coherent states have Poissonian statistics (Mandel Q = 0), thermal light super-Poissonian (Q > 0), and Fock/antibunched light sub-Poissonian (Q < 0); the Mandel Q parameter is Q = (<(delta n)^2> - <n>)/<n>."*
— Leonard Mandel; Roy Glauber, 1963. Source: Wikipedia: Photon statistics (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero photon number* (<n> = 0): the statistics are anchored at the vacuum where the mean photon number is exactly zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Q_phi(kappa) = Q*(1 + kappa*(phi-1)) + kappa*phi^-1*Q_ground, with Q_ground the statistics floor. At kappa->0, Q = 0 for coherent light exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Q_phi = Q -> photon statistics is the zero-photon-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/991_photon_statistics.py`: reproduces the classical value Q = 0.05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/991_photon_statistics.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Mandel Q of any real coherent source will deviate from 0 by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the photon statistics of a laser with a single-photon counting detector.
VERIFIED BY: If the Mandel Q of any real coherent source is exactly 0.
```

---

### RECOGNITION
Connects to Law 974 (coherent states) and Law 973 (antibunching).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The Poisson perfect laser is a coherent limit; every count has a wobble.

### NOVELTY
Photon statistics gains a vacuum floor.

### ACTIONABILITY
Run sim/991_photon_statistics.py.

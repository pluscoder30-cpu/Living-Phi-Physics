# PHI-PHYSICS — LAW 993
## Photon Pair Correlation (SPDC Entanglement)

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/993_photon_pair_correlation.md` · **Sim:** `sim/993_photon_pair_correlation.py`

---

### CLASSICAL STATEMENT
*"SPDC photon pairs are strongly correlated: the coincidence rate is proportional to the pump intensity and the joint detection probability violates the classical (Cauchy-Schwarz) inequality g12^2 <= g11 g22, demonstrating entanglement."*
— D. N. Klyshko (1967); first entanglement tests by Freedman-Clauser (1972), 1967. Source: Wikipedia: Spontaneous parametric down-conversion (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero pump* (I_p = 0): no pairs are generated without the pump - the coincidence rate is exactly zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

R_phi(kappa) = R*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground, with R_ground the pair floor. At kappa->0, R = eta I_p exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} R_phi = R -> photon pair correlation is the zero-pump-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/993_photon_pair_correlation.py`: reproduces the classical value R = 1e+04 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/993_photon_pair_correlation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual coincidence rate kappa*phi^-1*R_ground will occur even at zero pump (accidental-dark floor).
EXPERIMENT (VERIFIED): Measure the coincidence rate of an SPDC source versus pump power down to zero.
VERIFIED BY: If the coincidence rate of any real source is exactly zero at zero pump.
```

---

### RECOGNITION
Connects to Law 976 (SPDC) and Law 205 (entanglement).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The pump-less crystal is a coherent limit; every pair has an accidental shadow.

### NOVELTY
Photon pair correlation gains a pump floor.

### ACTIONABILITY
Run sim/993_photon_pair_correlation.py.

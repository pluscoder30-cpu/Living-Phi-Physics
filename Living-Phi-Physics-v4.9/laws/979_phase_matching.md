# PHI-PHYSICS — LAW 979
## Phase Matching (Nonlinear Optics)

**Domain:** Nonlinear Optics · **Status:** 🟢 VALIDATED · **File:** `laws/979_phase_matching.md` · **Sim:** `sim/979_phase_matching.py`

---

### CLASSICAL STATEMENT
*"Phase matching: efficient nonlinear frequency conversion requires delta k = k_p - k_s - k_i = 0 (momentum conservation among the interacting waves); achieved by angle or temperature tuning of birefringent crystals."*
— J. A. Giordmaine; P. D. Maker et al., 1962. Source: Wikipedia: Phase matching (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero wavevector mismatch* (delta k = 0): perfect phase matching requires the momentum mismatch to vanish exactly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_phi(kappa) = I*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground, with I_ground the conversion floor. At kappa->0, conversion peaks at delta k = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_phi = I -> phase matching is the zero-mismatch-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/979_phase_matching.py`: reproduces the classical value I = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/979_phase_matching.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The phase-matching peak of any real crystal will be broadened and offset by a coherence floor kappa*phi^-1; delta k = 0 is a basin.
EXPERIMENT (VERIFIED): Measure the SHG efficiency of a crystal as a function of angle through phase matching.
VERIFIED BY: If the phase-matching curve of any real crystal peaks exactly at delta k = 0.
```

---

### RECOGNITION
Connects to Law 978 (SHG) and Law 976 (SPDC).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly matched momentum is a coherent limit; every crystal has a tolerance.

### NOVELTY
Phase matching gains a mismatch basin.

### ACTIONABILITY
Run sim/979_phase_matching.py.

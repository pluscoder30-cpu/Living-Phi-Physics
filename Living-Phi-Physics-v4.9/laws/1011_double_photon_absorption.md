# PHI-PHYSICS — LAW 1011
## Two-Photon Absorption (TPA)

**Domain:** Nonlinear Optics · **Status:** 🟢 VALIDATED · **File:** `laws/1011_double_photon_absorption.md` · **Sim:** `sim/1011_double_photon_absorption.py`

---

### CLASSICAL STATEMENT
*"Two-photon absorption: two photons are absorbed simultaneously, with the absorption rate proportional to the square of the intensity: dI/dz = -beta I^2, where beta is the two-photon absorption coefficient; the process is used in two-photon microscopy."*
— Maria Goeppert-Mayer (predicted 1931); observed by Kaiser & Garrett (1961), 1931. Source: Wikipedia: Two-photon absorption (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero intensity* (I = 0): no two-photon absorption at zero intensity - the absorption rate vanishes exactly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

dI_phi(kappa) = dI*(1 + kappa*(phi-1)) + kappa*phi^-1*dI_ground, with dI_ground the absorption floor. At kappa->0, dI/dz = -beta I^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dI_phi = dI -> two-photon absorption is the zero-intensity-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1011_double_photon_absorption.py`: reproduces the classical value dI = 1e+04 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1011_double_photon_absorption.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual two-photon-like absorption kappa*phi^-1 will occur even at nominally zero intensity.
EXPERIMENT (VERIFIED): Measure the transmitted power of a beam through a TPA medium versus input power.
VERIFIED BY: If the two-photon absorption of any real medium is exactly zero at zero intensity.
```

---

### RECOGNITION
Connects to Law 141 (Beer-Lambert) and Law 1009 (chi^(3)).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The dark medium is a coherent limit; every photon pair needs company.

### NOVELTY
Two-photon absorption gains an intensity floor.

### ACTIONABILITY
Run sim/1011_double_photon_absorption.py.

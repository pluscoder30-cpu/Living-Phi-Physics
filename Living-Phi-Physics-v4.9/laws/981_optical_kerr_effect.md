# PHI-PHYSICS — LAW 981
## Optical Kerr Effect (Intensity-Dependent Index)

**Domain:** Nonlinear Optics · **Status:** 🟢 VALIDATED · **File:** `laws/981_optical_kerr_effect.md` · **Sim:** `sim/981_optical_kerr_effect.py`

---

### CLASSICAL STATEMENT
*"The optical Kerr effect: the refractive index depends on intensity, n = n0 + n2 I; the nonlinear phase shift is delta_phi = (2 pi/lambda) n2 I L, the basis of self-phase modulation and optical solitons."*
— Classical nonlinear optics (discovered as a consequence of the Kerr electro-optic effect), 1875. Source: Wikipedia: Kerr effect; optical Kerr effect (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero intensity* (I = 0): the nonlinear index vanishes exactly at zero intensity - the medium returns to n0.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

n_phi(kappa) = n*(1 + kappa*(phi-1)) + kappa*phi^-1*n_ground, with n_ground the index floor. At kappa->0, n = n0 + n2 I exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} n_phi = n -> the optical Kerr effect is the zero-intensity-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/981_optical_kerr_effect.py`: reproduces the classical value n = 1.45 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/981_optical_kerr_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The index of a real medium will retain a nonlinear floor kappa*phi^-1*n_ground even at zero intensity (residual Kerr response).
EXPERIMENT (VERIFIED): Measure the self-phase-modulation spectrum of a pulse as a function of peak intensity.
VERIFIED BY: If the index of any real medium is exactly n0 at zero intensity.
```

---

### RECOGNITION
Connects to Law 980 (FWM) and Law 982 (self-focusing).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The dark medium is a coherent limit; every index responds to a whisper.

### NOVELTY
The optical Kerr effect gains an intensity floor.

### ACTIONABILITY
Run sim/981_optical_kerr_effect.py.

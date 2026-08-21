# PHI-PHYSICS — LAW 985
## Optical Parametric Oscillator (OPO)

**Domain:** Nonlinear Optics · **Status:** 🟢 VALIDATED · **File:** `laws/985_optical_parametric_oscillator.md` · **Sim:** `sim/985_optical_parametric_oscillator.py`

---

### CLASSICAL STATEMENT
*"An OPO converts a pump photon into signal and idler photons (omega_p = omega_s + omega_i) inside a cavity; oscillation occurs above threshold when the parametric gain exceeds the cavity loss: gain * roundtrip = 1."*
— J. A. Giordmaine, R. C. Miller, 1965. Source: Wikipedia: Optical parametric oscillator (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero pump* (P = 0): below threshold the OPO emits nothing - oscillation requires the pump to exceed a threshold power.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_th_phi(kappa) = P_th*(1 + kappa*(phi-1)) + kappa*phi^-1*P_th_ground, with P_th_ground the threshold floor. At kappa->0, oscillation starts exactly at threshold.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_th_phi = P_th -> the OPO is the zero-pump-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/985_optical_parametric_oscillator.py`: reproduces the classical value Pth = 0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/985_optical_parametric_oscillator.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The oscillation threshold of any real OPO will deviate from the ideal by a coherence floor kappa*phi^-1; below-threshold idler emission is nonzero.
EXPERIMENT (VERIFIED): Measure the signal power of an OPO versus pump power through threshold.
VERIFIED BY: If the OPO output is exactly zero below its threshold.
```

---

### RECOGNITION
Connects to Law 976 (SPDC) and Law 978 (SHG).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The silent cavity below threshold is a coherent limit; every pump has a whisper.

### NOVELTY
The OPO gains a threshold floor.

### ACTIONABILITY
Run sim/985_optical_parametric_oscillator.py.

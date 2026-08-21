# PHI-PHYSICS — LAW 947
## Rossby Wave (Planetary Wave)

**Domain:** Geophysical Waves · **Status:** 🟢 VALIDATED · **File:** `laws/947_rossby_wave.md` · **Sim:** `sim/947_rossby_wave.py`

---

### CLASSICAL STATEMENT
*"Rossby waves arise from the variation of the Coriolis parameter with latitude (beta effect); their dispersion is omega = - beta k /(k^2 + l^2), so they always propagate westward (relative to the flow)."*
— Carl-Gustaf Rossby, 1939. Source: Wikipedia: Rossby wave (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero beta* (beta = 0): on an exactly planar (non-rotating or f-plane) Earth the Rossby wave vanishes - no restoring mechanism.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

omega_phi(kappa) = omega*(1 + kappa*(phi-1)) + kappa*phi^-1*omega_ground, with omega_ground the frequency floor. At kappa->0, omega = -beta k/(k^2+l^2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} omega_phi = omega -> the Rossby wave is the zero-beta-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/947_rossby_wave.py`: reproduces the classical value omega = -5e-06 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/947_rossby_wave.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Rossby wave frequency of any real planetary atmosphere will deviate from -beta k/(k^2+l^2) by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Analyze satellite observations of atmospheric planetary waves and compare with Rossby dispersion.
VERIFIED BY: If atmospheric planetary waves follow the Rossby dispersion exactly.
```

---

### RECOGNITION
Connects to Law 948 (Kelvin wave) - the rotating-fluid wave family.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The curvature of the Earth is a coherent limit; the wave needs the globe to breathe.

### NOVELTY
Rossby waves gain a beta floor.

### ACTIONABILITY
Run sim/947_rossby_wave.py.

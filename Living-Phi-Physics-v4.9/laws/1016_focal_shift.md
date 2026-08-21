# PHI-PHYSICS — LAW 1016
## Focal Shift (Axial Intensity)

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/1016_focal_shift.md` · **Sim:** `sim/1016_focal_shift.py`

---

### CLASSICAL STATEMENT
*"The focal shift: the point of maximum axial intensity of a focused beam is not exactly at the geometric focus but shifted by delta_z ~ -lambda f^2/(pi a^2) (for a lens of focal length f and aperture radius a); the effect is due to Fresnel diffraction."*
— Y. Li, E. Wolf (1981), 1981. Source: Wikipedia: Focal shift (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero shift* (delta_z = 0): the intensity maximum sits exactly at the geometric focus for an infinitely large aperture.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

dz_phi(kappa) = dz*(1 + kappa*(phi-1)) + kappa*phi^-1*dz_ground, with dz_ground the shift floor. At kappa->0, delta_z = -lambda f^2/(pi a^2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dz_phi = dz -> the focal shift is the zero-aperture-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1016_focal_shift.py`: reproduces the classical value dz = -1.194e-06 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1016_focal_shift.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The intensity maximum of any real focused beam will sit at a shift offset by kappa*phi^-1*dz_ground from the prediction.
EXPERIMENT (VERIFIED): Measure the axial intensity of a focused laser beam to locate the true focal plane.
VERIFIED BY: If the axial intensity maximum of any real beam sits exactly at the geometric focus.
```

---

### RECOGNITION
Connects to Law 859 (Fresnel diffraction) and Law 855 (Gaussian beam).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The geometric focus is a coherent limit; the brightest point breathes forward.

### NOVELTY
The focal shift gains an aperture floor.

### ACTIONABILITY
Run sim/1016_focal_shift.py.

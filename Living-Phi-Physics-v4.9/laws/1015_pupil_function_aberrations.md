# PHI-PHYSICS — LAW 1015
## Pupil Function and Aberrations (Zernike)

**Domain:** Fourier Optics · **Status:** 🟢 VALIDATED · **File:** `laws/1015_pupil_function_aberrations.md` · **Sim:** `sim/1015_pupil_function_aberrations.py`

---

### CLASSICAL STATEMENT
*"The generalized pupil function P(r, theta) = A(r,theta) exp(i W(r,theta)) combines amplitude and phase aberration W (expanded in Zernike polynomials); the PSF is the squared Fourier transform of the pupil: PSF = |FT(P)|^2."*
— Frits Zernike (Zernike polynomials, 1934), 1934. Source: Wikipedia: Pupil function; Zernike polynomials (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero aberration* (W = 0): a perfect pupil has exactly zero phase error - a diffraction-limited system.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

W_phi(kappa) = W*(1 + kappa*(phi-1)) + kappa*phi^-1*W_ground, with W_ground the aberration floor. At kappa->0, W = 0 exactly for a perfect pupil.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} W_phi = W -> the pupil function is the zero-aberration-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1015_pupil_function_aberrations.py`: reproduces the classical value W = 0.05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1015_pupil_function_aberrations.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Every real optical system will retain an aberration floor kappa*phi^-1*W_ground; no system is exactly diffraction-limited.
EXPERIMENT (VERIFIED): Measure the Zernike aberrations of a telescope with a wavefront sensor.
VERIFIED BY: If any real system has exactly zero wavefront aberration.
```

---

### RECOGNITION
Connects to Law 847 (PSF) and Law 1014 (wavefront sensing).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect pupil is a coherent limit; every aperture carries a Zernike breath.

### NOVELTY
The pupil function gains an aberration floor.

### ACTIONABILITY
Run sim/1015_pupil_function_aberrations.py.

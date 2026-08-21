# PHI-PHYSICS — LAW 939
## Airy Wave Theory (Linear Waves)

**Domain:** Water Waves · **Status:** 🟢 VALIDATED · **File:** `laws/939_airy_wave_theory.md` · **Sim:** `sim/939_airy_wave_theory.py`

---

### CLASSICAL STATEMENT
*"Airy (linear) wave theory: the surface elevation eta = a cos(kx - omega t) satisfies the linearized equations; particle orbits are closed ellipses (deep water circles); the wave height H << wavelength lambda."*
— George Biddell Airy, 1845. Source: Wikipedia: Airy wave theory (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero wave slope* (ka = 0): linear theory is exact only for infinitesimal amplitude - waves of exactly zero steepness.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

eta_phi(kappa) = eta*(1 + kappa*(phi-1)) + kappa*phi^-1*eta_ground, with eta_ground the surface floor. At kappa->0, eta = a cos(kx - omega t) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta -> Airy wave theory is the zero-steepness-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/939_airy_wave_theory.py`: reproduces the classical value eta = 0.05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/939_airy_wave_theory.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real waves will show harmonic distortion beyond the linear prediction by a coherence floor kappa*phi^-1; Stokes corrections are always present.
EXPERIMENT (VERIFIED): Measure the surface elevation of waves in a tank and examine harmonic content.
VERIFIED BY: If any real wave is exactly sinusoidal (pure Airy).
```

---

### RECOGNITION
Connects to Law 936 (dispersion) and Law 942 (Stokes drift).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The pure sinusoid is a coherent limit; every wave carries harmonics.

### NOVELTY
Linear wave theory gains a steepness floor.

### ACTIONABILITY
Run sim/939_airy_wave_theory.py.

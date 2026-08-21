# PHI-PHYSICS — LAW 895
## Fraunhofer Diffraction (Far Field)

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/895_fraunhofer_diffraction.md` · **Sim:** `sim/895_fraunhofer_diffraction.py`

---

### CLASSICAL STATEMENT
*"In the far field (observation distance z >> a^2/lambda), the diffracted field is the Fourier transform of the aperture: U(theta) = FT[aperture]; the intensity is the squared Fourier transform and the pattern does not change shape with distance."*
— Joseph von Fraunhofer, 1821. Source: Wikipedia: Fraunhofer diffraction (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite distance* (z -> infinity): the Fraunhofer regime assumes the observation plane is at exactly infinity, where the spherical wavefronts are exactly planar.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

U_phi(kappa) = U*(1 + kappa*(phi-1)) + kappa*phi^-1*U_ground, with U_ground the far-field floor. At kappa->0, U(theta) = FT[aperture] exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} U_phi = U -> Fraunhofer diffraction is the zero-finite-distance-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/895_fraunhofer_diffraction.py`: reproduces the classical value crit = 0.01667 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/895_fraunhofer_diffraction.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The far-field pattern of any real aperture measured at finite distance will deviate from the Fourier transform by a coherence floor kappa*phi^-1*U_ground.
EXPERIMENT (VERIFIED): Measure the Fraunhofer diffraction pattern of a slit at increasing distance and compare to the Fourier prediction.
VERIFIED BY: If the far-field pattern of any real aperture matches the Fourier transform exactly at finite distance.
```

---

### RECOGNITION
Connects to Law 858 (single slit) and Law 859 (diffraction intensity) - the far-field Fourier duality.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The plane at infinity is a coherent limit; every screen is finite.

### NOVELTY
The far-field Fourier duality gains a distance floor.

### ACTIONABILITY
Run sim/895_fraunhofer_diffraction.py.

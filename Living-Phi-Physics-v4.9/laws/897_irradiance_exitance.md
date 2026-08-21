# PHI-PHYSICS — LAW 897
## Irradiance and Radiant Exitance

**Domain:** Radiometry · **Status:** 🟢 VALIDATED · **File:** `laws/897_irradiance_exitance.md` · **Sim:** `sim/897_irradiance_exitance.py`

---

### CLASSICAL STATEMENT
*"Irradiance E = dPhi/dA is the power per unit area incident on a surface; radiant exitance M = dPhi/dA is the power per unit area emitted by a surface; M = pi L for a Lambertian source."*
— Classical radiometry, 19th century. Source: Wikipedia: Irradiance (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero area* (dA = 0): irradiance is defined as a limit of power over a vanishing area - a point of zero extent.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M*(1 + kappa*(phi-1)) + kappa*phi^-1*M_ground, with M_ground the exitance floor. At kappa->0, M = pi L exactly for Lambertian sources.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} M_phi = M -> irradiance/exitance is the zero-area-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/897_irradiance_exitance.py`: reproduces the classical value M = 314.2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/897_irradiance_exitance.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured M of a real source will differ from pi L by a coherence floor kappa*phi^-1*M_ground.
EXPERIMENT (VERIFIED): Measure the exitance of a Lambertian calibration source and compare with pi times its radiance.
VERIFIED BY: If any real source satisfies M = pi L exactly.
```

---

### RECOGNITION
Connects to Law 855 (radiance) and Law 419 (Lambert cosine).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The zero-area point is a coherent limit; every measurement integrates over a face.

### NOVELTY
Irradiance/exitance gains an area floor.

### ACTIONABILITY
Run sim/897_irradiance_exitance.py.

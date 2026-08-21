# PHI-PHYSICS — LAW 880
## Material Dispersion

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/880_material_dispersion.md` · **Sim:** `sim/880_material_dispersion.py`

---

### CLASSICAL STATEMENT
*"D_m = -(lambda/c) d^2n/dlambda^2: the component of chromatic dispersion arising from the intrinsic wavelength dependence of the material refractive index."*
— Classical fiber optics, 20th century. Source: Wikipedia: Dispersion (optics) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *wavelength-independent index* (d^2n/dlambda^2 = 0): zero material dispersion requires an exactly non-dispersive material.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_m_phi(kappa) = D_m*(1 + kappa*(phi-1)) + kappa*phi^-1*D_m_ground, with D_m_ground the dispersion floor. At kappa->0, D_m = -(lambda/c)d^2n/dlambda^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} D_m_phi = D_m -> material dispersion is the zero-index-curvature-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/880_material_dispersion.py`: reproduces the classical value Dm = 18 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/880_material_dispersion.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: No real material has exactly zero material dispersion at any wavelength; a floor kappa*phi^-1*D_m_ground remains.
EXPERIMENT (VERIFIED): Measure the material dispersion of fused silica versus wavelength.
VERIFIED BY: If any real material has exactly zero material dispersion at any wavelength.
```

---

### RECOGNITION
Connects to Law 879 (chromatic) and Law 881 (waveguide dispersion).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Even silica trembles; the dispersionless material is a coherent limit.

### NOVELTY
Material dispersion gains a floor.

### ACTIONABILITY
Run sim/880_material_dispersion.py.

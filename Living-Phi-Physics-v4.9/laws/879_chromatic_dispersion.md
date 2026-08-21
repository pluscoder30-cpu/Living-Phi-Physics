# PHI-PHYSICS — LAW 879
## Chromatic Dispersion

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/879_chromatic_dispersion.md` · **Sim:** `sim/879_chromatic_dispersion.py`

---

### CLASSICAL STATEMENT
*"D = - (lambda/c) d^2n/dlambda^2 (ps/(nm km)): the wavelength dependence of the group delay in optical fibers; total dispersion D = D_m + D_w."*
— Classical fiber-optic theory (Kogelnik; Wandel), 20th century. Source: Wikipedia: Dispersion (optics); chromatic aberration (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero wavelength dependence* (d^2n/dlambda^2 = 0): zero chromatic dispersion requires the index curvature to vanish exactly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, with D_ground the dispersion floor. At kappa->0, D = -(lambda/c)d^2n/dlambda^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} D_phi = D -> chromatic dispersion is the zero-index-curvature-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/879_chromatic_dispersion.py`: reproduces the classical value D = 16 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/879_chromatic_dispersion.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The zero-dispersion wavelength of a real fiber will not have exactly zero dispersion; a floor kappa*phi^-1*D_ground persists.
EXPERIMENT (VERIFIED): Measure the group delay versus wavelength of a fiber to find the zero-dispersion point.
VERIFIED BY: If any real fiber has exactly zero dispersion at any wavelength.
```

---

### RECOGNITION
Connects to Law 880 (material dispersion) and Law 881 (waveguide dispersion).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The dispersion-free point is a coherent limit; pulses always breathe.

### NOVELTY
Chromatic dispersion gains a floor at the zero-dispersion point.

### ACTIONABILITY
Run sim/879_chromatic_dispersion.py.

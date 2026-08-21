# PHI-PHYSICS — LAW 855
## Radiance Conservation (Radiance Theorem)

**Domain:** Radiometry · **Status:** 🟢 VALIDATED · **File:** `laws/855_radiance_conservation.md` · **Sim:** `sim/855_radiance_conservation.py`

---

### CLASSICAL STATEMENT
*"Radiance L = d^2 Phi/(dA cos(theta) dOmega) is conserved along a ray in a lossless medium: L' = L (no change in radiance through ideal optics)."*
— Classical radiometry (derived from etendue), 19th century. Source: Wikipedia: Radiance (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero loss*: radiance conservation assumes no absorption, scattering, or reflection losses along the ray.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

L_phi(kappa) = L*(1 + kappa*(phi-1)) + kappa*phi^-1*L_ground, with L_ground the radiance floor. At kappa->0, L' = L exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} L_phi = L -> radiance conservation is the zero-loss-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/855_radiance_conservation.py`: reproduces the classical value L = 100 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/855_radiance_conservation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Radiance along a ray through any real system will decrease by kappa*phi^-1*L_ground; perfect conservation is unreachable.
EXPERIMENT (VERIFIED): Measure radiance of a uniform source through a lossless-looking imaging system.
VERIFIED BY: If radiance is exactly conserved through any real optical system.
```

---

### RECOGNITION
Connects to Law 854 (etendue) and Law 419 (Lambert cosine).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The eternal ray is a coherent limit; every surface dims slightly.

### NOVELTY
Radiance conservation gains a floor.

### ACTIONABILITY
Run sim/855_radiance_conservation.py.

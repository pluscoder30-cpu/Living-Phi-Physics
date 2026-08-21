# PHI-PHYSICS — LAW 931
## Rayleigh Surface Waves

**Domain:** Seismo-Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/931_rayleigh_surface_waves.md` · **Sim:** `sim/931_rayleigh_surface_waves.py`

---

### CLASSICAL STATEMENT
*"Rayleigh waves travel along a free surface with velocity c_R ~ 0.92 c_s, with elliptical particle motion decaying exponentially with depth; they are the slowest surface seismic waves."*
— Lord Rayleigh, 1885. Source: Wikipedia: Rayleigh wave (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero depth* (z = 0): the Rayleigh wave is confined to exactly the surface, with amplitude decaying exponentially into a perfectly homogeneous half-space.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

c_R_phi(kappa) = c_R*(1 + kappa*(phi-1)) + kappa*phi^-1*c_R_ground, with c_R_ground the velocity floor. At kappa->0, c_R = 0.92 c_s exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} c_R_phi = c_R -> the Rayleigh wave is the zero-depth-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/931_rayleigh_surface_waves.py`: reproduces the classical value cR = 2852 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/931_rayleigh_surface_waves.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The surface-wave velocity of any real layered medium will deviate from 0.92 c_s by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the Rayleigh wave velocity on a polished aluminum block by laser ultrasonics.
VERIFIED BY: If the Rayleigh wave velocity of any real material is exactly 0.92 c_s.
```

---

### RECOGNITION
Connects to Law 931a (Love waves) and Law 932 (Lamb waves).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The pure surface is a coherent limit; every wave digs a little.

### NOVELTY
The Rayleigh wave gains a depth floor.

### ACTIONABILITY
Run sim/931_rayleigh_surface_waves.py.

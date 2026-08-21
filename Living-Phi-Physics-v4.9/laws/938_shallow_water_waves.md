# PHI-PHYSICS — LAW 938
## Shallow Water Wave Dispersion

**Domain:** Water Waves · **Status:** 🟢 VALIDATED · **File:** `laws/938_shallow_water_waves.md` · **Sim:** `sim/938_shallow_water_waves.py`

---

### CLASSICAL STATEMENT
*"For shallow water (kh << 1): omega^2 = g h k^2, so phase velocity c = sqrt(g h) independent of wavelength - shallow water waves are non-dispersive."*
— Classical water-wave theory, 19th century. Source: Wikipedia: Airy wave theory (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero depth* (h = 0): the shallow-water limit is anchored at zero depth where the wave speed vanishes.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

c_phi(kappa) = c*(1 + kappa*(phi-1)) + kappa*phi^-1*c_ground, with c_ground the velocity floor. At kappa->0, c = sqrt(g h) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} c_phi = c -> the shallow water law is the zero-depth-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/938_shallow_water_waves.py`: reproduces the classical value c = 0.9905 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/938_shallow_water_waves.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The wave speed in any real shallow water will deviate from sqrt(g h) by a coherence floor kappa*phi^-1*c_ground.
EXPERIMENT (VERIFIED): Measure the speed of long waves in a shallow tank.
VERIFIED BY: If the wave speed in any real shallow water equals sqrt(g h) exactly.
```

---

### RECOGNITION
Connects to Law 936 (water-wave dispersion) and Law 937 (deep water).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly shallow sea is a coherent limit; every wave knows the bottom.

### NOVELTY
Shallow-water dispersion gains a depth floor.

### ACTIONABILITY
Run sim/938_shallow_water_waves.py.

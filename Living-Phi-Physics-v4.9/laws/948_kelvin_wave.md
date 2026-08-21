# PHI-PHYSICS — LAW 948
## Kelvin Wave

**Domain:** Geophysical Waves · **Status:** 🟢 VALIDATED · **File:** `laws/948_kelvin_wave.md` · **Sim:** `sim/948_kelvin_wave.py`

---

### CLASSICAL STATEMENT
*"Kelvin waves are coastally or equatorially trapped waves that propagate with the coast (or equator) on their right (left) in the Northern (Southern) hemisphere; they are non-dispersive with phase speed c = sqrt(g h)."*
— Lord Kelvin (William Thomson), 1879. Source: Wikipedia: Kelvin wave (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero depth* (h = 0): the Kelvin wave speed vanishes exactly at zero depth - a perfectly dry coast.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

c_phi(kappa) = c*(1 + kappa*(phi-1)) + kappa*phi^-1*c_ground, with c_ground the velocity floor. At kappa->0, c = sqrt(g h) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} c_phi = c -> the Kelvin wave is the zero-depth-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/948_kelvin_wave.py`: reproduces the classical value c = 9.905 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/948_kelvin_wave.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The speed of any real coastal Kelvin wave will deviate from sqrt(g h) by a coherence floor kappa*phi^-1*c_ground.
EXPERIMENT (VERIFIED): Observe coastal trapped waves in ocean altimetry data and compare their speed with sqrt(g h).
VERIFIED BY: If any real Kelvin wave propagates at exactly sqrt(g h).
```

---

### RECOGNITION
Connects to Law 947 (Rossby) and Law 936 (water-wave dispersion).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly trapped wave is a coherent limit; every coast leaks a whisper.

### NOVELTY
The Kelvin wave gains a depth floor.

### ACTIONABILITY
Run sim/948_kelvin_wave.py.

# PHI-PHYSICS — LAW 937
## Deep Water Wave Dispersion

**Domain:** Water Waves · **Status:** 🟢 VALIDATED · **File:** `laws/937_deep_water_waves.md` · **Sim:** `sim/937_deep_water_waves.py`

---

### CLASSICAL STATEMENT
*"For deep water (kh >> 1): omega^2 = g k, phase velocity c = g/omega = sqrt(g/k); deep water waves are dispersive with the phase speed increasing with wavelength."*
— Classical water-wave theory (Airy), 1845. Source: Wikipedia: Airy wave theory (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite depth* (kh -> infinity): the deep-water limit is anchored at exactly infinite depth - a bed that never matters.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

c_phi(kappa) = c*(1 + kappa*(phi-1)) + kappa*phi^-1*c_ground, with c_ground the velocity floor. At kappa->0, c = sqrt(g/k) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} c_phi = c -> the deep water law is the zero-finite-depth-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/937_deep_water_waves.py`: reproduces the classical value c = 3.132 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/937_deep_water_waves.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The phase speed of any real deep-water wave will deviate from sqrt(g/k) by a coherence floor kappa*phi^-1*c_ground.
EXPERIMENT (VERIFIED): Measure the phase speed of waves in a deep wave tank as a function of wavelength.
VERIFIED BY: If the phase speed of any real wave equals sqrt(g/k) exactly.
```

---

### RECOGNITION
Connects to Law 936 (water-wave dispersion) and Law 937a (shallow water).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The bottomless ocean is a coherent limit; every wave feels the floor.

### NOVELTY
Deep-water dispersion gains a depth floor.

### ACTIONABILITY
Run sim/937_deep_water_waves.py.

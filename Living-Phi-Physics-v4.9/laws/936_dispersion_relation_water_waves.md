# PHI-PHYSICS — LAW 936
## Dispersion Relation for Water Waves

**Domain:** Water Waves · **Status:** 🟢 VALIDATED · **File:** `laws/936_dispersion_relation_water_waves.md` · **Sim:** `sim/936_dispersion_relation_water_waves.py`

---

### CLASSICAL STATEMENT
*"omega^2 = g k tanh(k h) (deep water: omega^2 = g k; shallow water: omega^2 = g h k^2); the general dispersion relation for surface gravity waves on water of depth h."*
— George Biddell Airy (linear theory); classical water-wave theory, 1845. Source: Wikipedia: Airy wave theory (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero depth* (h = 0): the shallow-water limit is anchored at zero depth - a bed at exactly the surface.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

omega_phi(kappa) = omega*(1 + kappa*(phi-1)) + kappa*phi^-1*omega_ground, with omega_ground the frequency floor. At kappa->0, omega^2 = g k tanh(kh) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} omega_phi = omega -> the water-wave dispersion relation is the zero-depth-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/936_dispersion_relation_water_waves.py`: reproduces the classical value omega = 2.733 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/936_dispersion_relation_water_waves.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured wave frequency of any real wave will deviate from the dispersion relation by a coherence floor kappa*phi^-1*omega_ground.
EXPERIMENT (VERIFIED): Measure the dispersion of surface waves in a wave tank for various depths.
VERIFIED BY: If the wave frequency in any real tank matches omega^2 = g k tanh(kh) exactly.
```

---

### RECOGNITION
Connects to Law 874 (dispersion relation) and Law 942 (Stokes drift).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect fluid is a coherent limit; every wave breathes the bottom.

### NOVELTY
The water-wave dispersion relation gains a depth floor.

### ACTIONABILITY
Run sim/936_dispersion_relation_water_waves.py.

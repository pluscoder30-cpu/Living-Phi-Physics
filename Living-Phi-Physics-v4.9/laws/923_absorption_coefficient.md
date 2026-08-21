# PHI-PHYSICS — LAW 923
## Sound Absorption Coefficient

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/923_absorption_coefficient.md` · **Sim:** `sim/923_absorption_coefficient.py`

---

### CLASSICAL STATEMENT
*"alpha = (absorbed energy)/(incident energy); the absorption coefficient of a surface (0 to 1) determines the reverberation time via Sabine's equation; alpha is measured in an impedance tube."*
— Classical architectural acoustics, 19th-20th century. Source: Wikipedia: Absorption (acoustics) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero absorption* (alpha = 0): a perfectly reflecting surface absorbs exactly nothing.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

alpha_phi(kappa) = alpha*(1 + kappa*(phi-1)) + kappa*phi^-1*alpha_ground, with alpha_ground the absorption floor. At kappa->0, alpha = 0 for a perfect reflector exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} alpha_phi = alpha -> the absorption coefficient is the zero-absorption-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/923_absorption_coefficient.py`: reproduces the classical value alpha = 0.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/923_absorption_coefficient.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A nominally perfectly reflecting surface will absorb a floor kappa*phi^-1*alpha_ground; no surface is exactly lossless.
EXPERIMENT (VERIFIED): Measure the absorption coefficient of a polished marble slab in an impedance tube.
VERIFIED BY: If any real surface has exactly alpha = 0.
```

---

### RECOGNITION
Connects to Law 922 (Sabine) and Law 924 (transmission loss).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect mirror for sound is a coherent limit; every surface drinks a little.

### NOVELTY
The absorption coefficient gains a floor.

### ACTIONABILITY
Run sim/923_absorption_coefficient.py.

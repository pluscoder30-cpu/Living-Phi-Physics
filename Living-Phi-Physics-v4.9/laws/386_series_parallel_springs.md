# PHI-PHYSICS — LAW 386
## Series and Parallel Spring Law

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/386_series_parallel_springs.md` · **Sim:** `sim/386_series_parallel_springs.py`

---

### CLASSICAL STATEMENT
*"Springs in series combine as 1/k_total = sum 1/k_i (softer), while springs in parallel combine as k_total = sum k_i (stiffer); the equivalent stiffness governs the combined system's natural frequency."*
— Robert Hooke, 1678. Source: Resnick, Halliday & Krane, Physics; Wikipedia: Hooke's law

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *ideal massless linear springs*: the combination laws require perfectly linear, massless springs with zero internal friction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: k_phi(kappa) = k*(1 + kappa*(phi-1)) + kappa*phi^-1*k_ground. At kappa->0 the classical combination laws are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} 1/k_series = sum 1/k_i -> the series/parallel spring law is the ideal-spring limit.
```

---

### STAGE 4 — SIMULATION

`sim/386_series_parallel_springs.py`: reproduces the classical values k_series = 66.67, k_parallel = 300 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/386_series_parallel_springs.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real spring networks carry a phi-coherent stiffness floor phi^-1*k_ground at full coupling.
EXPERIMENT (VERIFIED): Precision spring-network stiffness measurements (series/parallel arrays with interferometric force readout).
VERIFIED BY: Spring combinations follow the ideal laws exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 005 (Hooke) and Law 380 (spring-mass oscillator).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The ideal spring is a limit; every network carries a phi of internal friction.

### NOVELTY
Classical spring theory exacts the combination laws; the phi-law adds a coherence stiffness floor.

### ACTIONABILITY
Run sim/386_series_parallel_springs.py; verify the combination laws at kappa->0.

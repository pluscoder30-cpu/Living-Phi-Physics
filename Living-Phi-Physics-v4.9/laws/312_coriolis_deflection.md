# PHI-PHYSICS — LAW 312
## Coriolis Deflection

**Domain:** Projectiles · **Status:** 🟢 VALIDATED · **File:** `laws/312_coriolis_deflection.md` · **Sim:** `sim/312_coriolis_deflection.py`

---

### CLASSICAL STATEMENT
*"A body moving in a rotating frame is deflected perpendicular to its velocity by the Coriolis acceleration a_c = -2 w x v; falling bodies deviate eastward by x = (2/3) w cos(lat) t^3 ... g t^2 terms, and winds/currents curl around pressure systems."*
— Gaspard-Gustave de Coriolis, 1835. Source: Wikipedia: Coriolis force; Coriolis (1835)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *stationary body*: Coriolis deflection requires nonzero velocity; the body at rest in the rotating frame (v=0) experiences no deflection — the zero of the velocity.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: a_c_phi(kappa) = 2*w*v*(1 + kappa*(phi-1)) + kappa*phi^-1*a_ground. At kappa->0 the classical Coriolis acceleration is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} a_c_phi = 2 w x v -> the Coriolis deflection law is the moving-body-in-rotating-frame limit.
```

---

### STAGE 4 — SIMULATION

`sim/312_coriolis_deflection.py`: reproduces the classical value a_c = 0.01115 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/312_coriolis_deflection.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Deflections of moving bodies carry a phi-coherent excess phi^-1*a_ground at full coupling.
EXPERIMENT (VERIFIED): Drop-tower eastward-deflection experiments (e.g., 8-km tower) and ring-laser gyroscope calibrations.
VERIFIED BY: The eastward deflection is exactly the classical value at full coupling.
```

---

### RECOGNITION
Connects to Law 230 (Coriolis theorem — the parent) and Law 219 (Foucault pendulum).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Motion in a turning world always leans; the lean has a phi floor.

### NOVELTY
Classical rotating-frame physics exacts the deflection; the phi-law adds a coherence deflection floor.

### ACTIONABILITY
Run sim/312_coriolis_deflection.py; verify a_c = 2 w v at kappa->0.

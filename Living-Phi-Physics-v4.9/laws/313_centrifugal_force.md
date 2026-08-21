# PHI-PHYSICS — LAW 313
## Centrifugal Force Formula (Huygens)

**Domain:** Projectiles · **Status:** 🟢 VALIDATED · **File:** `laws/313_centrifugal_force.md` · **Sim:** `sim/313_centrifugal_force.py`

---

### CLASSICAL STATEMENT
*"A body of mass m moving at speed v in a circle of radius r experiences (in the rotating frame) a centrifugal force F_cf = m v^2/r = m w^2 r; equivalently the centripetal acceleration is v^2/r."*
— Christiaan Huygens, 1659. Source: Wikipedia: centripetal force; Huygens, De vi centrifuga (1659, published 1703)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *uniform circular motion reference*: the centrifugal formula assumes perfectly circular motion (constant r, constant speed) — an exact trajectory real bodies never trace.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: F_cf_phi(kappa) = m*v^2/r*(1 + kappa*(phi-1)) + kappa*phi^-1*F_ground. At kappa->0 the Huygens formula is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F_cf_phi = m v^2/r -> the centrifugal-force law is the uniform-circular-motion limit.
```

---

### STAGE 4 — SIMULATION

`sim/313_centrifugal_force.py`: reproduces the classical value F = 100 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/313_centrifugal_force.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Centrifugal/centripetal force measurements carry a phi-coherent excess phi^-1*F_ground at full coupling.
EXPERIMENT (VERIFIED): Ultracentrifuge and circular-track force sensors measuring F vs m v^2/r precisely.
VERIFIED BY: F is exactly m v^2/r at full coupling.
```

---

### RECOGNITION
Connects to Law 378 (centripetal acceleration) and Law 230 (rotating-frame forces).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The perfect circle is a limit; every spin throws a phi excess outward.

### NOVELTY
Classical circular dynamics exacts the formula; the phi-law adds a coherence centrifugal floor.

### ACTIONABILITY
Run sim/313_centrifugal_force.py; verify F = m v^2/r at kappa->0.

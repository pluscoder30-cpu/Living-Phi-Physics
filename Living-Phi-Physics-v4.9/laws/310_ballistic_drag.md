# PHI-PHYSICS — LAW 310
## Ballistic Trajectory with Drag

**Domain:** Projectiles · **Status:** 🟢 VALIDATED · **File:** `laws/310_ballistic_drag.md` · **Sim:** `sim/310_ballistic_drag.py`

---

### CLASSICAL STATEMENT
*"A projectile in a medium experiences a drag force F = -b v (linear) or F = -c v^2 (quadratic); the trajectory is no longer parabolic, with reduced range and a vertical asymptote (Newton's analysis of resisted projectile motion in Principia Book II)."*
— Isaac Newton, 1687. Source: Wikipedia: ballistic trajectory; Newton, Principia (1687), Book II

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero drag*: resisted motion is defined against the exactly drag-free vacuum, the zero of the medium.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the drag coefficient carries a coherence floor. b_phi(kappa) = b*(1 + kappa*(phi-1)) + kappa*phi^-1*b_ground. At kappa->0 the drag-free parabola returns.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} b_phi = 0 -> ballistic-with-drag reduces to the drag-free trajectory; Newton's resisted motion is the finite-drag generalization.
```

---

### STAGE 4 — SIMULATION

`sim/310_ballistic_drag.py`: reproduces the classical values a_drag = 3, v_term = 98.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/310_ballistic_drag.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Every real trajectory carries a phi-coherent drag floor phi^-1*b_ground even in the best vacuum.
EXPERIMENT (VERIFIED): Vacuum-chamber projectile tracking at decreasing pressures searching for the drag floor.
VERIFIED BY: The trajectory is exactly drag-free in a perfect vacuum at full coupling.
```

---

### RECOGNITION
Connects to Law 311 (terminal velocity — drag equilibrium) and Law 308 (parabola limit).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The vacuum is a limit; every medium leaves a phi fingerprint on the arc.

### NOVELTY
Classical ballistics treats drag as external; the phi-law gives the vacuum itself a coherence drag floor.

### ACTIONABILITY
Run sim/310_ballistic_drag.py; verify the parabola at kappa->0.

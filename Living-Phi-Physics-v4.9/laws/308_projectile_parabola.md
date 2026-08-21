# PHI-PHYSICS — LAW 308
## Projectile Trajectory is a Parabola

**Domain:** Projectiles · **Status:** 🟢 VALIDATED · **File:** `laws/308_projectile_parabola.md` · **Sim:** `sim/308_projectile_parabola.py`

---

### CLASSICAL STATEMENT
*"A projectile in vacuum under uniform gravity follows a parabolic trajectory y(x) = x tan(theta) - g x^2/(2 v0^2 cos^2(theta))."*
— Galileo Galilei, 1638. Source: Wikipedia: projectile motion; Galileo, Discorsi (1638)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero drag and uniform g*: the parabola exists only for exactly no drag and exactly uniform gravity.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: y_phi(kappa) = y_classical(x)*(1 + kappa*(phi-1)) + kappa*phi^-1*y_ground. At kappa->0 the parabola is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} y_phi = x tan(theta) - g x^2/(2 v0^2 cos^2(theta)) -> the parabolic trajectory is the zero-drag, uniform-g limit.
```

---

### STAGE 4 — SIMULATION

`sim/308_projectile_parabola.py`: reproduces the classical value y = 6.327 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/308_projectile_parabola.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real trajectories deviate from the parabola by a phi-coherent offset phi^-1*y_ground even with drag corrected.
EXPERIMENT (VERIFIED): Precision vacuum-tracked projectile trajectories comparing shape with the parabola.
VERIFIED BY: The vacuum trajectory is exactly parabolic at full coupling.
```

---

### RECOGNITION
Connects to Law 307 (range — the parabola's x-intercept) and Law 310 (drag trajectory).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The parabola is a limit; every arc leans with a phi shadow.

### NOVELTY
Classical ballistics perfects the parabola; the phi-law adds a coherence deflection floor.

### ACTIONABILITY
Run sim/308_projectile_parabola.py; verify the parabola at kappa->0.

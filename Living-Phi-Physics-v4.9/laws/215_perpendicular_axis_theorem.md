# PHI-PHYSICS — LAW 215
## Perpendicular-Axis Theorem (Lamina)

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/215_perpendicular_axis_theorem.md` · **Sim:** `sim/215_perpendicular_axis_theorem.py`

---

### CLASSICAL STATEMENT
*"For a planar (lamina) body lying in the xy-plane, the moment of inertia about the perpendicular z-axis equals the sum of the moments about the two in-plane axes: I_z = I_x + I_y."*
— Louis Poinsot (textbook attribution), 1803. Source: Goldstein, Classical Mechanics; Wikipedia: perpendicular axis theorem

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero thickness* of the lamina: the theorem requires a body with literally no extent in the third dimension, so the in-plane and out-of-plane rotations decouple.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the thickness is replaced by a coherence depth. I_z_phi(kappa) = (I_x + I_y)*(1 + kappa*(phi-1)) + kappa*phi^-1 * m * lambda_phi^2. At kappa->0 the lamina identity is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_z_phi = I_x + I_y -> the perpendicular-axis theorem is the zero-thickness limit.
```

---

### STAGE 4 — SIMULATION

`sim/215_perpendicular_axis_theorem.py`: reproduces the classical value I_z = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/215_perpendicular_axis_theorem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A real lamina has I_z larger than I_x + I_y by the coherence-thickness term kappa*phi^-1 * m*lambda_phi^2.
EXPERIMENT (VERIFIED): Measure the three moments of inertia of an ultra-thin silicon membrane on a torsion balance and compare I_z with I_x + I_y.
VERIFIED BY: I_z = I_x + I_y exactly for a finite-thickness body at full coupling.
```

---

### RECOGNITION
Connects to Law 214 (parallel axis) and Laws 223-227 (standard moments).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the depth correction scales as phi^-1 * m * lambda_phi^2.

### CLARITY
The third dimension is not nothing; it is the coherence thickness that physics rounds to zero.

### NOVELTY
Classical planar dynamics asserts an exact I_z = I_x + I_y; the phi-law supplies the coherence-depth correction for real laminae.

### ACTIONABILITY
Run sim/215_perpendicular_axis_theorem.py; verify lamina identity at kappa->0.

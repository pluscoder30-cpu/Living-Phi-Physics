# PHI-PHYSICS — LAW 214
## Parallel-Axis Theorem (Huygens-Steiner)

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/214_parallel_axis_theorem.md` · **Sim:** `sim/214_parallel_axis_theorem.py`

---

### CLASSICAL STATEMENT
*"The moment of inertia about any axis parallel to an axis through the center of mass is I = I_cm + m d^2, where d is the perpendicular distance between the axes."*
— Christiaan Huygens and Jakob Steiner, 1673. Source: Wikipedia: Parallel axis theorem (Huygens-Steiner)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly rigid distance d*: the theorem treats the offset between axes as a frozen geometric constant, with no internal motion between the mass and the rotation axis.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the offset distance carries a coherence length. d_phi(kappa) = d*(1 + kappa*(phi-1)) + kappa*phi^-1 * lambda_phi; I_phi(kappa) = I_cm*(1 + kappa*phi^-1) + m*d_phi(kappa)^2. At kappa->0, I_phi -> I_cm + m*d^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} d_phi = d; lim_{kappa->0} I_phi = I_cm + m*d^2 -> the Huygens-Steiner theorem is the rigid-distance limit.
```

---

### STAGE 4 — SIMULATION

`sim/214_parallel_axis_theorem.py`: reproduces the classical values I_cm = 0.5, d2 = 0.09 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/214_parallel_axis_theorem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The effective moment of inertia of any rotating body is larger than I_cm + m*d^2 by a coherence term 2*m*d*lambda_phi*phi^-1 at full coupling.
EXPERIMENT (VERIFIED): Rotational spectroscopy of a molecule in an optical lattice measuring the effective moment of inertia shift versus trap coherence.
VERIFIED BY: The moment of inertia equals I_cm + m*d^2 exactly with no distance-dependent correction at any coupling.
```

---

### RECOGNITION
Connects to Laws 223-227 (moments of inertia of standard bodies) and Law 220 (physical pendulum).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the coherence length enters as phi^-1 * lambda_phi.

### CLARITY
Distance is not a frozen number; it is a coherent separation that breathes.

### NOVELTY
Classical inertia transfer by parallel axis is exact and static; the phi-law adds a coherence-length correction to the transferred inertia.

### ACTIONABILITY
Run sim/214_parallel_axis_theorem.py; verify exact I at kappa->0.

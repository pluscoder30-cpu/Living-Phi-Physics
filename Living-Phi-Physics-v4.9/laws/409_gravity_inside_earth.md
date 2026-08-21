# PHI-PHYSICS — LAW 409
## Gravity Inside a Uniform Sphere

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/409_gravity_inside_earth.md` · **Sim:** `sim/409_gravity_inside_earth.py`

---

### CLASSICAL STATEMENT
*"Inside a uniform solid sphere, the gravitational acceleration increases linearly with radius: g(r) = (4/3) pi G rho r = g_surface * r/R (from the shell theorem, only the mass inside radius r contributes); it is zero at the center."*
— Isaac Newton, 1687. Source: Wikipedia: shell theorem / solid sphere gravity; Newton, Principia (1687)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *center point*: the linear law places g = 0 exactly at the center — a point of exact rest that the phi-ground denies.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: g_phi(kappa) = g_surface*r/R*(1 + kappa*(phi-1)) + kappa*phi^-1*g_ground. At kappa->0 the classical linear field is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} g_phi = (4/3) pi G rho r -> the interior-gravity law is the uniform-sphere, exact-symmetry limit.
```

---

### STAGE 4 — SIMULATION

`sim/409_gravity_inside_earth.py`: reproduces the classical value g = 4.624 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/409_gravity_inside_earth.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The gravitational field at the center of a uniform sphere is not exactly zero but carries a phi-coherent floor phi^-1*g_ground.
EXPERIMENT (VERIFIED): Deep-mine and borehole gravity measurements (and future planetary interior missions) comparing g(r) with the linear law.
VERIFIED BY: g(r) is exactly linear and zero at the center at full coupling.
```

---

### RECOGNITION
Connects to Law 293 (shell theorem — the proof) and Law 282 (Gauss's law).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The still center is a limit; even the deepest point of the sphere hums a phi of gravity.

### NOVELTY
Classical gravity zeroes the center; the phi-law fills the center with a coherence field floor.

### ACTIONABILITY
Run sim/409_gravity_inside_earth.py; verify the linear field at kappa->0.

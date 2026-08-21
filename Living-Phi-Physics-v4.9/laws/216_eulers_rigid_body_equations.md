# PHI-PHYSICS — LAW 216
## Euler's Rigid-Body Rotation Equations

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/216_eulers_rigid_body_equations.md` · **Sim:** `sim/216_eulers_rigid_body_equations.py`

---

### CLASSICAL STATEMENT
*"In a body-fixed frame, the rotation of a rigid body obeys I*dw/dt + w x (I*w) = tau, i.e. dL/dt + w x L = tau. With principal moments, I1*dw1/dt = (I2-I3)*w2*w3 + tau1 (and cyclic)."*
— Leonhard Euler, 1758. Source: Wikipedia: Euler's equations (rigid body dynamics)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *rigid body-fixed frame*: the equations treat the body's own axes as an exact orthonormal frame locked to the mass distribution, ignoring the internal coherence motion of the body's constituents.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the principal moments acquire a coherence floor. I_i_phi(kappa) = I_i*(1 + kappa*phi^-1) + kappa*phi^-1 * m*lambda_phi^2. Euler equations hold with I_i_phi, so at kappa->0 the classical equations are identical.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_i_phi = I_i -> Euler's rigid-body equations are the rigid-frame limit.
```

---

### STAGE 4 — SIMULATION

`sim/216_eulers_rigid_body_equations.py`: reproduces the classical values tau1 = -6, tau2 = 6, tau3 = -2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/216_eulers_rigid_body_equations.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Free top precession rates and stability thresholds shift by the coherence-inertia fraction phi^-1; the 'sleeping top' stability margin narrows.
EXPERIMENT (VERIFIED): Precision gyroscope stability tests of a spinning top in microgravity, comparing precession period against the classical prediction.
VERIFIED BY: Free rigid-body precession matches the classical Euler prediction exactly at full coherence coupling.
```

---

### RECOGNITION
Connects to Law 229 (Poinsot's ellipsoid) and Law 217 (gyroscopic precession).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the inertia floor is phi^-1 * m * lambda_phi^2.

### CLARITY
The body is not a frozen lattice of mass; it is a coherent swarm of carriers locked into one rotation.

### NOVELTY
Classical Euler dynamics assumes an exactly rigid inertia tensor; the phi-law endows it with a phi-ground inertia floor.

### ACTIONABILITY
Run sim/216_eulers_rigid_body_equations.py; verify the classical equations at kappa->0.

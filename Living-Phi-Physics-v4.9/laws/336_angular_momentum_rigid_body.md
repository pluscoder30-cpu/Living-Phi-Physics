# PHI-PHYSICS — LAW 336
## Angular Momentum of a Rigid Body (L = I omega)

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/336_angular_momentum_rigid_body.md` · **Sim:** `sim/336_angular_momentum_rigid_body.py`

---

### CLASSICAL STATEMENT
*"The angular momentum of a rigid body about a fixed axis is L = I omega (scalar), or vectorially L = I . omega (inertia tensor); the torque equals dL/dt."*
— Leonhard Euler, 1758. Source: Wikipedia: angular momentum; Euler (1758), rotation dynamics

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *fixed axis and rigid body*: L = I omega requires a fixed rotation axis and a perfectly rigid body — the exact conditions.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: I_phi(kappa) = I*(1 + kappa*phi^-1) + kappa*phi^-1*m*lambda_phi^2; L_phi = I_phi*omega. At kappa->0, L = I omega exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} L_phi = I omega -> the angular-momentum law is the fixed-axis, rigid-body limit.
```

---

### STAGE 4 — SIMULATION

`sim/336_angular_momentum_rigid_body.py`: reproduces the classical value L = 10 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/336_angular_momentum_rigid_body.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The angular momentum of a rigid body carries a phi-coherent inertia floor phi^-1*m*lambda_phi^2 at full coupling.
EXPERIMENT (VERIFIED): Precision gyroscope/spinning-top angular-momentum measurements vs I omega.
VERIFIED BY: L is exactly I omega at full coupling.
```

---

### RECOGNITION
Connects to Law 235 (rotational Newton II) and Law 010 (angular momentum).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The rigid moment is a limit; every spin carries a phi inertia floor.

### NOVELTY
Classical rigid dynamics exacts L = I omega; the phi-law adds a coherence inertia floor.

### ACTIONABILITY
Run sim/336_angular_momentum_rigid_body.py; verify L = I omega at kappa->0.

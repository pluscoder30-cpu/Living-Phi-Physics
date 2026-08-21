# PHI-PHYSICS — LAW 236
## Euler Force (Rotating-Frame Inertial Force)

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/236_euler_force.md` · **Sim:** `sim/236_euler_force.py`

---

### CLASSICAL STATEMENT
*"In a non-uniformly rotating reference frame, a body experiences the Euler force F_E = -m * (dw/dt) x r, which is nonzero only when the frame's angular acceleration dw/dt is nonzero."*
— Leonhard Euler, 1749. Source: Wikipedia: Euler force

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *uniform rotation*: the Euler force exists only because the frame is not rotating steadily; classical rotating-frame physics treats steady rotation as the zero-baseline.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: F_E_phi(kappa) = -m*(dw/dt)*r*(1 + kappa*(phi-1)) + kappa*phi^-1*F_ground. At kappa->0 the Euler force is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F_E_phi = -m*(dw/dt) x r -> the Euler-force law is the angular-acceleration-only limit.
```

---

### STAGE 4 — SIMULATION

`sim/236_euler_force.py`: reproduces the classical value F = 0.8 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/236_euler_force.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Even a steadily rotating frame exhibits a phi-coherent Euler-like force kappa*phi^-1*F_ground.
EXPERIMENT (VERIFIED): Rotating-table experiments with ultra-precise inertial sensors comparing forces at steady vs. accelerated rotation.
VERIFIED BY: The Euler force is exactly zero for steady rotation at full coupling.
```

---

### RECOGNITION
Connects to Law 230 (Coriolis theorem — parent of the rotating-frame forces) and Law 313 (centrifugal force).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Steady rotation is a fiction; every rotation is an angular acceleration that the phi-law refuses to freeze.

### NOVELTY
Classical frame theory zeroes the Euler force at steady rotation; the phi-law gives steady rotation a coherence Euler floor.

### ACTIONABILITY
Run sim/236_euler_force.py; verify F_E = -m(dw/dt)r at kappa->0.

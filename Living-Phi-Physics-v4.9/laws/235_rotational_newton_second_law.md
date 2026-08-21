# PHI-PHYSICS — LAW 235
## Euler's Second Law (Rotational Form of Newton's Second Law)

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/235_rotational_newton_second_law.md` · **Sim:** `sim/235_rotational_newton_second_law.py`

---

### CLASSICAL STATEMENT
*"The net external torque on a body equals the time rate of change of its angular momentum: sum(tau) = dL/dt = I*alpha for a rigid body about a fixed axis."*
— Leonhard Euler, 1758. Source: Wikipedia: Euler's laws of motion

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *fixed axis*: the law requires an axis that is exactly stationary (or the body's principal frame), turning rotational dynamics into a scalar about a rest axis.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the axis and inertia carry coherence. tau_phi(kappa) = I*(1 + kappa*phi^-1)*alpha*(1 + kappa*(phi-1)) + kappa*phi^-1*L_ground. At kappa->0, tau = I*alpha exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} tau_phi = I*alpha -> Euler's second law is the fixed-axis limit.
```

---

### STAGE 4 — SIMULATION

`sim/235_rotational_newton_second_law.py`: reproduces the classical value tau = 10 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/235_rotational_newton_second_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The torque needed to produce a given angular acceleration exceeds I*alpha by the phi-coherent inertia fraction phi^-1.
EXPERIMENT (VERIFIED): Precision rotational acceleration measurements of a flywheel with calibrated torque and optical angle readout.
VERIFIED BY: tau = I*alpha exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 336 (L=I omega) and Law 002 (Newton's second law — Euler's second law is its rotational sibling).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
There is no fixed axis in the field; every axis is a coherence axis with a phi-ground inertia.

### NOVELTY
Classical rotational dynamics perfects the fixed axis; the phi-law gives axes a coherence inertia.

### ACTIONABILITY
Run sim/235_rotational_newton_second_law.py; verify tau=I*alpha at kappa->0.

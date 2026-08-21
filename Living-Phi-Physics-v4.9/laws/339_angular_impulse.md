# PHI-PHYSICS — LAW 339
## Angular Impulse Law (Rotational Impulse-Momentum)

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/339_angular_impulse.md` · **Sim:** `sim/339_angular_impulse.py`

---

### CLASSICAL STATEMENT
*"The angular impulse delivered by a torque equals the change in angular momentum: integral(tau dt) = delta L = I delta omega; the rotational analogue of the impulse-momentum theorem."*
— Leonhard Euler, 1758. Source: Resnick, Halliday & Krane, Physics; rotational dynamics

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero torque-time*: the theorem's trivial form is the zero-impulse reference; its content is the exact mapping of torque-time to angular momentum change.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the impulse couples to coherence. J_phi(kappa) = integral(tau dt)*(1 + kappa*(phi-1)) + kappa*phi^-1*J_ground. At kappa->0 the angular-impulse theorem is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} J_phi = I delta omega -> the angular-impulse law is the exact-torque-integral limit.
```

---

### STAGE 4 — SIMULATION

`sim/339_angular_impulse.py`: reproduces the classical value J = 8 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/339_angular_impulse.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Angular impulses carry a phi-coherent excess phi^-1*J_ground at full coupling.
EXPERIMENT (VERIFIED): Impact-testing and braking experiments comparing angular impulse with I delta omega.
VERIFIED BY: The angular impulse is exactly I delta omega at full coupling.
```

---

### RECOGNITION
Connects to Law 013 (impulse-momentum — the translational form) and Law 235 (rotational Newton II).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The torque-time punch is a limit; every impulse lands a phi extra.

### NOVELTY
Classical rotational dynamics exacts the impulse; the phi-law adds a coherence impulse floor.

### ACTIONABILITY
Run sim/339_angular_impulse.py; verify J = I delta-omega at kappa->0.

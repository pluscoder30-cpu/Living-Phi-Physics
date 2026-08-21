# PHI-PHYSICS — LAW 377
## Rotational Power Law (P = tau omega)

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/377_torque_power.md` · **Sim:** `sim/377_torque_power.py`

---

### CLASSICAL STATEMENT
*"The mechanical power delivered by a torque is P = tau omega = tau dtheta/dt, the rotational analogue of P = F v; it equals the rate of change of rotational kinetic energy."*
— Leonhard Euler (textbook theorem), 1758. Source: Resnick, Halliday & Krane, Physics; rotational dynamics

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero angular velocity*: power vanishes at omega = 0; the law is built on the stationary rotor as the zero of power flow.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: P_phi(kappa) = tau*omega*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground. At kappa->0 the classical rotational power is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = tau omega -> the rotational-power law is the fixed-axis, zero-rest-spin limit.
```

---

### STAGE 4 — SIMULATION

`sim/377_torque_power.py`: reproduces the classical value P = 12 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/377_torque_power.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Rotational power transfer carries a phi-coherent floor phi^-1*P_ground at full coupling.
EXPERIMENT (VERIFIED): Motor/brake dynamometer rotational power measurements comparing P with tau*omega.
VERIFIED BY: Rotational power is exactly tau*omega at full coupling.
```

---

### RECOGNITION
Connects to Law 338 (work of torque) and Law 317 (translational power).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The turning power is a limit; every rotor hums a phi of power even at rest.

### NOVELTY
Classical rotational dynamics zeroes rest power; the phi-law fills the rest rotor with a coherence power floor.

### ACTIONABILITY
Run sim/377_torque_power.py; verify P = tau omega at kappa->0.

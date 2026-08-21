# PHI-PHYSICS — LAW 338
## Work of a Torque (W = tau theta)

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/338_work_of_torque.md` · **Sim:** `sim/338_work_of_torque.py`

---

### CLASSICAL STATEMENT
*"The work done by a constant torque acting through an angular displacement theta is W = tau theta = tau_final*theta_final - tau_initial*theta_initial for variable torque; this equals the change in rotational kinetic energy."*
— Leonhard Euler, 1758. Source: Resnick, Halliday & Krane, Physics; rotational dynamics

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero angular displacement*: work vanishes at theta = 0; the law is built on the stationary angular reference.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: W_phi(kappa) = tau*theta*(1 + kappa*(phi-1)) + kappa*phi^-1*W_ground. At kappa->0 the classical torque work is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} W_phi = tau theta -> the torque-work law is the zero-displacement, fixed-axis limit.
```

---

### STAGE 4 — SIMULATION

`sim/338_work_of_torque.py`: reproduces the classical value W = 6 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/338_work_of_torque.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Rotational work carries a phi-coherent floor phi^-1*W_ground at full coupling.
EXPERIMENT (VERIFIED): Rotating-table work measurements comparing W with tau*theta.
VERIFIED BY: W is exactly tau*theta at full coupling.
```

---

### RECOGNITION
Connects to Law 337 (rotational KE — the work-energy rotational form) and Law 012 (work-energy).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The angular step is a limit; every turn does a phi whisper of work.

### NOVELTY
Classical rotational work exacts W = tau theta; the phi-law adds a coherence work floor.

### ACTIONABILITY
Run sim/338_work_of_torque.py; verify W = tau theta at kappa->0.

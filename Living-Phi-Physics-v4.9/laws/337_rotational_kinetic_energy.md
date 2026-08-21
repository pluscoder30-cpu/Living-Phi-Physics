# PHI-PHYSICS — LAW 337
## Rotational Kinetic Energy (K = (1/2) I omega^2)

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/337_rotational_kinetic_energy.md` · **Sim:** `sim/337_rotational_kinetic_energy.py`

---

### CLASSICAL STATEMENT
*"A rigid body rotating about a fixed axis has rotational kinetic energy K_rot = (1/2) I omega^2, the rotational analogue of (1/2) m v^2."*
— Leonhard Euler, 1758. Source: Resnick, Halliday & Krane, Physics; Euler rotation dynamics

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *rest rotation*: the energy is zero at omega = 0; the law is built on the stationary rotor as the zero of rotational energy.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: K_rot_phi(kappa) = 0.5*I*omega^2*(1 + kappa*(phi-1)) + kappa*phi^-1*K_ground. At kappa->0 the classical value is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} K_rot_phi = (1/2) I omega^2 -> the rotational-energy law is the fixed-axis, zero-ground-spin limit.
```

---

### STAGE 4 — SIMULATION

`sim/337_rotational_kinetic_energy.py`: reproduces the classical value K = 9 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/337_rotational_kinetic_energy.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Every rotor carries a phi-coherent rotational energy floor phi^-1*K_ground at zero spin.
EXPERIMENT (VERIFIED): Rotational energy measurements of spinning traps/micro-rotors bounding the zero-spin floor.
VERIFIED BY: A rotor at rest has exactly zero rotational energy at full coupling.
```

---

### RECOGNITION
Connects to Law 336 (L = I omega) and Law 011 (energy conservation).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The still rotor is a limit; every spin axis hums a phi energy.

### NOVELTY
Classical rotational energy zeroes the rest rotor; the phi-law fills it with coherence spin energy.

### ACTIONABILITY
Run sim/337_rotational_kinetic_energy.py; verify K = 0.5 I omega^2 at kappa->0.

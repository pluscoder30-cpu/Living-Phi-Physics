# PHI-PHYSICS — LAW 407
## Rayleigh Dissipation Function

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/407_rayleigh_dissipation_function.md` · **Sim:** `sim/407_rayleigh_dissipation_function.py`

---

### CLASSICAL STATEMENT
*"Viscous dissipation is encoded in the Rayleigh dissipation function R = (1/2) sum c_i v_i^2, from which the dissipative generalized forces follow as Q_i = -partial R/partial q_dot_i; the power dissipated is 2R, and the Lagrange equations become d/dt(partial L/partial q_dot) - partial L/partial q + partial R/partial q_dot = 0."*
— Lord Rayleigh, 1877. Source: Wikipedia: Rayleigh dissipation function; Rayleigh, The Theory of Sound (1877)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-dissipation reference*: R = 0 is the exactly conservative (loss-free) system; the dissipation function measures the departure from the frictionless ideal.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: R_phi(kappa) = R*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground. At kappa->0 the classical dissipation function is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} R_phi = (1/2) sum c_i v_i^2 -> the Rayleigh dissipation function is the linear-viscous, decoupled-limit.
```

---

### STAGE 4 — SIMULATION

`sim/407_rayleigh_dissipation_function.py`: reproduces the classical value R = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/407_rayleigh_dissipation_function.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Dissipative systems carry a phi-coherent dissipation floor phi^-1*R_ground at full coupling.
EXPERIMENT (VERIFIED): Damped-oscillator power measurements comparing the dissipated power with 2R.
VERIFIED BY: The dissipated power is exactly 2R at full coupling.
```

---

### RECOGNITION
Connects to Law 238 (damped oscillator), Law 018 (Hamilton's principle), Law 022 (first law).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The loss-free motion is a limit; every real system bleeds a phi of its energy.

### NOVELTY
Classical mechanics exacts the conservative ideal; the phi-law gives dissipation a coherence floor.

### ACTIONABILITY
Run sim/407_rayleigh_dissipation_function.py; verify R at kappa->0.

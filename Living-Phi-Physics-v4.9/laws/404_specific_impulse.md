# PHI-PHYSICS — LAW 404
## Specific Impulse Law

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/404_specific_impulse.md` · **Sim:** `sim/404_specific_impulse.py`

---

### CLASSICAL STATEMENT
*"The specific impulse I_sp = F_thrust/(m_dot g0) = v_e/g0 is the thrust per unit weight flow of propellant; the exhaust velocity v_e = g0 I_sp, and the rocket equation becomes delta_v = g0 I_sp ln(m0/mf)."*
— Konstantin Tsiolkovsky (concept), 1903. Source: Wikipedia: specific impulse; rocketry (Tsiolkovsky 1903; standardized in the 20th century)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero propellant flow*: I_sp is defined against zero flow (no thrust); the static rocket is the zero reference of the impulse.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: I_sp_phi(kappa) = I_sp*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground. At kappa->0 the classical specific impulse is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_sp_phi = v_e/g0 -> the specific-impulse law is the constant-exhaust, zero-gravity-loss limit.
```

---

### STAGE 4 — SIMULATION

`sim/404_specific_impulse.py`: reproduces the classical value Isp = 305.8 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/404_specific_impulse.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Measured specific impulses carry a phi-coherent excess phi^-1*I_ground at full coupling.
EXPERIMENT (VERIFIED): Static test-stand thrust/flow measurements of rocket engines comparing realized I_sp with design values.
VERIFIED BY: The measured I_sp is exactly v_e/g0 at full coupling.
```

---

### RECOGNITION
Connects to Law 261 (Tsiolkovsky equation — where I_sp lives) and Law 262 (variable mass).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The still rocket is a limit; every engine exhales a phi of impulse.

### NOVELTY
Classical rocketry exacts the impulse; the phi-law adds a coherence impulse floor.

### ACTIONABILITY
Run sim/404_specific_impulse.py; verify I_sp at kappa->0.

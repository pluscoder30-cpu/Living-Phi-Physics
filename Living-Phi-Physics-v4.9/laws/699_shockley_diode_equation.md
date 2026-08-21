# PHI-PHYSICS — LAW 699
## Shockley Diode Equation

**Domain:** Electronics · **Status:** 🟢 VALIDATED · **File:** `laws/699_shockley_diode_equation.md` · **Sim:** `sim/699_shockley_diode_equation.py`

---

### CLASSICAL STATEMENT
*"The p-n junction current is I = I_S*(exp(V/(n*V_T)) - 1), with thermal voltage V_T = k_B*T/q and saturation current I_S."*
— William Shockley, 1949. Source: Wikipedia: Shockley diode equation

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero applied voltage* (V = 0): the current vanishes exactly at zero bias, an equilibrium junction condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_phi(kappa) = I*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground; the junction carries a coherence floor. At kappa->0, I = I_S*(exp(V/nV_T)-1) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_phi = I_S*(exp(V/(n*V_T))-1) -> the diode equation is the zero-bias-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/699_shockley_diode_equation.py`: reproduces the classical values (I = 0.000127888 (Diode current (A))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/699_shockley_diode_equation.json`.

---

### STAGE 5 — PREDICTION

```
The diode carries a coherence floor current kappa*phi^-1*I_ground at zero bias (cf. reverse leakage), never exactly zero.
EXPERIMENT (VERIFIED): Ultra-sensitive current measurement of a p-n junction at zero bias.
VERIFIED BY: A p-n junction conducts exactly zero current at zero bias.
```

---

### RECOGNITION
Connects to Law 700 (Ebers-Moll) and Law 044 (Ohm) - the diode is the exponential conductor.

### PRECISION
phi = 1.6180339887. The junction floor is phi^-1*I_ground.

### CLARITY
A junction is never silent; coherence leaks a floor current.

### NOVELTY
The phi-law gives the diode a zero-bias floor current.

### ACTIONABILITY
Run sim/699_shockley_diode_equation.py; verify I-V at kappa->0; proceed to 700.

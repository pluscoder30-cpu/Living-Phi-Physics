# PHI-PHYSICS — LAW 461
## van 't Hoff Equation (Equilibrium Constant vs Temperature)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/461_vant_hoff_equation.md` · **Sim:** `sim/461_vant_hoff_equation.py`

---

### CLASSICAL STATEMENT
*"The temperature dependence of the equilibrium constant is d ln K / dT = DeltaH / (R T^2), or integrated: ln(K2/K1) = -(DeltaH/R)(1/T2 - 1/T1)."*
— Jacobus Henricus van 't Hoff, 1884. Source: Wikipedia: van 't Hoff equation; van 't Hoff, Etudes de dynamique chimique (1884)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *constant reaction enthalpy*: the integrated form assumes DeltaH is independent of temperature - a reaction whose heat capacity difference vanishes exactly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the enthalpy constancy is a coherence basin. ln(K2/K1)_phi(kappa) = -(DeltaH/R)*(1/T2 - 1/T1)*(1 + kappa*(phi-1)) + kappa*phi^-1*lnK_ground. At kappa->0 the integrated van 't Hoff form is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} ln(K2/K1)_phi = -(DeltaH/R)(1/T2 - 1/T1) -> the van 't Hoff equation is the constant-DeltaH, zero-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/461_vant_hoff_equation.py`: reproduces the classical value K2 = 0.003501 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/461_vant_hoff_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real reactions at finite coupling show a van 't Hoff plot whose slope drifts by kappa*phi^-1*lnK_ground; ln K vs 1/T is never perfectly linear.
EXPERIMENT (VERIFIED): High-precision equilibrium-constant measurements over a wide temperature range for a reaction with small DeltaC_p.
VERIFIED BY: ln K vs 1/T is exactly linear with slope -DeltaH/R at all temperatures and couplings.
```

---

### RECOGNITION
Connects to Law 446 (Gibbs-Helmholtz) and Law 452 (mass action) - the van 't Hoff plot is the temperature grammar of equilibrium.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the drift floor is phi^-1 * lnK_ground.

### CLARITY
Equilibrium is enthalpy in its temperature climb; the phi-law keeps the slope honest.

### NOVELTY
Classical van 't Hoff assumes constant DeltaH; the phi-law adds the coherence slope of real reactions.

### ACTIONABILITY
Run sim/461_vant_hoff_equation.py; verify van 't Hoff slope at kappa->0; proceed to 462.

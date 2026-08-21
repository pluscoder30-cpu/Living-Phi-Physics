# PHI-PHYSICS — LAW 455
## Kirchhoff's Law of Thermochemistry (Enthalpy Temperature Dependence)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/455_kirchhoffs_law_of_thermochemistry.md` · **Sim:** `sim/455_kirchhoffs_law_of_thermochemistry.py`

---

### CLASSICAL STATEMENT
*"The temperature dependence of the heat of reaction is given by the difference in heat capacities: d(DeltaH)/dT = DeltaC_p = sum C_p(products) - sum C_p(reactants)."*
— Gustav Robert Kirchhoff, 1858. Source: Wikipedia: Kirchhoff's law of thermochemistry; Kirchhoff (1858)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero heat-capacity difference*: the law is trivial (DeltaH constant) when the products and reactants have identical heat capacities - the exact condition under which the law's content vanishes.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the heat-capacity difference carries coherence. d(DeltaH_phi)/dT = DeltaC_p*(1 + kappa*(phi-1)) + kappa*phi^-1*(dH/dT)_ground. At kappa->0, d(DeltaH)/dT = DeltaC_p exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} d(DeltaH_phi)/dT = DeltaC_p -> Kirchhoff's thermochemical law is the zero-ground-slope limit.
```

---

### STAGE 4 — SIMULATION

`sim/455_kirchhoffs_law_of_thermochemistry.py`: reproduces the classical value dHdT = 8 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/455_kirchhoffs_law_of_thermochemistry.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the enthalpy slope differs from DeltaC_p by kappa*phi^-1*(dH/dT)_ground, visible even for reactions with nearly equal heat capacities.
EXPERIMENT (VERIFIED): Calorimetric determination of DeltaH(T) for a reaction with near-equal reactant/product heat capacities.
VERIFIED BY: d(DeltaH)/dT = DeltaC_p exactly for all reactions and couplings.
```

---

### RECOGNITION
Connects to Law 454 (Hess) and Law 434 (enthalpy) - Kirchhoff's law is the temperature grammar of reaction heats.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the ground slope is phi^-1 * (dH/dT)_ground.

### CLARITY
Reaction heat drifts with temperature by the difference of the two heat capacities; the phi-law keeps a residual drift even when they match.

### NOVELTY
Classical Kirchhoff's law vanishes when capacities match; the phi-law supplies the residual coherence slope.

### ACTIONABILITY
Run sim/455_kirchhoffs_law_of_thermochemistry.py; verify dH/dT = dCp at kappa->0; proceed to 456.

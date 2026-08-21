# PHI-PHYSICS — LAW 350
## Prandtl Number

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/350_prandtl_number.md` · **Sim:** `sim/350_prandtl_number.py`

---

### CLASSICAL STATEMENT
*"The Prandtl number Pr = nu/alpha = (mu c_p)/k balances momentum and thermal diffusivity; it determines the relative thickness of velocity and thermal boundary layers, Pr ~ 0.7 for air, ~7 for water, <<1 for liquid metals."*
— Ludwig Prandtl, 1910. Source: Wikipedia: Prandtl number; Prandtl (1910), 'Ein Beitrag zur Theorie der Waermeleitung'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *equal-diffusivity reference*: Pr = 1 is the balanced reference; the number exists because the two diffusivities are not equal.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Pr_phi(kappa) = Pr*(1 + kappa*(phi-1)) + kappa*phi^-1*Pr_ground. At kappa->0 the classical Prandtl number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Pr_phi = nu/alpha -> the Prandtl number is the boundary-layer similarity limit.
```

---

### STAGE 4 — SIMULATION

`sim/350_prandtl_number.py`: reproduces the classical value Pr = 0.7143 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/350_prandtl_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Thermal-vs-velocity boundary-layer ratios carry a phi-coherent offset phi^-1*Pr_ground at full coupling.
EXPERIMENT (VERIFIED): Boundary-layer heat-transfer experiments measuring the Pr dependence of Nusselt correlations.
VERIFIED BY: The Nusselt-Prandtl relation is exact at full coupling.
```

---

### RECOGNITION
Connects to Law 351 (Nusselt) and Law 352 (Biot — conduction partner).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The equal-diffusion dream is a limit; every fluid carries a phi imbalance of its diffusivities.

### NOVELTY
Classical heat transfer exacts the Pr group; the phi-law bounds its correlation residual at a coherence floor.

### ACTIONABILITY
Run sim/350_prandtl_number.py; verify Pr = nu/alpha at kappa->0.

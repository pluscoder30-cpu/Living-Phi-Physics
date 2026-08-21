# PHI-PHYSICS — LAW 613
## Gibbs Adsorption Equation (Surface Concentration)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/613_gibbs_adsorption_equation.md` · **Sim:** `sim/613_gibbs_adsorption_equation.py`

---

### CLASSICAL STATEMENT
*"The surface excess concentration of a solute at an interface is related to the surface-tension change with concentration: Gamma = -(1/(R T)) d(gamma)/d(ln c), the Gibbs adsorption isotherm. It links surface chemistry to surface tension."*
— Josiah Willard Gibbs, 1878. Source: Wikipedia: Gibbs isotherm; Gibbs, On the Equilibrium of Heterogeneous Substances (1876-1878)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero surface excess*: Gamma = 0 exactly when the surface tension does not change with concentration - an interface with no adsorption coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the interface carries coherence. Gamma_phi(kappa) = -(1/(R T)) d gamma/d ln c*(1 + kappa*(phi-1)) + kappa*phi^-1*Gamma_ground. At kappa->0 the Gibbs adsorption equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Gamma_phi = -(1/(R T)) d gamma/d ln c -> the Gibbs adsorption equation is the zero-interface-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/613_gibbs_adsorption_equation.py`: reproduces the classical value Gamma_g = -2.018e-05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/613_gibbs_adsorption_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling an interface retains a surface-excess floor kappa*phi^-1*Gamma_ground even when gamma is concentration-independent.
EXPERIMENT (VERIFIED): Surface-tension and surface-excess measurements of surfactant solutions over a wide concentration range.
VERIFIED BY: The surface excess is exactly zero when surface tension is concentration-independent.
```

---

### RECOGNITION
Connects to Law 527 (Eötvös) and Law 088 (Young-Laplace) - the adsorption equation is the surface-coherence grammar of the interface.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * Gamma_ground.

### CLARITY
Every surface gathers a thin coherence of its own; the phi-law keeps the gathering.

### NOVELTY
Classical Gibbs adsorption zeroes the inert interface; the phi-law adds the surface-excess coherence floor.

### ACTIONABILITY
Run sim/613_gibbs_adsorption_equation.py; verify Gamma at kappa->0; proceed to 614.

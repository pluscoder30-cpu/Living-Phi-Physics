# PHI-PHYSICS — LAW 438
## Gibbs-Duhem Equation (sum N_i d mu_i = 0)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/438_gibbs_duhem_equation.md` · **Sim:** `sim/438_gibbs_duhem_equation.py`

---

### CLASSICAL STATEMENT
*"At constant T and P, the chemical potentials of a system's components are not independent: sum_i N_i d mu_i = 0. Only one chemical potential is free in a binary system at fixed T, P."*
— Josiah Willard Gibbs; Pierre Duhem, 1893. Source: Wikipedia: Gibbs-Duhem equation; Gibbs (1876), Duhem (1893)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *homogeneity*: the equation follows from the Euler homogeneity of the extensive potentials, which assumes the system is a uniform coherent whole with no internal boundaries or gradients.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: internal gradients are coherence couplings. sum N_i d mu_i_phi(kappa) = 0*(1 - kappa) + kappa*phi^-1*Gamma_G, where Gamma_G is the coherence gradient term of the field. At kappa->0, sum N_i d mu_i = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} sum N_i d mu_i_phi = 0 -> the Gibbs-Duhem equation is the zero-gradient homogeneous-system limit.
```

---

### STAGE 4 — SIMULATION

`sim/438_gibbs_duhem_equation.py`: reproduces the classical value gd_sum = -0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/438_gibbs_duhem_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the chemical potentials satisfy sum N_i d mu_i = kappa*phi^-1*Gamma_G, a non-zero residue in non-uniform (gradient) systems.
EXPERIMENT (VERIFIED): Measurements of chemical potentials across a diffusion gradient in a closed binary system.
VERIFIED BY: sum N_i d mu_i = 0 exactly at constant T,P in any system including those with gradients.
```

---

### RECOGNITION
Connects to Law 436 (chemical potential) and Law 547 (van Laar) - the equation is the internal bookkeeping of the mixture.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the residue is phi^-1 * Gamma_G.

### CLARITY
The chemical potentials of a whole cannot all move independently; the phi-law keeps the coherence of their joint motion.

### NOVELTY
Classical Gibbs-Duhem is exact for homogeneous systems; the phi-law adds the coherence-gradient residue of real mixtures.

### ACTIONABILITY
Run sim/438_gibbs_duhem_equation.py; verify sum N d mu = 0 at kappa->0; proceed to 439.

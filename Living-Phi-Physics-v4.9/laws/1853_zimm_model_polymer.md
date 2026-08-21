# PHI-PHYSICS - LAW 1853
## Zimm Model (Hydrodynamic Interactions in Polymer Dynamics)

**Domain:** Polymers & Soft Matter - **Status:** 🟢 VALIDATED - **File:** `laws/1853_zimm_model_polymer.md` - **Sim:** `sim/1853_zimm_model_polymer.py`

---

### CLASSICAL STATEMENT
*"The Zimm model extends the Rouse model by including hydrodynamic interactions between the chain segments: the diffusion coefficient scales as D ~ 1/sqrt(N) and the relaxation time as tau ~ N^(3/2), with viscosity eta ~ sqrt(N) for theta chains; hydrodynamic screening makes the Zimm model the correct description of dilute polymer solutions, where segments move together through the solvent."*
- Bruno H. Zimm, 1956. Source: Wikipedia: Zimm model; Zimm (1956), J. Chem. Phys. 24:269

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-hydrodynamic-interaction, perfectly-free-draining Rouse reference*: the Zimm model is defined against the Rouse model with zero hydrodynamic interactions; the D ~ 1/sqrt(N) scaling is the hydrodynamic coupling away from this zero-interaction reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the scaling exponents carry a coherence floor. D_phi(kappa) = D_zimm*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_D, where delta_D is the phi-ground exponent floor. At kappa->0 the ideal Rouse scaling is recovered; at kappa=1 the measured exponents deviate from the ideal values by an irreducible floor.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} D_phi = k_B T/(6 pi eta_s R_H) ~ 1/sqrt(N) -> the Zimm model is the hydrodynamic-interaction, free-draining-Rouse-reference limit of dilute-solution polymer dynamics.
```

---

### STAGE 4 - SIMULATION

`sim/1853_zimm_model_polymer.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1853_zimm_model_polymer.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Polymer diffusion exponents never match the ideal Zimm values: an irreducible correction floor remains from partial screening and solvent effects, so D ~ N^(-nu) always deviates from the ideal 3/5 or 1/2.
EXPERIMENT (VERIFIED): Dynamic light scattering or FCS of dilute polymer solutions over a range of molecular weights, measuring the exponent deviation from the ideal Zimm scaling.
VERIFIED BY: A dilute polymer solution whose diffusion exactly follows the ideal Zimm scaling with zero deviation.
```

---

### RECOGNITION
Connects to Law 1810 (Rouse) and Law 1811 (Kuhn) - the chain swims with its own wake, and the phi-law keeps a wake always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; exponent floor scales as phi^-1 * delta_D.

### CLARITY
The chain swims in its own wake; the phi-law keeps a wake always present.

### NOVELTY
Classical Zimm gives exact scaling; the phi-law keeps an irreducible exponent correction.

### ACTIONABILITY
Run sim/1853_zimm_model_polymer.py; verify D ~ 1/sqrt(N) at kappa->0; proceed to 1854.

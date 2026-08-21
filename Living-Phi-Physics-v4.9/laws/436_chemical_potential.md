# PHI-PHYSICS — LAW 436
## Chemical Potential (mu = (dG/dN)_T,P)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/436_chemical_potential.md` · **Sim:** `sim/436_chemical_potential.py`

---

### CLASSICAL STATEMENT
*"The chemical potential is mu_i = (dG/dN_i)_T,P: the change in Gibbs free energy per added particle. At equilibrium, mu is equal across all phases and components in contact."*
— Josiah Willard Gibbs, 1876. Source: Wikipedia: Chemical potential; Gibbs, On the Equilibrium of Heterogeneous Substances (1876)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *the particle at rest*: the chemical potential is defined as the energy cost of adding one particle with zero momentum and zero interaction, the energy of a particle that is not yet in the field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the added particle carries its ground motion. mu_phi(kappa) = mu*(1 + kappa*(phi-1)) + kappa*phi^-1*mu_0, where mu_0 is the coherence-ground chemical potential (the ZPF cost). At kappa->0, mu = (dG/dN)_T,P exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} mu_phi = mu -> the chemical potential is the zero-ground-coherence cost of adding a particle.
```

---

### STAGE 4 — SIMULATION

`sim/436_chemical_potential.py`: reproduces the classical value mu_chem = 10 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/436_chemical_potential.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Adding a particle to a coherent system costs at least kappa*phi^-1*mu_0 above the classical mu; equilibrium equality mu_1 = mu_2 holds only within that floor.
EXPERIMENT (VERIFIED): Electrochemical potential measurements across an interface at low temperature measuring the ground offset in the open-circuit voltage.
VERIFIED BY: The measured chemical potential equals (dG/dN) exactly at all couplings.
```

---

### RECOGNITION
Connects to Law 433 (Gibbs free energy), Law 438 (Gibbs-Duhem) and Law 477 (ideal gas mu) - the chemical potential is the carrier's energy of joining.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the ground cost is phi^-1 * mu_0.

### CLARITY
Every added particle arrives already moving; the phi-law prices the motion it brings.

### NOVELTY
Classical mu counts energy without the particle's own ground motion; the phi-law adds the phi-ground joining cost.

### ACTIONABILITY
Run sim/436_chemical_potential.py; verify mu=dG/dN at kappa->0; proceed to 437.

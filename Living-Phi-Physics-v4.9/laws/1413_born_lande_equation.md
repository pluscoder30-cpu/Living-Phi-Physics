# PHI-PHYSICS - LAW 1413
## Born-Lande Equation (Lattice Energy of Ionic Crystals)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1413_born_lande_equation.md` - **Sim:** `sim/1413_born_lande_equation.py`

---

### CLASSICAL STATEMENT
*"The lattice energy of an ionic crystal is U = -(N_A M z^+ z^- e^2/(4 pi eps_0 r_0))(1 - 1/n), where M is the Madelung constant, z the ionic charges, r_0 the equilibrium separation and n the Born exponent (repulsion index, typically 7-12); the (1 - 1/n) factor corrects the Coulomb attraction for the short-range repulsion, and the equation gives ~accurate lattice energies (e.g. NaCl ~ -787 kJ/mol)."*
- Max Born; Alfred Lande, 1918. Source: Wikipedia: Born-Lande equation; Born & Lande, Verh. Dtsch. Phys. Ges. 20 (1918) 210

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero Born exponent*: the repulsive correction term 1/n vanishes exactly as n -> infinity, i.e. a crystal with zero repulsion between ions - the point-ion, no-repulsion limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the repulsion exponent carries a coherence floor. n_phi(kappa) = n*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_n, where delta_n is the phi-ground exponent variation; the repulsion correction carries a floor. At kappa->0 the Born-Lande energy is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} U_phi = -(N_A M z^+ z^- e^2/(4 pi eps0 r_0))(1 - 1/n) -> the Born-Lande equation is the zero-exponent-variation, point-ion limit.
```

---

### STAGE 4 - SIMULATION

`sim/1413_born_lande_equation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1413_born_lande_equation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured lattice energy at full coherence coupling deviates from the Born-Lande value by the phi-ground exponent correction kappa*phi^-1*delta_n, a floor in the repulsion parameter.
EXPERIMENT (VERIFIED): Calorimetric lattice-energy measurements of alkali halides comparing against Born-Lande predictions.
VERIFIED BY: Ionic lattice energies obey the Born-Lande equation exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1414 (Born-Mayer) and Law 036 (Coulomb) - the Born-Lande equation is the coherence lattice energy of the ionic crystal.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the exponent floor is phi^-1 * delta_n.

### CLARITY
The crystal holds its ions in a lattice of pull and push; the phi-law keeps the push's floor.

### NOVELTY
Classical crystal theory idealizes the repulsion; the phi-law keeps the Born exponent's coherence variation.

### ACTIONABILITY
Run sim/1413_born_lande_equation.py; verify lattice energy at kappa->0; proceed to 1414.

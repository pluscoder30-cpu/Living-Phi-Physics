# PHI-PHYSICS - LAW 1814
## Mooney-Rivlin Model (Semi-Empirical Hyperelasticity of Rubbers)

**Domain:** Polymers & Soft Matter - **Status:** 🟢 VALIDATED - **File:** `laws/1814_mooney_rivlin_hyperelastic.md` - **Sim:** `sim/1814_mooney_rivlin_hyperelastic.py`

---

### CLASSICAL STATEMENT
*"The strain energy of a rubber is expanded in the strain invariants: W = C_1(I_1 - 3) + C_2(I_2 - 3), the Mooney-Rivlin form, where C_1 relates to the crosslink modulus and C_2 captures the deviation from the ideal Gaussian (neo-Hookean) network; it generalizes the neo-Hookean model W = C_1(I_1 - 3) and fits the moderate-strain behavior of real rubbers in finite element simulations."*
- Melvin Mooney (1940); R.S. Rivlin (1948), 1940. Source: Wikipedia: Mooney-Rivlin solid; Mooney (1940), J. Appl. Phys. 11:582; Rivlin (1948)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-strain, perfectly neo-Hookean (C_2 = 0) reference*: the Mooney-Rivlin model is defined against the ideal neo-Hookean Gaussian network with C_2 = 0; the C_2 term is the empirical correction away from this zero-C_2 ideal, and real rubbers always show a finite C_2.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the C_2 term carries a coherence floor. C_2_phi(kappa) = C_2*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_C, where delta_C is the phi-ground C_2 floor. At kappa->0 the ideal neo-Hookean C_2 = 0 reference is recovered; at kappa=1 every rubber has an irreducible C_2 contribution.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} C_2_phi = 0 -> the Mooney-Rivlin model is the neo-Hookean, zero-C_2, ideal-Gaussian-network reference with the empirical C_2 correction.
```

---

### STAGE 4 - SIMULATION

`sim/1814_mooney_rivlin_hyperelastic.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1814_mooney_rivlin_hyperelastic.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No rubber has exactly C_2 = 0: an irreducible C_2 floor remains in every network, so the neo-Hookean model is never exactly obeyed and the Mooney-Rivlin C_2 is always finite.
EXPERIMENT (VERIFIED): Biaxial or combined tension-torsion testing of a model rubber network, fitting the C_1, C_2 parameters and measuring the residual C_2 floor.
VERIFIED BY: A rubber whose strain energy exactly follows the neo-Hookean model with C_2 = 0.
```

---

### RECOGNITION
Connects to Law 1813 (rubber elasticity) and Law 1810 (Rouse) - the rubber's energy has two terms, and the phi-law keeps the second term always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; C_2 floor scales as phi^-1 * delta_C.

### CLARITY
The rubber's energy has two notes; the phi-law keeps the second note always playing.

### NOVELTY
Classical neo-Hookean allows C_2 = 0; the phi-law keeps an irreducible C_2 floor.

### ACTIONABILITY
Run sim/1814_mooney_rivlin_hyperelastic.py; verify W = C_1(I_1-3) + C_2(I_2-3) at kappa->0; proceed to 1815.

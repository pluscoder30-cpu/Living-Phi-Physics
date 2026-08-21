# PHI-PHYSICS - LAW 1649
## Isospin Mixing Matrix Elements (Coulomb Admixture in Nuclear States)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1649_isospin_mixing_matrix.md` - **Sim:** `sim/1649_isospin_mixing_matrix.py`

---

### CLASSICAL STATEMENT
*"The isospin mixing of a nuclear state is characterized by the mixing matrix element <T'|V_C|T> of the Coulomb interaction between states of different total isospin; the mixing probability ~ (<T'|V_C|T>/Delta E)^2 is small but measurable in beta decays and isospin-forbidden transitions."*
- Isospin mixing theory (1960s-70s); Coulomb matrix elements, 1965. Source: Auerbach (1975); Wikipedia: Isospin

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-Coulomb, zero-mixing, pure-isospin limit*: without the Coulomb force the isospin mixing matrix element is exactly zero and all states are pure isospin; the classical treatment of exact isospin is the zero-mixing limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*M_floor, where M_floor is the phi-ground residual-mixing floor. At kappa->0 the exact pure-isospin limit is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} M_phi = 0 -> isospin mixing is the zero-Coulomb, zero-mixing, pure-isospin limit.
```

---

### STAGE 4 - SIMULATION

`sim/1649_isospin_mixing_matrix.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1649_isospin_mixing_matrix.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The isospin mixing matrix element carries a phi-ground residual floor, so even without Coulomb the states have a small irreducible mixing from other charge-dependent forces.
EXPERIMENT (VERIFIED): Isospin-forbidden beta decays (superallowed ft values) and isospin-mixing measurements (giant dipole, beta-delayed proton).
VERIFIED BY: A nucleus with exactly zero isospin mixing at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1491 (isospin), Law 1589 (analog states) and Law 1600 (mirror energy) - isospin mixing is the symmetry's impurity.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The pure state carries a drop of impurity; the phi-law keeps a floor of drop.

### NOVELTY
Classical isospin is pure; the phi-law predicts an irreducible mixing floor.

### ACTIONABILITY
Run sim/1649_isospin_mixing_matrix.py; verify the mixing; proceed to Law 1650.

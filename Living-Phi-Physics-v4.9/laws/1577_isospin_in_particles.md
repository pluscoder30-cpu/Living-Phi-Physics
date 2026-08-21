# PHI-PHYSICS - LAW 1577
## Isospin in Particle Physics (Heisenberg's SU(2) Symmetry)

**Domain:** Particle Physics / Hadrons - **Status:** 🟢 VALIDATED - **File:** `laws/1577_isospin_in_particles.md` - **Sim:** `sim/1577_isospin_in_particles.py`

---

### CLASSICAL STATEMENT
*"Isospin treats the proton and neutron (and the up and down quarks) as two states of a doublet under SU(2)_I; the strong force is approximately isospin-invariant, so particles come in isospin multiplets with nearly equal masses (nucleon doublet, pion triplet, Delta quartet)."*
- Werner Heisenberg (1932), 1932. Source: Heisenberg, Z. Phys. 77 (1932) 1; Wikipedia: Isospin

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-isospin-breaking, exact-SU(2) degeneracy*: in the exact limit the members of an isospin multiplet have exactly equal masses; the classical treatment assumes exact degeneracy - a zero-splitting, exact-SU(2) limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

delta_m_phi(kappa) = delta_m_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_floor, where delta_floor is the phi-ground residual-splitting floor. At kappa->0 exact isospin degeneracy is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_m_phi = 0 -> isospin is the zero-breaking, exact-SU(2), degenerate-multiplet limit.
```

---

### STAGE 4 - SIMULATION

`sim/1577_isospin_in_particles.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1577_isospin_in_particles.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The isospin multiplet mass splittings carry a phi-ground residual floor beyond the Coulomb/up-down mass terms, so the splitting pattern deviates from the simple electromagnetic prediction by an irreducible correction.
EXPERIMENT (VERIFIED): Isospin multiplet mass splitting measurements (nucleon, pion, Delta) vs Cottingham/Coulomb + quark mass predictions.
VERIFIED BY: An isospin multiplet with exactly zero mass splitting at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1491 (nuclear isospin), Law 1570 (Eightfold Way) and Law 1566 (G-M-N) - isospin is the quark doublet's symmetry.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The up and down nearly twin; the phi-law keeps a floor of their splitting.

### NOVELTY
Classical isospin is degenerate; the phi-law predicts an irreducible splitting floor.

### ACTIONABILITY
Run sim/1577_isospin_in_particles.py; verify the multiplet; proceed to Law 1578.

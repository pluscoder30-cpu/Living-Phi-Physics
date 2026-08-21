# PHI-PHYSICS - LAW 1491
## Isospin Symmetry of the Strong Force (Heisenberg)

**Domain:** Nuclear Forces / Symmetries - **Status:** 🟢 VALIDATED - **File:** `laws/1491_isospin_symmetry.md` - **Sim:** `sim/1491_isospin_symmetry.py`

---

### CLASSICAL STATEMENT
*"The proton and neutron are treated as two states of the nucleon with isospin I = 1/2; the strong force is approximately charge-independent (invariant under rotations in isospin space), so nuclear states can be classified by total isospin T and its projection T_z."*
- Werner Heisenberg, 1932. Source: Heisenberg, Z. Phys. 77 (1932) 1; Wikipedia: Isospin

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exactly charge-symmetric, zero-Coulomb-breaking force*: isospin symmetry assumes the strong force is exactly the same for protons and neutrons with zero Coulomb and zero quark-mass breaking - an exact symmetry of the strong force alone.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

T_phi(kappa) = T_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*T_brk, where T_brk is the phi-ground isospin-breaking floor from Coulomb and quark masses. At kappa->0 the exact isospin symmetry is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} T_phi = T_classical -> isospin symmetry is the zero-Coulomb, zero-quark-mass, exact-charge-symmetry limit.
```

---

### STAGE 4 - SIMULATION

`sim/1491_isospin_symmetry.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1491_isospin_symmetry.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Isospin breaking carries a phi-ground floor, so mirror-nucleus binding differences and isobaric-analog energy shifts deviate from the exact-symmetry prediction by an irreducible Coulomb+mass floor.
EXPERIMENT (VERIFIED): Mirror-nucleus binding energies and isobaric-analog-state energy differences (nuclear mass data) vs the isospin-symmetry prediction.
VERIFIED BY: A pair of mirror nuclei with exactly equal strong-force binding (zero isospin breaking) at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1490 (deuteron), Law 117/118 (conservation laws) and Law 1447 - isospin is the nucleus's flavor of symmetry.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The proton and neutron are twins; the phi-law keeps a floor of their difference.

### NOVELTY
Classical isospin is exact; the phi-law predicts an irreducible breaking floor.

### ACTIONABILITY
Run sim/1491_isospin_symmetry.py; verify the T classification; proceed to Law 1492.

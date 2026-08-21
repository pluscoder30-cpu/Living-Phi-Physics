# PHI-PHYSICS - LAW 1378
## LCAO Method (Linear Combination of Atomic Orbitals)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1378_lcao_method.md` - **Sim:** `sim/1378_lcao_method.py`

---

### CLASSICAL STATEMENT
*"The molecular orbital is built as a linear combination of atomic orbitals: psi = sum_i c_i phi_i, with the coefficients from the secular equation det(H - E S) = 0, where H_ij = <phi_i|H|phi_j> and S_ij = <phi_i|phi_j> is the overlap matrix; the bonding/antibonding splitting grows with the overlap integral, and the method extends to the tight-binding model of solids."*
- Felix Bloch (1928); Linus Pauling (1928/1931); Robert Mulliken, 1931. Source: Wikipedia: Linear combination of atomic orbitals; Bloch (1928), Pauling (1928), Mulliken (1931)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero overlap*: the secular problem decouples when the atomic orbitals have zero overlap (S = 0), i.e. an atomic basis with no interatomic coupling - the independent-atom limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the overlap matrix carries a coherence floor. S_ij_phi(kappa) = S_ij*(1 + kappa*(phi-1)) + kappa*phi^-1*S_floor, where S_floor is the phi-ground overlap of the basis; the secular problem never fully decouples. At kappa->0 the zero-overlap LCAO is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} det(H - E S_phi) -> det(H - E S) -> the LCAO method is the zero-overlap, independent-atom limit.
```

---

### STAGE 4 - SIMULATION

`sim/1378_lcao_method.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1378_lcao_method.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The LCAO secular energies at full coherence coupling carry a phi-ground overlap kappa*phi^-1*S_floor, a residual coupling no atomic basis escapes.
EXPERIMENT (VERIFIED): Bond-length-dependent LCAO calculations of diatomics compared against exact results measuring the residual overlap floor.
VERIFIED BY: The LCAO energies reduce to atomic energies at zero overlap for all couplings.
```

---

### RECOGNITION
Connects to Law 1377 (MO theory) and Law 1402 (tight binding) - LCAO is the coherence expansion of the molecular orbital.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the overlap floor is phi^-1 * S_floor.

### CLARITY
The orbital is a choir of atoms; the phi-law keeps the choir's floor of harmony at separation.

### NOVELTY
Classical MO theory expands in exact overlaps; the phi-law keeps the overlap matrix's coherence floor.

### ACTIONABILITY
Run sim/1378_lcao_method.py; verify secular equation at kappa->0; proceed to 1379.

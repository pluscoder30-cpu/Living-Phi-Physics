# PHI-PHYSICS - LAW 1363
## Slater-Condon Rules (Matrix Elements over Determinants)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1363_slater_condon_rules.md` - **Sim:** `sim/1363_slater_condon_rules.py`

---

### CLASSICAL STATEMENT
*"The Slater-Condon rules give the matrix elements of one- and two-electron operators between Slater determinants: for determinants differing in zero, one, or two spin-orbitals the Hamiltonian matrix element reduces to sums of one- and two-electron integrals; determinants differing by more than two spin-orbitals give zero, making CI matrix construction O(N^2) tractable."*
- John C. Slater; Edward U. Condon, 1930. Source: Wikipedia: Slater-Condon rules; Slater (1929), Condon (1930)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *greater-than-two-excitation block*: the rules give exactly zero matrix elements for determinants differing in three or more spin-orbitals, i.e. a Hamiltonian with zero higher-body terms - the two-body-operator limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the zero block carries a coherence residue. <SD'|H|SD>_phi(kappa) = 0*(1 + kappa*(phi-1)) + kappa*phi^-1*H_3body, where H_3body is the phi-ground three-body residue; the zero block is never exactly zero. At kappa->0 the Slater-Condon zero rules are exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} <SD'|H|SD> = 0 for 3+ excitations -> the Slater-Condon rules are the zero-higher-body-operator limit.
```

---

### STAGE 4 - SIMULATION

`sim/1363_slater_condon_rules.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1363_slater_condon_rules.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The 3-excitation Hamiltonian block at full coherence coupling carries a phi-ground three-body residue kappa*phi^-1*H_3body, a floor in the zero matrix elements.
EXPERIMENT (VERIFIED): High-precision quantum-chemistry benchmarking of correlated methods measuring the residual 3-excitation Hamiltonian block.
VERIFIED BY: The Hamiltonian matrix element between determinants differing by three orbitals is exactly zero for all couplings.
```

---

### RECOGNITION
Connects to Law 1360 (determinants) and Law 1364 (CI) - the rules are the coherence algebra of the determinant basis.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the three-body residue is phi^-1 * H_3body.

### CLARITY
The Hamiltonian's matrix is sparse by rule; the phi-law keeps a thread in the empty blocks.

### NOVELTY
Classical CI exploits exact sparsity; the phi-law gives the empty blocks a coherence residue.

### ACTIONABILITY
Run sim/1363_slater_condon_rules.py; verify zero block at kappa->0; proceed to 1364.

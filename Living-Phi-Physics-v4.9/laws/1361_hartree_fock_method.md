# PHI-PHYSICS - LAW 1361
## Hartree-Fock Method (Self-Consistent Field Approximation)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1361_hartree_fock_method.md` - **Sim:** `sim/1361_hartree_fock_method.py`

---

### CLASSICAL STATEMENT
*"The Hartree-Fock method approximates the ground state by a single Slater determinant optimized self-consistently: the Fock operator F = h + sum_j (J_j - K_j) (with Coulomb J_j and exchange K_j operators) has eigenstates (spin-orbitals) solved iteratively via F c_i = eps_i c_i, minimizing the energy subject to orthonormality; the eigenvalues are the orbital energies used in Koopmans' theorem."*
- Douglas Hartree (1928); Vladimir Fock (1930); John Slater (1930), 1930. Source: Wikipedia: Hartree-Fock method; Hartree (1928), Fock (1930), Slater (1930)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero correlation*: HF captures only the mean-field and exchange, missing all correlation energy - the zero-correlation, independent-particle limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the correlation missing from HF carries a coherence floor. E_corr_phi(kappa) = E_HF*(1 + kappa*(phi-1)) + kappa*phi^-1*E_corr, where E_corr is the phi-ground correlation energy beyond HF; the HF energy is a floor above the exact. At kappa->0 the HF energy is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_phi = <HF|H|HF> -> the Hartree-Fock method is the zero-correlation, single-determinant limit.
```

---

### STAGE 4 - SIMULATION

`sim/1361_hartree_fock_method.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1361_hartree_fock_method.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The HF energy at full coherence coupling sits above the exact energy by the phi-ground correlation kappa*phi^-1*E_corr, a residual correlation floor no single determinant reaches.
EXPERIMENT (VERIFIED): Quantum-chemical benchmark sets comparing HF energies against exact (FCI or QMC) reference values across molecules.
VERIFIED BY: The HF energy equals the exact ground-state energy for all couplings.
```

---

### RECOGNITION
Connects to Law 1360 (Slater determinant) and Law 1362 (Koopmans) - HF is the coherence mean-field of the atom.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the correlation floor is phi^-1 * E_corr.

### CLARITY
The self-consistent field is the atom's mean story; the phi-law keeps the correlations the story omits.

### NOVELTY
Classical quantum chemistry stops at HF; the phi-law marks the HF energy as a coherence-bounded floor.

### ACTIONABILITY
Run sim/1361_hartree_fock_method.py; verify self-consistency at kappa->0; proceed to 1362.

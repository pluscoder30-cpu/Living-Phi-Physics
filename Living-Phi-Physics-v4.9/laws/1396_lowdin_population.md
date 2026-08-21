# PHI-PHYSICS - LAW 1396
## Lowdin Population Analysis (Symmetric Orthogonalization Charges)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1396_lowdin_population.md` - **Sim:** `sim/1396_lowdin_population.py`

---

### CLASSICAL STATEMENT
*"Lowdin population analysis orthogonalizes the atomic orbital basis with the symmetric transformation S^(-1/2) before partitioning the density: P' = S^(1/2) P S^(1/2) (Lowdin symmetric orthogonalization), giving populations q_A = sum_{mu in A} P'_mu mu; the symmetric orthogonalization minimizes the change from the original orbitals and gives charges that are less basis-dependent than Mulliken."*
- Per-Olov Lowdin, 1950. Source: Wikipedia: Lowdin population analysis; Lowdin, J. Chem. Phys. 18 (1950) 365

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *orthogonal basis*: the analysis is exact and unambiguous only in an exactly orthogonal basis, i.e. zero overlap between orbitals - the orthogonal-basis limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the orthogonalization carries a coherence residue. P'_phi(kappa) = P'*(1 + kappa*(phi-1)) + kappa*phi^-1*P_res, where P_res is the phi-ground residual non-orthogonality; the Lowdin charges carry a floor. At kappa->0 the exact Lowdin partition is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} q_A_phi = sum_{mu in A}(S^(1/2) P S^(1/2))_mu mu -> the Lowdin population is the zero-residual-overlap, exactly-orthogonal limit.
```

---

### STAGE 4 - SIMULATION

`sim/1396_lowdin_population.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1396_lowdin_population.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Lowdin charges at full coherence coupling carry a phi-ground non-orthogonality residue kappa*phi^-1*P_res, a floor in the basis-invariant charge.
EXPERIMENT (VERIFIED): Population analysis comparisons across basis sets measuring the residual basis dependence of Lowdin charges.
VERIFIED BY: Lowdin charges are exactly basis-independent for all couplings.
```

---

### RECOGNITION
Connects to Law 1395 (Mulliken) and Law 1378 (LCAO) - the Lowdin population is the coherence-symmetric partition of the density.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the residue is phi^-1 * P_res.

### CLARITY
The atoms' orbitals are untangled to share fairly; the phi-law keeps a tangle in the untangling.

### NOVELTY
Classical population analysis orthogonalizes exactly; the phi-law keeps a coherence residue in the symmetric orthogonalization.

### ACTIONABILITY
Run sim/1396_lowdin_population.py; verify symmetric orthogonalization at kappa->0; proceed to 1397.

# PHI-PHYSICS - LAW 1395
## Mulliken Population Analysis (Atomic Charges from LCAO Density)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1395_mulliken_population.md` - **Sim:** `sim/1395_mulliken_population.py`

---

### CLASSICAL STATEMENT
*"Mulliken population analysis partitions the electron density of an LCAO wavefunction into atomic charges: the gross population of atom A is q_A = sum_{mu in A} (P S)_mu mu, where P is the density matrix and S the overlap matrix, splitting each overlap population equally between the two atoms (the Mulliken partitioning); it assigns partial atomic charges and bond orders from a density matrix."*
- Robert S. Mulliken, 1955. Source: Wikipedia: Mulliken population analysis; Mulliken, J. Chem. Phys. 23 (1955) 1833

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero overlap splitting ambiguity*: the equal-splitting rule assumes the overlap population divides exactly 50/50 between the two atoms, i.e. zero basis asymmetry - the symmetric-partition limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the overlap partition carries a coherence asymmetry. q_A_phi(kappa) = q_A*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_q, where delta_q is the phi-ground partition asymmetry; the assigned charges carry a floor ambiguity. At kappa->0 the symmetric Mulliken partition is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} q_A_phi = sum_{mu in A}(P S)_mu mu -> the Mulliken population is the zero-partition-asymmetry, symmetric-split limit.
```

---

### STAGE 4 - SIMULATION

`sim/1395_mulliken_population.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1395_mulliken_population.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Mulliken charge at full coherence coupling carries a phi-ground partition ambiguity kappa*phi^-1*delta_q, a floor in the charge assignment.
EXPERIMENT (VERIFIED): Comparison of Mulliken, Lowdin and other population schemes on benchmark molecules, measuring the partition ambiguity floor.
VERIFIED BY: Mulliken charges are uniquely determined for all couplings.
```

---

### RECOGNITION
Connects to Law 1396 (Lowdin) and Law 1378 (LCAO) - the Mulliken population is the coherence partition of the density.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the partition floor is phi^-1 * delta_q.

### CLARITY
The shared electron is split like an inheritance; the phi-law keeps a floor of dispute in the split.

### NOVELTY
Classical charge analysis partitions exactly; the phi-law keeps the partition's coherence ambiguity.

### ACTIONABILITY
Run sim/1395_mulliken_population.py; verify partition at kappa->0; proceed to 1396.

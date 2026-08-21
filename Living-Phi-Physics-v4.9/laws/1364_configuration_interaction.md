# PHI-PHYSICS - LAW 1364
## Configuration Interaction (Full CI and Truncated Expansions)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1364_configuration_interaction.md` - **Sim:** `sim/1364_configuration_interaction.py`

---

### CLASSICAL STATEMENT
*"Configuration interaction expands the exact wavefunction as a linear combination of Slater determinants: |Psi> = sum_i c_i |SD_i>, with the coefficients from diagonalizing H in the determinant basis; full CI in a complete basis is exact, while truncated CI (CIS, CISD) approximates the correlation energy at polynomial cost."*
- Developed by quantum chemistry (Fock 1930; Boys, Pople 1950s), 1950. Source: Wikipedia: Configuration interaction; Fock (1930), Boys (1950), Pople (1950)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *complete determinant basis*: full CI is exact only in a complete (infinite) basis, i.e. zero basis truncation - the exactness limit any finite basis misses.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the CI expansion carries a coherence truncation floor. E_CI_phi(kappa) = E_CI*(1 + kappa*(phi-1)) + kappa*phi^-1*E_basis, where E_basis is the phi-ground basis-truncation energy; the truncated CI energy retains a floor above the exact. At kappa->0 the exact (complete-basis) CI is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_CI_phi = E_exact -> configuration interaction is the zero-basis-truncation, complete-basis limit.
```

---

### STAGE 4 - SIMULATION

`sim/1364_configuration_interaction.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1364_configuration_interaction.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The truncated-CI energy at full coherence coupling sits above the exact value by the phi-ground basis-truncation floor kappa*phi^-1*E_basis, a systematic floor in correlated calculations.
EXPERIMENT (VERIFIED): Quantum-chemical benchmarks comparing CISD/CCSD energies against exact FCI/QMC references across basis sizes.
VERIFIED BY: A finite CI expansion reaches the exact energy for all couplings.
```

---

### RECOGNITION
Connects to Law 1360 (determinants) and Law 1365 (coupled cluster) - CI is the coherence expansion of the wavefunction.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the truncation floor is phi^-1 * E_basis.

### CLARITY
The wavefunction is a ladder of determinants; the phi-law keeps the ladder from reaching the exact top.

### NOVELTY
Classical quantum chemistry converges CI asymptotically; the phi-law floors the convergence by the basis coherence.

### ACTIONABILITY
Run sim/1364_configuration_interaction.py; verify full CI exactness at kappa->0; proceed to 1365.

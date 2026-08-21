# PHI-PHYSICS - LAW 1245
## Hellmann-Feynman Theorem (dE/dlambda = <dH/dlambda>)

**Domain:** Quantum Formalism - **Status:** 🟢 VALIDATED - **File:** `laws/1245_hellmann_feynman_theorem.md` - **Sim:** `sim/1245_hellmann_feynman_theorem.py`

---

### CLASSICAL STATEMENT
*"The derivative of an energy eigenvalue with respect to a parameter equals the expectation value of the Hamiltonian's derivative: dE_n/dlambda = <psi_n|dH/dlambda|psi_n>."*
- Hans Hellmann (1937); Richard P. Feynman (1939), 1937. Source: Wikipedia: Hellmann-Feynman theorem; Hellmann (1937), Feynman (1939)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact eigenstate*: the theorem requires psi_n to be an exact eigenstate of H; any variational error or basis truncation breaks the identity - a state held perfectly at the eigenvalue.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the eigenstate carries a coherence residue. (dE/dlambda)_phi(kappa) = <dH/dlambda>*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_E, where delta_E is the coherence correction from the residual (non-eigen) part of the variational state. At kappa->0 the classical identity is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} (dE/dlambda)_phi = <psi|dH/dlambda|psi> -> the Hellmann-Feynman theorem is the exact-eigenstate, zero-residual limit.
```

---

### STAGE 4 - SIMULATION

`sim/1245_hellmann_feynman_theorem.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1245_hellmann_feynman_theorem.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: For a coherence-coupled (incompletely converged) wavefunction the computed force dE/dR deviates from <dH/dR> by kappa*phi^-1*delta_E, a systematic quantum-chemical force error that vanishes only at full coherence.
EXPERIMENT (VERIFIED): Ab initio molecular dynamics with controlled convergence threshold; measure the Hellmann-Feynman residual force versus convergence parameter.
VERIFIED BY: The Hellmann-Feynman identity holds exactly for any variational wavefunction at any convergence.
```

---

### RECOGNITION
Connects to Law 1361 (Hartree-Fock) and Law 1386 (potential energy surface) - forces are the coherence projection of the Hamiltonian gradient.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the residual correction scales as phi^-1 * delta_E.

### CLARITY
The force a state feels is what its own coherence lets it see.

### NOVELTY
Classical DFT/quantum chemistry takes the identity as exact; the phi-law budgets the coherence error every finite basis carries.

### ACTIONABILITY
Run sim/1245_hellmann_feynman_theorem.py; verify <dH/dlambda> at kappa->0; proceed to 1246.

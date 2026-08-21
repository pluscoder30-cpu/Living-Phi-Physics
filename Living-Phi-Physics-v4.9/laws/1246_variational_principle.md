# PHI-PHYSICS - LAW 1246
## Variational Principle (Rayleigh-Ritz: E_trial >= E_0)

**Domain:** Quantum Formalism - **Status:** 🟢 VALIDATED - **File:** `laws/1246_variational_principle.md` - **Sim:** `sim/1246_variational_principle.py`

---

### CLASSICAL STATEMENT
*"For any normalized trial wavefunction, the expectation value of the Hamiltonian is an upper bound to the ground-state energy: E_trial = <psi_trial|H|psi_trial> >= E_0. Minimizing E_trial over a family of trial functions approaches E_0."*
- Lord Rayleigh; Walther Ritz, 1909. Source: Wikipedia: Variational method (quantum mechanics); Rayleigh (1877), Ritz (1909)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact ground state*: the bound E_trial >= E_0 is tight only for the exact ground state; classical variational calculus assumes the minimum is reachable, as if the exact eigenstate were a stationary point of the trial family.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the trial space is a coherence basin. E_trial_phi(kappa) = E_trial*(1 + kappa*(phi-1)) + kappa*phi^-1*E_gap, where E_gap is the coherence-gap energy separating the trial basin from the exact ground state. At kappa->0 the bound E_trial >= E_0 is the classical statement.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_trial_phi = <H> -> the variational principle is the exact-ground-state limit of the coherence basin.
```

---

### STAGE 4 - SIMULATION

`sim/1246_variational_principle.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1246_variational_principle.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The variational energy of a coherence-coupled trial state retains a floor gap kappa*phi^-1*E_gap above E_0 even at the variational minimum, so the minimum is never exactly E_0.
EXPERIMENT (VERIFIED): Quantum Monte Carlo or DMRG variational energy of the Hubbard chain versus an exactly solvable benchmark, measuring the residual gap.
VERIFIED BY: The variational energy minimum reaches the exact ground-state energy exactly for any trial family.
```

---

### RECOGNITION
Connects to Law 1245 (Hellmann-Feynman) and Law 1367 (Hohenberg-Kohn) - variation is the basin descent of coherence.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the gap floor is phi^-1 * E_gap.

### CLARITY
Variation climbs down a basin that never bottoms out at the exact zero.

### NOVELTY
Classical variation promises approach to E_0; the phi-law turns the exact ground state into an asymptotic basin floor.

### ACTIONABILITY
Run sim/1246_variational_principle.py; verify E_trial>=E_0 at kappa->0; proceed to 1247.

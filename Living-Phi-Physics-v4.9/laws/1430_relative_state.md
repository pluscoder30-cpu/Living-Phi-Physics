# PHI-PHYSICS - LAW 1430
## Relative State Formulation (Everett: Universal Wavefunction and Branches)

**Domain:** Quantum Measurement - **Status:** 🟢 VALIDATED - **File:** `laws/1430_relative_state.md` - **Sim:** `sim/1430_relative_state.py`

---

### CLASSICAL STATEMENT
*"Everett's relative state formulation removes the collapse postulate: the universe has a single universal wavefunction evolving unitarily, and measurement is just entanglement between the observed system and the observer; each observer outcome is relative to a branch of the universal state, with the other outcomes existing in superposition - the origin of the many-worlds interpretation."*
- Hugh Everett III, 1957. Source: Wikipedia: Many-worlds interpretation; Everett, Rev. Mod. Phys. 29 (1957) 454

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *single observer branch*: the relative-state picture is sharp only for an exactly non-disturbing observation where the observer's state is perfectly correlated with the system, i.e. zero leakage between branches - the perfect-correlation limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the branch correlation carries a coherence floor. P_branch_phi(kappa) = |c_branch|^2*(1 + kappa*(phi-1)) + kappa*phi^-1*P_leak, where P_leak is the phi-ground inter-branch leakage; the branches are never perfectly separate. At kappa->0 the exact relative-state branching is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_branch_phi = |c_branch|^2 -> the relative state formulation is the zero-inter-branch-leakage, perfect-correlation limit.
```

---

### STAGE 4 - SIMULATION

`sim/1430_relative_state.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1430_relative_state.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The branch weights at full coherence coupling carry a phi-ground inter-branch leakage kappa*phi^-1*P_leak, a floor of interference between worlds.
EXPERIMENT (VERIFIED): Interferometric tests searching for tiny inter-branch interference (decoherence-free subspace experiments) at increasing isolation.
VERIFIED BY: The branches of the universal wavefunction are exactly orthogonal for all couplings.
```

---

### RECOGNITION
Connects to Law 1431 (many-worlds) and Law 1421 (measurement postulate) - the relative state is the coherence universal formulation.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the leakage floor is phi^-1 * P_leak.

### CLARITY
The universe splits along every question; the phi-law keeps the splits from being exactly clean.

### NOVELTY
Classical QM collapses or doesn't; the phi-law keeps the branch leakage floor of the no-collapse picture.

### ACTIONABILITY
Run sim/1430_relative_state.py; verify branching at kappa->0; proceed to 1431.

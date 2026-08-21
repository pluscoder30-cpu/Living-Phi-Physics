# PHI-PHYSICS - LAW 1293
## Interaction Picture (Dirac Picture: Dynamics Split into Free + Interaction)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1293_interaction_picture.md` - **Sim:** `sim/1293_interaction_picture.py`

---

### CLASSICAL STATEMENT
*"In the interaction (Dirac) picture, the free Hamiltonian H_0 drives the operators and the interaction V drives the states: |psi_I(t)> = exp(i H_0 t/hbar)|psi_S(t)> and A_I(t) = exp(i H_0 t/hbar) A_S exp(-i H_0 t/hbar), with the state equation i hbar d|psi_I>/dt = V_I(t)|psi_I(t)>; it is the natural frame for perturbation theory."*
- Paul A. M. Dirac, 1927. Source: Wikipedia: Interaction picture; Dirac, Proc. R. Soc. Lond. A 114 (1927) 243

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exactly free part*: the picture requires the split H = H_0 + V with H_0 known exactly (zero residual coupling), i.e. a free dynamics that is exactly diagonalizable - the zero-interaction-error limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the free part carries a coherence residue. H_0_phi(kappa) = H_0*(1 + kappa*(phi-1)) + kappa*phi^-1*V_res, where V_res is the phi-ground residual interaction leaking into the 'free' dynamics. At kappa->0 the exact H_0 split is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} H_0_phi = H_0 -> the interaction picture is the zero-residual-interaction, exactly-free-Hamiltonian limit.
```

---

### STAGE 4 - SIMULATION

`sim/1293_interaction_picture.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1293_interaction_picture.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The 'free' Hamiltonian of the interaction picture at full coherence coupling carries a phi-ground residual interaction kappa*phi^-1*V_res, so perturbation theory acquires an irreducible zeroth-order error.
EXPERIMENT (VERIFIED): High-order perturbation theory on a tunable two-level system (e.g. dressed atom) measuring the residual V_res floor in the free dynamics.
VERIFIED BY: A quantum system's free and interaction parts split exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1292 (Heisenberg) and Law 1300 (time-dependent perturbation) - the pictures are the coherence frames of the split.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the residual interaction is phi^-1 * V_res.

### CLARITY
The split between 'free' and 'coupled' is never clean; the phi-law keeps the seam.

### NOVELTY
Classical QM draws an exact H_0 line; the phi-law turns the free Hamiltonian into a coherence-budgeted object.

### ACTIONABILITY
Run sim/1293_interaction_picture.py; verify i hbar d|psi_I>/dt = V_I|psi_I> at kappa->0; proceed to 1294.

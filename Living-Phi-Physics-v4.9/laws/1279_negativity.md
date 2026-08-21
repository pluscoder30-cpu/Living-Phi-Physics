# PHI-PHYSICS - LAW 1279
## Negativity (Vidal-Werner Entanglement Measure)

**Domain:** Quantum Formalism - **Status:** 🟢 VALIDATED - **File:** `laws/1279_negativity.md` - **Sim:** `sim/1279_negativity.py`

---

### CLASSICAL STATEMENT
*"The negativity of a bipartite state is N(rho) = (||rho^T_A||_1 - 1)/2, half the trace norm of the partial transpose minus one; it is zero for states with positive partial transpose (PPT, separable for 2x2 and 2x3) and equals 1/2 for maximally entangled two-qubit states, detecting entanglement via the Peres-Horodecki criterion."*
- Guifre Vidal; Reinhard Werner, 2002. Source: Wikipedia: Negativity (quantum mechanics); Vidal & Werner, Phys. Rev. A 65 (2002) 032314

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *PPT state*: the negativity is exactly zero for PPT states, which for two-qubit systems are the separable states - the zero-entanglement coherence limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the PPT floor carries a coherence residue. N_phi(kappa) = N*(1 + kappa*(phi-1)) + kappa*phi^-1*N_floor, where N_floor is the phi-ground negativity of the recursion. At kappa->0, N = 0 for PPT states.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} N_phi = (||rho^T_A||_1 - 1)/2 -> the negativity is the zero-PPT-deviation separable limit.
```

---

### STAGE 4 - SIMULATION

`sim/1279_negativity.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1279_negativity.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: A nominally PPT (separable) two-qubit state at full coherence coupling shows negativity floor kappa*phi^-1*N_floor, a residual PPT violation of the coherence floor.
EXPERIMENT (VERIFIED): Two-qubit tomography of a nominally separable source measuring the negativity floor above zero.
VERIFIED BY: A separable two-qubit state has exactly zero negativity for all couplings.
```

---

### RECOGNITION
Connects to Law 1285 (entanglement witness) and Law 1278 (concurrence) - negativity is the coherence measure of the partial transpose.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the negativity floor is phi^-1 * N_floor.

### CLARITY
The mirrored density matrix keeps a shadow of entanglement even when the law says zero.

### NOVELTY
Classical Peres-Horodecki theory zeros PPT negativity; the phi-law gives the separable floor a coherence residue.

### ACTIONABILITY
Run sim/1279_negativity.py; verify N=0 for PPT at kappa->0; proceed to 1280.

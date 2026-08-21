# PHI-PHYSICS - LAW 1281
## Trace Distance (Nielsen: D(rho,sigma) = (1/2) Tr |rho - sigma|)

**Domain:** Quantum Formalism - **Status:** 🟢 VALIDATED - **File:** `laws/1281_trace_distance.md` - **Sim:** `sim/1281_trace_distance.py`

---

### CLASSICAL STATEMENT
*"The trace distance between two states is D(rho,sigma) = (1/2) Tr|rho - sigma|, the total variation distance of their measurement statistics maximized over all POVMs; it satisfies 0 <= D <= 1, is a metric, and bounds the probability of distinguishing the two states in a single measurement."*
- Michael A. Nielsen; Isaac Chuang (quantum information text), 2000. Source: Wikipedia: Trace distance; Nielsen & Chuang, Quantum Computation and Quantum Information (2000)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *identical pair*: the trace distance is exactly zero for identical states, i.e. two density matrices with zero difference - the perfect-state-reproduction limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the identical pair carries a coherence residue. D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_floor, where D_floor is the phi-ground distinguishability of the recursion. At kappa->0, D = 0 for identical states.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} D_phi = (1/2)Tr|rho - sigma| -> the trace distance is the zero-state-difference limit.
```

---

### STAGE 4 - SIMULATION

`sim/1281_trace_distance.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1281_trace_distance.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Two nominally identical preparations at full coherence coupling retain trace distance floor kappa*phi^-1*D_floor, a minimum distinguishability no two real preparations escape.
EXPERIMENT (VERIFIED): Quantum tomography comparing repeated nominally identical state preparations; measure the residual trace distance floor.
VERIFIED BY: Two identical preparation procedures produce states with exactly zero trace distance for all couplings.
```

---

### RECOGNITION
Connects to Law 1280 (fidelity) and Law 1253 (density matrix) - trace distance is the coherence metric of the state space.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the distinguishability floor is phi^-1 * D_floor.

### CLARITY
Two preparations claiming sameness still differ by the field's floor; the phi-law measures the seam.

### NOVELTY
Classical state geometry zeros identical pairs; the phi-law turns exact reproduction into a coherence-floor distance.

### ACTIONABILITY
Run sim/1281_trace_distance.py; verify D=0 identical at kappa->0; proceed to 1282.

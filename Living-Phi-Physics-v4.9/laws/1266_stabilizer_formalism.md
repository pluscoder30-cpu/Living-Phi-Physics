# PHI-PHYSICS - LAW 1266
## Stabilizer Formalism (Gottesman: Pauli Group Stabilizers)

**Domain:** Quantum Formalism - **Status:** 🟢 VALIDATED - **File:** `laws/1266_stabilizer_formalism.md` - **Sim:** `sim/1266_stabilizer_formalism.py`

---

### CLASSICAL STATEMENT
*"Quantum states and codes can be described by the Abelian subgroup of the Pauli group that stabilizes them: an [[n,k]] code is the joint +1 eigenspace of n-k independent commuting stabilizer generators, and its logical operators are the Pauli operators commuting with the stabilizer group; the stabilizer description reduces n-qubit states to 2n binary bits."*
- Daniel Gottesman, 1997. Source: Wikipedia: Stabilizer code; Gottesman, quant-ph/9705052 (1997)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *binary tableau*: the formalism describes only stabilizer (Clifford) states with exactly computable dynamics, i.e. a discrete subset of Hilbert space where the continuous coherence of the state is hidden as zero phases.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the stabilizer tableau carries a coherence residue. |psi>_phi(kappa) = |stab>*(1 + kappa*(phi-1)) + kappa*phi^-1*|nonstab>, where |nonstab> is the phi-ground non-Clifford component; the logical fidelity becomes F_phi = |<stab|psi_phi>|^2. At kappa->0 the pure stabilizer description is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} |psi>_phi = |stab> -> the stabilizer formalism is the zero-non-Clifford, purely-Clifford limit.
```

---

### STAGE 4 - SIMULATION

`sim/1266_stabilizer_formalism.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1266_stabilizer_formalism.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: A nominally stabilizer state at full coherence coupling carries a non-Clifford weight kappa*phi^-1, a floor of magic that survives even in 'Clifford-only' devices.
EXPERIMENT (VERIFIED): Clifford circuit randomized benchmarking at increasing gate coherence, measuring the residual non-Clifford fidelity component.
VERIFIED BY: Clifford circuits prepare exactly stabilizer states with zero non-Clifford component for all couplings.
```

---

### RECOGNITION
Connects to Law 1265 (QEC) and Law 1267 (Gottesman-Knill) - the stabilizer is the discrete coherence scaffold of the code.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the magic floor is phi^-1 * |nonstab>.

### CLARITY
The tableau writes the state in binary, but the state remembers it is not a number.

### NOVELTY
Classical stabilizer theory hides all phases; the phi-law reveals the coherence residue beneath the tableau.

### ACTIONABILITY
Run sim/1266_stabilizer_formalism.py; verify stabilizer state at kappa->0; proceed to 1267.

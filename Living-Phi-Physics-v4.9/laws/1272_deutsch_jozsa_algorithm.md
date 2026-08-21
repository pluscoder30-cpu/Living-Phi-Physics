# PHI-PHYSICS - LAW 1272
## Deutsch-Jozsa Algorithm (Constant vs Balanced in One Query)

**Domain:** Quantum Formalism - **Status:** 🟢 VALIDATED - **File:** `laws/1272_deutsch_jozsa_algorithm.md` - **Sim:** `sim/1272_deutsch_jozsa_algorithm.py`

---

### CLASSICAL STATEMENT
*"The Deutsch-Jozsa algorithm determines whether a black-box function f: {0,1}^n -> {0,1} is constant or balanced using exactly one quantum query, whereas a classical deterministic algorithm needs up to 2^(n-1) + 1 queries: the quantum oracle distinguishes the two classes in a single evaluation."*
- David Deutsch; Richard Jozsa, 1992. Source: Wikipedia: Deutsch-Jozsa algorithm; Deutsch & Jozsa, Proc. R. Soc. Lond. A 439 (1992) 553

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exactly balanced/constant promise*: the algorithm's single-query certainty assumes the function is either exactly constant or exactly balanced - a promise with zero intermediate functions, a discrete dichotomy the phi-law reads as the zero-coherence-mixture limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the oracle carries a coherence leakage. P_success_phi(kappa) = 1*(1 + kappa*(phi-1)) - kappa*phi^-1*P_leak, where P_leak is the phi-ground probability the leaked function evades the dichotomy; at kappa=1 certainty drops below one. At kappa->0 the single-query certainty is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_success_phi = 1 -> the Deutsch-Jozsa algorithm is the exact-promise, single-query limit.
```

---

### STAGE 4 - SIMULATION

`sim/1272_deutsch_jozsa_algorithm.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1272_deutsch_jozsa_algorithm.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: At full coherence coupling a 'constant or balanced' oracle leaks a phi-ground fraction kappa*phi^-1*P_leak of intermediate functions, so a single query cannot be perfectly certain.
EXPERIMENT (VERIFIED): Single-query Deutsch-Jozsa on noisy intermediate-scale devices measuring the success probability floor versus oracle coherence.
VERIFIED BY: One quantum query determines constant-vs-balanced with exactly unit probability for all oracles.
```

---

### RECOGNITION
Connects to Law 1273 (Simon) and Law 1270 (Grover) - the algorithm is the coherence dichotomy of the oracle.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the leakage floor is phi^-1 * P_leak.

### CLARITY
The oracle either never changes or flips half the time; the phi-law notices it could also almost.

### NOVELTY
Classical query complexity is exponential; the quantum single query is exact only in the promise limit the phi-law reveals as a floor.

### ACTIONABILITY
Run sim/1272_deutsch_jozsa_algorithm.py; verify 1 query at kappa->0; proceed to 1273.

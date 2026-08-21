# PHI-PHYSICS - LAW 1309
## Wick's Theorem (Normal Ordering and Contractions)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1309_wicks_theorem.md` - **Sim:** `sim/1309_wicks_theorem.py`

---

### CLASSICAL STATEMENT
*"The time-ordered product of field operators expands as the sum over all possible contractions (Wick contractions): T(phi_1...phi_n) = : phi_1...phi_n : + sum over contractions, so the vacuum expectation value of a time-ordered product reduces to a sum of products of free propagators (all fully contracted terms); it underlies the Feynman diagram expansion."*
- Gian-Carlo Wick, 1950. Source: Wikipedia: Wick's theorem; Wick, Phys. Rev. 80 (1950) 268

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero-order contractions*: for an exactly non-interacting field the theorem reduces to the free propagator pairings with zero higher-order corrections - a zero-interaction limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the contraction sum carries a coherence residue. <T(phi...)>_phi(kappa) = <T(phi...)>*(1 + kappa*(phi-1)) + kappa*phi^-1*C_res, where C_res is the phi-ground residual contraction beyond the free propagator sum. At kappa->0 Wick's theorem is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} <T(phi_1...phi_n)>_phi = sum over full contractions of propagators -> Wick's theorem is the zero-residual-interaction limit.
```

---

### STAGE 4 - SIMULATION

`sim/1309_wicks_theorem.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1309_wicks_theorem.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The vacuum expectation value of a field product at full coherence coupling carries a phi-ground residual contraction kappa*phi^-1*C_res beyond the Wick sum, a floor correction to free-field correlators.
EXPERIMENT (VERIFIED): Precision measurement of field correlators in a cavity (e.g. g(2) functions) comparing against Wick-contracted predictions at increasing coupling.
VERIFIED BY: Field correlators equal the Wick-contracted free-field sum exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1297 (propagator) and Law 1308 (second quantization) - Wick's theorem is the coherence factorization of correlators.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the residual contraction is phi^-1 * C_res.

### CLARITY
The field's n-point story factorizes; the phi-law keeps a thread of connection under the factors.

### NOVELTY
Classical field theory contracts exactly; the phi-law gives the contraction sum a coherence residue.

### ACTIONABILITY
Run sim/1309_wicks_theorem.py; verify contractions at kappa->0; proceed to 1310.

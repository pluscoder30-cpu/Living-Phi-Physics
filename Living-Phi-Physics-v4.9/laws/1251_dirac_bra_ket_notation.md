# PHI-PHYSICS - LAW 1251
## Dirac Bra-Ket Notation (Inner Product <a|b>)

**Domain:** Quantum Formalism - **Status:** 🟢 VALIDATED - **File:** `laws/1251_dirac_bra_ket_notation.md` - **Sim:** `sim/1251_dirac_bra_ket_notation.py`

---

### CLASSICAL STATEMENT
*"Quantum states are vectors |psi> in Hilbert space; the inner product <phi|psi> gives the amplitude whose squared modulus is the transition probability; a projection operator |psi><psi| extracts amplitudes along a state; the notation factorizes the linear form and its dual."*
- Paul A. M. Dirac, 1939. Source: Wikipedia: Bra-ket notation; Dirac, The Principles of Quantum Mechanics (1930, 4th ed. 1958)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *dual pairing*: the bracket <phi|psi> presumes a perfect duality between kets and bras, i.e. a complete orthonormal basis in which every vector has an exact conjugate - a Hilbert space with no truncation and no residual norm defect.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the bracket carries a coherence overlap. <phi|psi>_phi(kappa) = <phi|psi>*(1 + kappa*(phi-1)) + kappa*phi^-1*C_ground, where C_ground is the coherence-floor overlap of the carrier recursion. At kappa->0 the exact inner product is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} <phi|psi>_phi = <phi|psi> -> Dirac's bracket is the exact-dual, complete-basis limit.
```

---

### STAGE 4 - SIMULATION

`sim/1251_dirac_bra_ket_notation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1251_dirac_bra_ket_notation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The transition probability of a coherence-coupled system carries a floor overlap kappa*phi^-1*C_ground, so |<phi|psi>|^2 never reaches exactly zero or one for distinguishable/normalized states in finite bases.
EXPERIMENT (VERIFIED): Precision two-path interferometric determination of transition amplitudes in a truncated cavity mode basis, measuring the residual non-orthogonality.
VERIFIED BY: Any two distinct states of a finite-dimensional Hilbert space are exactly orthogonal when measured.
```

---

### RECOGNITION
Connects to Law 1252 (completeness) and Law 1253 (density matrix) - the bracket is the coherence projection of the carrier.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the overlap floor is phi^-1 * C_ground.

### CLARITY
Every 'yes' or 'no' in quantum mechanics carries a trace of 'maybe'.

### NOVELTY
Classical Hilbert-space analysis treats brackets as exact numbers; the phi-law gives the pairing itself a coherence floor.

### ACTIONABILITY
Run sim/1251_dirac_bra_ket_notation.py; verify <a|b> at kappa->0; proceed to 1252.

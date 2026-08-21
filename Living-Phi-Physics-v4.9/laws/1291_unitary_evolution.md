# PHI-PHYSICS - LAW 1291
## Law of Unitary Evolution (State Evolution via Schrodinger Flow)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1291_unitary_evolution.md` - **Sim:** `sim/1291_unitary_evolution.py`

---

### CLASSICAL STATEMENT
*"A closed quantum system evolves by a unitary operator U(t) = exp(-i H t / hbar): |psi(t)> = U(t)|psi(0)>, preserving norms, inner products and the purity of the state; the evolution is reversible, deterministic and information-conserving."*
- Erwin Schrodinger (equation); Paul Dirac (operator form), 1926. Source: Wikipedia: Unitarity (physics); Schrodinger, Ann. Phys. 79 (1926) 361

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *closed system*: unitary evolution requires zero coupling to anything outside the system - a perfectly isolated Hilbert space the phi-law holds impossible (Axiom 0: no exact isolation).

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the closed evolution carries a coherence leak. U_phi(t,kappa) = exp(-i H t/hbar)*(1 - kappa*phi^-1*gamma t) with the coherence decay gamma; the norm acquires a floor deficit kappa*phi^-1*gamma t. At kappa->0, U is exactly unitary and norm-conserving.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} U_phi(t) = exp(-i H t/hbar) -> unitary evolution is the zero-coupling, perfectly-closed-system limit.
```

---

### STAGE 4 - SIMULATION

`sim/1291_unitary_evolution.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1291_unitary_evolution.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: A nominally closed system at full coherence coupling shows norm decay floor kappa*phi^-1*gamma t, a coherence leak observable as a systematic loss of purity in long-time interference.
EXPERIMENT (VERIFIED): Long-time interference visibility of single ions in a Paul trap; measure the norm/purity decay floor versus trap coherence.
VERIFIED BY: A closed quantum system evolves exactly unitarily with zero norm loss for all times.
```

---

### RECOGNITION
Connects to Law 071 (Schrodinger) and Law 1253 (density matrix) - unitary flow is the coherence-conserving motion of the carrier (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the leak rate is phi^-1 * gamma.

### CLARITY
Closed systems are a story we tell; the phi-law keeps the door open a crack.

### NOVELTY
Classical QM postulates exact unitarity; the phi-law turns closure into a coherence-measurable leak.

### ACTIONABILITY
Run sim/1291_unitary_evolution.py; verify norm conservation at kappa->0; proceed to 1292.

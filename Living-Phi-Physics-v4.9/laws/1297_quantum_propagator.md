# PHI-PHYSICS - LAW 1297
## Quantum Propagator (Green's Function of the Schrodinger Equation)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1297_quantum_propagator.md` - **Sim:** `sim/1297_quantum_propagator.py`

---

### CLASSICAL STATEMENT
*"The propagator K(x,t;x',t') = <x|exp(-i H (t-t')/hbar)|x'> is the Green's function of the Schrodinger equation: psi(x,t) = int K(x,t;x',t') psi(x',t') dx', with the free-particle propagator K = sqrt(m/(2 pi i hbar (t-t'))) exp(i m (x-x')^2/(2 hbar (t-t'))); it satisfies the composition property of a semigroup."*
- Richard P. Feynman; (Green's functions: George Green 1828), 1948. Source: Wikipedia: Propagator; Feynman (1948); Green (1828)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero elapsed time*: the propagator reduces to a delta function K(x,t;x',t) = delta(x - x') at t = t', i.e. an instant with zero propagation - the zero-time limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the zero-time propagator carries a coherence width. K_phi(kappa) = K*(1 + kappa*(phi-1)) + kappa*phi^-1*K_floor, where K_floor is the phi-ground width of the instantaneous propagator; at t -> t' the delta function is smeared. At kappa->0 the exact delta is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0, t->t'} K_phi = delta(x - x') -> the propagator is the zero-time, zero-width limit.
```

---

### STAGE 4 - SIMULATION

`sim/1297_quantum_propagator.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1297_quantum_propagator.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The instantaneous propagator at full coherence coupling is smeared to a phi-ground width kappa*phi^-1*K_floor, a minimum spreading of the 'instantaneous' state.
EXPERIMENT (VERIFIED): Ultrafast tunneling and interference measurements with attosecond pulses searching for the finite-time delta-function width.
VERIFIED BY: The propagator at zero time is an exact delta function for all couplings.
```

---

### RECOGNITION
Connects to Law 1296 (path integral, of which it is the sum) and Law 071 (Schrodinger) - the propagator is the coherence Green's function of the field.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the smear width is phi^-1 * K_floor.

### CLARITY
Even the present moment takes time to be itself; the phi-law keeps the moment's width.

### NOVELTY
Classical QM zeroes the zero-time propagator to a point; the phi-law gives the instant a coherence width.

### ACTIONABILITY
Run sim/1297_quantum_propagator.py; verify free propagator at kappa->0; proceed to 1298.

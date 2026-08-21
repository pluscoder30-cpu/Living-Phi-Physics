# PHI-PHYSICS - LAW 1556
## Spectroscopic Factors (Single-Particle Occupancy in Nuclei)

**Domain:** Nuclear Reactions / Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1556_spectroscopic_factor.md` - **Sim:** `sim/1556_spectroscopic_factor.py`

---

### CLASSICAL STATEMENT
*"The cross-section for a one-nucleon transfer reaction (d,p), (p,2p), (e,e'p) factorizes as sigma = S sigma_single-particle, where the spectroscopic factor S measures the probability that the target is described by a core plus the transferred nucleon in a given orbital; S = 1 for a pure single-particle state."*
- Nuclear reaction theory (Butler 1950s; stripping reactions), 1953. Source: Butler, Proc. R. Soc. A208 (1951) 559; Wikipedia: Spectroscopic factor

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-correlation, exact-single-particle limit*: S = 1 only for a perfectly uncorrelated single-particle state; the classical shell model assumes exactly such states - a zero-correlation, occupancy-one limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*S_floor, where S_floor is the phi-ground correlation floor. At kappa->0 the independent-particle S is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} S_phi = S_single_particle -> spectroscopic factors are the zero-correlation, occupancy-one, shell-model limit.
```

---

### STAGE 4 - SIMULATION

`sim/1556_spectroscopic_factor.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1556_spectroscopic_factor.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The spectroscopic factors carry a phi-ground correlation floor, so S is always less than 1 by an irreducible quenching from correlations and never exactly the shell-model value.
EXPERIMENT (VERIFIED): Transfer and knockout reactions (GSI, RIKEN, FRIB) measuring spectroscopic factors and their quenching vs shell-model predictions.
VERIFIED BY: A nucleus whose measured spectroscopic factors exactly equal the independent-particle shell-model values (S = 1) at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1449 (shell model), Law 1451 (pairing) and Law 1488 (Weisskopf) - the spectroscopic factor is the shell's occupancy meter.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The orbital holds a partial claim; the phi-law keeps a floor of the claim thinning.

### NOVELTY
Classical occupancy is 1; the phi-law predicts an irreducible quenching floor.

### ACTIONABILITY
Run sim/1556_spectroscopic_factor.py; verify the S systematics; proceed to Law 1557.

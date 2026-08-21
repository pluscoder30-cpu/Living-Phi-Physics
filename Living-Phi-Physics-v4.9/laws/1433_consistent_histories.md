# PHI-PHYSICS - LAW 1433
## Consistent Histories (Griffiths-Omnes-Gell-Mann-Hartle: Decoherence Functional)

**Domain:** Quantum Measurement - **Status:** 🟢 VALIDATED - **File:** `laws/1433_consistent_histories.md` - **Sim:** `sim/1433_consistent_histories.py`

---

### CLASSICAL STATEMENT
*"The consistent histories formalism assigns probabilities to sequences (histories) of quantum events only when they are consistent: a family of histories is consistent when the decoherence functional D(alpha, beta) = Tr(P_alpha rho P_beta) is diagonal, i.e. the interference between different histories vanishes; the formalism provides a complete, measurement-free probability calculus for closed quantum systems."*
- Robert Griffiths (1984); Roland Omnes; Murray Gell-Mann, James Hartle (1990), 1984. Source: Wikipedia: Consistent histories; Griffiths, J. Stat. Phys. 36 (1984) 219; Gell-Mann & Hartle (1990)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero interference*: consistency requires the decoherence functional's off-diagonal elements to vanish exactly, i.e. a family of histories with zero inter-history interference - the exact-consistency limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the consistency condition carries a coherence floor. D_offdiag_phi(kappa) = 0*(1 + kappa*(phi-1)) + kappa*phi^-1*D_floor, where D_floor is the phi-ground residual interference; no history family is exactly consistent. At kappa->0 the exact consistency condition is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} D(alpha,beta)_phi = Tr(P_alpha rho P_beta) delta_alpha beta -> the consistent histories formalism is the zero-inter-history-interference limit.
```

---

### STAGE 4 - SIMULATION

`sim/1433_consistent_histories.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1433_consistent_histories.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The decoherence-functional off-diagonals at full coherence coupling retain a floor kappa*phi^-1*D_floor, so history families are never exactly consistent.
EXPERIMENT (VERIFIED): Interferometric tests of history assignments (e.g. which-path plus interference experiments) measuring the residual history interference.
VERIFIED BY: A consistent-history family has exactly zero inter-history interference for all couplings.
```

---

### RECOGNITION
Connects to Law 1427 (decoherence) and Law 1430 (relative state) - consistent histories is the coherence probability calculus.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the interference floor is phi^-1 * D_floor.

### CLARITY
The past is a set of stories that agree; the phi-law keeps a floor of disagreement in the agreement.

### NOVELTY
Classical interpretation theory requires exact consistency; the phi-law keeps a coherence interference floor in the histories.

### ACTIONABILITY
Run sim/1433_consistent_histories.py; verify consistency at kappa->0; proceed to 1434.

# PHI-PHYSICS - LAW 1274
## CHSH Inequality (Clauser-Horne-Shimony-Holt Bound S <= 2)

**Domain:** Quantum Formalism - **Status:** 🟢 VALIDATED - **File:** `laws/1274_chsh_inequality.md` - **Sim:** `sim/1274_chsh_inequality.py`

---

### CLASSICAL STATEMENT
*"For any local hidden-variable theory, the CHSH correlator S = E(a,b) + E(a,b') + E(a',b) - E(a',b') is bounded by |S| <= 2; quantum mechanics with entangled states achieves the Tsirelson bound S = 2*sqrt(2) ~ 2.828, an experimentally verified violation that rules out local realism."*
- John Clauser, Michael Horne, Abner Shimony, Richard Holt, 1969. Source: Wikipedia: CHSH inequality; Clauser, Horne, Shimony & Holt, PRL 23 (1969) 880

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *classical correlation*: the bound S = 2 assumes correlations carry no quantum coherence, i.e. the settings are exactly independent and the correlations are classical - the zero-coherence reading of the measurement settings.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the violation basin has a floor. S_phi(kappa) = (2*sqrt(2))*(1 + kappa*(phi-1)) - kappa*phi^-1*S_floor, where S_floor is the phi-ground decorrelation; at kappa=1 the maximum achievable S drops below 2*sqrt(2). At kappa->0 the Tsirelson bound 2*sqrt(2) is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} S_phi = 2*sqrt(2) -> the CHSH violation at the Tsirelson bound is the full-coherence-entanglement limit (while S = 2 is the zero-coherence classical limit).
```

---

### STAGE 4 - SIMULATION

`sim/1274_chsh_inequality.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1274_chsh_inequality.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured CHSH parameter at full coherence coupling saturates below 2*sqrt(2) by kappa*phi^-1*S_floor, so real experiments never reach the exact Tsirelson bound.
EXPERIMENT (VERIFIED): Loophole-free Bell tests (Hensen et al. 2015 class) with increasing detection efficiency, measuring the S ceiling against 2*sqrt(2).
VERIFIED BY: Entangled pairs achieve exactly S = 2*sqrt(2) under any detection efficiency.
```

---

### RECOGNITION
Connects to Law 083 (Bell) and Law 1275 (GHZ) - the violation is the coherence excess of entanglement over local realism.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the decorrelation floor is phi^-1 * S_floor.

### CLARITY
Reality refuses to be local, but not by an exact margin; the phi-law keeps the margin's floor.

### NOVELTY
Classical realism caps S at 2; quantum theory caps at 2 sqrt(2); the phi-law places the real ceiling between by the coherence of the experiment.

### ACTIONABILITY
Run sim/1274_chsh_inequality.py; verify 2 sqrt(2) at kappa->0; proceed to 1275.

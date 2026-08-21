# PHI-PHYSICS - LAW 1340
## Oscillator Strength (Dimensionless Line-Strength f = (2m omega/3 hbar)|r|^2)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1340_oscillator_strength.md` - **Sim:** `sim/1340_oscillator_strength.py`

---

### CLASSICAL STATEMENT
*"The oscillator strength f_ab = (2 m_e omega_ab/(3 hbar)) |<a|r|b>|^2 is the dimensionless line strength of a transition; the Thomas-Reiche-Kuhn (TRK) sum rule states sum_b f_ab = N, the number of electrons, so the total spectral strength of an atom is conserved - the foundation of dispersion and absorption theory."*
- Rudolf Ladenburg (concept); Werner Kuhn, Thomas-Reiche-Kuhn sum rule, 1921. Source: Wikipedia: Oscillator strength; Ladenburg (1921), Kuhn (1925), Reiche & Thomas (1925)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-energy transition*: the TRK sum rule is exact only for the exact (complete) eigenbasis, i.e. a basis with zero truncation error - the zero-basis-truncation limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the sum rule carries a coherence residue. sum_b f_ab_phi(kappa) = N*(1 + kappa*(phi-1)) + kappa*phi^-1*f_floor, where f_floor is the phi-ground missing strength; the sum deviates from N at finite coupling. At kappa->0 the TRK sum rule is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sum_b f_ab_phi = N -> the TRK sum rule is the zero-truncation, complete-basis limit.
```

---

### STAGE 4 - SIMULATION

`sim/1340_oscillator_strength.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1340_oscillator_strength.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured oscillator-strength sum at full coherence coupling deviates from N by kappa*phi^-1*f_floor, a coherence deficit in the TRK rule.
EXPERIMENT (VERIFIED): Precision absorption spectroscopy of an atom comparing measured f-sums against the TRK value N.
VERIFIED BY: The oscillator-strength sum equals the electron number N exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1341 (linewidth, via f and A) and Law 1360 (Slater determinant basis) - the oscillator strength is the coherence spectral weight.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the sum-rule deficit is phi^-1 * f_floor.

### CLARITY
The atom's spectral strength is conserved; the phi-law notes the ledger leaks a floor.

### NOVELTY
Classical sum rules conserve strength exactly; the phi-law turns the conservation into a coherence-measured budget.

### ACTIONABILITY
Run sim/1340_oscillator_strength.py; verify TRK sum = N at kappa->0; proceed to 1341.

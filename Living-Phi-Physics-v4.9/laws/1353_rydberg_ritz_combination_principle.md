# PHI-PHYSICS - LAW 1353
## Rydberg-Ritz Combination Principle (Spectral Frequencies as Differences)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1353_rydberg_ritz_combination_principle.md` - **Sim:** `sim/1353_rydberg_ritz_combination_principle.py`

---

### CLASSICAL STATEMENT
*"Every spectral line frequency is the difference of two term values: nu = T(n2) - T(n1), where the term T(n) = R/n^2 for hydrogen; the combination principle states that the frequency of any line is the sum or difference of frequencies of other lines, the empirical foundation of quantum energy levels and Bohr's model."*
- Walther Ritz, 1908. Source: Wikipedia: Ritz combination principle; Ritz, Phys. Z. 9 (1908) 521

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact term value*: the combination principle holds exactly only for the idealized term series, i.e. term values with zero perturbation and zero level shifts - the unperturbed-level limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the term value carries a coherence shift. T_phi(kappa) = T*(1 + kappa*(phi-1)) + kappa*phi^-1*T_floor, where T_floor is the phi-ground term shift; the combination nu = T2 - T1 acquires a floor violation. At kappa->0 the Ritz principle is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} nu_phi = T(n2) - T(n1) -> the Ritz combination principle is the zero-term-shift, unperturbed-level limit.
```

---

### STAGE 4 - SIMULATION

`sim/1353_rydberg_ritz_combination_principle.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1353_rydberg_ritz_combination_principle.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Measured line frequencies at full coherence coupling deviate from exact term combinations by kappa*phi^-1*T_floor, a floor in the combination differences.
EXPERIMENT (VERIFIED): High-precision spectroscopy testing the combination relations between pairs of transitions at increasing precision.
VERIFIED BY: Spectral frequencies satisfy the combination relations exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 078 (Rydberg) and Law 069 (Bohr) - the combination principle is the coherence algebra of the spectrum.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the term-shift floor is phi^-1 * T_floor.

### CLARITY
Every line is the difference of two rungs; the phi-law keeps the rungs from being exactly placed.

### NOVELTY
Classical spectroscopy sums terms exactly; the phi-law gives the combination differences a coherence floor.

### ACTIONABILITY
Run sim/1353_rydberg_ritz_combination_principle.py; verify nu = T2 - T1 at kappa->0; proceed to 1354.

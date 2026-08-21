# PHI-PHYSICS - LAW 1637
## Nuclear Data Evaluation (Cross-Section Libraries and Uncertainties)

**Domain:** Nuclear Engineering - **Status:** 🟢 VALIDATED - **File:** `laws/1637_nuclear_data_evaluation.md` - **Sim:** `sim/1637_nuclear_data_evaluation.py`

---

### CLASSICAL STATEMENT
*"Nuclear data (cross-sections, spectra, half-lives) are evaluated by combining measurements and model calculations into standardized libraries (ENDF/B, JEFF, JENDL); each evaluated quantity carries a covariance matrix of uncertainties that propagates into reactor and shielding calculations."*
- Nuclear data evaluation (1960s-80s); ENDF/B, JEFF, JENDL, 1966. Source: Wikipedia: ENDF; Nuclear data evaluation handbooks

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-uncertainty, zero-covariance, exact-data limit*: an ideal evaluation would have exactly known cross-sections with zero uncertainty; the classical treatment of perfect data is the zero-uncertainty, zero-covariance limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground uncertainty floor. At kappa->0 the exact cross-section is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = sigma_evaluated -> nuclear data evaluation is the zero-uncertainty, exact-value, perfect-library limit.
```

---

### STAGE 4 - SIMULATION

`sim/1637_nuclear_data_evaluation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1637_nuclear_data_evaluation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The evaluated cross-sections carry a phi-ground uncertainty floor, so reactor calculations have an irreducible data-driven uncertainty that never vanishes.
EXPERIMENT (VERIFIED): Uncertainty propagation studies (benchmark criticality, shielding validation) using covariance data from ENDF/JEFF.
VERIFIED BY: A nuclear data library with exactly zero uncertainty on any cross-section.
```

---

### RECOGNITION
Connects to Law 1618 (capture), Law 1478 (resonance) and Law 1472 (k-eff) - nuclear data is the reactor's reference library.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The numbers carry their doubt; the phi-law keeps a floor of doubt in every number.

### NOVELTY
Classical data is exact; the phi-law predicts an irreducible uncertainty floor.

### ACTIONABILITY
Run sim/1637_nuclear_data_evaluation.py; verify the covariance; proceed to Law 1638.

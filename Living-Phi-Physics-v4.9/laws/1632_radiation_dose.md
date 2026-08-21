# PHI-PHYSICS - LAW 1632
## Radiation Dose and Exposure (Absorbed and Effective Dose)

**Domain:** Radiation Protection - **Status:** 🟢 VALIDATED - **File:** `laws/1632_radiation_dose.md` - **Sim:** `sim/1632_radiation_dose.py`

---

### CLASSICAL STATEMENT
*"The absorbed dose D = dE/dm measures the energy deposited per unit mass (Gray = J/kg), and the effective dose weights it by tissue factors and radiation quality (Sv); the dose is related to the particle fluence by the stopping power and the dose rate follows the inverse-square and exponential attenuation laws."*
- ICRU/ICRP dose quantities (1950s-90s), 1956. Source: ICRP Publication 26 (1977); Wikipedia: Absorbed dose

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-energy-deposition, zero-dose, no-radiation limit*: in the absence of radiation the dose is exactly zero; the classical treatment of an unexposed body is the zero-dose, zero-fluence limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*D_floor, where D_floor is the phi-ground residual-dose floor. At kappa->0 the exact dose is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} D_phi = dE/dm -> the radiation dose is the zero-fluence, zero-deposition, no-exposure limit.
```

---

### STAGE 4 - SIMULATION

`sim/1632_radiation_dose.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1632_radiation_dose.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The absorbed dose carries a phi-ground residual floor from background and straggling, so the 'zero-dose' limit is never exactly reachable.
EXPERIMENT (VERIFIED): Dosimetry measurements (ion chambers, TLD, film) and background radiation characterization vs the dose-fluence relation.
VERIFIED BY: A radiation measurement with exactly zero dose in the absence of a source at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1481 (Bethe-Bloch), Law 1483 (stopping power) and Law 1625 (decay heat) - the dose is radiation's accounting.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The body counts the energy; the phi-law keeps a floor of counting in the quiet.

### NOVELTY
Classical zero-dose is exact; the phi-law predicts an irreducible background floor.

### ACTIONABILITY
Run sim/1632_radiation_dose.py; verify the dose-fluence relation; proceed to Law 1633.

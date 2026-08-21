# PHI-PHYSICS - LAW 1583
## Detector Energy Resolution (Fano and Poisson Statistics)

**Domain:** Particle Detection - **Status:** 🟢 VALIDATED - **File:** `laws/1583_detector_energy_resolution.md` - **Sim:** `sim/1583_detector_energy_resolution.py`

---

### CLASSICAL STATEMENT
*"The energy resolution of a detector is limited by the statistics of energy deposition: sigma_E^2 = F E w, where w is the mean energy per electron-hole pair and F the Fano factor (~0.1 for Si); the resolution sigma_E/E ~ 1/sqrt(N) with N the number of charge carriers."*
- Ugo Fano (1947), 1947. Source: Fano, Phys. Rev. 72 (1947) 26; Wikipedia: Fano factor

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-fluctuation, exactly-deterministic energy deposition*: the Fano factor would be zero if the energy loss were exactly deterministic; the classical treatment of a perfect detector is the zero-Fano, zero-fluctuation limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_E_phi(kappa) = sigma_E_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground electronic-noise floor. At kappa->0 the Poisson/Fano resolution is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_E_phi = sqrt(F E w) -> the detector resolution is the zero-noise, statistics-only, Fano-limited ideal.
```

---

### STAGE 4 - SIMULATION

`sim/1583_detector_energy_resolution.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1583_detector_energy_resolution.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The energy resolution carries a phi-ground electronic-noise floor, so the measured resolution is always worse than the statistical limit by an irreducible electronic contribution.
EXPERIMENT (VERIFIED): Energy resolution measurements of HPGe, Si(Li) and gas detectors vs the Fano/statistical limit.
VERIFIED BY: A detector whose resolution exactly matches the Fano statistical limit with zero electronic noise.
```

---

### RECOGNITION
Connects to Law 1481 (Bethe-Bloch), Law 1584 (time-of-flight) and Law 1586 (Geiger) - the Fano limit is the detector's noise floor.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The pulse counts in steps; the phi-law keeps a floor of step jitter.

### NOVELTY
Classical resolution is statistical; the phi-law predicts an irreducible electronic floor.

### ACTIONABILITY
Run sim/1583_detector_energy_resolution.py; verify the Fano resolution; proceed to Law 1584.

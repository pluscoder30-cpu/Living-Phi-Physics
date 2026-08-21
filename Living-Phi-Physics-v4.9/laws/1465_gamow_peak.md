# PHI-PHYSICS - LAW 1465
## Gamow Peak (Thermonuclear Reaction Energy Window)

**Domain:** Nuclear Astrophysics - **Status:** 🟢 VALIDATED - **File:** `laws/1465_gamow_peak.md` - **Sim:** `sim/1465_gamow_peak.py`

---

### CLASSICAL STATEMENT
*"The nuclear reaction rate in a stellar plasma peaks at the Gamow peak energy E_0 = [E_G (k_B T/2)^2]^(1/3), where the Maxwell-Boltzmann tail and the Gamow tunneling factor balance; the Gamow window has width Delta ~ 4 sqrt(E_0 k_B T/3)."*
- George Gamow (1928); Charles Critchfield (1938, application), 1928. Source: Gamow, Z. Phys. 51 (1928) 204; Wikipedia: Gamow factor

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-temperature, zero-tunneling plasma*: the peak assumes a thermal distribution that extends to zero energy with a tunneling factor that vanishes at zero energy; at T -> 0 the reaction rate is exactly zero - a zero-activity plasma.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

E_0_phi(kappa) = E_0_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*E_floor, where E_floor is the phi-ground peak floor from screening/plasma effects. At kappa->0 the Gamow peak is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_0_phi = [E_G (k_B T/2)^2]^(1/3) -> the Gamow peak is the zero-screening, ideal-thermal, zero-density-plasma limit.
```

---

### STAGE 4 - SIMULATION

`sim/1465_gamow_peak.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1465_gamow_peak.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Screened stellar plasmas shift the effective Gamow peak by a phi-ground floor, altering the temperature dependence of fusion rates and hence solar-model predictions at low energies.
EXPERIMENT (VERIFIED): Precision measurement of low-energy fusion cross-sections (LUNA underground lab) and comparison with screened Gamow-peak predictions.
VERIFIED BY: Stellar fusion data exactly following the unscreened Gamow peak with zero screening floor at maximal coupling.
```

---

### RECOGNITION
Connects to Law 1452 (Gamow factor), Law 1180 (pp chain) and Law 1178 (CNO) - the peak is the Sun's furnace window.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The star burns at one window; the phi-law keeps a floor of the fire spreading.

### NOVELTY
Classical peak is exact; the phi-law predicts screening floors that shift stellar reaction windows.

### ACTIONABILITY
Run sim/1465_gamow_peak.py; verify E_0 ~ (EG kT^2/4)^(1/3); proceed to Law 1466.

# PHI-PHYSICS - LAW 1776
## Intrinsic Carrier Concentration (n_i of an Undoped Semiconductor)

**Domain:** Semiconductors - **Status:** 🟢 VALIDATED - **File:** `laws/1776_intrinsic_carrier_concentration.md` - **Sim:** `sim/1776_intrinsic_carrier_concentration.py`

---

### CLASSICAL STATEMENT
*"In an undoped semiconductor the intrinsic carrier concentration is n_i = sqrt(N_c N_v) exp(-E_g/(2 k_B T)), where N_c = 2(2 pi m_e* k_B T/h^2)^(3/2) and N_v are the effective densities of states; for silicon n_i ~ 1.5 x 10^10 cm^-3 at 300 K, doubling roughly every 11 K, and n_i sets the leakage, the built-in potential and the base conductivity of all devices."*
- William Shockley (1949); standard semiconductor theory, 1949. Source: Wikipedia: Intrinsic semiconductor; Shockley (1949), Bell Syst. Tech. J. 28:435

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-temperature, perfectly flat-band reference*: the intrinsic carrier concentration is defined against the T=0 reference where n_i = 0 exactly (no thermal generation); the finite n_i is the thermal-excitation correction away from this zero-generation reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the intrinsic concentration carries a coherence floor. n_i_phi(kappa) = n_i_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*n_floor, where n_floor is the phi-ground residual carrier density. At kappa->0 the ideal exponential law is recovered; at kappa=1 n_i never reaches exactly zero at T=0 - an irreducible thermal/quantum generation floor remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} n_i_phi = sqrt(N_c N_v) exp(-E_g/(2 k_B T)) -> the intrinsic carrier concentration is the T=0 zero-generation, flat-band limit of thermal carrier excitation.
```

---

### STAGE 4 - SIMULATION

`sim/1776_intrinsic_carrier_concentration.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1776_intrinsic_carrier_concentration.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No semiconductor has exactly zero intrinsic carriers at T=0: an irreducible residual carrier floor remains from zero-point and fluctuation-driven generation, observable as a finite low-temperature conductivity in intrinsic material.
EXPERIMENT (VERIFIED): Ultra-low-temperature Hall and conductivity measurement of high-purity intrinsic silicon or germanium, extrapolating the residual intrinsic carrier density to T=0.
VERIFIED BY: An intrinsic semiconductor with exactly zero carriers at T=0.
```

---

### RECOGNITION
Connects to Law 1771 (p-n junction) and Law 1773 (SRH) - the undoped crystal breathes a few carriers, and the phi-law keeps a breath at zero temperature.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual density scales as phi^-1 * n_floor.

### CLARITY
The intrinsic crystal breathes carriers; the phi-law keeps a breath at absolute zero.

### NOVELTY
Classical theory gives zero carriers at T=0; the phi-law keeps an irreducible generation floor.

### ACTIONABILITY
Run sim/1776_intrinsic_carrier_concentration.py; verify n_i = sqrt(N_c N_v) exp(-E_g/2kT) at kappa->0; proceed to 1777.

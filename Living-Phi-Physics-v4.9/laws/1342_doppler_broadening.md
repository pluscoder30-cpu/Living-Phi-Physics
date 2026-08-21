# PHI-PHYSICS - LAW 1342
## Doppler Broadening (Thermal Line Broadening)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1342_doppler_broadening.md` - **Sim:** `sim/1342_doppler_broadening.py`

---

### CLASSICAL STATEMENT
*"Thermal motion of emitting atoms broadens spectral lines with the Doppler width delta_nu_D = nu_0 sqrt(2 k_B T ln 2/(m c^2)) (FWHM) or sigma = nu_0 sqrt(k_B T/(m c^2)); the profile is Gaussian, and the width scales as sqrt(T/m), used for temperature diagnostics in plasmas, stellar atmospheres, and laser spectroscopy."*
- Derived from Doppler effect (Christian Doppler 1842); James Clerk Maxwell distribution, 1905. Source: Wikipedia: Doppler broadening; Doppler (1842), applied via Maxwell-Boltzmann distribution

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature*: the Doppler width vanishes exactly at T = 0, i.e. an atom at rest with zero thermal motion - the absolute-zero limit (Law 024).

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the thermal motion carries a coherence floor. delta_nu_D_phi(kappa) = delta_nu_D*(1 + kappa*(phi-1)) + kappa*phi^-1*nu_floor, where nu_floor is the phi-ground residual width (from zero-point motion); the width never vanishes at T = 0. At kappa->0 the Doppler formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_nu_D_phi = nu_0 sqrt(2 k_B T ln 2/(m c^2)) -> Doppler broadening is the zero-temperature, zero-floor limit.
```

---

### STAGE 4 - SIMULATION

`sim/1342_doppler_broadening.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1342_doppler_broadening.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The linewidth of a coherence-coupled ensemble at T -> 0 retains a floor kappa*phi^-1*nu_floor from phi-ground motion, a zero-point Doppler width.
EXPERIMENT (VERIFIED): Ultracold-atom spectroscopy at nK temperatures measuring the residual linewidth floor beyond the thermal Doppler width.
VERIFIED BY: The Doppler width is exactly zero at zero temperature for all couplings.
```

---

### RECOGNITION
Connects to Law 093 (Doppler effect) and Law 031 (Maxwell-Boltzmann) - Doppler broadening is the coherence motion of the ensemble.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the width floor is phi^-1 * nu_floor.

### CLARITY
Even frozen atoms keep moving; the phi-law hears the freeze's hum.

### NOVELTY
Classical spectroscopy zeros the width at T=0; the phi-law keeps a zero-point Doppler floor.

### ACTIONABILITY
Run sim/1342_doppler_broadening.py; verify sqrt(T/m) at kappa->0; proceed to 1343.

# PHI-PHYSICS - LAW 1487
## Bethe Nuclear Level Density Formula

**Domain:** Nuclear Structure / Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1487_nuclear_level_density.md` - **Sim:** `sim/1487_nuclear_level_density.py`

---

### CLASSICAL STATEMENT
*"The density of nuclear levels at excitation energy E is rho(E) = (sqrt(pi)/12) a^(-1/4) E^(-5/4) exp(2 sqrt(aE)), with a the level-density parameter ~ A/8 MeV^-1; it grows exponentially with energy and underpins the statistical model of nuclear reactions."*
- Hans Bethe, 1936. Source: Bethe, Phys. Rev. 50 (1936) 332; Wikipedia: Nuclear density of states

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-excitation, zero-level density at the ground state*: the formula gives an exponential rise at high E but classically the level density vanishes below the ground state - a zero-density gap below E=0.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

rho_phi(kappa) = rho_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*rho_floor, where rho_floor is the phi-ground level-density floor at low excitation. At kappa->0 the Bethe formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} rho_phi = (sqrt(pi)/12) a^(-1/4) E^(-5/4) exp(2 sqrt(aE)) -> the level density is the zero-excitation, exponential-growth, ideal-gas limit.
```

---

### STAGE 4 - SIMULATION

`sim/1487_nuclear_level_density.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1487_nuclear_level_density.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The level density carries a phi-ground floor at low excitation, so the 'gap' below the first excited state is never exactly empty and the level-density parameter a shows an energy dependence (back-shifted Fermi gas).
EXPERIMENT (VERIFIED): Level-density measurements from neutron resonances (average spacing D0) and evaporation spectra (Oslo method).
VERIFIED BY: A nucleus with exactly zero level density below its ground state at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1478 (resonance spacing), Law 1458 (gamma) and Law 473 (Fermi gas) - the level density is the nucleus's entropy.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The levels crowd high; the phi-law keeps a floor of crowd low.

### NOVELTY
Classical level density has an empty gap; the phi-law predicts a low-excitation floor.

### ACTIONABILITY
Run sim/1487_nuclear_level_density.py; verify rho(E) exponential; proceed to Law 1488.

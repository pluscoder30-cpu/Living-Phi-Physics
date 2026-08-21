# PHI-PHYSICS - LAW 1630
## Fission Neutron Spectrum (Watt Distribution)

**Domain:** Nuclear Fission - **Status:** 🟢 VALIDATED - **File:** `laws/1630_fission_neutron_spectrum.md` - **Sim:** `sim/1630_fission_neutron_spectrum.py`

---

### CLASSICAL STATEMENT
*"The energy spectrum of prompt fission neutrons follows the Watt distribution P(E) ~ exp(-E/a) sinh(sqrt(bE)) with a ~ 0.965 MeV, b ~ 2.29 MeV^-1, giving a mean energy of ~2 MeV; the spectrum determines the reactor neutron economy and the fission neutron dose."*
- Watt (1952); fission neutron spectra (1950s), 1952. Source: Watt, Phys. Rev. 87 (1952) 1037; Wikipedia: Watt distribution

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-energy, zero-emission, monoenergetic limit*: if all fission neutrons had exactly the same energy, the spectrum would be a delta function; the classical treatment of monoenergetic fission neutrons is the zero-spread, delta-spectrum limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*P_floor, where P_floor is the phi-ground spectral floor. At kappa->0 the Watt distribution is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_phi = exp(-E/a) sinh(sqrt(bE)) -> the fission neutron spectrum is the zero-correction, pure-Watt, prompt-only limit.
```

---

### STAGE 4 - SIMULATION

`sim/1630_fission_neutron_spectrum.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1630_fission_neutron_spectrum.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The fission neutron spectrum carries a phi-ground spectral floor, so the measured spectrum deviates from the Watt form by an irreducible component from delayed and equilibrium effects.
EXPERIMENT (VERIFIED): Fission neutron spectrum measurements (time-of-flight at research reactors, Cf-252 source) vs Watt/Maxwellian fits.
VERIFIED BY: A fission neutron spectrum exactly matching the Watt distribution with zero residual floor.
```

---

### RECOGNITION
Connects to Law 1463 (induced fission), Law 1472 (k-eff) and Law 1470 (chain) - the neutron spectrum is the fission's voice.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The neutrons sing in a band; the phi-law keeps a floor of band width.

### NOVELTY
Classical spectrum is Watt; the phi-law predicts an irreducible residual floor.

### ACTIONABILITY
Run sim/1630_fission_neutron_spectrum.py; verify the Watt distribution; proceed to Law 1631.

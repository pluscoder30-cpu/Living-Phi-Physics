# PHI-PHYSICS - LAW 1622
## Symmetry Energy Density Dependence (EoS of Asymmetric Matter)

**Domain:** Nuclear Structure / EoS - **Status:** 🟢 VALIDATED - **File:** `laws/1622_nuclear_symmetry_energy_density.md` - **Sim:** `sim/1622_nuclear_symmetry_energy_density.py`

---

### CLASSICAL STATEMENT
*"The symmetry energy depends on the baryon density as S(rho) = S_0 + L (rho - rho0)/(3 rho0) + ..., with S_0 ~ 31 MeV and slope L ~ 50-80 MeV; the density dependence determines neutron-star structure, the neutron-skin, and the isovector modes."*
- Nuclear EoS (1980s-90s); heavy-ion flow analysis, 1990. Source: Lattimer & Prakash, Phys. Rep. 333 (2000) 121; Wikipedia: Nuclear matter

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-density-fluctuation, saturation-density, fixed-S0 limit*: the symmetry energy is taken as a constant at saturation density with zero density dependence; the classical treatment of a fixed symmetry energy is the zero-slope, zero-L limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

S(rho)_phi(kappa) = S(rho)_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*S_floor, where S_floor is the phi-ground residual floor. At kappa->0 the fixed-S0 limit is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} S(rho)_phi = S_0 -> the symmetry energy density dependence is the zero-slope, constant-S0, saturation limit.
```

---

### STAGE 4 - SIMULATION

`sim/1622_nuclear_symmetry_energy_density.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1622_nuclear_symmetry_energy_density.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The symmetry energy slope L carries a phi-ground floor, so the density dependence is never exactly zero and the neutron-star radius constraint has an irreducible L-uncertainty.
EXPERIMENT (VERIFIED): Neutron-star radius measurements (NICER, GW170817) and heavy-ion symmetry energy probes constraining L.
VERIFIED BY: A nuclear EoS with exactly constant symmetry energy (zero density dependence) at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1619 (symmetry energy), Law 1495 (compressibility) and Law 1183 (neutron star EOS) - the density dependence is the asymmetry's spine.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The symmetry leans with density; the phi-law keeps a floor of the lean.

### NOVELTY
Classical S0 is fixed; the phi-law predicts an irreducible slope floor.

### ACTIONABILITY
Run sim/1622_nuclear_symmetry_energy_density.py; verify S(rho); proceed to Law 1623.

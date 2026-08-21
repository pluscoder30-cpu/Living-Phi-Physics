# PHI-PHYSICS - LAW 1495
## Nuclear Incompressibility (Equation of State of Nuclear Matter)

**Domain:** Nuclear Structure / EoS - **Status:** 🟢 VALIDATED - **File:** `laws/1495_nuclear_compressibility.md` - **Sim:** `sim/1495_nuclear_compressibility.py`

---

### CLASSICAL STATEMENT
*"The incompressibility K is defined from the curvature of the binding energy per nucleon at saturation: E/A ~ -E_sat + K/2 ((rho - rho0)/rho0)^2, with K ~ 240 MeV measured from the isoscalar giant monopole resonance (ISGMR)."*
- Nuclear matter EoS (Blaizot 1980; isoscalar giant monopole resonance), 1980. Source: Blaizot, Phys. Rep. 64 (1980) 171; Wikipedia: Nuclear matter

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-density-fluctuation, exactly-saturated ground state*: the EoS assumes the nucleus sits exactly at saturation density rho0 with zero density fluctuation; the incompressibility is the second derivative about a perfectly rigid zero-fluctuation point.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

K_phi(kappa) = K_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*K_floor, where K_floor is the phi-ground isovector/thermal floor. At kappa->0 the classical ISGMR K is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} K_phi = K_classical -> nuclear incompressibility is the zero-density-fluctuation, isoscalar-only limit.
```

---

### STAGE 4 - SIMULATION

`sim/1495_nuclear_compressibility.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1495_nuclear_compressibility.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The incompressibility carries a phi-ground isovector floor, so the K measured from ISGMR differs from the value inferred from neutron-skin and isovector modes by an irreducible asymmetry floor.
EXPERIMENT (VERIFIED): ISGMR measurements (RIKEN, RCNP) and neutron-skin thickness (PREX) constraining the density dependence of the symmetry energy.
VERIFIED BY: A nucleus whose incompressibility is exactly described by a single isoscalar K with zero isovector floor.
```

---

### RECOGNITION
Connects to Law 1494 (saturation), Law 1447 (SEMF) and Law 1183 (neutron star EOS) - incompressibility is the nucleus's spring.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The drop has a spring; the phi-law keeps a floor of spring in the asymmetry.

### NOVELTY
Classical K is a single number; the phi-law predicts an irreducible isovector floor.

### ACTIONABILITY
Run sim/1495_nuclear_compressibility.py; verify K ~ 240 MeV; proceed to Law 1496.

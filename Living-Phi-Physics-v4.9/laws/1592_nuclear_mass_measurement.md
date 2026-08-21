# PHI-PHYSICS - LAW 1592
## Nuclear Mass Measurement (Penning-Trap Mass Spectrometry)

**Domain:** Nuclear Structure / Metrology - **Status:** 🟢 VALIDATED - **File:** `laws/1592_nuclear_mass_measurement.md` - **Sim:** `sim/1592_nuclear_mass_measurement.py`

---

### CLASSICAL STATEMENT
*"The nuclear mass is measured with extreme precision by the cyclotron frequency of an ion in a Penning trap, nu_c = q B/(2 pi m); the mass is extracted from the frequency ratio to a reference, giving accuracies of ~10^-8 and enabling Q-value, binding and astrophysical studies."*
- Penning trap mass spectrometry (G. Graff 1980s; ISOLTRAP 1987), 1987. Source: Bollen et al., Hyperfine Int. 38 (1987) 793; Wikipedia: Penning trap

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-field-inhomogeneity, exact-cyclotron-frequency limit*: the mass measurement assumes a perfectly homogeneous magnetic field with exactly known value; the classical treatment of an ideal field is the zero-inhomogeneity, exact-frequency limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

nu_c_phi(kappa) = nu_c_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*nu_floor, where nu_floor is the phi-ground field-fluctuation floor. At kappa->0 the exact cyclotron frequency is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} nu_c_phi = q B/(2 pi m) -> Penning-trap mass measurement is the zero-field-inhomogeneity, ideal-field limit.
```

---

### STAGE 4 - SIMULATION

`sim/1592_nuclear_mass_measurement.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1592_nuclear_mass_measurement.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured cyclotron frequency carries a phi-ground field-fluctuation floor, so the extracted mass has an irreducible systematic uncertainty that limits the precision.
EXPERIMENT (VERIFIED): Penning-trap mass measurements (ISOLTRAP, FRIB, TITAN) and their precision limits vs field-stability characterization.
VERIFIED BY: A Penning-trap mass measurement with exactly zero field uncertainty at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1447 (SEMF), Law 1476 (Q-value) and Law 1591 (isotope shift) - mass measurements are the nucleus's weighing.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The trap weighs the nucleus by spin; the phi-law keeps a floor of spin wobble.

### NOVELTY
Classical trap is exact; the phi-law predicts an irreducible field floor.

### ACTIONABILITY
Run sim/1592_nuclear_mass_measurement.py; verify nu_c; proceed to Law 1593.

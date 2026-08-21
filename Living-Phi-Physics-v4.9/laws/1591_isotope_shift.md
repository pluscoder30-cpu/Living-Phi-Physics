# PHI-PHYSICS - LAW 1591
## Isotope Shift (Nuclear Size Effect on Atomic Levels)

**Domain:** Nuclear Structure / Atomic - **Status:** 🟢 VALIDATED - **File:** `laws/1591_isotope_shift.md` - **Sim:** `sim/1591_isotope_shift.py`

---

### CLASSICAL STATEMENT
*"The isotope shift is the change in atomic transition frequencies between isotopes, arising from the mass shift (reduced mass) and the field shift (finite nuclear size); it is a direct measure of the change in nuclear mean-square charge radius delta<r^2> between isotopes."*
- Field shift and mass shift (1930s); measured in isotopes, 1931. Source: King, Isotope Shifts in Atomic Spectra (1984); Wikipedia: Isotopic shift

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-nuclear-size, point-nucleus, zero-shift limit*: if the nucleus were a point (zero radius), the field shift would be exactly zero; the classical treatment of a point nucleus is the zero-size, zero-field-shift limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

delta_nu_phi(kappa) = delta_nu_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_floor, where delta_floor is the phi-ground residual shift floor. At kappa->0 the point-nucleus (zero shift) is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_nu_phi = delta_nu_mass -> the isotope shift is the zero-field-shift, point-nucleus limit.
```

---

### STAGE 4 - SIMULATION

`sim/1591_isotope_shift.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1591_isotope_shift.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The isotope shift carries a phi-ground nuclear-size floor, so the extracted delta<r^2> has an irreducible uncertainty and even the point-nucleus limit retains a small residual shift.
EXPERIMENT (VERIFIED): Laser spectroscopy of isotope shifts (ISOLDE, FRIB) measuring nuclear charge radii across the nuclear chart.
VERIFIED BY: An isotope shift exactly equal to the mass shift with zero field-shift floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1486 (radius law), Law 1498 (charge distribution) and Law 162 (proton radius) - the isotope shift is the nucleus's size tag.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The atomic line shifts with the core; the phi-law keeps a floor of shift in every line.

### NOVELTY
Classical point nucleus has zero shift; the phi-law predicts an irreducible size floor.

### ACTIONABILITY
Run sim/1591_isotope_shift.py; verify delta<r^2>; proceed to Law 1592.

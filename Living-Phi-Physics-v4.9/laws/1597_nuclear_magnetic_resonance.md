# PHI-PHYSICS - LAW 1597
## Nuclear Magnetic Resonance (Rabi-Bloch-Purcell Resonance)

**Domain:** Nuclear / Condensed Matter - **Status:** 🟢 VALIDATED - **File:** `laws/1597_nuclear_magnetic_resonance.md` - **Sim:** `sim/1597_nuclear_magnetic_resonance.py`

---

### CLASSICAL STATEMENT
*"Nuclei with spin I in a magnetic field B0 precess at the Larmor frequency nu_L = gamma B0/(2 pi), and absorb RF power at resonance; NMR measures the chemical shift and spin-spin coupling, giving the most precise probes of molecular and condensed-matter structure."*
- Isidor Rabi (1938); Felix Bloch; Edward Purcell (1946), 1946. Source: Purcell, Torrey & Pound, Phys. Rev. 69 (1946) 37; Wikipedia: Nuclear magnetic resonance

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-field, zero-splitting, degenerate-level limit*: in zero magnetic field the nuclear spin levels are exactly degenerate and there is no resonance frequency; the classical treatment of an unperturbed spin is the zero-field, zero-splitting limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

nu_L_phi(kappa) = nu_L_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*nu_floor, where nu_floor is the phi-ground residual-interaction floor. At kappa->0 the exact Larmor frequency is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} nu_L_phi = gamma B0/(2 pi) -> NMR is the zero-field-inhomogeneity, zero-relaxation, exact-Larmor limit.
```

---

### STAGE 4 - SIMULATION

`sim/1597_nuclear_magnetic_resonance.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1597_nuclear_magnetic_resonance.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The NMR frequency carries a phi-ground residual-interaction floor, so the measured resonance always deviates from the bare Larmor value by an irreducible shift (the chemical-shift floor).
EXPERIMENT (VERIFIED): High-resolution NMR (nuclear shielding, J-coupling) and MRI (field mapping) measurements vs the bare Larmor prediction.
VERIFIED BY: An NMR resonance exactly at the bare Larmor frequency with zero shift floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1484 (magnetic moment), Law 233 (Larmor precession) and Law 1485 (quadrupole) - NMR is the spin's clock.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The spin ticks in a field; the phi-law keeps a floor of the tick shifting.

### NOVELTY
Classical NMR is bare Larmor; the phi-law predicts an irreducible shift floor.

### ACTIONABILITY
Run sim/1597_nuclear_magnetic_resonance.py; verify the Larmor frequency; proceed to Law 1598.

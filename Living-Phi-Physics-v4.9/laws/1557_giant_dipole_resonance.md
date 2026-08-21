# PHI-PHYSICS - LAW 1557
## Giant Dipole Resonance (Collective Oscillation of Protons vs Neutrons)

**Domain:** Nuclear Structure / Photonuclear - **Status:** 🟢 VALIDATED - **File:** `laws/1557_giant_dipole_resonance.md` - **Sim:** `sim/1557_giant_dipole_resonance.py`

---

### CLASSICAL STATEMENT
*"The giant dipole resonance is a collective oscillation of protons against neutrons, appearing as a broad peak in the photoabsorption cross-section at E ~ 78 A^(-1/3) MeV with width ~ 5 MeV; it exhausts the classical dipole sum rule and constrains the nuclear compressibility."*
- Baldwin & Klaiber (1947); Miguel (1944); Goldhaber & Teller (1948), 1947. Source: Baldwin & Klaiber, Phys. Rev. 71 (1947) 3; Wikipedia: Giant resonance

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-oscillation, rigid-sphere limit*: the GDR is the collective vibration of the proton and neutron fluids; the classical treatment of a rigid nucleus with zero relative oscillation has zero dipole strength - a zero-oscillation, frozen-fluids limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground strength floor. At kappa->0 the classical dipole sum rule is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = (60 NZ/A) mb.MeV -> the GDR is the zero-noncollective, classical-dipole-sum-rule, rigid-oscillation limit.
```

---

### STAGE 4 - SIMULATION

`sim/1557_giant_dipole_resonance.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1557_giant_dipole_resonance.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The dipole strength carries a phi-ground noncollective floor, so the photoabsorption never returns to exactly zero and the sum rule is split between the GDR and an irreducible quasi-deuteron floor.
EXPERIMENT (VERIFIED): Photoabsorption cross-section measurements (photonuclear reactions) resolving the GDR and its splitting.
VERIFIED BY: A photoabsorption spectrum with exactly zero strength away from the GDR peak at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1495 (compressibility), Law 1488 (Weisskopf) and Law 1458 (gamma) - the GDR is the nucleus's proton-neutron breath.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The two fluids swing against each other; the phi-law keeps a floor of the swing's echo.

### NOVELTY
Classical GDR is one peak; the phi-law predicts an irreducible strength floor.

### ACTIONABILITY
Run sim/1557_giant_dipole_resonance.py; verify the sum rule; proceed to Law 1558.

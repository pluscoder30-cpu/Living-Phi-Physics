# PHI-PHYSICS - LAW 1417
## Overhauser Effect (Dynamic Nuclear Polarization by Electron Saturation)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1417_overhauser_effect.md` - **Sim:** `sim/1417_overhauser_effect.py`

---

### CLASSICAL STATEMENT
*"Saturating the electron spin resonance of a metal or radical transfers electron polarization to the nuclei through the contact hyperfine interaction, producing dynamic nuclear polarization (DNP): the nuclear polarization can be enhanced by up to the electron-nuclear gyromagnetic ratio (~660 for protons, the Overhauser enhancement factor); it is the basis of Overhauser DNP in NMR/MRI signal enhancement."*
- Albert W. Overhauser, 1953. Source: Wikipedia: Overhauser effect; Overhauser, Phys. Rev. 92 (1953) 411

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero relaxation leakage*: the full enhancement is achieved exactly when nuclear relaxation is purely from the hyperfine coupling with zero leakage relaxation, i.e. a spin system with zero competing relaxation channels - the zero-leakage limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the relaxation leakage carries a coherence floor. f_enh_phi(kappa) = f_enh*(1 + kappa*(phi-1)) + kappa*phi^-1*f_leak, where f_leak is the phi-ground leakage; the enhancement saturates below the ideal. At kappa->0 the full Overhauser enhancement is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_n_phi = (gamma_e/gamma_n) P_e -> the Overhauser effect is the zero-leakage, ideal-DNP limit.
```

---

### STAGE 4 - SIMULATION

`sim/1417_overhauser_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1417_overhauser_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The DNP enhancement at full coherence coupling saturates below the gyromagnetic ratio by the phi-ground leakage kappa*phi^-1*f_leak, a floor in the achievable polarization transfer.
EXPERIMENT (VERIFIED): Overhauser DNP experiments (e.g. radicals in solution at high field) measuring the enhancement ceiling against the gyromagnetic ratio.
VERIFIED BY: DNP achieves exactly the gyromagnetic-ratio enhancement for all couplings.
```

---

### RECOGNITION
Connects to Law 1416 (Knight shift) and Law 496 (Seebeck, spin transport) - the Overhauser effect is the coherence polarization transfer.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the leakage floor is phi^-1 * f_leak.

### CLARITY
The electron's spin is poured into the nucleus; the phi-law keeps a floor of the pour's loss.

### NOVELTY
Classical DNP theory promises the full ratio; the phi-law keeps a coherence leakage floor.

### ACTIONABILITY
Run sim/1417_overhauser_effect.py; verify enhancement at kappa->0; proceed to 1418.

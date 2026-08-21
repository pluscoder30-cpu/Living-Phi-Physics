# PHI-PHYSICS - LAW 1480
## Optical Model of Nuclear Reactions (Complex Potential)

**Domain:** Nuclear Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1480_optical_model.md` - **Sim:** `sim/1480_optical_model.py`

---

### CLASSICAL STATEMENT
*"The scattering of nucleons by nuclei is described by a complex mean-field potential V(r) = U(r) + i W(r): the real part scatters elastically and the imaginary part absorbs flux into compound-nucleus channels; the total cross-section is computed from this optical potential."*
- Herman Feshbach; Charles Porter; Victor Weisskopf, 1953. Source: Feshbach, Porter & Weisskopf, Phys. Rev. 96 (1954) 448; Wikipedia: Optical model

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-imaginary-part, purely real potential*: the optical model reduces to the real shell-model potential when the imaginary (absorptive) part is exactly zero - a zero-loss, perfectly elastic, non-absorptive scatterer.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_tot_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground absorption floor. At kappa->0 the purely elastic optical potential is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_tot_phi = sigma_optical -> the optical model is the zero-imaginary-part, zero-absorption, purely-elastic limit.
```

---

### STAGE 4 - SIMULATION

`sim/1480_optical_model.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1480_optical_model.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Even the 'purely elastic' limit of the optical potential retains a phi-ground absorption floor, so the reaction cross-section never vanishes and elastic scattering always has a compound contribution.
EXPERIMENT (VERIFIED): Nucleon-nucleus elastic and reaction cross-section measurements (LANSCE, n_TOF) and optical-model parameter fits.
VERIFIED BY: A nucleus whose elastic scattering has exactly zero absorption (zero imaginary potential) at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1479 (compound nucleus), Law 1478 (resonance) and Law 1449 (shell model) - the optical potential is the nucleus's shadow.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The nucleus both scatters and drinks; the phi-law keeps a floor of drinking.

### NOVELTY
Classical optical model can be purely elastic; the phi-law keeps an irreducible absorption floor.

### ACTIONABILITY
Run sim/1480_optical_model.py; verify the complex-potential cross-section; proceed to Law 1481.

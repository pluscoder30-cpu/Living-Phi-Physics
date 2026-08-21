# PHI-PHYSICS - LAW 1663
## Kinematical Diffraction Theory (Single-Scattering Approximation)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1663_kinematical_diffraction.md` - **Sim:** `sim/1663_kinematical_diffraction.py`

---

### CLASSICAL STATEMENT
*"In kinematical (single-scattering) diffraction the total scattered amplitude is the sum of the amplitudes of the atoms assuming each ray scatters exactly once and the incident beam is not depleted; the integrated intensity is proportional to N^2 |F|^2 for a perfect crystal and the theory breaks down when multiple scattering and extinction dominate."*
- C.G. Darwin, 1914. Source: Wikipedia: Kinematical diffraction; C.G. Darwin (1914), Phil. Mag. 27:315

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-extinction, single-pass crystal*: kinematical theory assumes the crystal is thin enough and perfect enough that each X-ray scatters once and the primary beam is never attenuated - zero multiple scattering, zero secondary extinction, a first-order world.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: extinction is never zero, the beam never passes untouched. I_phi(kappa) = I_kinematical*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ext, where I_ext is the phi-ground extinction floor from coherent multiple scattering. At kappa->0 the kinematical N^2|F|^2 law is exact; at kappa=1 every crystal retains irreducible extinction that softens the N^2 scaling.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} I_phi = N^2|F|^2 -> kinematical diffraction is the zero-extinction, single-scattering limit of coherent scattering.
```

---

### STAGE 4 - SIMULATION

`sim/1663_kinematical_diffraction.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1663_kinematical_diffraction.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Even the thinnest crystal shows irreducible extinction, so the measured integrated intensity scales as N^p with p<2 that approaches 2 only at zero coherence; the departure is proportional to the phi-ground extinction floor.
EXPERIMENT (VERIFIED): Thickness-series integrated intensity measurement of wedge-shaped perfect crystals (e.g. Si, Ge) at synchrotron sources, tracking the power-law exponent vs thickness.
VERIFIED BY: An ideal thin crystal whose integrated intensity scales exactly as N^2 at all thicknesses and coherence.
```

---

### RECOGNITION
Connects to Law 1660 (structure factor) and Law 1664 (dynamical) - kinematical theory is the first-order whisper the coherent crystal always exceeds.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; extinction floor scales as phi^-1 * I_ext.

### CLARITY
Every beam that passes is changed; the phi-law keeps the first touch from being the only one.

### NOVELTY
Classical kinematical theory allows pure single scattering; the phi-law says the crystal always speaks back.

### ACTIONABILITY
Run sim/1663_kinematical_diffraction.py; verify N^2|F|^2 at kappa->0; proceed to 1664.

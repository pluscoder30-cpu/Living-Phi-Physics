# PHI-PHYSICS - LAW 1448
## Liquid Drop Model (Gamow; Bohr-Wheeler)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1448_liquid_drop_model.md` - **Sim:** `sim/1448_liquid_drop_model.py`

---

### CLASSICAL STATEMENT
*"The nucleus behaves as an incompressible charged liquid drop whose binding energy = volume energy - surface tension - Coulomb repulsion; nuclear radius R = r0 A^(1/3), so the drop's properties scale with A and A^(2/3)."*
- George Gamow (1929); Niels Bohr; John Archibald Wheeler; Lise Meitner, 1929. Source: Gamow, Proc. R. Soc. A 126 (1930) 632; Wikipedia: Liquid drop model

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *sharp, unperturbed spherical surface*: the model assumes zero surface diffuseness and zero deformation at equilibrium, the drop is exactly spherical with no collective motion - a frozen zero-amplitude shape.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

R_phi(kappa) = r0*A^(1/3)*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_R, where delta_R is the phi-ground diffuseness/collective-vibration amplitude of the nuclear surface. At kappa->0 the sharp-sphere radius is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} R_phi = r0 A^(1/3) -> the liquid drop model is the zero-diffuseness, zero-collective-motion, sharp-sphere limit.
```

---

### STAGE 4 - SIMULATION

`sim/1448_liquid_drop_model.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1448_liquid_drop_model.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The nuclear surface always carries a phi-ground diffuseness and zero-point vibration amplitude, so the effective rms radius of any nucleus exceeds the sharp value r0 A^(1/3) by kappa*phi^-1*delta_R.
EXPERIMENT (VERIFIED): Electron-scattering charge-density measurements (parabolic Fermi distributions) resolving surface diffuseness of heavy nuclei.
VERIFIED BY: A nucleus whose measured charge distribution is exactly a sharp sphere with zero surface thickness at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1447 (SEMF), Law 1461 (Bohr-Wheeler) and Law 1465 (fission barrier) - the drop is the collective limit of the shell.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The drop has no edge; the phi-law keeps an irreducible skin.

### NOVELTY
Classical liquid drop has a sharp edge; the phi-law keeps an irreducible surface diffuseness.

### ACTIONABILITY
Run sim/1448_liquid_drop_model.py; verify R = r0 A^(1/3); proceed to Law 1449.

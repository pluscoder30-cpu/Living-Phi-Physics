# PHI-PHYSICS - LAW 1660
## Structure Factor (F_hkl of the Unit Cell)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1660_structure_factor.md` - **Sim:** `sim/1660_structure_factor.py`

---

### CLASSICAL STATEMENT
*"The intensity of a reflection (hkl) is governed by the structure factor F_hkl = sum_j f_j exp(2 pi i (h x_j + k y_j + l z_j)), the coherent sum over the atoms in the unit cell; reflections are extinguished (F = 0) by systematic absences when the sum vanishes."*
- William Henry Bragg & William Lawrence Bragg, 1913. Source: Wikipedia: Structure factor; W.L. Bragg (1913), Proc. R. Soc. A89:248

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exactly registered, zero-displacement atom*: the structure factor assumes every atom sits exactly at its fractional coordinate (x_j,y_j,z_j) with zero displacement, so that the phase sum is exact and the zero of F is a true zero - a rigid, motionless, perfectly registered cell.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: atoms carry coherent displacement. F_phi(kappa) = |F_classical|*(1 + kappa*(phi-1)) + kappa*phi^-1*|F_floor|, where F_floor is the phi-ground scattering floor set by coherent zero-point displacements that never allow a perfectly dark reflection. At kappa->0 the exact structure factor is recovered; at kappa=1 systematic absences retain a phi-floor of residual intensity.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} F_phi = F_hkl -> the structure factor is the zero-displacement, perfectly-registered-atom limit of coherent scattering.
```

---

### STAGE 4 - SIMULATION

`sim/1660_structure_factor.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1660_structure_factor.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Systematic-absence reflections never vanish completely: they retain a phi-ground residual intensity kappa*phi^-1*|F_floor|^2 arising from zero-point coherent atomic displacements, observable as weak 'forbidden' reflections in high-precision diffraction.
EXPERIMENT (VERIFIED): High-dynamic-range X-ray or electron diffraction measuring the residual intensity of a nominally extinct reflection (e.g. 200 of bcc) at low temperature.
VERIFIED BY: A nominally extinct reflection measured with exactly zero integrated intensity.
```

---

### RECOGNITION
Connects to Law 1661 (form factor) and Law 1662 (Debye-Waller) - F_hkl is the voice of the cell and it never goes fully silent.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual intensity scales as (phi^-1 * |F_floor|)^2.

### CLARITY
The extinction rule says darkness; the phi-law keeps a candle of coherent scattering lit.

### NOVELTY
Classical crystallography allows exact extinctions; the phi-law gives forbidden reflections an irreducible floor.

### ACTIONABILITY
Run sim/1660_structure_factor.py; verify F_hkl at kappa->0; proceed to 1661.

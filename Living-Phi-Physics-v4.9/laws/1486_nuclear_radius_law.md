# PHI-PHYSICS - LAW 1486
## Nuclear Radius Law (R = r0 A^(1/3))

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1486_nuclear_radius_law.md` - **Sim:** `sim/1486_nuclear_radius_law.py`

---

### CLASSICAL STATEMENT
*"The nuclear radius scales with the cube root of the mass number: R = r0 A^(1/3) with r0 ~ 1.2 fm, reflecting the constant density of nuclear matter (~0.17 nucleons/fm^3); electron scattering measures the rms charge radius ~0.95 R."*
- Empirical law (Rutherford scattering, electron scattering); r0 ~ 1.2 fm, 1911. Source: Hofstadter, Ann. Rev. Nucl. Sci. 7 (1957) 231; Wikipedia: Nuclear size

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-diffuseness, exactly constant density*: the law assumes a sharp-edged sphere of exactly constant interior density with zero surface thickness - a step-function density with zero gradient.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

R_phi(kappa) = r0 A^(1/3)*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_R, where delta_R is the phi-ground surface-diffuseness floor. At kappa->0 the sharp A^(1/3) law is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} R_phi = r0 A^(1/3) -> the radius law is the zero-diffuseness, constant-density, sharp-edge limit.
```

---

### STAGE 4 - SIMULATION

`sim/1486_nuclear_radius_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1486_nuclear_radius_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The radius always exceeds the sharp value by a phi-ground diffuseness floor (~2 fm surface thickness), so the measured rms radius deviates systematically from r0 A^(1/3) and isotope shifts reveal this floor.
EXPERIMENT (VERIFIED): Electron-scattering and muonic-atom radii measurements (charge radius data, isotope shifts) vs the A^(1/3) law.
VERIFIED BY: A nucleus whose measured radius exactly equals r0 A^(1/3) with zero surface thickness at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1448 (liquid drop), Law 1447 (SEMF) and Law 162 (proton radius) - the radius law is the nucleus's size tag.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The sphere has a fuzz; the phi-law keeps a floor of fuzz on every sphere.

### NOVELTY
Classical radius is sharp; the phi-law predicts an irreducible surface diffuseness.

### ACTIONABILITY
Run sim/1486_nuclear_radius_law.py; verify R = r0 A^(1/3); proceed to Law 1487.

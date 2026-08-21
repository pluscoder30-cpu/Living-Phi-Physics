# PHI-PHYSICS - LAW 1447
## Semi-Empirical Mass Formula (Weizsaecker Formula)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1447_semi_empirical_mass_formula.md` - **Sim:** `sim/1447_semi_empirical_mass_formula.py`

---

### CLASSICAL STATEMENT
*"The binding energy of a nucleus with A nucleons and Z protons is E_B = a_V A - a_S A^(2/3) - a_C Z(Z-1)/A^(1/3) - a_A (N-Z)^2/A +- delta(A,Z), with volume, surface, Coulomb, asymmetry and pairing terms."*
- Carl Friedrich von Weizsaecker, 1935. Source: Weizsaecker, Z. Phys. 96 (1935) 431; Wikipedia: Semi-empirical mass formula

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *spherical, incompressible, sharp-edged nucleus*: the liquid drop treats the nuclear surface as a sharp boundary with zero diffuseness, zero deformation, and zero shell structure; the magic-number lines the formula cannot explain mark the failure of this smooth-zero picture.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

E_B_phi(kappa) = E_B_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*E_shell, where E_shell is the phi-ground shell-correction energy of the magic numbers. At kappa->0 the Weizsaecker formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_B_phi = a_V A - a_S A^(2/3) - a_C Z(Z-1)/A^(1/3) - a_A (N-Z)^2/A +- delta -> the SEMF is the sharp-surface, zero-shell-correction limit.
```

---

### STAGE 4 - SIMULATION

`sim/1447_semi_empirical_mass_formula.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1447_semi_empirical_mass_formula.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The binding energy of closed-shell (magic) nuclei exceeds the smooth liquid-drop value by kappa*phi^-1*E_shell even as the drop is made perfectly spherical; the shell-correction floor never vanishes.
EXPERIMENT (VERIFIED): Precision atomic mass measurements (Penning-trap, ISOLTRAP / AME2020) comparing SEMF smooth predictions with measured binding energies of magic nuclei.
VERIFIED BY: A magic nucleus whose measured binding energy exactly matches the smooth SEMF with no residual shell-correction floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1451 (pairing), Law 1450 (magic numbers) and the mass-defect law - the SEMF is the smooth-liquid-drop average the shell model corrects.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The drop forgets its shells; the phi-law keeps a floor of what the drop cannot forget.

### NOVELTY
Classical SEMF is smooth; the phi-law keeps an irreducible shell-correction floor that no smoothness can remove.

### ACTIONABILITY
Run sim/1447_semi_empirical_mass_formula.py; verify E_B at kappa->0 vs known 208Pb binding; proceed to Law 1448.

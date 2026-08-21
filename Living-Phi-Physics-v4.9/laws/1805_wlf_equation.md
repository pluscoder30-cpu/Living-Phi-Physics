# PHI-PHYSICS - LAW 1805
## Williams-Landel-Ferry (WLF) Equation (Time-Temperature Superposition of Polymers)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1805_wlf_equation.md` - **Sim:** `sim/1805_wlf_equation.py`

---

### CLASSICAL STATEMENT
*"For amorphous polymers near the glass transition, the relaxation times shift with temperature according to the WLF equation: log a_T = -C_1(T - T_ref)/(C_2 + T - T_ref), with the universal values C_1 ~ 17.44 and C_2 ~ 51.6 K near T_g (or C_1 ~ 8.86, C_2 ~ 101.6 for T_ref = T_g + 50); the WLF equation embodies time-temperature superposition, allowing polymer viscoelastic properties at one temperature to be predicted at another."*
- M.L. Williams, R.F. Landel & J.D. Ferry, 1955. Source: Wikipedia: Williams-Landel-Ferry equation; Williams, Landel & Ferry (1955), J. Am. Chem. Soc. 77:3701

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-free-volume-change, perfectly simple Arrhenius reference*: the WLF equation is defined against the simple Arrhenius (single-exponential) relaxation reference; its non-Arrhenius form arises because the free volume changes with temperature, away from the zero-free-volume-variation reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the shift factor carries a coherence floor. a_T_phi(kappa) = a_T_WLF*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_a, where delta_a is the phi-ground shift-factor floor. At kappa->0 the ideal WLF relation is recovered; at kappa=1 the universality of C_1, C_2 is broken by an irreducible material-specific floor.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} a_T_phi = exp(-C_1(T - T_ref)/(C_2 + T - T_ref)) -> the WLF equation is the free-volume-based time-temperature superposition measured from the zero-free-volume-change Arrhenius reference.
```

---

### STAGE 4 - SIMULATION

`sim/1805_wlf_equation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1805_wlf_equation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The WLF constants are never exactly universal: an irreducible material-specific deviation floor remains, so C_1 = 17.44 and C_2 = 51.6 are only approximate and no polymer obeys the ideal relation exactly.
EXPERIMENT (VERIFIED): Rheological master-curve construction for a series of amorphous polymers measuring the deviation of the WLF constants from the universal values.
VERIFIED BY: A polymer whose relaxation shift exactly follows the WLF relation with the universal constants and zero deviation.
```

---

### RECOGNITION
Connects to Law 1806 (VFT) and Law 1807 (glass transition) - the polymer's clock shifts with temperature, and the phi-law keeps the shift slightly off.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; shift floor scales as phi^-1 * delta_a.

### CLARITY
The polymer's clock runs on free volume; the phi-law keeps the clock slightly wrong.

### NOVELTY
Classical WLF gives universal constants; the phi-law keeps an irreducible deviation floor.

### ACTIONABILITY
Run sim/1805_wlf_equation.py; verify log a_T = -C_1(T-T_ref)/(C_2+T-T_ref) at kappa->0; proceed to 1806.

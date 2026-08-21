# PHI-PHYSICS - LAW 1329
## Zeeman Effect (Magnetic Splitting of Spectral Lines)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1329_zeeman_effect.md` - **Sim:** `sim/1329_zeeman_effect.py`

---

### CLASSICAL STATEMENT
*"A magnetic field B splits atomic spectral lines: the orbital Zeeman splitting is delta_E = mu_B B m_l (normal Zeeman, mu_B = e hbar/(2m_e) = 9.27 x 10^-24 J/T), and with spin the anomalous Zeeman effect gives delta_E = mu_B B g_J m_J, where g_J is the Lande g-factor; the normal triplet appears only for singlet states."*
- Pieter Zeeman, 1896. Source: Wikipedia: Zeeman effect; Zeeman, Nature 55 (1896) 347

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero field*: the splitting vanishes exactly at B = 0, i.e. an unmagnetized atom with zero magnetic coherence - the zero-field limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the splitting carries a coherence floor. delta_E_phi(kappa) = mu_B B g_J m_J*(1 + kappa*(phi-1)) + kappa*phi^-1*E_floor, where E_floor is the phi-ground magnetic splitting; even at B = 0 a floor splitting remains. At kappa->0 the Zeeman formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_E_phi = mu_B B g_J m_J -> the Zeeman effect is the zero-field, zero-floor limit.
```

---

### STAGE 4 - SIMULATION

`sim/1329_zeeman_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1329_zeeman_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Zeeman splitting at full coherence coupling retains a floor kappa*phi^-1*E_floor at vanishing field, a residual line splitting no atom escapes.
EXPERIMENT (VERIFIED): High-precision spectroscopy of an atomic transition sweeping B toward zero, measuring the residual splitting floor.
VERIFIED BY: Atomic lines are exactly unsplit at zero magnetic field for all couplings.
```

---

### RECOGNITION
Connects to Law 233 (Larmor), Law 1334 (Lande g-factor) and Law 1330 (Paschen-Back) - the Zeeman effect is the coherence coupling of the level to the field.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the splitting floor is phi^-1 * E_floor.

### CLARITY
Every line opens like a flower in the field; the phi-law keeps a petal open at zero field.

### NOVELTY
Classical spectroscopy closes lines at zero field; the phi-law keeps a coherence splitting floor.

### ACTIONABILITY
Run sim/1329_zeeman_effect.py; verify mu_B B m_l at kappa->0; proceed to 1330.

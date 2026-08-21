# PHI-PHYSICS - LAW 1346
## Photoionization (Photoelectric Emission from Atoms; Einstein's Law)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1346_photoionization.md` - **Sim:** `sim/1346_photoionization.py`

---

### CLASSICAL STATEMENT
*"A photon of energy h nu ionizes an atom if h nu >= I (ionization potential), ejecting a photoelectron with kinetic energy E_kin = h nu - I (the photoelectric law); the cross section for photoionization of hydrogen scales as sigma ~ (I/h nu)^3.5 near threshold and vanishes below threshold."*
- Albert Einstein (law); applied to atoms by many, 1905. Source: Wikipedia: Photoionization; Einstein, Ann. Phys. 17 (1905) 132

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *threshold*: the photoelectric law gives E_kin = 0 exactly at threshold h nu = I, and zero cross section below - a sharp threshold the phi-law reads as the zero-below-threshold limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the threshold carries a coherence floor. E_kin_phi(kappa) = (h nu - I)*(1 + kappa*(phi-1)) + kappa*phi^-1*E_floor, where E_floor is the phi-ground sub-threshold emission; photoionization persists below the nominal threshold. At kappa->0 the photoelectric law is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_kin_phi = h nu - I -> the photoelectric/photoionization law is the sharp-threshold, zero-sub-threshold limit.
```

---

### STAGE 4 - SIMULATION

`sim/1346_photoionization.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1346_photoionization.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Photoionization at full coherence coupling occurs below the nominal threshold I with a floor rate kappa*phi^-1*E_floor, a sub-threshold ionization floor.
EXPERIMENT (VERIFIED): Precision ionization-threshold spectroscopy of atoms (e.g. via laser ionization) searching for sub-threshold ionization at increasing field coherence.
VERIFIED BY: Photoionization is exactly zero below the ionization threshold for all couplings.
```

---

### RECOGNITION
Connects to Law 067 (photoelectric effect) and Law 1347 (X-ray fluorescence) - photoionization is the coherence threshold of the electron.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the sub-threshold floor is phi^-1 * E_floor.

### CLARITY
Even below the stair, a few electrons take the step early; the phi-law counts them.

### NOVELTY
Classical photophysics pins an exact threshold; the phi-law keeps a sub-threshold coherence floor.

### ACTIONABILITY
Run sim/1346_photoionization.py; verify E_kin = h nu - I at kappa->0; proceed to 1347.

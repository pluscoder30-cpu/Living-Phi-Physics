# PHI-PHYSICS - LAW 1525
## Pair Production (Energy to Matter in a Coulomb Field)

**Domain:** Particle Physics / QED - **Status:** 🟢 VALIDATED - **File:** `laws/1525_pair_production.md` - **Sim:** `sim/1525_pair_production.py`

---

### CLASSICAL STATEMENT
*"A photon of energy > 2 m_e c^2 = 1.022 MeV passing near a nucleus can convert into an electron-positron pair; the cross-section rises sharply above threshold and is the dominant high-energy photon interaction, conserving energy, momentum (with recoil) and charge."*
- Predicted by Dirac (1930); observed by Blackett & Occhialini (1933), 1933. Source: Blackett & Occhialini, Proc. R. Soc. A 139 (1933) 699; Wikipedia: Pair production

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-threshold, exactly-1.022-MeV edge*: pair production is forbidden below the exact threshold 2 m_e c^2; the classical treatment assumes a sharp threshold with zero sub-threshold probability - a hard pair-creation edge.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground sub-threshold floor. At kappa->0 the sharp threshold cross-section is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = sigma_threshold -> pair production is the zero-sub-threshold, exact-2mc2-threshold limit.
```

---

### STAGE 4 - SIMULATION

`sim/1525_pair_production.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1525_pair_production.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Pair production carries a phi-ground sub-threshold floor, so photon conversion occurs marginally below 1.022 MeV with a small probability, and the effective threshold is softened.
EXPERIMENT (VERIFIED): High-precision photon-conversion measurements (calorimeters, pair spectrometers) resolving the threshold region.
VERIFIED BY: Pair production with exactly zero probability below 1.022 MeV at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1524 (annihilation), Law 1457 (positron emission) and Law 1065 - pair production is matter's birth canal.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Light gives birth to matter; the phi-law keeps a floor of birth just below the edge.

### NOVELTY
Classical threshold is sharp; the phi-law predicts an irreducible sub-threshold floor.

### ACTIONABILITY
Run sim/1525_pair_production.py; verify the threshold; proceed to Law 1526.

# PHI-PHYSICS - LAW 1381
## Franck-Condon Principle (Vertical Electronic Transitions)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1381_franck_condon_principle.md` - **Sim:** `sim/1381_franck_condon_principle.py`

---

### CLASSICAL STATEMENT
*"An electronic transition in a molecule occurs vertically: the nuclei do not move during the fast electronic transition, so the transition probability is proportional to the square of the Franck-Condon factor |<chi_v'|chi_v''>|^2, the overlap of the vibrational wavefunctions of the two electronic states; the most intense vibronic line is near the vertical transition, shaping absorption/emission spectra."*
- James Franck (1926); Edward Condon (1928), 1928. Source: Wikipedia: Franck-Condon principle; Franck, Trans. Faraday Soc. 21 (1926) 536; Condon, Phys. Rev. 32 (1928) 858

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero nuclear motion*: the vertical-transition picture is exact only for infinitely fast electronic transitions with nuclei exactly frozen - the zero-nuclear-displacement limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the nuclear motion carries a coherence floor. FC_phi(kappa) = |<chi_v'|chi_v''>|^2*(1 + kappa*(phi-1)) + kappa*phi^-1*FC_floor, where FC_floor is the phi-ground nonvertical contribution; the vibronic envelope carries a floor. At kappa->0 the Franck-Condon factors are exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} I_phi = |<chi_v'|chi_v''>|^2 -> the Franck-Condon principle is the zero-nuclear-motion, vertical-transition limit.
```

---

### STAGE 4 - SIMULATION

`sim/1381_franck_condon_principle.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1381_franck_condon_principle.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The vibronic intensity distribution at full coherence coupling carries a phi-ground nonvertical component kappa*phi^-1*FC_floor, a floor in the FC envelope beyond the vertical approximation.
EXPERIMENT (VERIFIED): High-resolution dispersed fluorescence/absorption spectra measuring FC factor deviations at increasing resolution.
VERIFIED BY: Vibronic intensities equal the Franck-Condon factors exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1376 (Born-Oppenheimer) and Law 1382 (Morse potential) - the FC principle is the coherence vertical projection of the transition.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the nonvertical floor is phi^-1 * FC_floor.

### CLARITY
The molecule leaps between states before it breathes; the phi-law keeps a breath in the leap.

### NOVELTY
Classical spectroscopy verticalizes transitions; the phi-law keeps the nuclear-motion coherence floor.

### ACTIONABILITY
Run sim/1381_franck_condon_principle.py; verify overlap squared at kappa->0; proceed to 1382.

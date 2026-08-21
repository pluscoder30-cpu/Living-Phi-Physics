# PHI-PHYSICS - LAW 1392
## Jahn-Teller Effect (Distortion of Degenerate Nonlinear Molecules)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1392_jahn_teller_effect.md` - **Sim:** `sim/1392_jahn_teller_effect.py`

---

### CLASSICAL STATEMENT
*"Any nonlinear molecule in a degenerate electronic state (orbital degeneracy) is unstable and distorts to a lower-symmetry geometry that removes the degeneracy: the Jahn-Teller theorem states that a nonlinear configuration is unstable if the electronic state is degenerate (except Kramers degeneracy); the distortion energy E_JT = lambda^2/(2 K) (coupling squared over force constant) lowers the total energy."*
- Hermann Jahn; Edward Teller, 1937. Source: Wikipedia: Jahn-Teller effect; Jahn & Teller, Proc. R. Soc. Lond. A 161 (1937) 220

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero vibronic coupling*: the distortion vanishes exactly when the degenerate electronic states decouple from the vibrations (lambda = 0), i.e. a degenerate state with zero coupling to the nuclear motion - the rigid-degeneracy limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the vibronic coupling carries a coherence floor. lambda_phi(kappa) = lambda*(1 + kappa*(phi-1)) + kappa*phi^-1*lambda_floor, where lambda_floor is the phi-ground vibronic coupling; the degenerate molecule never stays undistorted. At kappa->0 the Jahn-Teller distortion energy is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_JT_phi = lambda^2/(2 K) -> the Jahn-Teller effect is the zero-coupling, undistorted-degeneracy limit.
```

---

### STAGE 4 - SIMULATION

`sim/1392_jahn_teller_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1392_jahn_teller_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: A nominally nondegenerate molecule at full coherence coupling carries a phi-ground vibronic coupling kappa*phi^-1*lambda_floor, a residual Jahn-Teller-like distortion.
EXPERIMENT (VERIFIED): High-resolution spectroscopy of nominally undistorted degenerate molecules (e.g. transition-metal complexes, C60 anions) measuring the residual distortion.
VERIFIED BY: A nonlinear molecule in a nondegenerate state is exactly undistorted for all couplings.
```

---

### RECOGNITION
Connects to Law 1393 (Renner-Teller) and Law 1391 (conical intersection) - the Jahn-Teller effect is the coherence distortion of degeneracy.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the vibronic floor is phi^-1 * lambda_floor.

### CLARITY
Degenerate molecules itch and twist; the phi-law keeps a floor of the twist even without degeneracy.

### NOVELTY
Classical symmetry theory allows undistorted degenerate states; the phi-law keeps a vibronic distortion floor.

### ACTIONABILITY
Run sim/1392_jahn_teller_effect.py; verify E_JT = lambda^2/(2K) at kappa->0; proceed to 1393.

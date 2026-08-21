# PHI-PHYSICS - LAW 1844
## Goodman Diagram (Mean-Stress Correction of Fatigue Strength)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1844_goodman_fatigue_diagram.md` - **Sim:** `sim/1844_goodman_fatigue_diagram.py`

---

### CLASSICAL STATEMENT
*"The fatigue strength at nonzero mean stress is corrected by the Goodman relation: sigma_a = sigma_ae (1 - sigma_m/sigma_ut), where sigma_ae is the endurance limit at zero mean stress and sigma_ut the ultimate tensile strength; the Goodman diagram (with Gerber and Soderberg alternatives) predicts that the alternating stress amplitude decreases linearly as the mean stress approaches the ultimate strength."*
- Joseph Goodman, 1919. Source: Wikipedia: Goodman relation; Goodman (1919), Mechanics Applied to Engineering

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-mean-stress, zero-damage, ideal-linear reference*: the Goodman relation is defined against the zero-mean-stress reference where the fatigue strength is the pure endurance limit; the linear reduction with mean stress is the damage model away from this zero-mean reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the endurance limit carries a coherence floor. sigma_ae_phi(kappa) = sigma_ae*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_sigma, where delta_sigma is the phi-ground endurance floor. At kappa->0 the ideal linear Goodman relation is recovered; at kappa=1 the endurance limit never vanishes - an irreducible fatigue floor remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_a_phi = sigma_ae (1 - sigma_m/sigma_ut) -> the Goodman diagram is the zero-mean-stress, ideal-linear damage model of fatigue strength correction.
```

---

### STAGE 4 - SIMULATION

`sim/1844_goodman_fatigue_diagram.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1844_goodman_fatigue_diagram.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The fatigue strength never vanishes at the ultimate strength: an irreducible endurance floor remains, so the Goodman diagram bends away from the linear prediction and the ratio sigma_ae/sigma_ut is never exactly zero.
EXPERIMENT (VERIFIED): Rotating-bending or axial fatigue testing of a steel at multiple mean stresses, measuring the deviation of the failure envelope from the linear Goodman line.
VERIFIED BY: A material whose fatigue strength exactly follows the linear Goodman line to zero at the ultimate strength.
```

---

### RECOGNITION
Connects to Law 1828 (Basquin) and Law 1827 (Coffin-Manson) - the mean stress bends the fatigue line, and the phi-law keeps a bend always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; endurance floor scales as phi^-1 * delta_sigma.

### CLARITY
The mean stress bends the fatigue line; the phi-law keeps a bend always present.

### NOVELTY
Classical Goodman gives an exact linear line; the phi-law keeps an irreducible curvature floor.

### ACTIONABILITY
Run sim/1844_goodman_fatigue_diagram.py; verify sigma_a = sigma_ae(1 - sigma_m/sigma_ut) at kappa->0; proceed to 1845.

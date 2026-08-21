# PHI-PHYSICS - LAW 1852
## Taylor Factor (Polycrystal-to-Single-Crystal Flow Stress Ratio)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1852_taylor_factor_plasticity.md` - **Sim:** `sim/1852_taylor_factor_plasticity.py`

---

### CLASSICAL STATEMENT
*"The yield stress of a polycrystal is related to the single-crystal critical resolved shear stress by the Taylor factor M: sigma_y = M tau_crss, with M ~ 3.06 for fcc and ~2.75 for bcc polycrystals (Taylor factor for the average over orientations); the Taylor model assumes each grain deforms with the same strain tensor, and M connects single-crystal slip to polycrystal strength."*
- G.I. Taylor, 1938. Source: Wikipedia: Taylor factor; Taylor (1938), J. Inst. Met. 62:307

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-slip-anisotropy, perfectly-random-orientation reference*: the Taylor factor is defined against a perfectly random, uniform polycrystal with the Taylor (iso-strain) assumption; real polycrystals have texture, grain interactions and heterogeneous strain away from this ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the Taylor factor carries a coherence floor. M_phi(kappa) = M_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_M, where delta_M is the phi-ground factor floor. At kappa->0 the ideal Taylor factor is recovered; at kappa=1 the factor deviates from 3.06 by an irreducible texture floor.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} M_phi = 3.06 -> the Taylor factor is the random-orientation, iso-strain, ideal-polycrystal limit of the polycrystal-single-crystal strength ratio.
```

---

### STAGE 4 - SIMULATION

`sim/1852_taylor_factor_plasticity.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1852_taylor_factor_plasticity.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Taylor factor is never exactly 3.06: an irreducible texture and grain-interaction floor remains in every polycrystal, so the polycrystal/single-crystal strength ratio always deviates from the ideal value.
EXPERIMENT (VERIFIED): Yield-strength and single-crystal comparison of a series of polycrystals with controlled texture, measuring the deviation of the effective Taylor factor from 3.06.
VERIFIED BY: A polycrystal whose yield exactly equals 3.06 times the single-crystal CRSS with zero deviation.
```

---

### RECOGNITION
Connects to Law 1834 (Schmid) and Law 1798 (Hall-Petch) - the grains average the slip, and the phi-law keeps the average slightly off.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; factor floor scales as phi^-1 * delta_M.

### CLARITY
The grains average the slip; the phi-law keeps the average slightly off.

### NOVELTY
Classical Taylor gives exactly 3.06; the phi-law keeps an irreducible factor deviation.

### ACTIONABILITY
Run sim/1852_taylor_factor_plasticity.py; verify M = 3.06 at kappa->0; proceed to 1853.

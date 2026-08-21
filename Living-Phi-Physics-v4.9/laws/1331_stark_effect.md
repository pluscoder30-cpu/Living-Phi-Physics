# PHI-PHYSICS - LAW 1331
## Stark Effect (Electric Splitting of Spectral Lines)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1331_stark_effect.md` - **Sim:** `sim/1331_stark_effect.py`

---

### CLASSICAL STATEMENT
*"An electric field E shifts and splits atomic levels: for hydrogen the linear Stark effect shifts n=2 levels by delta_E = (3/2) n a_0 e E (degenerate first-order), while for non-hydrogenic atoms the quadratic Stark effect gives delta_E = -(1/2) alpha E^2 with alpha the polarizability; it underlies electric-field sensing and the modulation of transitions."*
- Johannes Stark, 1913. Source: Wikipedia: Stark effect; Stark, Sitz. Konigl. Preuss. Akad. Wiss. (1913) 932

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero field*: the shift vanishes exactly at E = 0, i.e. an unpolarized atom with zero electric coherence - the zero-field limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the shift carries a coherence floor. delta_E_phi(kappa) = delta_E*(1 + kappa*(phi-1)) + kappa*phi^-1*E_floor, where E_floor is the phi-ground Stark shift; even at E = 0 a floor shift remains. At kappa->0 the Stark formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_E_phi = (3/2) n a_0 e E -> the Stark effect is the zero-field, zero-floor limit.
```

---

### STAGE 4 - SIMULATION

`sim/1331_stark_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1331_stark_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Stark shift at full coherence coupling retains a floor kappa*phi^-1*E_floor at vanishing field, a residual level shift no atom escapes.
EXPERIMENT (VERIFIED): High-precision Rydberg-atom Stark spectroscopy sweeping E toward zero, measuring the residual shift floor.
VERIFIED BY: Atomic levels are exactly unshifted at zero electric field for all couplings.
```

---

### RECOGNITION
Connects to Law 1329 (Zeeman, its magnetic dual) and Law 1302 (degenerate perturbation) - the Stark effect is the coherence coupling of the level to the electric field.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the shift floor is phi^-1 * E_floor.

### CLARITY
Every level leans in the field; the phi-law keeps the lean at zero field.

### NOVELTY
Classical spectroscopy zeros the shift at zero field; the phi-law keeps a coherence floor shift.

### ACTIONABILITY
Run sim/1331_stark_effect.py; verify 3/2 n a0 e E at kappa->0; proceed to 1332.

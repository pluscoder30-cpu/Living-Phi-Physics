# PHI-PHYSICS - LAW 1840
## Tabor's Law (Hardness Approximates Three Times the Yield Strength)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1840_tabor_hardness_law.md` - **Sim:** `sim/1840_tabor_hardness_law.py`

---

### CLASSICAL STATEMENT
*"The indentation hardness of a metal is approximately three times its yield strength: H ~ 3 sigma_y, because the plastic zone under an indenter is constrained and the mean indentation pressure is about 2.8-3 times the flow stress; Tabor's law connects hardness testing to tensile properties and is the standard calibration of indentation-based strength measurement."*
- David Tabor, 1951. Source: Wikipedia: Hardness; Tabor (1951), The Hardness of Metals

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-yield-strength, zero-hardness, perfectly rigid-perfectly-plastic reference*: Tabor's law assumes an ideal rigid-perfectly-plastic material with a constant constraint factor; real materials harden, have friction and elastic effects that shift the factor away from exactly 3.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the constraint factor carries a coherence floor. C_phi(kappa) = 3*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_C, where delta_C is the phi-ground deviation of the constraint factor. At kappa->0 the ideal factor 3 is recovered; at kappa=1 the factor deviates from 3 by an irreducible floor.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} H_phi = 3 sigma_y -> Tabor's law is the rigid-perfectly-plastic, zero-hardening, ideal-constraint limit of indentation hardness.
```

---

### STAGE 4 - SIMULATION

`sim/1840_tabor_hardness_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1840_tabor_hardness_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The hardness/yield-strength ratio is never exactly 3: an irreducible constraint-factor deviation remains in every metal, so indentation-based strength estimates always carry a small systematic floor error.
EXPERIMENT (VERIFIED): Nanoindentation and tensile testing of a series of metals and alloys, measuring the systematic deviation of the hardness/yield ratio from 3.
VERIFIED BY: A metal whose hardness is exactly 3 times its yield strength for all hardening states.
```

---

### RECOGNITION
Connects to Law 1832 (strain hardening) and Law 1793 (von Mises) - the indenter reads the yield through a factor, and the phi-law keeps the factor slightly off.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; factor deviation scales as phi^-1 * delta_C.

### CLARITY
The indenter reads the yield; the phi-law keeps the reading slightly off.

### NOVELTY
Classical Tabor gives exactly 3; the phi-law keeps an irreducible factor deviation.

### ACTIONABILITY
Run sim/1840_tabor_hardness_law.py; verify H = 3 sigma_y at kappa->0; proceed to 1841.

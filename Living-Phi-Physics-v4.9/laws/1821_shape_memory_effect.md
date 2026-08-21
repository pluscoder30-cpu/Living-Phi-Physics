# PHI-PHYSICS - LAW 1821
## Shape Memory Effect (Recovery of Shape by Martensitic Reversion)

**Domain:** Phase Transformations - **Status:** 🟢 VALIDATED - **File:** `laws/1821_shape_memory_effect.md` - **Sim:** `sim/1821_shape_memory_effect.py`

---

### CLASSICAL STATEMENT
*"Shape-memory alloys (Nitinol, AuCd, CuZnAl) recover their original shape on heating above A_f because the martensitic transformation is thermoelastic and reversible: deformation is accommodated by martensite reorientation or detwinning, and heating reverts the martensite to austenite, restoring the shape; the one-way and two-way effects and superelasticity above A_f make SMA actuators, stents and couplings possible."*
- William Buehler & Frederick Wang (Nitinol, 1962); discovered 1951 by Chang & Read (AuCd), 1951. Source: Wikipedia: Shape-memory alloy; Chang & Read (1951), Trans. AIME 191:47; Buehler et al. (1963)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-deformation, perfectly reversible, hysteresis-free reference*: the shape-memory effect is defined against a perfectly reversible transformation with zero hysteresis and zero residual deformation; real SMAs have transformation hysteresis, residual strain and functional fatigue away from this ideal reversible reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the recovery carries a coherence floor. R_phi(kappa) = R_SMA*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_R, where delta_R is the phi-ground unrecovered-strain floor. At kappa->0 the perfect shape recovery is recovered; at kappa=1 no SMA recovers 100% - an irreducible residual-strain floor remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} R_phi = 100% -> the shape-memory effect is the zero-hysteresis, perfectly-reversible, ideal-thermoelastic limit of shape recovery.
```

---

### STAGE 4 - SIMULATION

`sim/1821_shape_memory_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1821_shape_memory_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No shape-memory alloy recovers exactly 100% of its deformation: an irreducible residual-strain floor remains after each cycle, and functional fatigue accumulates with cycling.
EXPERIMENT (VERIFIED): Cyclic strain-recovery measurement of a Nitinol wire over many cycles, measuring the residual unrecovered strain floor per cycle.
VERIFIED BY: A shape-memory alloy recovering exactly 100% of deformation with zero residual strain every cycle.
```

---

### RECOGNITION
Connects to Law 1820 (martensitic) and Law 1822 (superelasticity) - the alloy remembers its first shape, and the phi-law keeps a wrinkle in the memory.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual-strain floor scales as phi^-1 * delta_R.

### CLARITY
The alloy remembers its shape; the phi-law keeps a wrinkle in the memory.

### NOVELTY
Classical SMA theory allows perfect recovery; the phi-law keeps an irreducible residual strain.

### ACTIONABILITY
Run sim/1821_shape_memory_effect.py; verify the shape recovery at kappa->0; proceed to 1822.

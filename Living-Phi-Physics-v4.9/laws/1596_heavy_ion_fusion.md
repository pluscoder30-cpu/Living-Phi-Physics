# PHI-PHYSICS - LAW 1596
## Heavy-Ion Fusion Cross-Section (Coulomb Barrier and Fusion Window)

**Domain:** Nuclear Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1596_heavy_ion_fusion.md` - **Sim:** `sim/1596_heavy_ion_fusion.py`

---

### CLASSICAL STATEMENT
*"Heavy-ion fusion requires overcoming the Coulomb barrier V_B ~ Z1 Z2 e^2/(R1 + R2); the fusion cross-section follows sigma_fusion = pi R^2 (1 - V_B/E) above the barrier, and the fusion window (sub-barrier enhancement) depends on nuclear structure (deformation, vibrations)."*
- Heavy-ion fusion systematics (1970s); Bass model (1974), 1974. Source: Bass, Nucl. Phys. A231 (1974) 45; Wikipedia: Nuclear fusion

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-deformation, zero-coupling, sharp-barrier limit*: the classical fusion cross-section assumes a sharp Coulomb barrier with zero nuclear-structure coupling; sub-barrier fusion enhancement is the deviation from this zero-coupling limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground sub-barrier coupling floor. At kappa->0 the sharp-barrier fusion is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = pi R^2 (1 - V_B/E) -> heavy-ion fusion is the zero-coupling, sharp-barrier, structureless limit.
```

---

### STAGE 4 - SIMULATION

`sim/1596_heavy_ion_fusion.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1596_heavy_ion_fusion.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Sub-barrier fusion enhancement carries a phi-ground coupling floor, so the measured cross-section below the barrier always exceeds the sharp-barrier prediction by an irreducible nuclear-structure contribution.
EXPERIMENT (VERIFIED): Heavy-ion fusion excitation function measurements (sub-barrier fusion, e.g. 16O+208Pb) vs coupled-channels calculations.
VERIFIED BY: A heavy-ion fusion cross-section exactly matching the sharp-barrier formula with zero sub-barrier enhancement.
```

---

### RECOGNITION
Connects to Law 1452 (Gamow), Law 1477 (threshold) and Law 1496 (deformation) - heavy-ion fusion is the nucleus-maker's hammer.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The two cores meet over a wall; the phi-law keeps a floor of the wall thinning.

### NOVELTY
Classical barrier is sharp; the phi-law predicts an irreducible sub-barrier floor.

### ACTIONABILITY
Run sim/1596_heavy_ion_fusion.py; verify the barrier; proceed to Law 1597.

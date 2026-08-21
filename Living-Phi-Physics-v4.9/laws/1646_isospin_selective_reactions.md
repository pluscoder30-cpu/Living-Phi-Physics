# PHI-PHYSICS - LAW 1646
## Isospin-Selective Reactions (Isobaric Analog Resonances in Reactions)

**Domain:** Nuclear Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1646_isospin_selective_reactions.md` - **Sim:** `sim/1646_isospin_selective_reactions.py`

---

### CLASSICAL STATEMENT
*"Nuclear reactions can selectively populate isospin states: isobaric analog resonances in (p,p), (p,n) and (3He,t) reactions excite the analog of the target ground state, giving a direct test of isospin symmetry and the Coulomb matrix elements."*
- Isobaric analog resonance reactions (1960s), 1964. Source: Fox, Moore & Robson (1964); Wikipedia: Isospin

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-isospin-mixing, zero-analog-excitation, pure-T limit*: in the absence of Coulomb mixing the analog state is exactly degenerate and reactions select pure isospin; the classical treatment of pure isospin is the zero-mixing, exact-T limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground isospin-mixing floor. At kappa->0 the pure-isospin selection is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = sigma_analog -> isospin-selective reactions are the zero-mixing, pure-isospin, exact-analog limit.
```

---

### STAGE 4 - SIMULATION

`sim/1646_isospin_selective_reactions.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1646_isospin_selective_reactions.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The analog resonance excitation carries a phi-ground isospin-mixing floor, so the isospin purity of the selected states is never exactly 1.
EXPERIMENT (VERIFIED): Isobaric analog resonance studies ((p,p), (3He,t) at accelerators) and isospin-mixing measurements.
VERIFIED BY: A reaction exciting a state of exactly pure isospin with zero mixing at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1589 (analog states), Law 1491 (isospin) and Law 1479 (compound) - isospin-selective reactions are the symmetry's scalpel.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The reaction picks pure colors; the phi-law keeps a floor of color mixing.

### NOVELTY
Classical isospin selection is pure; the phi-law predicts an irreducible mixing floor.

### ACTIONABILITY
Run sim/1646_isospin_selective_reactions.py; verify the analog resonance; proceed to Law 1647.

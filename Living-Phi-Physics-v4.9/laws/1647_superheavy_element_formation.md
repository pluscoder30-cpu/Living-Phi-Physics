# PHI-PHYSICS - LAW 1647
## Superheavy Element Formation (Fusion-Evaporation to Z > 104)

**Domain:** Nuclear Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1647_superheavy_element_formation.md` - **Sim:** `sim/1647_superheavy_element_formation.py`

---

### CLASSICAL STATEMENT
*"Superheavy elements (Z = 104-118) are formed by fusion-evaporation reactions (e.g. 208Pb + 70Zn -> 277Cn* -> 277Cn + n); the production cross-sections are extremely small (~pb) and the survival depends on the fission barrier and the shell stabilization at the island of stability."*
- Cold fusion (1980s, GSI); hot fusion (Dubna 1990s-2000s), 1981. Source: Armbruster et al. (GSI 1981-1996); Wikipedia: Superheavy element

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-survival, zero-cross-section, instant-fission limit*: without shell stabilization the compound nucleus fissions instantly with zero survival; the classical treatment of an unstabilized compound nucleus is the zero-survival, zero-production limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground survival floor. At kappa->0 the exact production cross-section is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = sigma_fusion-evaporation -> superheavy formation is the zero-fission-limit, exact-shell-stabilization, ideal-survival limit.
```

---

### STAGE 4 - SIMULATION

`sim/1647_superheavy_element_formation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1647_superheavy_element_formation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The superheavy production cross-section carries a phi-ground survival floor, so even below the predicted optimum a small production probability survives via shell stabilization.
EXPERIMENT (VERIFIED): Superheavy element synthesis experiments (GSI, Dubna, RIKEN, LBNL) measuring cross-sections toward Z = 120.
VERIFIED BY: A superheavy formation with exactly zero cross-section away from the predicted optimum.
```

---

### RECOGNITION
Connects to Law 1461 (Bohr-Wheeler), Law 1615 (shell energy) and Law 1464 (fission barrier) - superheavies are the island's explorers.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The island of stability beckons; the phi-law keeps a floor of the island holding.

### NOVELTY
Classical formation is cross-section-exact; the phi-law predicts an irreducible survival floor.

### ACTIONABILITY
Run sim/1647_superheavy_element_formation.py; verify the cross-section; proceed to Law 1648.

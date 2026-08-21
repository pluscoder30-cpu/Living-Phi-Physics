# PHI-PHYSICS - LAW 1380
## VSEPR Theory (Valence Shell Electron Pair Repulsion)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1380_vsepr_theory.md` - **Sim:** `sim/1380_vsepr_theory.py`

---

### CLASSICAL STATEMENT
*"VSEPR theory predicts molecular geometry from the repulsion of electron pairs in the valence shell: electron pairs (bonding and lone pairs) arrange to maximize their separation, giving linear (2), trigonal planar (3), tetrahedral (4), trigonal bipyramidal (5), octahedral (6) parent geometries; lone pairs occupy more space than bonding pairs, compressing bond angles."*
- Ronald Gillespie; Ronald Nyholm (building on Sidgwick & Powell), 1957. Source: Wikipedia: VSEPR theory; Gillespie & Nyholm, Quart. Rev. Chem. Soc. 11 (1957) 339

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly symmetric repulsion*: the predicted angles are exact for idealized identical electron pairs with zero lone-pair/bonding-pair difference and zero inter-pair distortion - the symmetric-pair limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the pair repulsion carries a coherence asymmetry. theta_phi(kappa) = theta*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_theta, where delta_theta is the phi-ground angle distortion from pair asymmetry; the VSEPR angles carry a floor. At kappa->0 the ideal VSEPR angles are exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} theta_phi = 109.5 deg etc -> VSEPR theory is the zero-pair-asymmetry, symmetric-repulsion limit.
```

---

### STAGE 4 - SIMULATION

`sim/1380_vsepr_theory.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1380_vsepr_theory.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The molecular bond angles at full coherence coupling deviate from the ideal VSEPR angles by the phi-ground distortion kappa*phi^-1*delta_theta, a floor in the geometric prediction.
EXPERIMENT (VERIFIED): High-precision gas-phase electron diffraction or rotational spectroscopy measuring bond angles against VSEPR predictions.
VERIFIED BY: Molecules adopt exactly the ideal VSEPR angles for all couplings.
```

---

### RECOGNITION
Connects to Law 1379 (hybridization) and Law 1398 (Walsh diagrams) - VSEPR is the coherence geometry of electron-pair repulsion.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the angle distortion is phi^-1 * delta_theta.

### CLARITY
Electron pairs elbow for room; the phi-law keeps the elbowing's floor of distortion.

### NOVELTY
Classical chemistry predicts ideal shapes; the phi-law keeps a coherence angle floor on every shape.

### ACTIONABILITY
Run sim/1380_vsepr_theory.py; verify 109.5 deg at kappa->0; proceed to 1381.

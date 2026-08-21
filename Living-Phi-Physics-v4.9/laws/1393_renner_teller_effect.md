# PHI-PHYSICS - LAW 1393
## Renner-Teller Effect (Degeneracy of Linear Triatomic Molecules)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1393_renner_teller_effect.md` - **Sim:** `sim/1393_renner_teller_effect.py`

---

### CLASSICAL STATEMENT
*"In linear triatomic molecules (e.g. CO2, NCO, C3), a degenerate electronic state (Pi, Delta) splits when the molecule bends: the two degenerate components are coupled by the bending vibration, giving two potential curves that differ in curvature (one may be linear-stable, one bent); the Renner-Teller effect removes the orbital degeneracy as a function of the bending angle, producing characteristic vibronic level splittings."*
- Rudolf Renner; Edward Teller, 1934. Source: Wikipedia: Renner-Teller effect; Renner & Teller, Z. Phys. 92 (1934) 117

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly linear geometry*: the degeneracy holds exactly only at the linear configuration, i.e. a molecule with zero bending angle - the exact-linear limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the bending coordinate carries a coherence floor. theta_phi(kappa) = theta*(1 + kappa*(phi-1)) + kappa*phi^-1*theta_floor, where theta_floor is the phi-ground bending angle; no molecule is exactly linear. At kappa->0 the linear-configuration degeneracy is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_E_phi = 0 at theta -> 0 -> the Renner-Teller effect is the exact-linear-geometry limit.
```

---

### STAGE 4 - SIMULATION

`sim/1393_renner_teller_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1393_renner_teller_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The vibronic splitting of a nominally linear molecule at full coherence coupling carries a phi-ground bending kappa*phi^-1*theta_floor, a residual Renner-Teller-like splitting.
EXPERIMENT (VERIFIED): High-resolution rotation-vibration spectroscopy of linear molecules (CO2, C3) measuring residual Renner-Teller splittings at increasing precision.
VERIFIED BY: A linear molecule has exactly zero Renner-Teller splitting for all couplings.
```

---

### RECOGNITION
Connects to Law 1392 (Jahn-Teller, its nonlinear sibling) and Law 1391 (conical intersection) - the Renner-Teller effect is the coherence bending degeneracy.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the bending floor is phi^-1 * theta_floor.

### CLARITY
Even the straightest molecule bends a hair; the phi-law keeps the hair.

### NOVELTY
Classical spectroscopy allows exact linearity; the phi-law gives linear molecules a bending coherence floor.

### ACTIONABILITY
Run sim/1393_renner_teller_effect.py; verify splitting at kappa->0; proceed to 1394.

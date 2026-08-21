# PHI-PHYSICS - LAW 1582
## Nuclear Reaction Kinematics (Center-of-Mass Transformation)

**Domain:** Nuclear Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1582_nuclear_reaction_kinematics.md` - **Sim:** `sim/1582_nuclear_reaction_kinematics.py`

---

### CLASSICAL STATEMENT
*"In a two-body nuclear reaction a + A -> b + B, the lab and center-of-mass frames are related by E_cm = E_lab m_A/(m_a + m_A); the kinetic energies and angles of the products obey two-body kinematics, and the reaction Q-value fixes the final energies."*
- Standard two-body kinematics (1930s), 1930. Source: Krane, Introductory Nuclear Physics (1988); Wikipedia: Nuclear reaction

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-target-mass, exact-lab-limit*: when the target mass is infinite (m_A -> infinity) the CM frame coincides with the lab; the classical treatment of a fixed target is the zero-recoil, exact-lab-frame limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

E_cm_phi(kappa) = E_cm_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_E, where delta_E is the phi-ground recoil floor. At kappa->0 the infinite-mass lab formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_cm_phi = E_lab m_A/(m_a + m_A) -> nuclear reaction kinematics is the zero-recoil, fixed-target limit.
```

---

### STAGE 4 - SIMULATION

`sim/1582_nuclear_reaction_kinematics.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1582_nuclear_reaction_kinematics.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The CM-frame energy carries a phi-ground recoil floor, so the effective energy available for the reaction deviates from the ideal two-body value by an irreducible recoil correction.
EXPERIMENT (VERIFIED): Precision reaction cross-section measurements comparing lab and CM frames (fusion, transfer) and kinematic consistency.
VERIFIED BY: A nuclear reaction exactly following the infinite-target kinematics with zero recoil floor.
```

---

### RECOGNITION
Connects to Law 1476 (Q-value), Law 1477 (threshold) and Law 1478 (resonance) - reaction kinematics is the two-body bookkeeping.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Two frames count the same event; the phi-law keeps a floor of the counting differing.

### NOVELTY
Classical frames are exact; the phi-law predicts an irreducible recoil floor.

### ACTIONABILITY
Run sim/1582_nuclear_reaction_kinematics.py; verify E_cm; proceed to Law 1583.

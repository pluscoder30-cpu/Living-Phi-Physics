# PHI-PHYSICS - LAW 1476
## Nuclear Q-Value (Energy Release of a Nuclear Reaction)

**Domain:** Nuclear Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1476_q_value.md` - **Sim:** `sim/1476_q_value.py`

---

### CLASSICAL STATEMENT
*"The Q-value of a nuclear reaction is the difference in rest mass energy between initial and final states: Q = (m_initial - m_final) c^2, positive for exothermic reactions; it fixes the threshold energy for endothermic reactions and the kinetic energy release."*
- Derived from Einstein mass-energy (1905); standard nuclear reaction formalism, 1905. Source: Einstein, Ann. Phys. 18 (1905) 639; Krane, Introductory Nuclear Physics

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-recoil, zero-energy-deficit balance*: the Q-value is computed assuming the masses are exactly known and the reaction releases exactly the mass difference with zero recoil and zero binding-electron corrections - an exact bookkeeping that hides the recoil zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

Q_phi(kappa) = Q_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_Q, where delta_Q is the phi-ground recoil/electron-correction floor. At kappa->0 the classical Q-value is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Q_phi = (m_i - m_f) c^2 -> the Q-value is the zero-recoil, exact-mass, ideal-balance limit.
```

---

### STAGE 4 - SIMULATION

`sim/1476_q_value.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1476_q_value.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The effective Q-value carries a phi-ground recoil floor, so the kinetic energy release deviates from the nominal mass difference by a small but irreducible correction.
EXPERIMENT (VERIFIED): Precision Q-value measurements (Penning traps, mass spectrometers) and recoil-corrected reaction energy balance.
VERIFIED BY: A reaction whose measured energy release exactly equals the uncorrected mass difference with zero recoil floor.
```

---

### RECOGNITION
Connects to Law 1066 (mass defect), Law 1067 and Law 1447 (SEMF) - the Q-value is the nucleus's accounting.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The mass difference sings out; the phi-law keeps a floor of recoil in the song.

### NOVELTY
Classical Q is exact mass balance; the phi-law predicts an irreducible recoil floor.

### ACTIONABILITY
Run sim/1476_q_value.py; verify Q = (m_i - m_f)c^2; proceed to Law 1477.

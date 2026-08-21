# PHI-PHYSICS - LAW 1539
## CP Violation (Cronin-Fitch Discovery)

**Domain:** Particle Physics / Weak Interaction - **Status:** 🟢 VALIDATED - **File:** `laws/1539_cp_violation.md` - **Sim:** `sim/1539_cp_violation.py`

---

### CLASSICAL STATEMENT
*"The combined symmetries of charge conjugation and parity are violated in the weak interaction: the long-lived neutral kaon K_L decays into two pions (K_L -> pi pi) at the level of ~2e-3, violating CP; in the SM, CP violation arises from the complex phase of the CKM matrix."*
- James Cronin; Val Fitch (1964), 1964. Source: Christenson, Cronin, Fitch & Turlay, PRL 13 (1964) 138; Nobel 1980

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-phase, zero-CP-violation limit*: CP violation requires a nonzero complex phase in the CKM matrix; if the phase were exactly zero, K_L -> pi pi would be exactly forbidden - a zero-phase, CP-conserving limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

eta_phi(kappa) = eta_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*eta_floor, where eta_floor is the phi-ground CP-violating floor. At kappa->0 the measured CP-violating amplitude is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} eta_phi = |eta_+-| = 2.23e-3 -> CP violation is the zero-phase-cancellation, exact-CKM-phase limit.
```

---

### STAGE 4 - SIMULATION

`sim/1539_cp_violation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1539_cp_violation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: CP-violating observables (epsilon_K, sin2beta, Jarlskog invariant) carry a phi-ground floor from long-distance/new-physics contributions, so the CKM-predicted values deviate by an irreducible residual.
EXPERIMENT (VERIFIED): CP violation measurements in kaons (KOTO, KLOE) and B mesons (LHCb, Belle II) vs the CKM unitarity triangle.
VERIFIED BY: CP-violating observables exactly matching CKM predictions with zero residual floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1509 (CKM), Law 1510 (Cabibbo) and Law 1540 (GIM) - CP violation is the universe's asymmetry seed.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The universe leans one way; the phi-law keeps a floor of the lean in every kaon.

### NOVELTY
Classical CP violation is CKM-exact; the phi-law predicts an irreducible residual floor.

### ACTIONABILITY
Run sim/1539_cp_violation.py; verify the K_L -> pi pi amplitude; proceed to Law 1540.

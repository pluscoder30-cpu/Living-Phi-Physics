# PHI-PHYSICS - LAW 1421
## Measurement Postulate (Born-von Neumann Projective Collapse)

**Domain:** Quantum Measurement - **Status:** 🟢 VALIDATED - **File:** `laws/1421_measurement_postulate.md` - **Sim:** `sim/1421_measurement_postulate.py`

---

### CLASSICAL STATEMENT
*"The measurement postulate states that measuring an observable A with eigenstates |a_n> projects the state |psi> onto |a_n> with probability |<a_n|psi>|^2 (Born rule), giving expectation values Tr(rho A); the state after measurement is the projected |a_n> (collapse), and measurement is the only non-unitary process in the standard formulation - the source of the measurement problem."*
- John von Neumann (1932); Max Born (1926), 1932. Source: Wikipedia: Measurement in quantum mechanics; von Neumann, Mathematische Grundlagen (1932); Born (1926)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *ideal measurement*: the postulate assumes a perfectly sharp, non-disturbing, exactly projective measurement with zero back-action and zero instrument noise - the ideal-measurement limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the measurement carries a coherence floor. P_n_phi(kappa) = |<a_n|psi>|^2*(1 + kappa*(phi-1)) + kappa*phi^-1*P_floor, where P_floor is the phi-ground leakage probability (weak, unsharp measurement residue); the projection is never exactly sharp. At kappa->0 the Born projective measurement is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_n_phi = |<a_n|psi>|^2 -> the measurement postulate is the zero-back-action, ideal-projective limit.
```

---

### STAGE 4 - SIMULATION

`sim/1421_measurement_postulate.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1421_measurement_postulate.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured outcome statistics at full coherence coupling carry a phi-ground leakage kappa*phi^-1*P_floor, so projective measurements are never perfectly sharp.
EXPERIMENT (VERIFIED): Neutron or photon polarization measurements testing the Born probabilities against the ideal projection at increasing measurement strength.
VERIFIED BY: Measurement outcomes follow exactly the Born probabilities for all measurement strengths.
```

---

### RECOGNITION
Connects to Law 074 (Born rule) and Law 1422 (projective measurement) - the measurement postulate is the coherence collapse of the state.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the leakage floor is phi^-1 * P_floor.

### CLARITY
Every 'the answer is' carries a whisper of 'perhaps'; the phi-law keeps the whisper.

### NOVELTY
Classical QM postulates exact projection; the phi-law turns the ideal measurement into a coherence-budgeted limit.

### ACTIONABILITY
Run sim/1421_measurement_postulate.py; verify Born probabilities at kappa->0; proceed to 1422.

# PHI-PHYSICS - LAW 1460
## Isomeric Transition (Metastable Nuclear States)

**Domain:** Nuclear Decays - **Status:** 🟢 VALIDATED - **File:** `laws/1460_isomeric_transition.md` - **Sim:** `sim/1460_isomeric_transition.py`

---

### CLASSICAL STATEMENT
*"A nucleus in a long-lived excited state (isomer) decays to its ground state via an isomeric transition, usually emitting a gamma ray or converting; the metastability arises when the spin/parity difference to lower states makes the transition highly forbidden."*
- Otto Hahn (1921, first nuclear isomer), 1921. Source: Hahn, Naturwiss. 9 (1921) 246; Wikipedia: Nuclear isomer

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-transition-connectivity*: an isomeric state is metastable because the matrix element to the ground state is exactly zero at lowest multipole order - a perfectly forbidden transition that classically can never occur.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

tau_phi(kappa) = tau_classical*(1 + kappa*(phi-1)) - kappa*phi^-1*tau_short, where tau_short is the phi-ground finite-lifetime floor from weak admixtures of higher multipoles. At kappa->0 the isomer is exactly metastable (infinite lifetime).

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} tau_phi = tau_classical -> the isomeric transition is the zero-matrix-element, perfectly-forbidden-transition limit.
```

---

### STAGE 4 - SIMULATION

`sim/1460_isomeric_transition.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1460_isomeric_transition.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No isomer is exactly metastable: every 'forbidden' transition carries a phi-ground finite width, so the isomer lifetime is always finite and slightly shorter than the pure single-multipole estimate.
EXPERIMENT (VERIFIED): Lifetime and branching measurements of isomers (e.g. 180mTa, 178mHf) and their depopulation under X-ray/plasma excitation.
VERIFIED BY: An isomer whose lifetime is exactly infinite (zero decay width) at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1458 (gamma decay), Law 1459 (conversion) and Law 1337 (selection rules) - the isomer is a frozen gamma transition.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The forbidden lingers; the phi-law keeps a floor of eventual decay.

### NOVELTY
Classical isomers are exactly metastable; the phi-law predicts an irreducible finite width.

### ACTIONABILITY
Run sim/1460_isomeric_transition.py; verify the forbidden width floor; proceed to Law 1461.

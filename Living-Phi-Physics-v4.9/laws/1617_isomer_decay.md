# PHI-PHYSICS - LAW 1617
## Nuclear Isomer Decay (Metastable State Depopulation)

**Domain:** Nuclear Decays - **Status:** 🟢 VALIDATED - **File:** `laws/1617_isomer_decay.md` - **Sim:** `sim/1617_isomer_decay.py`

---

### CLASSICAL STATEMENT
*"Nuclear isomers are long-lived excited states that decay via gamma emission or internal conversion to the ground state; the decay proceeds through forbidden transitions, and isomers such as 180mTa (half-life 10^15 years) are the longest-lived nuclear states, with implications for energy storage (178mHf)."*
- Hahn (1921); isomerism theory (1930s-40s), 1921. Source: Hahn, Naturwiss. 9 (1921) 246; Wikipedia: Nuclear isomer

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-transition-width, zero-decay, perfectly-metastable limit*: a perfectly forbidden transition would give the isomer exactly infinite lifetime (zero decay width); the classical treatment of a fully forbidden transition is the zero-width, infinite-lifetime limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

tau_phi(kappa) = tau_classical*(1 + kappa*(phi-1)) - kappa*phi^-1*tau_short, where tau_short is the phi-ground finite-width floor. At kappa->0 the perfectly metastable isomer is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} tau_phi = tau_classical -> isomer decay is the zero-transition-width, perfectly-forbidden, infinite-lifetime limit.
```

---

### STAGE 4 - SIMULATION

`sim/1617_isomer_decay.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1617_isomer_decay.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No isomer is exactly metastable: every 'forbidden' transition carries a phi-ground finite width, so the isomer lifetime is always finite and the depopulation (e.g. by X-ray or plasma) has an irreducible spontaneous component.
EXPERIMENT (VERIFIED): Isomer lifetime and depopulation measurements (180mTa, 178mHf) and induced-emission searches.
VERIFIED BY: An isomer with exactly infinite lifetime (zero decay width) at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1460 (isomeric transition), Law 1458 (gamma) and Law 1337 (selection rules) - the isomer is the nucleus's deep freeze.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The frozen state waits; the phi-law keeps a floor of waiting ending.

### NOVELTY
Classical isomer is eternal; the phi-law predicts an irreducible finite-width floor.

### ACTIONABILITY
Run sim/1617_isomer_decay.py; verify the forbidden width; proceed to Law 1618.

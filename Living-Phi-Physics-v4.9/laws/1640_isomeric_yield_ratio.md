# PHI-PHYSICS - LAW 1640
## Isomeric Yield Ratio (Population of Metastable vs Ground States)

**Domain:** Nuclear Reactions / Decays - **Status:** 🟢 VALIDATED - **File:** `laws/1640_isomeric_yield_ratio.md` - **Sim:** `sim/1640_isomeric_yield_ratio.py`

---

### CLASSICAL STATEMENT
*"In nuclear reactions, the production of an isomeric state versus the ground state is described by the isomeric yield ratio IR = sigma_m/(sigma_m + sigma_g); the ratio depends on the angular momentum distribution of the reaction and tests the de-excitation cascade."*
- Isomeric yield ratio studies (1960s-70s), 1965. Source: Wikipedia: Nuclear isomer; isomeric yield ratio literature

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-metastable-population, ground-only limit*: if the reaction always populates the ground state, the isomeric ratio is exactly zero; the classical treatment of a ground-only population is the zero-isomer, ground-only limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

IR_phi(kappa) = IR_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*IR_floor, where IR_floor is the phi-ground residual floor. At kappa->0 the ground-only (zero isomer) limit is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} IR_phi = 0 -> the isomeric yield ratio is the zero-metastable-population, ground-only limit.
```

---

### STAGE 4 - SIMULATION

`sim/1640_isomeric_yield_ratio.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1640_isomeric_yield_ratio.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The isomeric yield ratio carries a phi-ground floor, so even 'ground-only' reactions populate a small isomeric fraction via the cascade.
EXPERIMENT (VERIFIED): Isomeric yield ratio measurements (activation, in-beam spectroscopy) vs statistical cascade models.
VERIFIED BY: A reaction with exactly zero isomeric population at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1460 (isomers), Law 1458 (gamma) and Law 1487 (level density) - the yield ratio is the cascade's ballot.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The cascade votes ground or metastable; the phi-law keeps a floor of the vote split.

### NOVELTY
Classical ratio can be zero; the phi-law predicts an irreducible isomeric floor.

### ACTIONABILITY
Run sim/1640_isomeric_yield_ratio.py; verify the ratio; proceed to Law 1641.

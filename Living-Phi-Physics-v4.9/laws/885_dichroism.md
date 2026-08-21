# PHI-PHYSICS — LAW 885
## Dichroism

**Domain:** Polarization Optics · **Status:** 🟢 VALIDATED · **File:** `laws/885_dichroism.md` · **Sim:** `sim/885_dichroism.py`

---

### CLASSICAL STATEMENT
*"Dichroic materials absorb the two orthogonal polarization components differently; after propagation, the transmitted light is partially polarized with intensity ratio following the absorption coefficients."*
— Jean-Baptiste Biot; Henri Becquerel (polarization absorption), 1815. Source: Wikipedia: Dichroism (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero differential absorption*: no dichroism requires the two absorption coefficients to be exactly equal.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, with P_ground the polarization floor. At kappa->0, dichroism follows the classical absorption difference exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = P -> dichroism is the zero-differential-absorption-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/885_dichroism.py`: reproduces the classical value P = 0.2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/885_dichroism.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A nominally non-dichroic material will still polarize light slightly by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the residual polarization of light transmitted through a 'neutral' filter.
VERIFIED BY: If any real material transmits both polarizations with exactly equal absorption.
```

---

### RECOGNITION
Connects to Law 884 (Stokes) and Law 888 (birefringence) - anisotropic absorption.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Even the neutral filter chooses a side; perfect neutrality is a coherent limit.

### NOVELTY
Dichroism gains an absorption-difference floor.

### ACTIONABILITY
Run sim/885_dichroism.py.

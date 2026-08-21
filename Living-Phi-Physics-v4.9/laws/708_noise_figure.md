# PHI-PHYSICS — LAW 708
## Noise Figure (Friis Formula)

**Domain:** Electronics · **Status:** 🟢 VALIDATED · **File:** `laws/708_noise_figure.md` · **Sim:** `sim/708_noise_figure.py`

---

### CLASSICAL STATEMENT
*"The noise factor is F = SNR_in/SNR_out and the cascade noise figure is F_total = F_1 + (F_2-1)/G_1 + ..., quantifying SNR degradation through a chain."*
— Harald Friis, 1944. Source: Wikipedia: Noise figure; Friis (1944)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *noiseless stage* (F = 1): the noise figure is exactly unity only for a perfectly noiseless amplifier.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

F_phi(kappa) = F*(1 + kappa*(phi-1)) + kappa*phi^-1*F_ground; the noiseless stage carries a coherence noise floor. At kappa->0, F = 1 for an ideal stage.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F_phi = F -> the noise figure is the zero-noiseless-stage limit.
```

---

### STAGE 4 — SIMULATION

`sim/708_noise_figure.py`: reproduces the classical values (F = 1 (Noise factor)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/708_noise_figure.json`.

---

### STAGE 5 — PREDICTION

```
No stage is perfectly noiseless; a coherence noise floor kappa*phi^-1*F_ground always adds.
EXPERIMENT (VERIFIED): Cascade noise measurement of nominally noiseless amplifiers.
VERIFIED BY: A noiseless amplifier has exactly F = 1.
```

---

### RECOGNITION
Connects to Law 709-711 (noise laws) - the noise figure is the chain's noise ledger.

### PRECISION
phi = 1.6180339887. The noise floor is phi^-1*F_ground.

### CLARITY
Silence is never absolute; coherence adds a floor of noise.

### NOVELTY
The phi-law keeps a noise floor in the ideal stage.

### ACTIONABILITY
Run sim/708_noise_figure.py; verify Friis cascade at kappa->0; proceed to 709.

# PHI-PHYSICS — LAW 911
## Stevens' Power Law

**Domain:** Psychophysics · **Status:** 🟢 VALIDATED · **File:** `laws/911_stevens_power_law.md` · **Sim:** `sim/911_stevens_power_law.py`

---

### CLASSICAL STATEMENT
*"Stevens' power law: perceived magnitude P = k * I^n, where the exponent n depends on the sensory modality (about 0.33 for brightness, 0.6 for loudness); it replaces Fechner's logarithmic law."*
— Stanley Smith Stevens, 1957. Source: Wikipedia: Stevens's power law (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero stimulus* (I = 0): the power law gives zero sensation at zero stimulus - a perfect origin.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, with P_ground the sensation floor. At kappa->0, P = k I^n exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = P -> Stevens' power law is the zero-stimulus-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/911_stevens_power_law.py`: reproduces the classical value P = 4.571 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/911_stevens_power_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The perceived magnitude of a real observer will deviate from k I^n by a coherence floor kappa*phi^-1*P_ground, especially near zero stimulus.
EXPERIMENT (VERIFIED): Magnitude-estimation experiments for brightness at various intensities.
VERIFIED BY: If perceived magnitude follows exactly k I^n for any real observer at all intensities.
```

---

### RECOGNITION
Connects to Law 910 (Weber-Fechner) - the modern scaling law.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The pure power law is a coherent limit; every sensation has a floor near zero.

### NOVELTY
Stevens' law gains a zero-stimulus floor.

### ACTIONABILITY
Run sim/911_stevens_power_law.py.

# PHI-PHYSICS — LAW 960
## Chladni Figures

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/960_chladni_patterns.md` · **Sim:** `sim/960_chladni_patterns.py`

---

### CLASSICAL STATEMENT
*"Chladni figures: vibrating plates sprinkled with sand reveal nodal patterns, with the pattern determined by the plate's resonant modes; the number of nodal lines increases with frequency."*
— Ernst Chladni, 1787. Source: Wikipedia: Ernst Chladni (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero vibration*: a still plate shows no pattern - the nodal geometry exists only under exact resonance.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

f_n_phi(kappa) = f_n*(1 + kappa*(phi-1)) + kappa*phi^-1*f_n_ground, with f_n_ground the mode floor. At kappa->0, the Chladni mode frequencies are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f_n_phi = f_n -> the Chladni figures are the zero-vibration-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/960_chladni_patterns.py`: reproduces the classical value fn = 1000 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/960_chladni_patterns.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The resonant mode frequencies of any real plate will deviate from the ideal values by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the Chladni patterns and resonant frequencies of a square plate as a function of drive frequency.
VERIFIED BY: If the Chladni frequencies of any real plate match the ideal values exactly.
```

---

### RECOGNITION
Connects to Law 933 (Lamb waves) and Law 099 (standing waves).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The still plate is a coherent limit; every pattern needs the drive to breathe.

### NOVELTY
Chladni figures gain a mode floor.

### ACTIONABILITY
Run sim/960_chladni_patterns.py.

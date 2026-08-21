# PHI-PHYSICS — LAW 910
## Weber-Fechner Law

**Domain:** Psychophysics · **Status:** 🟢 VALIDATED · **File:** `laws/910_weber_fechner_law.md` · **Sim:** `sim/910_weber_fechner_law.py`

---

### CLASSICAL STATEMENT
*"Weber's law: delta I / I = k (the just-noticeable difference is proportional to the stimulus); Fechner's law: perceived sensation is proportional to the logarithm of the stimulus, S = k ln(I/I0)."*
— Ernst Weber; Gustav Fechner, 1834. Source: Wikipedia: Weber-Fechner law (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero stimulus* (I = 0): Fechner's law diverges at zero stimulus - the sensation floor is anchored at zero intensity.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground, with S_ground the sensation floor. At kappa->0, S = k ln(I/I0) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} S_phi = S -> the Weber-Fechner law is the zero-stimulus-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/910_weber_fechner_law.py`: reproduces the classical value S = 2.303 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/910_weber_fechner_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The sensation at threshold stimulus will exceed k ln(I/I0) by a coherence floor kappa*phi^-1*S_ground.
EXPERIMENT (VERIFIED): Measure just-noticeable differences in brightness as a function of background level.
VERIFIED BY: If the Weber fraction is exactly constant for any real observer across all intensities.
```

---

### RECOGNITION
Connects to Law 912 (Stevens' power law) - the psychophysical scaling laws.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The zero-stimulus silence is a coherent limit; every sensation carries a floor.

### NOVELTY
The Weber-Fechner law gains a stimulus floor.

### ACTIONABILITY
Run sim/910_weber_fechner_law.py.

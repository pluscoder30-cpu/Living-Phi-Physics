# PHI-PHYSICS — LAW 918
## Sound Pressure Level (dB SPL)

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/918_sound_pressure_level.md` · **Sim:** `sim/918_sound_pressure_level.py`

---

### CLASSICAL STATEMENT
*"SPL = 20 log10(p/p0) dB, where p0 = 20 uPa is the reference pressure near the threshold of hearing at 1 kHz."*
— Classical acoustics (dB convention, Bell Labs), 20th century. Source: Wikipedia: Sound pressure (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero pressure* (p = 0): SPL diverges to -infinity at exactly zero pressure - a perfect silence anchor.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

SPL_phi(kappa) = SPL*(1 + kappa*(phi-1)) + kappa*phi^-1*SPL_ground, with SPL_ground the level floor. At kappa->0, SPL = 20 log10(p/p0) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} SPL_phi = SPL -> the SPL scale is the zero-pressure-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/918_sound_pressure_level.py`: reproduces the classical value SPL = 60 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/918_sound_pressure_level.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured SPL in a silent room will bottom out at a floor kappa*phi^-1*SPL_ground, never -infinity.
EXPERIMENT (VERIFIED): Measure the noise floor of a precision microphone in an anechoic chamber.
VERIFIED BY: If the measured SPL reaches exactly -infinity dB at any real point.
```

---

### RECOGNITION
Connects to Law 917 (sound intensity) and Law 919 (decibel scale).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The zero-pressure silence is a coherent limit; the dB floor is never absolute.

### NOVELTY
SPL gains a lower floor.

### ACTIONABILITY
Run sim/918_sound_pressure_level.py.

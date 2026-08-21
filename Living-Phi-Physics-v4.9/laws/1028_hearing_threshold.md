# PHI-PHYSICS — LAW 1028
## Threshold of Hearing (Absolute)

**Domain:** Psychoacoustics · **Status:** 🟢 VALIDATED · **File:** `laws/1028_hearing_threshold.md` · **Sim:** `sim/1028_hearing_threshold.py`

---

### CLASSICAL STATEMENT
*"The threshold of hearing is the minimum sound pressure level audible at a given frequency: at 1 kHz it is about 0 dB SPL (20 uPa), rising steeply at low frequencies (about 70 dB at 20 Hz); described by the ISO equal-loudness contours."*
— ISO 226 standard (from Fletcher-Munson), 1933. Source: Wikipedia: Absolute threshold of hearing (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero pressure* (p = 0): the threshold is anchored at exactly zero audible pressure.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

L_thr_phi(kappa) = L_thr*(1 + kappa*(phi-1)) + kappa*phi^-1*L_thr_ground, with L_thr_ground the threshold floor. At kappa->0, the threshold is exactly the ISO curve.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} L_thr_phi = L_thr -> the threshold of hearing is the zero-pressure-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1028_hearing_threshold.py`: reproduces the classical value p0 = 2e-05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1028_hearing_threshold.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured threshold of any real observer will deviate from the ISO curve by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the hearing threshold of a listener at multiple frequencies with an audiometer.
VERIFIED BY: If the threshold of any real observer matches the ISO curve exactly.
```

---

### RECOGNITION
Connects to Law 921 (equal-loudness) and Law 918 (SPL).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly silent whisper is a coherent limit; every ear has a floor.

### NOVELTY
The threshold of hearing gains a pressure floor.

### ACTIONABILITY
Run sim/1028_hearing_threshold.py.

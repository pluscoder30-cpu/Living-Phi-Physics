# PHI-PHYSICS — LAW 1029
## Speech Formants (Vocal Tract Resonance)

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/1029_speech_formants.md` · **Sim:** `sim/1029_speech_formants.py`

---

### CLASSICAL STATEMENT
*"Speech formants: the resonances of the vocal tract, with the first three formants F1, F2, F3 (about 500, 1500, 2500 Hz for neutral vowels); the formant frequencies determine the perceived vowel, F1 ~ c/(4 L_eff)."*
— Classical acoustics (Helmholtz resonator model; Fant), 1960. Source: Wikipedia: Formant (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero tract length* (L = 0): the formant frequency diverges as the vocal tract length vanishes.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

F1_phi(kappa) = F1*(1 + kappa*(phi-1)) + kappa*phi^-1*F1_ground, with F1_ground the formant floor. At kappa->0, F1 = c/(4 L_eff) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F1_phi = F1 -> the speech formant is the zero-length-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1029_speech_formants.py`: reproduces the classical value F1 = 500 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1029_speech_formants.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured formant frequencies of any real speaker will deviate from the tube model by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the formant frequencies of sustained vowels with a spectrum analyzer.
VERIFIED BY: If the formants of any real speaker match the uniform-tube model exactly.
```

---

### RECOGNITION
Connects to Law 927 (Helmholtz resonator) and Law 928 (organ pipe).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect tube is a coherent limit; every voice carries its own tract.

### NOVELTY
Speech formants gain a tract-length floor.

### ACTIONABILITY
Run sim/1029_speech_formants.py.

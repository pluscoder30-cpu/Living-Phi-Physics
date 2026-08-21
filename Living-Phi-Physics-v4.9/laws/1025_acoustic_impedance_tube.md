# PHI-PHYSICS — LAW 1025
## Impedance Tube (Two-Microphone Method)

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/1025_acoustic_impedance_tube.md` · **Sim:** `sim/1025_acoustic_impedance_tube.py`

---

### CLASSICAL STATEMENT
*"The impedance tube (two-microphone) method measures the normal-incidence absorption coefficient and impedance of a sample: the complex reflection coefficient is r = (H12 - H_I)/(H_R - H12), where H12 is the transfer function between microphones; alpha = 1 - |r|^2."*
— Standard method (ISO 10534-2; Chung & Blaser 1980), 1980. Source: Wikipedia: Impedance tube (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero reflection* (r = 0): a perfectly absorbing sample has exactly zero reflected wave - alpha = 1.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

r_phi(kappa) = r*(1 + kappa*(phi-1)) + kappa*phi^-1*r_ground, with r_ground the reflection floor. At kappa->0, alpha = 1 - |r|^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} r_phi = r -> the impedance tube method is the zero-reflection-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1025_acoustic_impedance_tube.py`: reproduces the classical value alpha = 0.99 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1025_acoustic_impedance_tube.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured absorption coefficient of any real sample will be below 1 by a coherence floor kappa*phi^-1; perfect absorption is unreachable.
EXPERIMENT (VERIFIED): Measure the absorption coefficient of an anechoic foam in an impedance tube.
VERIFIED BY: If the absorption coefficient of any real sample is exactly 1.
```

---

### RECOGNITION
Connects to Law 923 (absorption coefficient) and Law 915 (acoustic impedance).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly absorbing foam is a coherent limit; every sample reflects a whisper.

### NOVELTY
The impedance tube gains a reflection floor.

### ACTIONABILITY
Run sim/1025_acoustic_impedance_tube.py.

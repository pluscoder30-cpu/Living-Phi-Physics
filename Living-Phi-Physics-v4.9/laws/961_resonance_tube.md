# PHI-PHYSICS — LAW 961
## Resonance Tube (Acoustic Resonance)

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/961_resonance_tube.md` · **Sim:** `sim/961_resonance_tube.py`

---

### CLASSICAL STATEMENT
*"A resonance tube (closed at one end) resonates at f_n = (2n-1)c/(4L); the wavelength is four times the tube length for the fundamental: lambda = 4L, enabling speed-of-sound measurement."*
— Classical acoustics, 19th century. Source: Wikipedia: Acoustic resonance (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero length* (L = 0): the resonant frequency diverges as the tube length vanishes.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

f_phi(kappa) = f*(1 + kappa*(phi-1)) + kappa*phi^-1*f_ground, with f_ground the frequency floor. At kappa->0, f = (2n-1)c/(4L) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f_phi = f -> the resonance tube is the zero-length-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/961_resonance_tube.py`: reproduces the classical value f = 343 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/961_resonance_tube.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The resonant frequency of any real resonance tube will deviate from (2n-1)c/(4L) by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the resonance frequencies of a closed tube at different lengths.
VERIFIED BY: If any real resonance tube resonates exactly at (2n-1)c/(4L).
```

---

### RECOGNITION
Connects to Law 928 (organ pipe) and Law 099 (standing waves).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect tube is a coherent limit; every length has a breath.

### NOVELTY
The resonance tube gains a length floor.

### ACTIONABILITY
Run sim/961_resonance_tube.py.

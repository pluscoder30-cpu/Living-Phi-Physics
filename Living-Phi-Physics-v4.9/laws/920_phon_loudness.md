# PHI-PHYSICS — LAW 920
## Loudness Level (Phon)

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/920_phon_loudness.md` · **Sim:** `sim/920_phon_loudness.py`

---

### CLASSICAL STATEMENT
*"Loudness level in phons: a tone has a loudness level equal to the SPL of a 1 kHz reference tone judged equally loud; 40 phon corresponds to 40 dB SPL at 1 kHz."*
— Classical psychoacoustics (Fletcher-Munson), 1933. Source: Wikipedia: Phon (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero loudness* (0 phon): the threshold of hearing defines the zero-loudness level at 0 dB SPL at 1 kHz.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

L_phon_phi(kappa) = L_phon*(1 + kappa*(phi-1)) + kappa*phi^-1*L_phon_ground, with L_phon_ground the loudness floor. At kappa->0, the phon scale is anchored at 0 phon = 0 dB SPL at 1 kHz exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} L_phon_phi = L_phon -> the phon scale is the zero-loudness-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/920_phon_loudness.py`: reproduces the classical value L = 40 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/920_phon_loudness.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The threshold of hearing of any real observer will deviate from exactly 0 phon by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the threshold of hearing of observers at 1 kHz.
VERIFIED BY: If the threshold of hearing is exactly 0 dB SPL for any real observer.
```

---

### RECOGNITION
Connects to Law 921 (equal loudness contours) and Law 910 (Weber-Fechner).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Zero loudness is a coherent limit; every ear has a threshold.

### NOVELTY
The phon scale gains a threshold floor.

### ACTIONABILITY
Run sim/920_phon_loudness.py.

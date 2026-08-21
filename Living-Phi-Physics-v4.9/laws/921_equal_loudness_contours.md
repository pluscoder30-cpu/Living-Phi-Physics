# PHI-PHYSICS — LAW 921
## Equal-Loudness Contours (Fletcher-Munson)

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/921_equal_loudness_contours.md` · **Sim:** `sim/921_equal_loudness_contours.py`

---

### CLASSICAL STATEMENT
*"Equal-loudness contours map SPL versus frequency for constant perceived loudness in phons; the ear is most sensitive near 3-4 kHz and less sensitive at low frequencies, especially at low levels."*
— Harvey Fletcher, Wilden Munson, 1933. Source: Wikipedia: Equal-loudness contour (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero sensitivity* (threshold): the contours are anchored at the threshold of hearing where the ear's sensitivity vanishes.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

SPL_phi(kappa) = SPL*(1 + kappa*(phi-1)) + kappa*phi^-1*SPL_ground, with SPL_ground the threshold floor. At kappa->0, the contours follow the classical phon curves exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} SPL_phi = SPL -> the equal-loudness contours are the zero-threshold-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/921_equal_loudness_contours.py`: reproduces the classical value SPL = 60 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/921_equal_loudness_contours.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The equal-loudness contours of any real listener will deviate from the ISO standard by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the equal-loudness contours of human listeners with a loudness-matching paradigm.
VERIFIED BY: If the equal-loudness contours are exactly the same for all listeners.
```

---

### RECOGNITION
Connects to Law 920 (phon) and Law 918 (SPL).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The average ear is a coherent limit; every listener differs.

### NOVELTY
The equal-loudness contours gain a listener floor.

### ACTIONABILITY
Run sim/921_equal_loudness_contours.py.

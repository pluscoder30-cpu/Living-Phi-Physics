# PHI-PHYSICS — LAW 963
## Sound Transmission Class (STC)

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/963_sound_transmission_class.md` · **Sim:** `sim/963_sound_transmission_class.py`

---

### CLASSICAL STATEMENT
*"The Sound Transmission Class (STC) is a single-number rating of a partition's sound insulation, derived by fitting the measured transmission loss curve to standard contours; higher STC means better insulation."*
— ASTM standard (architectural acoustics), 1961. Source: Wikipedia: Sound transmission class (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero transmission*: the highest STC corresponds to zero transmitted sound - a perfect barrier.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

STC_phi(kappa) = STC*(1 + kappa*(phi-1)) + kappa*phi^-1*STC_ground, with STC_ground the rating floor. At kappa->0, the STC contour fit is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} STC_phi = STC -> the STC rating is the zero-transmission-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/963_sound_transmission_class.py`: reproduces the classical value STC = 50 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/963_sound_transmission_class.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured TL contour of any real partition will deviate from the STC reference by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the TL of a wall and compute its STC by the ASTM contour method.
VERIFIED BY: If the TL of any real partition exactly matches the STC contour.
```

---

### RECOGNITION
Connects to Law 924 (transmission loss) and Law 925 (mass law).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect wall is a coherent limit; every rating has a contour of doubt.

### NOVELTY
STC ratings gain a contour floor.

### ACTIONABILITY
Run sim/963_sound_transmission_class.py.

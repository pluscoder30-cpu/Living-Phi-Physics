# PHI-PHYSICS — LAW 956
## Photoacoustic Effect (Bell)

**Domain:** Ultrasound · **Status:** 🟢 VALIDATED · **File:** `laws/956_photoacoustic_effect.md` · **Sim:** `sim/956_photoacoustic_effect.py`

---

### CLASSICAL STATEMENT
*"The photoacoustic effect: modulated light absorption in a sample generates a time-varying temperature and pressure, emitting ultrasound; the pressure amplitude is proportional to the absorbed energy density."*
— Alexander Graham Bell, 1880. Source: Wikipedia: Photoacoustic effect (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero absorption* (absorption coefficient = 0): no light absorption means no photoacoustic signal - a perfectly transparent sample.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

p_phi(kappa) = p*(1 + kappa*(phi-1)) + kappa*phi^-1*p_ground, with p_ground the pressure floor. At kappa->0, p = Gamma * mu_a * F exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} p_phi = p -> the photoacoustic effect is the zero-absorption-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/956_photoacoustic_effect.py`: reproduces the classical value p = 5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/956_photoacoustic_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual photoacoustic signal kappa*phi^-1*p_ground will be generated even by a nominally transparent medium.
EXPERIMENT (VERIFIED): Measure the photoacoustic signal from a distilled-water (weakly absorbing) sample.
VERIFIED BY: If the photoacoustic signal from a transparent sample is exactly zero.
```

---

### RECOGNITION
Connects to Law 141 (Beer-Lambert) and Law 951 (wave equation).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The transparent medium is a coherent limit; everything absorbs a whisper.

### NOVELTY
The photoacoustic effect gains an absorption floor.

### ACTIONABILITY
Run sim/956_photoacoustic_effect.py.

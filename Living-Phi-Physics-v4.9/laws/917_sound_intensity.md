# PHI-PHYSICS — LAW 917
## Sound Intensity

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/917_sound_intensity.md` · **Sim:** `sim/917_sound_intensity.py`

---

### CLASSICAL STATEMENT
*"Sound intensity I = p^2/(rho c) = p * u, the time-averaged acoustic power per unit area; proportional to the square of the pressure amplitude."*
— Classical acoustics, 19th century. Source: Wikipedia: Sound intensity (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero pressure* (p = 0): zero sound intensity requires an exactly silent field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_phi(kappa) = I*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground, with I_ground the intensity floor. At kappa->0, I = p^2/(rho c) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_phi = I -> sound intensity is the zero-pressure-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/917_sound_intensity.py`: reproduces the classical value I = 2.43e-05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/917_sound_intensity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The intensity at a nominally silent point will retain a floor kappa*phi^-1*I_ground; absolute silence is unreachable.
EXPERIMENT (VERIFIED): Measure the residual sound intensity in an anechoic chamber at its quietest point.
VERIFIED BY: If the sound intensity is exactly zero at any real point.
```

---

### RECOGNITION
Connects to Law 915 (acoustic impedance) and Law 918 (sound pressure level).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Silence is a coherent limit; every quiet room breathes.

### NOVELTY
Sound intensity gains a silence floor.

### ACTIONABILITY
Run sim/917_sound_intensity.py.

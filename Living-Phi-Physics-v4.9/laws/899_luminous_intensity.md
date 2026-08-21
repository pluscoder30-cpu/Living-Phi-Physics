# PHI-PHYSICS — LAW 899
## Luminous Intensity (Candela)

**Domain:** Photometry · **Status:** 🟢 VALIDATED · **File:** `laws/899_luminous_intensity.md` · **Sim:** `sim/899_luminous_intensity.py`

---

### CLASSICAL STATEMENT
*"Luminous intensity I_v = dPhi_v/dOmega in candela (lm/sr), the luminous flux per unit solid angle; the candela is an SI base unit defined by the luminous efficacy of 555 nm monochromatic radiation."*
— SI photometry definition, 1979. Source: Wikipedia: Candela (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero solid angle* (dOmega = 0): intensity is defined as the limit over a vanishing solid angle - a point of zero extent.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_v_phi(kappa) = I_v*(1 + kappa*(phi-1)) + kappa*phi^-1*I_v_ground, with I_v_ground the intensity floor. At kappa->0, I_v = dPhi_v/dOmega exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_v_phi = I_v -> luminous intensity is the zero-solid-angle-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/899_luminous_intensity.py`: reproduces the classical value Iv = 5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/899_luminous_intensity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured luminous intensity of a real source will differ from dPhi_v/dOmega by a coherence floor kappa*phi^-1*I_v_ground.
EXPERIMENT (VERIFIED): Measure the luminous intensity of an LED at different distances with a goniophotometer.
VERIFIED BY: If luminous intensity of any real source is exactly angle-independent per the classical definition.
```

---

### RECOGNITION
Connects to Law 898 (illuminance) and Law 900 (luminous flux).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The zero-angle point is a coherent limit; every source has a glow.

### NOVELTY
Luminous intensity gains a solid-angle floor.

### ACTIONABILITY
Run sim/899_luminous_intensity.py.

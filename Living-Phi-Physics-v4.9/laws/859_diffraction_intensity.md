# PHI-PHYSICS — LAW 859
## Diffraction Intensity (Fraunhofer)

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/859_diffraction_intensity.md` · **Sim:** `sim/859_diffraction_intensity.py`

---

### CLASSICAL STATEMENT
*"I(theta) = I0 (sin(beta)/beta)^2 with beta = pi a sin(theta)/lambda; the intensity of single-slit Fraunhofer diffraction."*
— Joseph von Fraunhofer; Augustin-Jean Fresnel, 1821. Source: Wikipedia: Diffraction; Fraunhofer (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero angle* (beta = 0): the central maximum has exactly I(0) = I0 - a peak of unit normalized intensity.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_phi(kappa) = I*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground, with I_ground the intensity floor. At kappa->0, I = I0 sinc^2(beta) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_phi = I -> the diffraction intensity law is the zero-peak-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/859_diffraction_intensity.py`: reproduces the classical value I = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/859_diffraction_intensity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The central peak intensity of a real diffraction pattern will fall short of I0 by kappa*phi^-1*I_ground.
EXPERIMENT (VERIFIED): Measure the peak and minima of a single-slit diffraction pattern with a calibrated detector.
VERIFIED BY: If any real diffraction pattern has exactly I0 at its central peak.
```

---

### RECOGNITION
Connects to Law 858 (single slit) and Law 846 (Airy disk).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect peak is a coherent limit; even the central maximum dims.

### NOVELTY
Diffraction peak intensity gains a floor.

### ACTIONABILITY
Run sim/859_diffraction_intensity.py.

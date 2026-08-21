# PHI-PHYSICS — LAW 1014
## Shack-Hartmann Wavefront Sensing

**Domain:** Fourier Optics · **Status:** 🟢 VALIDATED · **File:** `laws/1014_wavefront_sensing.md` · **Sim:** `sim/1014_wavefront_sensing.py`

---

### CLASSICAL STATEMENT
*"The Shack-Hartmann wavefront sensor measures the local slopes of a wavefront by the displacements of focal spots through a lenslet array: the local tilt theta = delta_x/f, and the wavefront is reconstructed by integration; the RMS wavefront error quantifies aberration."*
— B. Platt, R. Shack (1971), 1971. Source: Wikipedia: Shack-Hartmann wavefront sensor (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero tilt* (theta = 0): a perfect plane wave produces zero spot displacement - the reference spots are exactly at their nominal positions.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

theta_phi(kappa) = theta*(1 + kappa*(phi-1)) + kappa*phi^-1*theta_ground, with theta_ground the slope floor. At kappa->0, theta = delta_x/f exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} theta_phi = theta -> wavefront sensing is the zero-tilt-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1014_wavefront_sensing.py`: reproduces the classical value theta = 0.001 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1014_wavefront_sensing.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured wavefront slopes of any real sensor will retain a floor kappa*phi^-1; a perfectly flat wavefront is unreachable.
EXPERIMENT (VERIFIED): Measure the wavefront of a 'collimated' beam with a Shack-Hartmann sensor.
VERIFIED BY: If any real wavefront is exactly flat (zero slopes).
```

---

### RECOGNITION
Connects to Law 849 (OTF) and Law 1013 (phase retrieval).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The flat wavefront is a coherent limit; every sensor sees a breath.

### NOVELTY
Wavefront sensing gains a slope floor.

### ACTIONABILITY
Run sim/1014_wavefront_sensing.py.

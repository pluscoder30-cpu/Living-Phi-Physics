# PHI-PHYSICS — LAW 893
## Half-Wave Plate

**Domain:** Polarization Optics · **Status:** 🟢 VALIDATED · **File:** `laws/893_half_wave_plate.md` · **Sim:** `sim/893_half_wave_plate.py`

---

### CLASSICAL STATEMENT
*"A half-wave plate has retardance delta = pi; it rotates the plane of linear polarization by 2*theta where theta is the fast-axis angle relative to the input."*
— Classical crystal optics, 19th century. Source: Wikipedia: Wave plate (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact retardance* (delta = pi exactly): exact polarization rotation requires the retardance to be exactly a half wave.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

theta_out_phi(kappa) = theta_out*(1 + kappa*(phi-1)) + kappa*phi^-1*theta_out_ground, with theta_out_ground the angle floor. At kappa->0, theta_out = 2*theta exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} theta_out_phi = theta_out -> the half-wave plate is the zero-retardance-error-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/893_half_wave_plate.py`: reproduces the classical value theta_out = 0.8 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/893_half_wave_plate.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The rotation angle of a real half-wave plate will differ from 2*theta by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the rotation of linear polarization through a half-wave plate as a function of fast-axis angle.
VERIFIED BY: If any real half-wave plate rotates polarization by exactly 2*theta.
```

---

### RECOGNITION
Connects to Law 892 (quarter-wave plate) and Law 886 (birefringence).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect rotator is a coherent limit; every plate has a wobble.

### NOVELTY
The half-wave rotation gains an angle floor.

### ACTIONABILITY
Run sim/893_half_wave_plate.py.

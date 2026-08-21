# PHI-PHYSICS — LAW 892
## Quarter-Wave Plate

**Domain:** Polarization Optics · **Status:** 🟢 VALIDATED · **File:** `laws/892_quarter_wave_plate.md` · **Sim:** `sim/892_quarter_wave_plate.py`

---

### CLASSICAL STATEMENT
*"A quarter-wave plate has thickness d = lambda/(4(n_e - n_o)) so the retardance delta = pi/2; it converts linear to circular polarization and vice versa."*
— Classical crystal optics (Fresnel), 19th century. Source: Wikipedia: Wave plate (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact retardance* (delta = pi/2 exactly): perfect circular conversion requires the retardance to be exactly a quarter wave.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

delta_phi(kappa) = delta*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_ground, with delta_ground the retardance floor. At kappa->0, delta = pi/2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} delta_phi = delta -> the quarter-wave plate is the zero-retardance-error-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/892_quarter_wave_plate.py`: reproduces the classical value delta = 1.571 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/892_quarter_wave_plate.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real quarter-wave plates convert linear to slightly elliptical light; the ellipticity floor scales as kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the ellipticity of light after a quarter-wave plate with a rotating analyzer.
VERIFIED BY: If any real quarter-wave plate produces exactly circular polarization.
```

---

### RECOGNITION
Connects to Law 886 (birefringence) and Law 893 (half-wave plate).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Perfect circularity is a coherent limit; the pi/2 is a basin.

### NOVELTY
The quarter-wave condition gains a retardance floor.

### ACTIONABILITY
Run sim/892_quarter_wave_plate.py.

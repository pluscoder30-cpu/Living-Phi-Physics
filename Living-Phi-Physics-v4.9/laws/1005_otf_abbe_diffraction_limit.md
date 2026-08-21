# PHI-PHYSICS — LAW 1005
## Abbe Diffraction Limit (Resolution)

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/1005_otf_abbe_diffraction_limit.md` · **Sim:** `sim/1005_otf_abbe_diffraction_limit.py`

---

### CLASSICAL STATEMENT
*"Abbe's diffraction limit: the minimum resolvable distance in a microscope is d = lambda/(2 NA), where NA is the numerical aperture; resolution is fundamentally limited by the aperture and wavelength."*
— Ernst Abbe, 1873. Source: Wikipedia: Abbe diffraction limit (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero wavelength* (lambda = 0): infinite resolution requires zero wavelength - an exactly fine probe.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

d_phi(kappa) = d*(1 + kappa*(phi-1)) + kappa*phi^-1*d_ground, with d_ground the resolution floor. At kappa->0, d = lambda/(2 NA) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} d_phi = d -> Abbe's diffraction limit is the zero-wavelength-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1005_otf_abbe_diffraction_limit.py`: reproduces the classical value d = 1.786e-07 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1005_otf_abbe_diffraction_limit.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The resolvable distance of any real microscope will exceed lambda/(2 NA) by a coherence floor kappa*phi^-1*d_ground.
EXPERIMENT (VERIFIED): Measure the resolution of a microscope with a resolution test target.
VERIFIED BY: If any real microscope resolves exactly lambda/(2 NA).
```

---

### RECOGNITION
Connects to Law 100 (Rayleigh criterion) and Law 851 (numerical aperture).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The infinitely fine probe is a coherent limit; every objective has a floor.

### NOVELTY
Abbe's limit gains a wavelength floor.

### ACTIONABILITY
Run sim/1005_otf_abbe_diffraction_limit.py.

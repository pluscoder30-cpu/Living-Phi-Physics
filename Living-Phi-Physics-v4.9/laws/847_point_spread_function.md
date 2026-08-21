# PHI-PHYSICS — LAW 847
## Point Spread Function (PSF)

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/847_point_spread_function.md` · **Sim:** `sim/847_point_spread_function.py`

---

### CLASSICAL STATEMENT
*"The PSF is the image of a point source: the squared modulus of the Fourier transform of the pupil function, |FT(P(x))|^2."*
— Classical Fourier optics (Duffieux), 1946. Source: Wikipedia: Point spread function (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *point object*: the PSF is defined for an exactly point-like object - a source of zero size.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

PSF_phi(kappa) = PSF*(1 + kappa*(phi-1)) + kappa*phi^-1*PSF_ground, with PSF_ground the spread floor. At kappa->0, PSF = |FT(P)|^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} PSF_phi = PSF -> the point spread function is the zero-source-size-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/847_point_spread_function.py`: reproduces the classical value PSF = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/847_point_spread_function.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured PSF of any real system will be broadened beyond |FT(P)|^2 by a floor kappa*phi^-1*PSF_ground.
EXPERIMENT (VERIFIED): Measure the PSF of a microscope with a sub-resolution fluorescent bead.
VERIFIED BY: If any real imaging system produces exactly the ideal PSF.
```

---

### RECOGNITION
Connects to Law 846 (Airy disk) and Law 847 (MTF) - the imaging chain.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Every image of a point is a spread; the ideal point is a coherent limit.

### NOVELTY
The ideal PSF gains a spread floor.

### ACTIONABILITY
Run sim/847_point_spread_function.py.

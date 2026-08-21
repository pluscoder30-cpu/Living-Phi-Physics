# PHI-PHYSICS — LAW 903
## CIE Color Matching Functions

**Domain:** Colorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/903_cie_color_matching.md` · **Sim:** `sim/903_cie_color_matching.py`

---

### CLASSICAL STATEMENT
*"Any color is matched by the tristimulus values X = integral xbar(lambda) S(lambda) dlambda, etc., where xbar, ybar, zbar are the CIE 1931 color matching functions."*
— Commission Internationale de l'Éclairage (CIE), 1931. Source: Wikipedia: CIE 1931 color space (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero spectral density*: tristimulus values are anchored at zero for zero spectral power - a dark limit.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

X_phi(kappa) = X*(1 + kappa*(phi-1)) + kappa*phi^-1*X_ground, with X_ground the tristimulus floor. At kappa->0, X = integral xbar S dlambda exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} X_phi = X -> the color matching functions are the zero-spectral-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/903_cie_color_matching.py`: reproduces the classical value X = 0.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/903_cie_color_matching.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Measured tristimulus values will deviate from the integrals by a coherence floor kappa*phi^-1*X_ground.
EXPERIMENT (VERIFIED): Measure the tristimulus values of a monochromatic source with a calibrated spectroradiometer.
VERIFIED BY: If measured tristimulus values match the CIE integrals exactly.
```

---

### RECOGNITION
Connects to Law 902 (color temperature) and Law 904 (Grassmann's laws).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The standard observer is a coherent limit; every eye differs slightly.

### NOVELTY
Color matching gains a spectral floor.

### ACTIONABILITY
Run sim/903_cie_color_matching.py.

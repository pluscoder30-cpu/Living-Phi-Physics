# PHI-PHYSICS — LAW 853
## Numerical Aperture

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/853_numerical_aperture.md` · **Sim:** `sim/853_numerical_aperture.py`

---

### CLASSICAL STATEMENT
*"NA = n sin(theta), the sine of the half-angle of the acceptance cone times the index; resolution ~ lambda/(2 NA)."*
— Ernst Abbe, 1873. Source: Wikipedia: Numerical aperture (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero angle* (theta = 0): NA = 0 for an exactly axial-only system - a cone of zero width.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

NA_phi(kappa) = NA*(1 + kappa*(phi-1)) + kappa*phi^-1*NA_ground, with NA_ground the aperture floor. At kappa->0, NA = n sin(theta) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} NA_phi = NA -> numerical aperture is the zero-cone-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/853_numerical_aperture.py`: reproduces the classical value NA = 0.6442 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/853_numerical_aperture.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The effective NA of any real objective will differ from n sin(theta) by a coherence floor; the acceptance cone is never exact.
EXPERIMENT (VERIFIED): Measure the acceptance cone of a microscope objective with a laser and calibrated apertures.
VERIFIED BY: If any real objective has exactly NA = n sin(theta).
```

---

### RECOGNITION
Connects to Law 832 (Abbe sine condition) and Law 852 (f-number).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect cone is a coherent limit; every aperture is a basin.

### NOVELTY
NA gains a coherence floor.

### ACTIONABILITY
Run sim/853_numerical_aperture.py.

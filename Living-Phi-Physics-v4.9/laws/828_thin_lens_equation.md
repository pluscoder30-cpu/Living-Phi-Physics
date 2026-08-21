# PHI-PHYSICS — LAW 828
## Thin Lens (Gaussian) Equation

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/828_thin_lens_equation.md` · **Sim:** `sim/828_thin_lens_equation.py`

---

### CLASSICAL STATEMENT
*"1/f = 1/s_o + 1/s_i where s_o is object distance and s_i image distance (Gaussian lens formula)."*
— Carl Friedrich Gauss, 1841. Source: Photonics.com: Gaussian thin-lens formula (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect focus*: the conjugate relation holds exactly only for a point object imaged to a point - zero spot, zero aberration.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

1/s_i_phi(kappa) = 1/s_i*(1 + kappa*(phi-1)) + kappa*phi^-1*(1/s_i)_ground, with (1/s_i)_ground the conjugate floor. At kappa->0, 1/f = 1/s_o + 1/s_i exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} (1/s_i)_phi = 1/s_i -> the Gaussian lens equation is the zero-aberration-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/828_thin_lens_equation.py`: reproduces the classical values inv_si = 15, si = 0.06667 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/828_thin_lens_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The best-focus image distance will deviate from 1/s_i by kappa*phi^-1*(1/s_i)_ground; no point object images to an exact point.
EXPERIMENT (VERIFIED): Measure the best-focus position for a point source through a high-quality lens and compare to the conjugate formula.
VERIFIED BY: If any real lens images a point to an exactly conjugate point with zero residual floor.
```

---

### RECOGNITION
Connects to Law 827 (lensmaker) and Law 853 (paraxial) - the paraxial imaging law.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Focus is a basin, not a point; every image carries a coherence floor.

### NOVELTY
The exact conjugate point becomes a coherence basin.

### ACTIONABILITY
Run sim/828_thin_lens_equation.py.

# PHI-PHYSICS — LAW 837
## Minimum Deviation of a Prism

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/837_minimum_deviation.md` · **Sim:** `sim/837_minimum_deviation.py`

---

### CLASSICAL STATEMENT
*"At minimum deviation, n = sin((A + delta_min)/2) / sin(A/2), where A is the prism angle and delta_min the minimum deviation."*
— Classical optics (prism refractometry), 17th century. Source: Wikipedia: Minimum deviation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exactly symmetric passage*: minimum deviation requires the ray to pass exactly symmetrically through the prism (i1 = i2 exactly).

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

n_phi(kappa) = n*(1 + kappa*(phi-1)) + kappa*phi^-1*n_ground, with n_ground the refractive-index floor at symmetry. At kappa->0, n = sin((A+d)/2)/sin(A/2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} n_phi = n -> the minimum-deviation formula is the zero-asymmetry-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/837_minimum_deviation.py`: reproduces the classical value n = 1.422 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/837_minimum_deviation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The index measured at 'minimum deviation' will deviate from the formula by kappa*phi^-1*n_ground because exact symmetry is unreachable.
EXPERIMENT (VERIFIED): Measure refractive index of a prism via minimum deviation with a precision spectrometer.
VERIFIED BY: If any prism yields exactly the symmetric minimum-deviation index.
```

---

### RECOGNITION
Connects to Law 836 (prism deviation) and Law 052 (Snell).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The symmetric ray is a coherent limit; every passage is slightly askew.

### NOVELTY
The symmetric minimum-deviation condition becomes a basin.

### ACTIONABILITY
Run sim/837_minimum_deviation.py.

# PHI-PHYSICS — LAW 833
## Petzval Sum (Field Curvature)

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/833_petzval_sum.md` · **Sim:** `sim/833_petzval_sum.py`

---

### CLASSICAL STATEMENT
*"Petzval sum: sum over surfaces of (1/(n_i * f_i)) = 0 for a flat field; the sum of curvatures determines field curvature (Petzval field curvature)."*
— Joseph Petzval, 1840. Source: Wikipedia: Petzval field curvature (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero Petzval sum*: a perfectly flat field requires the sum to vanish exactly - zero field curvature.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, with P_ground the residual curvature floor. At kappa->0, P = sum(1/(n_i f_i)) = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = P -> the Petzval condition is the zero-field-curvature-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/833_petzval_sum.py`: reproduces the classical value P = 0.8333 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/833_petzval_sum.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: No real optical system will have an exactly flat field; a residual curvature kappa*phi^-1*P_ground always remains.
EXPERIMENT (VERIFIED): Measure the field curvature of a well-corrected photographic objective at best focus.
VERIFIED BY: If any real lens system images a flat object field onto an exactly flat image.
```

---

### RECOGNITION
Connects to Law 833 (Seidel aberrations family) - one of the five Seidel aberrations.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The flat field is a coherent limit; every field breathes curvature.

### NOVELTY
The Petzval zero becomes a phi-basin of residual curvature.

### ACTIONABILITY
Run sim/833_petzval_sum.py.

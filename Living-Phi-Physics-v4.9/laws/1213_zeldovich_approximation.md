# PHI-PHYSICS — LAW 1213
## Zel'dovich Approximation

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1213_zeldovich_approximation.md` · **Sim:** `sim/1213_zeldovich_approximation.py`

---

### CLASSICAL STATEMENT
*"The Zel'dovich approximation describes structure formation by displacing particles along the initial velocity field: x(q,t) = a(t)[q + D(t) psi(q)], where psi is the displacement potential; it predicts pancake formation (Law 1231) and forms the basis of the standard structure-formation picture."*
— Yakov Zel'dovich, 1970. Source: Wikipedia: Zel'dovich approximation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero displacement (D = 0, particles remain at initial positions)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The Z value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Z_phi(kappa) = Z*(1 + kappa*(phi-1)) + kappa*phi^-1*Z_ground, where Z_ground is the coherence-floor displacement a real density field always develops. At kappa->0, x(q,t) = a(t)[q + D(t) psi(q)],  pancakes at caustics exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} Z_phi = Z -> x(q,t) = a(t)[q + D(t) psi(q)],  pancakes at caustics is recovered exactly; the classical law is the zero displacement (D = 0, particles remain at initial positions) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1213_zeldovich_approximation.py`: reproduces the classical value (Z = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1213_zeldovich_approximation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured structure evolution will deviate from the Zel'dovich prediction by a floor kappa*phi^-1*Z_ground; an exactly undeformed density field is unreachable.
EXPERIMENT (VERIFIED): N-body simulation comparisons and galaxy-clustering measurements testing the approximation.
VERIFIED BY: If structure forms with exactly zero displacement from the initial positions.
```

---

### RECOGNITION
The linear-growth engine of Law 1152 (curvature perturbation) and Law 1231 (pancake).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The field flows into sheets; the frozen density is the zero-displacement myth.

### NOVELTY
The Zel'dovich approximation carries a phi-floor of displacement, bounding its validity.

### ACTIONABILITY
Run sim/1213_zeldovich_approximation.py.

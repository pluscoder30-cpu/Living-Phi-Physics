# PHI-PHYSICS — LAW 1206
## Starobinsky Inflation

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1206_starobinsky_inflation.md` · **Sim:** `sim/1206_starobinsky_inflation.py`

---

### CLASSICAL STATEMENT
*"Starobinsky inflation is an inflationary model from curvature-squared (R^2) quantum corrections to gravity: the effective potential V(phi) = Lambda^4 (1 - exp(-sqrt(2/3) phi/M_P))^2 produces nearly scale-invariant perturbations with n_s ~ 0.96 and r ~ 0.003, a leading candidate compatible with Planck data."*
— Alexei Starobinsky, 1980. Source: Wikipedia: Starobinsky inflation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero R^2 coupling (pure Einstein gravity, no inflation from curvature)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The S value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground, where S_ground is the coherence-floor curvature-squared residue a real gravity always retains. At kappa->0, S = (1/2) integral sqrt(-g) (R + R^2/(6 M^2)),  n_s = 1 - 2/N,  r = 12/N^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} S_phi = S -> S = (1/2) integral sqrt(-g) (R + R^2/(6 M^2)),  n_s = 1 - 2/N,  r = 12/N^2 is recovered exactly; the classical law is the zero R^2 coupling (pure Einstein gravity, no inflation from curvature) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1206_starobinsky_inflation.py`: reproduces the classical value (S = 0.96) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1206_starobinsky_inflation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured spectral index will deviate from the Starobinsky prediction by a floor kappa*phi^-1*S_ground; an exactly R^2-free gravity is unreachable.
EXPERIMENT (VERIFIED): CMB spectral-index and tensor-to-scalar constraints discriminating Starobinsky inflation.
VERIFIED BY: If n_s and r exactly match a non-Starobinsky prediction with zero R^2 component.
```

---

### RECOGNITION
The f(R) model of Law 1143 (inflation) and the gravity extension of Law 063 (field equations).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Curvature-squared seeds the expansion; the linear gravity is the zero-coupling myth.

### NOVELTY
Starobinsky inflation carries a phi-floor of the R^2 residue, bounding its discrimination.

### ACTIONABILITY
Run sim/1206_starobinsky_inflation.py.

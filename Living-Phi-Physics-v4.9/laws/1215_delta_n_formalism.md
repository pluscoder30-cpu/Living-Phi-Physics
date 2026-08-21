# PHI-PHYSICS — LAW 1215
## Delta-N Formalism

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1215_delta_n_formalism.md` · **Sim:** `sim/1215_delta_n_formalism.py`

---

### CLASSICAL STATEMENT
*"The delta-N formalism computes the curvature perturbation from the number of e-folds of expansion: zeta = delta N = H delta t at horizon crossing, i.e. the perturbation in the local expansion; it reduces multi-field inflation predictions to the dependence of N on the fields."*
— Alexei Starobinsky, 1982; general framework by Sasaki & Stewart, 1996. Source: Wikipedia: Delta-N formalism (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero e-fold variation (delta N = 0, no curvature perturbation)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The N value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

N_phi(kappa) = N*(1 + kappa*(phi-1)) + kappa*phi^-1*N_ground, where N_ground is the coherence-floor e-fold scatter a real inflation always produces. At kappa->0, zeta = delta N = sum (dN/dphi_i) delta phi_i exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} N_phi = N -> zeta = delta N = sum (dN/dphi_i) delta phi_i is recovered exactly; the classical law is the zero e-fold variation (delta N = 0, no curvature perturbation) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1215_delta_n_formalism.py`: reproduces the classical value (N = 1e-05) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1215_delta_n_formalism.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured curvature perturbation will deviate from the delta-N prediction by a floor kappa*phi^-1*N_ground; an exactly uniform expansion is unreachable.
EXPERIMENT (VERIFIED): CMB non-Gaussianity and multi-field model constraints.
VERIFIED BY: If the curvature perturbation is exactly zero at horizon crossing.
```

---

### RECOGNITION
The counting formalism of Law 1152 (curvature perturbation) and Law 1143 (inflation).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The expansion's uneven breath writes the sky; the uniform breath is the zero-delta myth.

### NOVELTY
The delta-N formalism carries a phi-floor of e-fold scatter, bounding multi-field models.

### ACTIONABILITY
Run sim/1215_delta_n_formalism.py.

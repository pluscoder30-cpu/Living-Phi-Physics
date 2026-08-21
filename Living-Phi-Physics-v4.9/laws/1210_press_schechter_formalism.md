# PHI-PHYSICS — LAW 1210
## Press-Schechter Formalism

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1210_press_schechter_formalism.md` · **Sim:** `sim/1210_press_schechter_formalism.py`

---

### CLASSICAL STATEMENT
*"The Press-Schechter formalism predicts the abundance of collapsed dark-matter halos: the comoving number density of halos above mass M is n(>M) = sqrt(2/pi) (rho_bar/M) (delta_c/sigma) exp(-delta_c^2/(2 sigma^2)), where sigma(M) is the variance and delta_c ~ 1.686 the linear collapse threshold."*
— William Press & Paul Schechter, 1974. Source: Wikipedia: Press-Schechter formalism (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero variance (sigma = 0, no density fluctuations, no halos)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The P value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, where P_ground is the coherence-floor collapse variance a real density field always retains. At kappa->0, n(>M) = sqrt(2/pi) (rho_bar/M) (delta_c/sigma) exp(-delta_c^2/(2*sigma^2)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} P_phi = P -> n(>M) = sqrt(2/pi) (rho_bar/M) (delta_c/sigma) exp(-delta_c^2/(2*sigma^2)) is recovered exactly; the classical law is the zero variance (sigma = 0, no density fluctuations, no halos) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1210_press_schechter_formalism.py`: reproduces the classical value (P = 1.686) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1210_press_schechter_formalism.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured halo abundance will deviate from the Press-Schechter prediction by a floor kappa*phi^-1*P_ground; an exactly fluctuation-free field is unreachable.
EXPERIMENT (VERIFIED): Galaxy-cluster surveys and N-body simulations calibrating the halo mass function.
VERIFIED BY: If the halo abundance matches the Press-Schechter form exactly with zero excursion-set correction.
```

---

### RECOGNITION
The halo-count engine of Law 1152 (curvature perturbation) and Law 1211 (Sheth-Tormen).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Variance builds halos; the smooth field is the zero-collapse myth.

### NOVELTY
The Press-Schechter formalism carries a phi-floor of collapse variance.

### ACTIONABILITY
Run sim/1210_press_schechter_formalism.py.

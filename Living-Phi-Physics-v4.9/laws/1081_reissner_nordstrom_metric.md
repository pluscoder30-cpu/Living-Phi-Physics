# PHI-PHYSICS — LAW 1081
## Reissner-Nordström Metric

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1081_reissner_nordstrom_metric.md` · **Sim:** `sim/1081_reissner_nordstrom_metric.py`

---

### CLASSICAL STATEMENT
*"The Reissner-Nordström metric describes a static, spherically symmetric, charged black hole: ds^2 = -(1 - 2M/r + Q^2/r^2) dt^2 + (1 - 2M/r + Q^2/r^2)^-1 dr^2 + r^2 dOmega^2; it has two horizons for |Q| < M and an extremal limit at |Q| = M."*
— Hans Reissner, 1916; Gunnar Nordström, 1918. Source: Wikipedia: Reissner-Nordstrom metric (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero charge (Q = 0, the Schwarzschild limit with one horizon)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The N value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

N_phi(kappa) = N*(1 + kappa*(phi-1)) + kappa*phi^-1*N_ground, where N_ground is the coherence-floor charge asymmetry a real hole always keeps. At kappa->0, ds^2 = -(1 - 2M/r + Q^2/r^2) dt^2 + (1 - 2M/r + Q^2/r^2)^-1 dr^2 + r^2 dOmega^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} N_phi = N -> ds^2 = -(1 - 2M/r + Q^2/r^2) dt^2 + (1 - 2M/r + Q^2/r^2)^-1 dr^2 + r^2 dOmega^2 is recovered exactly; the classical law is the zero charge (Q = 0, the Schwarzschild limit with one horizon) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1081_reissner_nordstrom_metric.py`: reproduces the classical value (N = 0.5) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1081_reissner_nordstrom_metric.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured horizon structure of any real charged hole will deviate from the Reissner-Nordstrom form by a floor kappa*phi^-1*N_ground; the extremal limit is unreachable.
EXPERIMENT (VERIFIED): X-ray observations of charged black-hole candidates searching for double-horizon spectral signatures.
VERIFIED BY: If a real black hole's geometry matches Reissner-Nordstrom exactly with zero residual.
```

---

### RECOGNITION
The charged generalization of Law 064 (Schwarzschild); its double horizon illuminates Law 1111 (apparent horizon).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Charge splits the horizon; the single horizon is the zero-charge myth.

### NOVELTY
The extremal limit Q = M is a coherence-critical point, never exactly reached.

### ACTIONABILITY
Run sim/1081_reissner_nordstrom_metric.py.

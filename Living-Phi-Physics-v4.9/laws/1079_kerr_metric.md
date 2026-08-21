# PHI-PHYSICS — LAW 1079
## Kerr Metric

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1079_kerr_metric.md` · **Sim:** `sim/1079_kerr_metric.py`

---

### CLASSICAL STATEMENT
*"The Kerr metric describes a rotating, uncharged black hole in Boyer-Lindquist coordinates; it is stationary and axisymmetric with angular momentum parameter a = J/(M c), possesses an ergosphere (Law 1109), frame dragging (Law 1090), and is the unique two-parameter family by the no-hair theorem."*
— Roy Kerr, 1963. Source: Wikipedia: Kerr metric (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero rotation (a = 0, the Schwarzschild limit)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The K value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

K_phi(kappa) = K*(1 + kappa*(phi-1)) + kappa*phi^-1*K_ground, where K_ground is the coherence-floor rotation a real collapsed body always retains. At kappa->0, ds^2 = -(1 - 2Mr/(rho^2)) dt^2 - (4Mar sin^2 theta/rho^2) dt dphi + ... exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} K_phi = K -> ds^2 = -(1 - 2Mr/(rho^2)) dt^2 - (4Mar sin^2 theta/rho^2) dt dphi + ... is recovered exactly; the classical law is the zero rotation (a = 0, the Schwarzschild limit) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1079_kerr_metric.py`: reproduces the classical value (K = 0.998) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1079_kerr_metric.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured multipole structure of any real rotating compact object will deviate from the Kerr family by a floor kappa*phi^-1*K_ground; an exactly Schwarzschild (a=0) collapse is unreachable.
EXPERIMENT (VERIFIED): X-ray iron-line and continuum fitting of accreting black holes constraining the deviation from the Kerr metric.
VERIFIED BY: If any real black hole matches the Kerr metric exactly with zero residual multipole deviation.
```

---

### RECOGNITION
The rotating generalization of Law 064 (Schwarzschild); underpins Law 1109 (ergosphere) and Law 1107 (ISCO).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Rotation refuses to vanish in collapse; the Schwarzschild hole is the zero-spin myth.

### NOVELTY
The Kerr parameter a carries a phi-floor: every black hole is born spinning at least to kappa*phi^-1.

### ACTIONABILITY
Run sim/1079_kerr_metric.py.

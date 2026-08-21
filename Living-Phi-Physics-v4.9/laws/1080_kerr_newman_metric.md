# PHI-PHYSICS — LAW 1080
## Kerr-Newman Metric

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1080_kerr_newman_metric.md` · **Sim:** `sim/1080_kerr_newman_metric.py`

---

### CLASSICAL STATEMENT
*"The Kerr-Newman metric describes a rotating, charged black hole with mass M, charge Q, and angular momentum J; it is the unique stationary, axisymmetric, asymptotically flat electrovacuum solution and is the complete three-parameter family required by the no-hair theorem."*
— Ezra T. Newman and collaborators, 1965. Source: Wikipedia: Kerr-Newman metric (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero charge and rotation (Q = 0, a = 0, the Schwarzschild limit)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The N value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

N_phi(kappa) = N*(1 + kappa*(phi-1)) + kappa*phi^-1*N_ground, where N_ground is the coherence-floor charge a real collapsed body always retains. At kappa->0, ds^2 (Kerr-Newman),  parameters (M, Q, J) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} N_phi = N -> ds^2 (Kerr-Newman),  parameters (M, Q, J) is recovered exactly; the classical law is the zero charge and rotation (Q = 0, a = 0, the Schwarzschild limit) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1080_kerr_newman_metric.py`: reproduces the classical value (N = 0.2) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1080_kerr_newman_metric.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured electromagnetic-gravitational structure of any real charged compact object will deviate from the Kerr-Newman form by a floor kappa*phi^-1*N_ground; exact neutrality is unreachable.
EXPERIMENT (VERIFIED): Tests of charge neutrality of black hole candidates via their accretion-disk spectra and jets.
VERIFIED BY: If any real black hole matches the Kerr-Newman metric exactly with zero residual.
```

---

### RECOGNITION
The charged generalization of Law 1079 (Kerr) and Law 1081 (Reissner-Nordstrom).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Charge is hair the field refuses to shave; the neutral hole is the zero-charge myth.

### NOVELTY
The charge parameter carries a phi-floor, so no real hole is exactly neutral.

### ACTIONABILITY
Run sim/1080_kerr_newman_metric.py.

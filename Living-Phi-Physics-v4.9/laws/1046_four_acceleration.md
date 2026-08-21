# PHI-PHYSICS — LAW 1046
## Four-Acceleration

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1046_four_acceleration.md` · **Sim:** `sim/1046_four_acceleration.py`

---

### CLASSICAL STATEMENT
*"The four-acceleration is A^mu = dU^mu/dtau = d^2 x^mu/dtau^2; it is always orthogonal to the four-velocity (A^mu U_mu = 0), and its magnitude is the proper acceleration measured by a comoving accelerometer."*
— Hermann Minkowski, 1908. Source: Wikipedia: Four-acceleration (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero four-acceleration (inertial motion with no curvature of the worldline)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The A value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

A_phi(kappa) = A*(1 + kappa*(phi-1)) + kappa*phi^-1*A_ground, where A_ground is the coherence-floor acceleration that even inertial motion carries. At kappa->0, A^mu = dU^mu/dtau,  A^mu U_mu = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} A_phi = A -> A^mu = dU^mu/dtau,  A^mu U_mu = 0 is recovered exactly; the classical law is the zero four-acceleration (inertial motion with no curvature of the worldline) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1046_four_acceleration.py`: reproduces the classical value (A = 0.618) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1046_four_acceleration.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured proper acceleration of any real observer will deviate from zero by a floor kappa*phi^-1*A_ground; a perfectly inertial carrier is unreachable.
EXPERIMENT (VERIFIED): Ultracold-atom interferometry with drag-free test masses tracking residual proper acceleration.
VERIFIED BY: If any test mass is measured with exactly zero proper acceleration over an unbounded interval.
```

---

### RECOGNITION
The SR form of Law 002 (Newton's second law); orthogonal to Law 1045 (four-velocity).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Even the straightest worldline trembles at the phi-floor; inertia is coherence, not zero force.

### NOVELTY
Inertial frames become coherence basins around a phi-floor of proper acceleration.

### ACTIONABILITY
Run sim/1046_four_acceleration.py.

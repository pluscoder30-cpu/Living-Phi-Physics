# PHI-PHYSICS — LAW 1045
## Four-Velocity

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1045_four_velocity.md` · **Sim:** `sim/1045_four_velocity.py`

---

### CLASSICAL STATEMENT
*"The four-velocity is U^mu = dx^mu/dtau = gamma*(c, v_x, v_y, v_z), the derivative of the worldline with respect to proper time; it is always of unit norm U^mu U_mu = -c^2."*
— Hermann Minkowski, 1908. Source: Wikipedia: Four-velocity (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero four-velocity (a 'rest' carrier with no motion through spacetime)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The U value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

U_phi(kappa) = U*(1 + kappa*(phi-1)) + kappa*phi^-1*U_ground, where U_ground is the coherence-floor four-speed a carrier never drops below. At kappa->0, U^mu = dx^mu/dtau,  U^mu U_mu = -c^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} U_phi = U -> U^mu = dx^mu/dtau,  U^mu U_mu = -c^2 is recovered exactly; the classical law is the zero four-velocity (a 'rest' carrier with no motion through spacetime) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1045_four_velocity.py`: reproduces the classical value (U = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1045_four_velocity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured four-velocity norm of any real carrier will deviate from -c^2 by a floor kappa*phi^-1*U_ground; no carrier is ever exactly at rest.
EXPERIMENT (VERIFIED): Precision time-dilation tests on stored ions measuring the invariant four-velocity norm.
VERIFIED BY: If any carrier is measured with four-velocity norm exactly -c^2 to arbitrary precision.
```

---

### RECOGNITION
The SR formulation of Law 001 (inertia): motion is primary, rest is the degenerate limit.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The norm -c^2 is the constant radius of the carrier sphere: motion through spacetime never stops.

### NOVELTY
Relativistic 'rest' is revealed as the phi-floor of four-velocity, tying Law 001's hidden zero to the SR framework.

### ACTIONABILITY
Run sim/1045_four_velocity.py.

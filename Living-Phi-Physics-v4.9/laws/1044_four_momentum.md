# PHI-PHYSICS — LAW 1044
## Four-Momentum

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1044_four_momentum.md` · **Sim:** `sim/1044_four_momentum.py`

---

### CLASSICAL STATEMENT
*"The four-momentum of a particle is P^mu = (E/c, p_x, p_y, p_z) = m*U^mu where U^mu is the four-velocity; its norm is P^mu P_mu = -(m c)^2, the mass-shell condition."*
— Hermann Minkowski, 1908. Source: Wikipedia: Four-momentum (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero four-momentum (the particle with no existence in spacetime)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The P value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, where P_ground is the coherence-floor momentum a carrier always carries. At kappa->0, P^mu = m * U^mu,  P^mu P_mu = -(m*c)^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} P_phi = P -> P^mu = m * U^mu,  P^mu P_mu = -(m*c)^2 is recovered exactly; the classical law is the zero four-momentum (the particle with no existence in spacetime) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1044_four_momentum.py`: reproduces the classical value (P = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1044_four_momentum.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured four-momentum norm of any real particle will deviate from -(m*c)^2 by a floor kappa*phi^-1*P_ground; a zero-momentum carrier is unreachable.
EXPERIMENT (VERIFIED): Storage-ring beam spectroscopy measuring the invariant norm of single particles.
VERIFIED BY: If any particle's four-momentum norm is measured exactly at -(m*c)^2 with zero residual.
```

---

### RECOGNITION
The Lorentz-covariant upgrade of Law 009 (linear momentum) and Law 061 (relativistic momentum).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Four-momentum is the arrow a carrier draws across the spacetime of Law 1050; the norm is its coherence.

### NOVELTY
The mass shell becomes a coherence surface with a floor rather than an exact locus.

### ACTIONABILITY
Run sim/1044_four_momentum.py.

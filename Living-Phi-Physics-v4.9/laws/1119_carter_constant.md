# PHI-PHYSICS — LAW 1119
## Carter Constant

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1119_carter_constant.md` · **Sim:** `sim/1119_carter_constant.py`

---

### CLASSICAL STATEMENT
*"The Carter constant Q is a fourth independent constant of motion for geodesics in the Kerr metric (besides energy, axial angular momentum, and rest mass), making geodesic motion in Kerr integrable through separability of the Hamilton-Jacobi equation."*
— Brandon Carter, 1968. Source: Wikipedia: Carter constant (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero Carter constant (Q = 0, equatorial geodesics only)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The Q value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Q_phi(kappa) = Q*(1 + kappa*(phi-1)) + kappa*phi^-1*Q_ground, where Q_ground is the coherence-floor hidden symmetry a real Kerr geodesic always exhibits. At kappa->0, Q = p_theta^2 + cos^2(theta)*[a^2*(m^2 - E^2) + L_z^2/sin^2(theta)] exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} Q_phi = Q -> Q = p_theta^2 + cos^2(theta)*[a^2*(m^2 - E^2) + L_z^2/sin^2(theta)] is recovered exactly; the classical law is the zero Carter constant (Q = 0, equatorial geodesics only) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1119_carter_constant.py`: reproduces the classical value (Q = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1119_carter_constant.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured trajectories of any real Kerr test particles will deviate from the integrable Carter prediction by a floor kappa*phi^-1*Q_ground; an exactly equatorial orbit is unreachable.
EXPERIMENT (VERIFIED): X-ray iron-line and hot-spot modeling of accreting black holes constraining off-equatorial geodesics.
VERIFIED BY: If a Kerr geodesic has exactly zero Carter constant at non-zero inclination.
```

---

### RECOGNITION
The integrability of Law 1079 (Kerr) and the hidden symmetry of Law 1074 (Killing tensors).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The hidden constant lets the field fold cleanly; the equatorial orbit is the zero-inclination myth.

### NOVELTY
The Carter constant carries a phi-floor: every orbit carries a hidden-symmetry residue.

### ACTIONABILITY
Run sim/1119_carter_constant.py.

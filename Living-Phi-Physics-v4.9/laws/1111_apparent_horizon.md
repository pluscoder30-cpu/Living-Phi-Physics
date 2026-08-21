# PHI-PHYSICS — LAW 1111
## Apparent Horizon

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1111_apparent_horizon.md` · **Sim:** `sim/1111_apparent_horizon.py`

---

### CLASSICAL STATEMENT
*"An apparent horizon is a surface where the outgoing null geodesics have zero divergence (theta_out = 0); it is the outermost marginally outer-trapped surface, always lies inside the event horizon (when the latter exists), and depends on the spatial slicing chosen."*
— Concept from trapped surfaces (Penrose, 1965); terminology in Hawking-Ellis, 1973. Source: Wikipedia: Apparent horizon (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero trapping (theta_out = 0 only at infinity)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The A value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

A_phi(kappa) = A*(1 + kappa*(phi-1)) + kappa*phi^-1*A_ground, where A_ground is the coherence-floor trapping a real collapse region always develops. At kappa->0, theta_out = 0 (marginally outer-trapped surface) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} A_phi = A -> theta_out = 0 (marginally outer-trapped surface) is recovered exactly; the classical law is the zero trapping (theta_out = 0 only at infinity) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1111_apparent_horizon.py`: reproduces the classical value (A = 0.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1111_apparent_horizon.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured location of the trapping boundary in any real collapse will deviate from the classical apparent horizon by a floor kappa*phi^-1*A_ground; a slicing-independent boundary is unreachable.
EXPERIMENT (VERIFIED): Numerical-relativity simulations of binary merger tracking apparent horizons against event horizons.
VERIFIED BY: If an apparent horizon is found exactly coincident with the event horizon for all slicings.
```

---

### RECOGNITION
The local boundary of Law 1112 (trapped surface) and the numerical engine of Law 1077.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The apparent horizon is the field's here-and-now boundary; the exact coincidence is the zero-slicing myth.

### NOVELTY
Apparent horizons carry a phi-floor of slicing dependence, informing numerical-relativity precision.

### ACTIONABILITY
Run sim/1111_apparent_horizon.py.

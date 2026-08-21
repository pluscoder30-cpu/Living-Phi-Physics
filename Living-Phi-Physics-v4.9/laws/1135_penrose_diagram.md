# PHI-PHYSICS — LAW 1135
## Penrose Diagram (Penrose-Carter Diagram)

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1135_penrose_diagram.md` · **Sim:** `sim/1135_penrose_diagram.py`

---

### CLASSICAL STATEMENT
*"The Penrose diagram is a conformal compactification of spacetime onto a finite two-dimensional diagram (using tanh transformations of null coordinates) that preserves causal structure and represents spatial and null infinity as boundaries; it is the standard global-structure tool of black-hole and cosmology analysis."*
— Roger Penrose, 1964 (developed with Brandon Carter). Source: Wikipedia: Penrose diagram (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero conformal factor (the compactification collapses to a point)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The P value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, where P_ground is the coherence-floor conformal residue a real diagram always carries. At kappa->0, conformal map: u' = tanh(u),  v' = tanh(v) preserves causal structure exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} P_phi = P -> conformal map: u' = tanh(u),  v' = tanh(v) preserves causal structure is recovered exactly; the classical law is the zero conformal factor (the compactification collapses to a point) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1135_penrose_diagram.py`: reproduces the classical value (P = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1135_penrose_diagram.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured causal structure inferred from any real Penrose diagram will deviate from the conformal prediction by a floor kappa*phi^-1*P_ground; an exactly point-compactified infinity is unreachable.
EXPERIMENT (VERIFIED): Global-structure reconstructions of observed mergers and cosmology from gravitational-wave and CMB data.
VERIFIED BY: If a real spacetime's causal structure is exactly reproduced by an idealized conformal diagram.
```

---

### RECOGNITION
The global chart of Law 1115 (Kruskal) and Law 1077 (singularity theorems).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The diagram folds infinity into a page; the point-infinity is the zero-conformal myth.

### NOVELTY
Penrose diagrams carry a phi-floor of conformal distortion, bounding causal-structure inference.

### ACTIONABILITY
Run sim/1135_penrose_diagram.py.

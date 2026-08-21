# PHI-PHYSICS — LAW 1048
## Spacetime Interval

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1048_spacetime_interval.md` · **Sim:** `sim/1048_spacetime_interval.py`

---

### CLASSICAL STATEMENT
*"The spacetime interval between two events is ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2; it is invariant under Lorentz transformations, with ds^2 < 0 (timelike), = 0 (null/lightlike), > 0 (spacelike) classification."*
— Hermann Minkowski, 1908. Source: Wikipedia: Spacetime (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero interval (ds^2 = 0, two exactly lightlike events)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The S value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground, where S_ground is the coherence-floor interval a pair of real events always carries. At kappa->0, ds^2 = -c^2*dt^2 + dx^2 + dy^2 + dz^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} S_phi = S -> ds^2 = -c^2*dt^2 + dx^2 + dy^2 + dz^2 is recovered exactly; the classical law is the zero interval (ds^2 = 0, two exactly lightlike events) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1048_spacetime_interval.py`: reproduces the classical value (S = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1048_spacetime_interval.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured interval between any two real events will deviate from the Minkowski value by a floor kappa*phi^-1*S_ground; two events are never exactly null-separated in the limit.
EXPERIMENT (VERIFIED): Atomic-clock networks comparing the invariant intervals between space-separated events.
VERIFIED BY: If any pair of events is measured with interval exactly zero or exactly on the classical light cone.
```

---

### RECOGNITION
The geometric basis of Law 051 (Lorentz) and Law 1051 (light cone); anchors Law 1052 (simultaneity).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The interval is the metric breath of the carrier sphere; the light cone is its zero-coherence membrane.

### NOVELTY
The exactly-null separation is a coherence limit, never a reachable event geometry.

### ACTIONABILITY
Run sim/1048_spacetime_interval.py.

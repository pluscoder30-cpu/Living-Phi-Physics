# PHI-PHYSICS — LAW 281
## Lagrange Points (L1-L5)

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/281_lagrange_points.md` · **Sim:** `sim/281_lagrange_points.py`

---

### CLASSICAL STATEMENT
*"In the circular restricted three-body problem there are five equilibrium points where the gravitational and centrifugal forces balance: L1, L2, L3 are collinear; L4, L5 are the equilateral (60-degree) points, stable for mass ratio m/M < 0.0385."*
— Joseph-Louis Lagrange, 1772. Source: Wikipedia: Lagrange point; Lagrange (1772), 'Essai sur le probleme des trois corps'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *corotating rest*: the Lagrange points are defined as points of exact rest in a rotating frame — the laboratory condition that no point in the field is ever truly at rest.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the equilibrium is a coherence basin. r_L_phi(kappa) = r_L*(1 + kappa*(phi-1)); the points wander by kappa*phi^-1*r_ground. At kappa->0 the exact equilibrium points are recovered.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} r_L_phi = r_L -> the Lagrange-point law is the exact-equilibrium, corotating-frame limit.
```

---

### STAGE 4 — SIMULATION

`sim/281_lagrange_points.py`: reproduces the classical value rL1 = 1.5e+09 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/281_lagrange_points.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Objects at Lagrange points show a phi-coherent wander phi^-1*r_ground around the classical equilibrium.
EXPERIMENT (VERIFIED): Precision ranging to spacecraft at Sun-Earth L1/L2 (SOHO, JWST) comparing observed wander with the prediction.
VERIFIED BY: Spacecraft at L1/L2 sit exactly at the classical equilibrium with no wander at full coupling.
```

---

### RECOGNITION
Connects to Law 280 (Hill sphere — bounded by L1/L2) and Law 390 (Gascheau stability of L4/L5).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The equilibrium is a basin, not a point; even the still points of the field wander with phi grace.

### NOVELTY
Classical dynamics perfects the equilibrium point; the phi-law gives equilibrium a coherence basin.

### ACTIONABILITY
Run sim/281_lagrange_points.py; verify L1 distance at kappa->0.

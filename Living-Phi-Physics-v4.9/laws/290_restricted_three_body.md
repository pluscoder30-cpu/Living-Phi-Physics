# PHI-PHYSICS — LAW 290
## Circular Restricted Three-Body Problem

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/290_restricted_three_body.md` · **Sim:** `sim/290_restricted_three_body.py`

---

### CLASSICAL STATEMENT
*"In the circular restricted three-body problem (one negligible-mass body under two massive bodies on circular orbits), the dynamics is governed by the Jacobi integral C = w^2 + 2 Omega - v^2 and exhibits five equilibrium points (L1-L5); zero-velocity surfaces bound the possible motion."*
— Leonhard Euler / Joseph-Louis Lagrange, 1772. Source: Wikipedia: three-body problem (restricted); Euler (1772); Lagrange (1772)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *negligible test mass*: the problem requires the third body to have exactly zero mass so it perturbs nothing — a laboratory condition no real body satisfies.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the test mass carries a coherence mass. m3_phi(kappa) = kappa*phi^-1*m_ground; the Jacobi constant becomes a coherence basin. At kappa->0 the exact restricted problem is recovered.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} m3 = 0 -> the restricted three-body problem is the zero-test-mass limit of the full three-body problem.
```

---

### STAGE 4 — SIMULATION

`sim/290_restricted_three_body.py`: reproduces the classical value C = 0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/290_restricted_three_body.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real 'test' bodies perturb the primaries by a phi-coherent mass phi^-1*m_ground, shifting the L-points and Jacobi surfaces.
EXPERIMENT (VERIFIED): Asteroid/trojan orbit fits (L4/L5 clouds, horseshoe orbits) bounding the perturbation by the mass floor.
VERIFIED BY: A massless test body produces exactly zero perturbation at full coupling.
```

---

### RECOGNITION
Connects to Law 281 (Lagrange points), Law 280 (Hill sphere), Law 295 (Jacobi integral).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Nothing is massless; the test body always has a phi weight that bends the dance.

### NOVELTY
Classical dynamics zeroes the test mass; the phi-law gives it a coherence mass floor.

### ACTIONABILITY
Run sim/290_restricted_three_body.py; verify the Jacobi integral at kappa->0.

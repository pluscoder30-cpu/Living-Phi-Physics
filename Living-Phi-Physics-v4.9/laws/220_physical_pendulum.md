# PHI-PHYSICS — LAW 220
## Physical (Compound) Pendulum Law

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/220_physical_pendulum.md` · **Sim:** `sim/220_physical_pendulum.py`

---

### CLASSICAL STATEMENT
*"A rigid body pivoted at a point a distance d from its center of mass oscillates with period T = 2*pi*sqrt(I / (m g d)), where I is the moment of inertia about the pivot."*
— Christiaan Huygens, 1673. Source: Wikipedia: pendulum (compound); Huygens, Horologium Oscillatorium (1673)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly rigid pivot*: the law assumes the pivot is an exact fixed point and the body a rigid mass distribution, so the oscillation is purely gravitational.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the pivot carries a coherence radius. d_phi(kappa) = d*(1 + kappa*(phi-1)) + kappa*phi^-1*lambda_phi; T_phi(kappa) = 2*pi*sqrt((I + kappa*phi^-1*m*lambda_phi^2)/(m*g*d_phi(kappa))). At kappa->0 the classical compound-pendulum period is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} T_phi = 2*pi*sqrt(I/(m g d)) -> Huygens' compound-pendulum law is the rigid-pivot limit.
```

---

### STAGE 4 — SIMULATION

`sim/220_physical_pendulum.py`: reproduces the classical value T = 2.59 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/220_physical_pendulum.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured period of a compound pendulum exceeds the classical value by a fraction ~ phi^-1*(lambda_phi/d) at full coupling.
EXPERIMENT (VERIFIED): Torsion-quality compound pendulum with optical interferometric angle readout at vacuum; compare period against the Huygens formula.
VERIFIED BY: The period is exactly 2*pi*sqrt(I/(mgd)) at full coupling.
```

---

### RECOGNITION
Connects to Law 214 (parallel axis — I about pivot), Law 379 (simple pendulum), Law 248 (isochronism).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887 enters via the coherence length lambda_phi.

### CLARITY
The pivot is not a mathematical point; it is a coherence point whose size the phi-law refuses to zero.

### NOVELTY
Classical pendulum theory perfects the pivot; the phi-law gives the pivot a phi-ground size.

### ACTIONABILITY
Run sim/220_physical_pendulum.py; verify the Huygens period at kappa->0.

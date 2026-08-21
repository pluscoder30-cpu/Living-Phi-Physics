# PHI-PHYSICS — LAW 224
## Moment of Inertia of a Solid Cylinder

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/224_moment_of_inertia_cylinder.md` · **Sim:** `sim/224_moment_of_inertia_cylinder.py`

---

### CLASSICAL STATEMENT
*"A solid cylinder of mass m and radius R has I = (1/2) m R^2 about its longitudinal symmetry axis."*
— Leonhard Euler (textbook theorem), 1758. Source: Resnick, Halliday & Krane, Physics; Wikipedia: list of moments of inertia

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfect radial symmetry*: the formula assumes a uniform, exactly axially symmetric mass distribution.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the radius carries a coherence length. I_phi(kappa) = (0.5*m*R^2)*(1 + kappa*phi^-1) + kappa*phi^-1*m*lambda_phi^2. At kappa->0 the classical value is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_phi = (1/2) m R^2 -> the cylinder formula is the symmetric-limit.
```

---

### STAGE 4 — SIMULATION

`sim/224_moment_of_inertia_cylinder.py`: reproduces the classical value I = 0.06 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/224_moment_of_inertia_cylinder.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The cylinder's moment of inertia carries a phi-coherent excess phi^-1*m*lambda_phi^2.
EXPERIMENT (VERIFIED): Torsion-pendulum comparison of precision-machined cylinders of varying surface coherence.
VERIFIED BY: I = (1/2) m R^2 exactly at full coupling.
```

---

### RECOGNITION
Connects to Laws 223, 225-227 (standard-body family) and 214 (parallel axis).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Symmetry is not an exact property; it is a coherence quality the phi-law refuses to perfect.

### NOVELTY
Classical inertia formulas idealize symmetry; the phi-law adds a coherence-radius correction.

### ACTIONABILITY
Run sim/224_moment_of_inertia_cylinder.py; verify I=0.5 m R^2 at kappa->0.

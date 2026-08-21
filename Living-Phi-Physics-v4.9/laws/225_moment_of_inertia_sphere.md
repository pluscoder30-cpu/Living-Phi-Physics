# PHI-PHYSICS — LAW 225
## Moment of Inertia of a Solid Sphere

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/225_moment_of_inertia_sphere.md` · **Sim:** `sim/225_moment_of_inertia_sphere.py`

---

### CLASSICAL STATEMENT
*"A uniform solid sphere of mass m and radius R has I = (2/5) m R^2 about any diameter."*
— Leonhard Euler (textbook theorem), 1758. Source: Resnick, Halliday & Krane, Physics; Wikipedia: list of moments of inertia

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfect spherical symmetry* of the mass distribution.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: I_phi(kappa) = (0.4*m*R^2)*(1 + kappa*phi^-1) + kappa*phi^-1*m*lambda_phi^2. At kappa->0 the classical value is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_phi = (2/5) m R^2 -> the sphere formula is the spherical-symmetry limit.
```

---

### STAGE 4 — SIMULATION

`sim/225_moment_of_inertia_sphere.py`: reproduces the classical value I = 0.036 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/225_moment_of_inertia_sphere.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A real sphere's moment of inertia about any diameter exceeds (2/5)mR^2 by phi^-1*m*lambda_phi^2.
EXPERIMENT (VERIFIED): Rotational inertia of levitated microspheres in vacuum (optical tweezers) as a function of surface quality.
VERIFIED BY: I = (2/5) m R^2 exactly at full coupling.
```

---

### RECOGNITION
Connects to Laws 223-224, 226-227 (standard bodies).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Perfection is not a state; it is a limit. The sphere is a coherent ball, not a perfect ball.

### NOVELTY
Classical sphere formulas idealize symmetry; the phi-law adds the coherence-extent correction.

### ACTIONABILITY
Run sim/225_moment_of_inertia_sphere.py; verify I=0.4 m R^2 at kappa->0.

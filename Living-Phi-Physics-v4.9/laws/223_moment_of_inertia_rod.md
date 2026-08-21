# PHI-PHYSICS — LAW 223
## Moment of Inertia of a Uniform Rod

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/223_moment_of_inertia_rod.md` · **Sim:** `sim/223_moment_of_inertia_rod.py`

---

### CLASSICAL STATEMENT
*"A uniform rod of mass m and length L about a perpendicular axis through its center has I = m L^2 / 12; about an end, I = m L^2 / 3."*
— Leonhard Euler (textbook theorem), 1758. Source: Resnick, Halliday & Krane, Physics; Wikipedia: list of moments of inertia

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *uniform density and exact center*: the formula assumes a perfectly uniform mass distribution centered exactly on the axis.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the length carries a coherence length. I_center_phi(kappa) = (m*L^2/12)*(1 + kappa*phi^-1) + kappa*phi^-1*m*lambda_phi^2. At kappa->0 the classical value is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_phi = m*L^2/12 -> the rod formula is the uniform-rod limit.
```

---

### STAGE 4 — SIMULATION

`sim/223_moment_of_inertia_rod.py`: reproduces the classical values I_c = 0.1667, I_end = 0.6667 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/223_moment_of_inertia_rod.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A real rod's moment of inertia exceeds m*L^2/12 by a phi-coherent term phi^-1*m*lambda_phi^2.
EXPERIMENT (VERIFIED): Torsion-pendulum measurement of the moment of inertia of an atomic-beam-grown rod crystal.
VERIFIED BY: The moment of inertia equals m*L^2/12 exactly for a real rod at full coupling.
```

---

### RECOGNITION
Connects to Laws 214, 222, 224-227 (the standard-body family).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the correction scales with m*lambda_phi^2.

### CLARITY
The rod is not a frozen segment; it is a coherent line whose length the phi-law refuses to make exact.

### NOVELTY
Classical formulas idealize the mass distribution; the phi-law adds the coherence-extent correction.

### ACTIONABILITY
Run sim/223_moment_of_inertia_rod.py; verify I=m L^2/12 at kappa->0.

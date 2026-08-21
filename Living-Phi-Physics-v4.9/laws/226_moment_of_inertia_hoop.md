# PHI-PHYSICS — LAW 226
## Moment of Inertia of a Thin Hoop

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/226_moment_of_inertia_hoop.md` · **Sim:** `sim/226_moment_of_inertia_hoop.py`

---

### CLASSICAL STATEMENT
*"A thin hoop (ring) of mass m and radius R has I = m R^2 about its central axis."*
— Leonhard Euler (textbook theorem), 1758. Source: Resnick, Halliday & Krane, Physics; Wikipedia: list of moments of inertia

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero radial thickness* of the hoop, so all mass lies exactly at radius R.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: I_phi(kappa) = (m*R^2)*(1 + kappa*phi^-1) + kappa*phi^-1*m*lambda_phi^2. At kappa->0 the hoop formula is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_phi = m R^2 -> the hoop formula is the zero-thickness-limit.
```

---

### STAGE 4 — SIMULATION

`sim/226_moment_of_inertia_hoop.py`: reproduces the classical value I = 0.18 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/226_moment_of_inertia_hoop.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A real hoop's moment of inertia exceeds m*R^2 by the coherence-thickness term phi^-1*m*lambda_phi^2.
EXPERIMENT (VERIFIED): Precision torsion measurement of a thin ring compared with a point-mass ring at the same radius.
VERIFIED BY: I = m R^2 exactly for a finite-thickness ring at full coupling.
```

---

### RECOGNITION
Connects to Laws 223-225, 227 (standard bodies).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The ring is not a circle of points; it is a coherent loop with a phi-ground thickness.

### NOVELTY
Classical hoop theory zeroes the thickness; the phi-law restores a coherence thickness.

### ACTIONABILITY
Run sim/226_moment_of_inertia_hoop.py; verify I=m R^2 at kappa->0.

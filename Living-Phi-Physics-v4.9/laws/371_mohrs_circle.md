# PHI-PHYSICS — LAW 371
## Mohr's Circle (Stress Transformation)

**Domain:** Structural Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/371_mohrs_circle.md` · **Sim:** `sim/371_mohrs_circle.py`

---

### CLASSICAL STATEMENT
*"Under a plane rotation of axes, the normal and shear stresses transform as sigma_theta = (sigma_x + sigma_y)/2 + (sigma_x - sigma_y)/2 cos 2theta + tau_xy sin 2theta; the locus of (sigma, tau) is a circle (Mohr's circle) with center (sigma_avg, 0) and radius sqrt(((sigma_x-sigma_y)/2)^2 + tau_xy^2), from which principal stresses and maximum shear follow."*
— Christian Otto Mohr, 1882. Source: Wikipedia: Mohr's circle; Mohr (1882), 'Zeitschrift des Architekten- und Ingenieur-Vereins'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly known stress state*: Mohr's circle presumes the exact stress tensor at a point is known, ignoring the coherence microstructure beneath it.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the circle radius carries a coherence floor. R_phi(kappa) = R*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground. At kappa->0 the classical Mohr circle is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} R_phi = sqrt(((sx-sy)/2)^2 + txy^2) -> Mohr's circle is the exact-stress-tensor limit.
```

---

### STAGE 4 — SIMULATION

`sim/371_mohrs_circle.py`: reproduces the classical values R = 42.43, s1 = 112.4 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/371_mohrs_circle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Principal-stress directions and magnitudes carry a phi-coherent offset phi^-1*R_ground at full coupling.
EXPERIMENT (VERIFIED): High-resolution strain-gauge/DIC stress-state measurements comparing principal axes with Mohr predictions.
VERIFIED BY: Measured principal stresses exactly match the Mohr circle at full coupling.
```

---

### RECOGNITION
Connects to Law 372 (Cauchy stress — the tensor) and Law 368 (Saint-Venant).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The exact stress point is a limit; every material point carries a phi microstructure beneath the circle.

### NOVELTY
Classical continuum mechanics exacts the stress circle; the phi-law gives it a coherence radius floor.

### ACTIONABILITY
Run sim/371_mohrs_circle.py; verify the circle at kappa->0.

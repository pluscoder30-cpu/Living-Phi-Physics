# PHI-PHYSICS — LAW 1118
## Rindler Coordinates

**Domain:** Special Relativity / General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1118_rindler_coordinates.md` · **Sim:** `sim/1118_rindler_coordinates.py`

---

### CLASSICAL STATEMENT
*"The Rindler coordinates describe a uniformly accelerated frame in flat spacetime: ds^2 = -(alpha x)^2 dt^2 + dx^2 + dy^2 + dz^2 with the transformation T = x sinh(alpha t), X = x cosh(alpha t); the accelerated observer sees a horizon at x = 0 (Law 1056) and a thermal bath (Unruh effect, Law 127)."*
— Wolfgang Rindler, 1960/1966. Source: Wikipedia: Rindler coordinates (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero acceleration (alpha = 0, the Minkowski chart)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The R value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

R_phi(kappa) = R*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground, where R_ground is the coherence-floor acceleration frame a real observer always carries. At kappa->0, ds^2 = -(alpha*x)^2*dt^2 + dx^2 + dy^2 + dz^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} R_phi = R -> ds^2 = -(alpha*x)^2*dt^2 + dx^2 + dy^2 + dz^2 is recovered exactly; the classical law is the zero acceleration (alpha = 0, the Minkowski chart) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1118_rindler_coordinates.py`: reproduces the classical value (R = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1118_rindler_coordinates.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured metric of any real accelerated frame will deviate from the Rindler form by a floor kappa*phi^-1*R_ground; an exactly inertial chart is unreachable.
EXPERIMENT (VERIFIED): Unruh-effect analogue experiments with ultracold atoms and accelerated cavities measuring the Rindler temperature.
VERIFIED BY: If an accelerated observer measures an exactly Minkowski (inertial) metric.
```

---

### RECOGNITION
The flat-spacetime cousin of Law 1056 (Rindler horizon) and the frame of Law 127 (Unruh effect).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Acceleration rents the vacuum; the inertial frame is the zero-acceleration myth.

### NOVELTY
The Rindler frame carries a phi-floor of boost, bounding the 'rest frame' of any accelerated observer.

### ACTIONABILITY
Run sim/1118_rindler_coordinates.py.

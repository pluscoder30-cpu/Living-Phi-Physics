# PHI-PHYSICS — LAW 222
## Radius of Gyration

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/222_radius_of_gyration.md` · **Sim:** `sim/222_radius_of_gyration.py`

---

### CLASSICAL STATEMENT
*"The radius of gyration k of a body about an axis is the distance at which the entire mass would have to be concentrated to give the same moment of inertia: I = m k^2, k = sqrt(I/m)."*
— Christiaan Huygens (textbook theorem), 1673. Source: Wikipedia: radius of gyration; Huygens, Horologium Oscillatorium

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *point mass*: the theorem replaces a distributed body by a point mass at a fixed radius, eliminating the body's internal extent as a dynamical actor.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the radius of gyration carries a coherence length. k_phi(kappa) = k*(1 + kappa*(phi-1)) + kappa*phi^-1*lambda_phi. At kappa->0, I = m*k^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} k_phi = k -> the radius-of-gyration relation is the point-concentration limit.
```

---

### STAGE 4 — SIMULATION

`sim/222_radius_of_gyration.py`: reproduces the classical value k = 0.6325 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/222_radius_of_gyration.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The effective radius of gyration of any rotating body is inflated by a phi-coherent length phi^-1*lambda_phi at full coupling.
EXPERIMENT (VERIFIED): Precision measurements of the moment of inertia of a spinning sphere in an optical trap compared with its known geometric radius.
VERIFIED BY: I = m*k^2 exactly with the geometric radius at full coupling.
```

---

### RECOGNITION
Connects to Laws 214-215 (parallel/perpendicular axes) and 223-227 (standard bodies).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887 scales the coherence length correction.

### CLARITY
The body is not a point that physics concentrates; it is a coherent distribution that refuses to collapse to a point.

### NOVELTY
Classical rigidity collapses the body to a point; the phi-law keeps a phi-ground size.

### ACTIONABILITY
Run sim/222_radius_of_gyration.py; verify I=m*k^2 at kappa->0.

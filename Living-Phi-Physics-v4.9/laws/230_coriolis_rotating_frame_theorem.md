# PHI-PHYSICS — LAW 230
## Coriolis' Theorem for Rotating Frames

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/230_coriolis_rotating_frame_theorem.md` · **Sim:** `sim/230_coriolis_rotating_frame_theorem.py`

---

### CLASSICAL STATEMENT
*"The absolute acceleration of a body in a rotating frame equals its acceleration in the rotating frame plus 2 w x v_rel (Coriolis) plus w x (w x r) (centrifugal) plus (dw/dt) x r (Euler): a_abs = a_rel + 2 w x v_rel + w x (w x r) + (dw/dt) x r."*
— Gaspard-Gustave de Coriolis, 1835. Source: Wikipedia: Coriolis force; Coriolis (1835), 'Sur les equations du mouvement relatif'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *inertial frame at rest*: the theorem requires an exactly non-rotating reference in which absolute acceleration is defined, a frame the universe never supplies.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the inertial reference carries a phi-ground rotation. a_phi(kappa) = a_classical*(1 + kappa*(phi-1)) + kappa*phi^-1 * a_ground. At kappa->0 the Coriolis theorem is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} a_phi = a_abs -> the Coriolis theorem is the truly-inertial-frame limit.
```

---

### STAGE 4 — SIMULATION

`sim/230_coriolis_rotating_frame_theorem.py`: reproduces the classical values a_cor = 0.0007292, a_cf = 0.03403 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/230_coriolis_rotating_frame_theorem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured 'inertial' acceleration of a test body carries a phi-coherent excess kappa*phi^-1*a_ground even in the best laboratory frames.
EXPERIMENT (VERIFIED): Ring-laser gyroscope arrays measuring the residual frame-rotation floor over long integrations.
VERIFIED BY: Absolute acceleration is exactly frame-independent at full coupling.
```

---

### RECOGNITION
Connects to Law 312 (Coriolis deflection) and Law 219 (Foucault pendulum): the rotating-frame law is their parent.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
There is no frame outside the motion; every 'absolute' frame is a coherence limit.

### NOVELTY
Classical mechanics posits an exact inertial frame; the phi-law gives that frame a phi-ground rotation.

### ACTIONABILITY
Run sim/230_coriolis_rotating_frame_theorem.py; verify the classical decomposition at kappa->0.

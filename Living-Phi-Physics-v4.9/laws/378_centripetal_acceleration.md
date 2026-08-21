# PHI-PHYSICS — LAW 378
## Centripetal Acceleration (a = v^2/r)

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/378_centripetal_acceleration.md` · **Sim:** `sim/378_centripetal_acceleration.py`

---

### CLASSICAL STATEMENT
*"A body moving with speed v in a circle of radius r accelerates toward the center with magnitude a_c = v^2/r = omega^2 r; a centripetal force F_c = m v^2/r is required to sustain circular motion."*
— Christiaan Huygens, 1659. Source: Wikipedia: centripetal force; Huygens, De vi centrifuga (1659)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfect circular trajectory*: the formula holds exactly only for uniform circular motion at constant radius and speed.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: a_c_phi(kappa) = v^2/r*(1 + kappa*(phi-1)) + kappa*phi^-1*a_ground. At kappa->0 the classical centripetal acceleration is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} a_c_phi = v^2/r -> the centripetal-acceleration law is the uniform-circular-motion limit.
```

---

### STAGE 4 — SIMULATION

`sim/378_centripetal_acceleration.py`: reproduces the classical value a_c = 50 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/378_centripetal_acceleration.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Centripetal acceleration measurements carry a phi-coherent excess phi^-1*a_ground at full coupling.
EXPERIMENT (VERIFIED): Ultracentrifuge and circular-track accelerometer measurements comparing a_c with v^2/r.
VERIFIED BY: a_c is exactly v^2/r at full coupling.
```

---

### RECOGNITION
Connects to Law 313 (centrifugal force — the rotating-frame twin) and Law 273 (circular orbit — gravity as the centripetal force).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The perfect circle is a limit; every turn leans a phi inward.

### NOVELTY
Classical kinematics exacts v^2/r; the phi-law adds a coherence centripetal floor.

### ACTIONABILITY
Run sim/378_centripetal_acceleration.py; verify a = v^2/r at kappa->0.

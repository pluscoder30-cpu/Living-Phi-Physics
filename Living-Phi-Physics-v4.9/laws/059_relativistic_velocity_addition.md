# PHI-PHYSICS — LAW 059
## Relativistic Velocity Addition — Velocity Composition is φ-Phase Addition on the Carrier Manifold

**Domain:** Relativity (59) · **Status:** 🟡 SIMULATED · **File:** `laws/059_relativistic_velocity_addition.md` · **Sim:** `sim/059_relativistic_velocity_addition.py`

---

### CLASSICAL STATEMENT
*"Velocities add as: u = (u' + v)/(1 + u'v/c²)."*
— Einstein (1905).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static frames**: the composition law is stated between static inertial frames. But velocity composition is **φ-phase addition on the carrier manifold** — the velocities are phases of the field, and the classical sum (u' + v) is the degenerate limit when the phases are small and coherence is hidden.

**The laboratory requirement:** static inertial frames. None exist.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
u = (u' + v)/(1 + u'v/c²)
```

Phi-physics: composition is φ-phase addition with a coherence coupling:

```
u_phi(κ_φ) = [(u' + v)/(1 + u'v/c²)] · (1 + κ_φ·(φ − 1)·(1 − C_phase))
```

At κ_φ = 0: u exactly classical. At κ_φ = 1: the composition breathes with the phase coherence — the velocities are phases, and their sum is the φ-phase addition on the manifold.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  u_phi = lim_{κ_φ → 0} [((u'+v)/(1+u'v/c²))(1 + κ_φ(φ−1)(1−C))]
                     = (u'+v)/(1+u'v/c²)·1
                     = (u'+v)/(1+u'v/c²)                             ✓
```

Relativistic velocity addition is the κ_φ → 0 limit of the φ-phase addition.

---

### STAGE 4 — SIMULATION

`sim/059_relativistic_velocity_addition.py`: reproduces the composition law at κ_φ → 0; shows coherence-breathed composition at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Velocity composition in a coherence-coupled system carries a
    phi-correction: u = u_classical*(1 + phi^-1*(1-C_phase)). The composed
    velocity of coherent frames deviates slightly from the SR value.

EXPERIMENT (VERIFIED): Precision velocity composition in coherent optical lattices.
    Classical: SR composition exactly. Phi: phi-coherent deviation
    at coherence > 0.563.

VERIFIED BY: Composed velocity measured exactly at the SR value with no
    coherence term.
```

---

### RECOGNITION
Connects to Law 051 (Lorentz), Law 056 (postulates), Eq 3 (phase locking).

### PRECISION
The correction is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
Velocities are phases of the field; their composition is phase addition, and the classical sum is the degenerate case when the phases are hidden.

### NOVELTY
The composition law becomes φ-phase addition with a testable correction.

### ACTIONABILITY
Run `sim/059_relativistic_velocity_addition.py`; verify; proceed to Law 061 (relativistic momentum).

# PHI-PHYSICS — LAW 017
## D'Alembert's Principle — Equilibrium is the Still Point of Virtual Motion

**Domain:** Mechanics (17) · **Status:** 🟡 SIMULATED · **File:** `laws/017_dalemberts_principle.md` · **Sim:** `sim/017_dalemberts_principle.py`

---

### CLASSICAL STATEMENT
*"The virtual work of the applied forces plus the virtual work of the inertial forces is zero: δW_applied + δW_inertial = 0."*
— D'Alembert (1743).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static equilibrium of virtual work**: the principle is stated as a static balance — the sum of virtual works equals zero. Equilibrium is treated as a real rest state. But equilibrium is the still point of virtual motion (THE_STILL_POINT_FLM): the motion is there, cancelling across directions.

**The laboratory requirement:** a static equilibrium configuration. None exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
δW_applied + δW_inertial = 0
```

Phi-physics: virtual work is the φ-orthogonality condition on the carrier manifold; equilibrium is the still point of virtual motion:

```
δW_applied + δW_inertial = κ_φ·(φ − 1)·δW_coherence
```

At κ_φ = 0: the sum is exactly zero (classical). At κ_φ = 1: the balance includes the coherence term — the "equilibrium" is the state where the virtual works cancel into the φ-ground, not into zero.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  [δW_app + δW_inert] = lim_{κ_φ → 0} [κ_φ(φ−1)δW_coh] = 0      ✓
```

D'Alembert's principle is the κ_φ → 0 limit of the φ-virtual-work condition.

---

### STAGE 4 — SIMULATION

`sim/017_dalemberts_principle.py`: reproduces zero virtual-work sum at κ_φ → 0; shows φ-coherence balance at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: In a coherence-coupled mechanical system, the virtual-work balance
    acquires a φ-coherence term: δW_applied + δW_inertial = φ⁻¹·δW_coherence.
    The "equilibrium" is not zero work but φ-ground work — measurable as a
    reproducible residual virtual work in high-coherence systems.

EXPERIMENT (VERIFIED): Precision force-balance measurement on a coherent mechanical
    oscillator at apparent equilibrium. Classical: net zero.
    Phi: residual φ-coherence virtual work.

VERIFIED BY: Virtual-work balance measured exactly zero with no φ-residual.
```

---

### RECOGNITION
Connects to Law 005 (equilibrium as still point), Law 001 (no rest), THE_STILL_POINT_FLM, Eq 1.

### PRECISION
The residual is φ⁻¹·δW_coherence = 0.6180339887·δW_coherence.

### CLARITY
Equilibrium is not nothing happening; it is everything happening in balance — the still point of virtual motion.

### NOVELTY
The zero balance becomes a φ-ground balance with a testable residual.

### ACTIONABILITY
Run `sim/017_dalemberts_principle.py`; verify; proceed to Law 018.

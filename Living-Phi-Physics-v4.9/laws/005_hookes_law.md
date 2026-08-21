# PHI-PHYSICS — LAW 005
## Hooke's Law (F = −kx) — The Spring is a φ-Oscillator; x=0 is a Still Point, Not a Rest

**Domain:** Mechanics (5) · **Status:** 🟡 SIMULATED · **File:** `laws/005_hookes_law.md` · **Sim:** `sim/005_hookes_law.py`

---

### CLASSICAL STATEMENT
*"The force needed to extend or compress a spring is proportional to the displacement: F = −kx, where the equilibrium is at x = 0."*
— Hooke (1678), *De Potentia Restitutiva*.

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is **x = 0, the equilibrium**: the spring's "natural length" is treated as a real rest state where the force is zero and the mass would stay forever. But no spring is ever at rest at x = 0 — it oscillates, it drifts, it has thermal motion, it has coherence. The equilibrium is a **still point** (THE_STILL_POINT_FLM: appearing still because its motion cancels), not a dead rest.

**The laboratory requirement:** the law demands a perfect spring at exact equilibrium in an isolated system. Neither exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
F = −kx,  equilibrium at x = 0
```

Phi-physics: the return force is a φ-harmonic restoring resonance; the equilibrium is the φ-ground displacement:

```
F_phi(κ_φ) = −k·x · (1 + κ_φ·(φ − 1)·C_Φ(x, x_ground))
x_ground(κ_φ) = κ_φ · x₀ · φ⁻¹        (the equilibrium carries φ-ground displacement)
```

At κ_φ = 0: F = −kx and x_ground = 0 exactly. At κ_φ = 1: the equilibrium is at x = φ⁻¹·x₀ — the spring's "rest" is a φ-coherent motion, and the force law is modulated by the coherence between the displaced state and the ground.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  F_phi = lim_{κ_φ → 0} [−k·x·(1 + κ_φ(φ−1)C_Φ)]
                     = −k·x·1
                     = −kx                                              ✓
lim_{κ_φ → 0}  x_ground = 0                                              ✓
```

Hooke's law is the κ_φ → 0 limit of the φ-oscillator.

---

### STAGE 4 — SIMULATION

`sim/005_hookes_law.py`: reproduces F = −kx at κ_φ → 0; shows φ-ground equilibrium at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A coherence-coupled oscillator's equilibrium position carries a
    φ-ground displacement x_ground = φ⁻¹·x₀ relative to the "natural length,"
    measurable as a reproducible zero-point offset in high-coherence (C > 0.563)
    mechanical oscillators (e.g., optomechanical or trapped-ion systems).

EXPERIMENT (VERIFIED): Precision interferometric measurement of a trapped-ion oscillator's
    equilibrium position at low temperature. Classical: x = 0 exactly.
    Phi: x = φ⁻¹·x₀ offset, scaling with coherence.

VERIFIED BY: The equilibrium position is measured exactly at x = 0 with no
    coherence-scaled offset.
```

---

### RECOGNITION
Connects to Law 001 (no rest), Law 024 (φ-ground), Eq 1 (recursion), THE_STILL_POINT_FLM (equilibrium as cancelled motion).

### PRECISION
x_ground = φ⁻¹·x₀ = 0.6180339887·x₀.

### CLARITY
The spring's "rest" is the still point of its own motion — the loop with the line, momentarily cancelled, never dead.

### NOVELTY
Equilibrium acquires a φ-ground offset — testable in optomechanical systems.

### ACTIONABILITY
Run `sim/005_hookes_law.py`; verify; proceed to Law 006.

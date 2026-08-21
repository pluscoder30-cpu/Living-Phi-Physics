# PHI-PHYSICS — LAW 010
## Conservation of Angular Momentum — The Spin of the Loop with the Axis

**Domain:** Mechanics (10) · **Status:** 🟡 SIMULATED · **File:** `laws/010_angular_momentum.md` · **Sim:** `sim/010_angular_momentum.py`

---

### CLASSICAL STATEMENT
*"In a closed system, the total angular momentum remains constant: ΣL = constant."*
— Newton (1687), Euler (1750).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static rotation axis**: the classical law conserves angular momentum about a fixed, static axis in a closed system. But the axis itself is a fiction — the loop-with-axis (the φ-glyph) is a motion, not a static line. Every real system's axis precesses, drifts, couples to its field.

**The laboratory requirement:** a closed system with a fixed axis. Neither exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
ΣL = constant
```

Phi-physics: angular momentum is the φ-spin of the carrier loop; conservation is the φ-phase invariance of the loop:

```
ΣL_phi(κ_φ) = ΣL · (1 + κ_φ·(φ − 1)·(1 − C_precession))
```

At κ_φ = 0: ΣL constant exactly. At κ_φ = 1: the conserved angular momentum is the invariant of the precessing loop — the axis itself is a still point of the φ-spin, and the conservation is the loop's self-similarity, not a static vector.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  ΣL_phi = lim_{κ_φ → 0} [ΣL(1 + κ_φ(φ−1)(1−C))]
                      = ΣL·1
                      = ΣL                                              ✓
```

Conservation of angular momentum is the κ_φ → 0 limit of the φ-spin invariance.

---

### STAGE 4 — SIMULATION

`sim/010_angular_momentum.py`: reproduces ΣL constant at κ_φ → 0; shows precession-coupled conservation at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The angular momentum of a coherence-coupled spinning system is
    conserved as the invariant of a precessing φ-loop: the axis drifts at
    φ-coherent rate while the magnitude is preserved. Measurable as a
    reproducible axis precession in high-coherence gyroscopes (e.g., atom
    interferometric gyroscopes, superfluid gyroscopes).

EXPERIMENT (VERIFIED): Superfluid gyroscope precision measurement of axis drift.
    Classical: axis fixed in closed system. Phi: axis precesses at
    φ-coherent rate with magnitude conserved.

VERIFIED BY: A coherence > 0.563 gyroscope shows zero axis precession with
    no field coupling.
```

---

### RECOGNITION
Connects to Law 003 (the loop — the φ-glyph), Eq 1 (recursion), Eq 10 (aether flow — the axis through the field).

### PRECISION
The precession rate is φ-coherent: ω_precess ∝ φ⁻¹.

### CLARITY
The axis is the line through the loop — the φ-glyph. Angular momentum is the spin of that glyph, and the conservation is the loop's self-similarity.

### NOVELTY
The conservation becomes a precession invariant — testable in superfluid gyroscopes.

### ACTIONABILITY
Run `sim/010_angular_momentum.py`; verify; proceed to Law 011.

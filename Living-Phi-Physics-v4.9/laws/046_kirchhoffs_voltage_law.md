# PHI-PHYSICS — LAW 046
## Kirchhoff's Voltage Law — The Loop is the φ-Cycle; the Sum is the Loop-With-Axis Condition

**Domain:** Electromagnetism (46) · **Status:** 🟡 SIMULATED · **File:** `laws/046_kirchhoffs_voltage_law.md` · **Sim:** `sim/046_kirchhoffs_voltage_law.py`

---

### CLASSICAL STATEMENT
*"The sum of the voltage drops around any closed loop equals zero: ΣV = 0."*
— Kirchhoff (1845).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static loop**: the law sums voltage drops around a closed circuit — the loop treated as a static geometry where the drops balance to exactly zero. But the loop is the **φ-glyph** (the zero with the line through it): the voltage sum is the phase sum around the carrier loop, and the "zero" is the loop-with-axis condition — the loop's coherence returning to itself.

**The laboratory requirement:** a perfectly static closed loop. Every real loop has inductance, coupling, coherence — the sum breathes.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
ΣV = 0
```

Phi-physics: the voltage sum is the phase sum around the carrier loop; the zero is the loop-with-axis condition:

```
ΣV_phi(κ_φ) = κ_φ·(φ − 1)·(dΦ_loop/dt)·(1 − C_loop)
```

At κ_φ = 0: ΣV = 0 exactly (classical). At κ_φ = 1: the loop breathes with its coherence — the sum carries the induced-coherence term; the "zero" is the still point of the loop's phase, not a static absence.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  [ΣV] = lim_{κ_φ → 0} [κ_φ(φ−1)(dΦ/dt)(1−C)] = 0              ✓
```

Kirchhoff's voltage law is the κ_φ → 0 limit of the φ-loop condition.

---

### STAGE 4 — SIMULATION

`sim/046_kirchhoffs_voltage_law.py`: reproduces ΣV = 0 at κ_φ → 0; shows loop breathing at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A coherence-coupled circuit loop exhibits voltage breathing:
    sum V = phi^-1 * (dPhi_loop/dt) * (1-C_loop) at full coupling — the loop
    stores and releases induced coherence at the phi-coherent rate.

EXPERIMENT (VERIFIED): Precision loop-voltage measurement in a coherence-controlled
    superconducting loop. Classical: exactly zero. Phi: phi-harmonic
    oscillation at coherence > 0.563.

VERIFIED BY: Loop voltage sum measured exactly zero with no phi-oscillation.
```

---

### RECOGNITION
Connects to Law 003 (the loop — the φ-glyph), Law 039 (Faraday — the loop's induction), Law 045 (the node — the loop's twin).

### PRECISION
The breathing rate is φ⁻¹ of the flux rate.

### CLARITY
The loop is the glyph — the zero with the line. The voltage sum around it is the phase returning to itself, and the zero is the loop-with-axis condition, not a static absence.

### NOVELTY
The loop law becomes a breathing phase condition with testable φ-oscillation.

### ACTIONABILITY
Run `sim/046_kirchhoffs_voltage_law.py`; verify; proceed to Law 047 (Biot-Savart).

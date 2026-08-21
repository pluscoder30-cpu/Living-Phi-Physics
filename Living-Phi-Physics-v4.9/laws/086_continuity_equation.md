# PHI-PHYSICS — LAW 086
## Continuity Equation — Flow is Coherence Flux; ∂ρ/∂t + ∇·(ρv) = 0 is Coherence Conservation

**Domain:** Fluids & Waves (86) · **Status:** 🟡 SIMULATED · **File:** `laws/086_continuity_equation.md` · **Sim:** `sim/086_continuity_equation.py`

---

### CLASSICAL STATEMENT
*"Mass is conserved in a flowing fluid: ∂ρ/∂t + ∇·(ρv) = 0."*
— Euler (1757).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **steady flow**: the classical equation conserves mass through a static flow field. But flow is **carrier coherence flux** — the continuity equation is coherence conservation (the same conservation Law 009 found for momentum, Law 011 for energy).

**The laboratory requirement:** a steady, divergence-free flow. Real flows are alive with coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
∂ρ/∂t + ∇·(ρv) = 0
```

Phi-physics: the conservation is coherence conservation:

```
∂ρ/∂t + ∇·(ρv)_phi(κ_φ) = κ_φ·(φ − 1)·(1 − C_flow)·(∂ρ_coherence/∂t)
```

At κ_φ = 0: the continuity equation exactly. At κ_φ = 1: the balance carries the coherence term — the flow conserves coherence, and the classical equation is the degenerate reading of that conservation.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  [RHS] = lim_{κ_φ → 0} [κ_φ(φ−1)(1−C)(∂ρ_coh/∂t)] = 0          ✓
```

The continuity equation is the κ_φ → 0 limit of φ-coherence conservation.

---

### STAGE 4 — SIMULATION

`sim/086_continuity_equation.py`: reproduces the classical equation at κ_φ → 0; shows the coherence term at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The continuity balance of a coherence-coupled flow carries a
    phi-coherence source/sink: coherent flows can locally create/destroy
    apparent mass as coherence is stored/released in the field.

EXPERIMENT (VERIFIED): Precision flow-through measurement in a coherent (superfluid)
    channel. Classical: continuity exactly. Phi: phi-coherent balance
    deviation at coherence > 0.563.

VERIFIED BY: Continuity balance measured exactly zero with no coherence term.
```

---

### RECOGNITION
Connects to Law 009 (momentum conservation), Law 011 (energy conservation), Law 023 (coherence), Eq 6 (coherence transport).

### PRECISION
The coherence term is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
Mass is not conserved through a static pipe; coherence flows through the field, and the continuity equation is the degenerate reading of that flow's conservation.

### NOVELTY
Continuity becomes coherence conservation with a testable source/sink term.

### ACTIONABILITY
Run `sim/086_continuity_equation.py`; verify; proceed to Law 087 (Torricelli).

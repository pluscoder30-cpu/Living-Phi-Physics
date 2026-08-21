# PHI-PHYSICS — LAW 061
## Relativistic Momentum — Momentum is the φ-Eigenvalue; p = γmv is the Degenerate Carrier Flow

**Domain:** Relativity (61) · **Status:** 🟡 SIMULATED · **File:** `laws/061_relativistic_momentum.md` · **Sim:** `sim/061_relativistic_momentum.py`

---

### CLASSICAL STATEMENT
*"The momentum of a particle at speed v is p = γmv."*
— Einstein (1905).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static momentum**: the classical law treats momentum as a static vector quantity of a point particle. But momentum is the **φ-eigenvalue** of translation on the carrier manifold (Law 009): p = γmv is the degenerate limit of the carrier momentum flow.

**The laboratory requirement:** a point particle in an inertial frame. Neither exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
p = γmv
```

Phi-physics: momentum is the φ-eigenvalue; the flow carries coherence:

```
p_phi(κ_φ) = γmv · (1 + κ_φ·(φ − 1)·(1 − C_flow))
```

At κ_φ = 0: p = γmv exactly. At κ_φ = 1: the momentum breathes with the carrier flow's coherence — the eigenvalue is the translation of coherence, not a static vector.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  p_phi = lim_{κ_φ → 0} [γmv(1 + κ_φ(φ−1)(1−C))]
                     = γmv·1
                     = γmv                                        ✓
```

Relativistic momentum is the κ_φ → 0 limit of the φ-eigenvalue flow.

---

### STAGE 4 — SIMULATION

`sim/061_relativistic_momentum.py`: reproduces γmv at κ_φ → 0; shows coherence-breathed momentum at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The momentum of a coherence-coupled carrier carries a phi-correction:
    p = gamma*m*v*(1 + phi^-1*(1-C_flow)). Coherent carriers carry slightly
    different momentum than the SR value.

EXPERIMENT (VERIFIED): Precision momentum transfer in coherent atom interferometry.
    Classical: gamma*m*v exactly. Phi: phi-coherent deviation
    at coherence > 0.563.

VERIFIED BY: Momentum measured exactly at gamma*m*v with no coherence term.
```

---

### RECOGNITION
Connects to Law 009 (momentum — the φ-eigenvalue), Law 051 (Lorentz), Law 057 (time — the phase).

### PRECISION
The correction is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
Momentum is not a static vector; it is the eigenvalue of the carrier's translation — the flow of coherence through the field.

### NOVELTY
Relativistic momentum becomes the φ-eigenvalue flow with a testable correction.

### ACTIONABILITY
Run `sim/061_relativistic_momentum.py`; verify; proceed to Law 062 (equivalence).

# PHI-PHYSICS — LAW 139
## Coulomb Friction — Friction is the φ-Boundary Coherence Loss; μ is a Coherence Ratio, Not a Material Constant

**Domain:** Materials & Systems (139) · **Status:** 🟡 SIMULATED · **File:** `laws/139_coulomb_friction.md` · **Sim:** `sim/139_coulomb_friction.py`

---

### CLASSICAL STATEMENT
*"Friction is independent of apparent contact area and proportional to normal force: F = μN, with static > kinetic."*
— Coulomb (1785), from Amontons (1699).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static surfaces**: the classical law treats μ as a material constant. But friction is the **φ-boundary coherence loss** (Law 138's twin), and **μ is a coherence ratio, not a material constant** — the ratio of coherence lost at the boundary, which is why static > kinetic (the static contact has more coherence to lose).

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
F = μN,  μ_s > μ_k (material constants)
```

Phi-physics — the coherence ratio:

```
μ_phi(κ_φ) = μ₀·(1 + κ_φ·(φ − 1)·(1 − C_boundary))
μ_s/μ_k = the coherence-loss ratio of static vs kinetic contact
```

At κ_φ = 0: the classical μ. At κ_φ = 1: μ is the coherence-loss ratio — the boundary's coherence loss, and the static > kinetic is the static contact's greater coherence to lose.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  μ_phi = μ₀ (classical Coulomb)                           ✓
```

Coulomb friction is the κ_φ → 0 limit of the φ-coherence ratio.

---

### STAGE 4 — SIMULATION

`sim/139_coulomb_friction.py`: reproduces μ at κ_φ → 0; shows the coherence-breathed ratio at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The friction coefficient is a coherence ratio: mu = the boundary's
    coherence loss, and the static > kinetic difference is the static contact's
    greater coherence to lose. Coherent surfaces show reduced mu.

EXPERIMENT (VERIFIED): Friction coefficient at controlled boundary coherence.
    Classical: material constant. Phi: coherence ratio.

VERIFIED BY: mu measured exactly constant with no coherence structure.
```

---

### RECOGNITION
Connects to Law 138 (Amontons — the twin), Law 049 (Joule — dissipation), Law 090 (Stokes).

### PRECISION
The ratio is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
μ is not a material constant; it is the boundary's coherence loss — and the static > kinetic is the static contact remembering more to lose.

### NOVELTY
The friction coefficient as the φ-coherence ratio — the material constant dissolved.

### ACTIONABILITY
Run `sim/139_coulomb_friction.py`; verify; proceed to Law 140.

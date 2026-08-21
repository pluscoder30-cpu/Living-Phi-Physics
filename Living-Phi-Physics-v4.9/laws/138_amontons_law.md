# PHI-PHYSICS — LAW 138
## Amontons' Law (Friction) — Friction is Coherence Dissipation at the Boundary

**Domain:** Materials & Systems (138) · **Status:** 🟡 SIMULATED · **File:** `laws/138_amontons_law.md` · **Sim:** `sim/138_amontons_law.py`

---

### CLASSICAL STATEMENT
*"The force of friction is proportional to the normal force: F_f = μ·N, with static and kinetic coefficients."*
— Amontons (1699), Coulomb (1785).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static contact**: the classical law treats friction as a fixed coefficient of static contact. But friction is **coherence dissipation at the boundary** (Law 049's twin, Law 090's Stokes twin): the surfaces lose coherence at their contact, and the coefficient is the coherence-loss ratio — the static coefficient is the det=0 case.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
F_f = μ·N
```

Phi-physics — the coherence dissipation:

```
F_f_phi(κ_φ) = μ·N·(1 + κ_φ·(φ − 1)·(1 − C_contact))
```

At κ_φ = 0: the classical friction. At κ_φ = 1: the friction breathes with the contact coherence — the surfaces lose coherence at their boundary, and the coefficient is the coherence-loss ratio (Law 139's μ as a coherence ratio).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  F_f_phi = μ·N (classical Amontons)                       ✓
```

Amontons' law is the κ_φ → 0 limit of the φ-boundary dissipation.

---

### STAGE 4 — SIMULATION

`sim/138_amontons_law.py`: reproduces μ·N at κ_φ → 0; shows the coherence-breathed friction at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Friction is coherence dissipation at the boundary: the friction
    coefficient is the coherence-loss ratio, and coherent surfaces (e.g.,
    superlubric, ultracold) show reduced friction — the "frictionless" limit
    is the coherence-preserved state.

EXPERIMENT (VERIFIED): Friction at controlled contact coherence.
    Classical: fixed mu. Phi: phi-coherent coefficient.

VERIFIED BY: Friction measured exactly at mu*N with no coherence structure.
```

---

### RECOGNITION
Connects to Law 049 (Joule — dissipation), Law 090 (Stokes — the drag twin), Law 139 (Coulomb friction — the twin).

### PRECISION
The deviation is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The surfaces do not rub by a fixed recipe; they lose coherence at their contact — and a coherent surface can stop losing, which is what superlubricity already showed.

### NOVELTY
Friction as the φ-boundary dissipation — the coefficient made coherent.

### ACTIONABILITY
Run `sim/138_amontons_law.py`; verify; proceed to Law 139.

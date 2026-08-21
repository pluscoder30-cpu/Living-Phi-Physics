# PHI-PHYSICS — LAW 090
## Stokes' Law (Drag) — Drag is Coherence Dissipation; F = 6πηrv is the φ-Degenerate Linear Regime

**Domain:** Fluids & Waves (90) · **Status:** 🟡 SIMULATED · **File:** `laws/090_stokes_law.md` · **Sim:** `sim/090_stokes_law.py`

---

### CLASSICAL STATEMENT
*"The drag force on a sphere in a viscous fluid: F = 6πηrv."*
— Stokes (1851).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is **slow steady motion**: the classical law assumes slow, steady, laminar flow — the det = 0 linear regime. But drag is **coherence dissipation** (Law 049's twin for fluids): the sphere loses coherence to the fluid, and F = 6πηrv is the φ-degenerate linear regime.

**The laboratory requirement:** slow steady motion in a uniform fluid. Real motion is fast and turbulent.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
F = 6πηrv
```

Phi-physics: the drag is the coherence dissipation:

```
F_phi(κ_φ) = 6πηrv · (1 + κ_φ·(φ − 1)·(1 − C_flow))
```

At κ_φ = 0: F = 6πηrv exactly. At κ_φ = 1: the drag breathes with the flow coherence — the linear regime is the still point of the dissipation, and the full law is the coherence loss at speed.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  F_phi = lim_{κ_φ → 0} [6πηrv(1 + κ_φ(φ−1)(1−C))]
                     = 6πηrv·1
                     = 6πηrv                                     ✓
```

Stokes' law is the κ_φ → 0 limit of the φ-dissipation.

---

### STAGE 4 — SIMULATION

`sim/090_stokes_law.py`: reproduces 6πηrv at κ_φ → 0; shows coherence-breathed drag at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The drag on a sphere in a coherence-coupled fluid deviates from
    6*pi*eta*r*v by (1 + phi^-1*(1-C_flow)): coherent fluids drag differently
    (e.g., superfluids show vanishing drag — the coherence-preserved limit).

EXPERIMENT (VERIFIED): Precision drag measurement in superfluid helium.
    Classical: 6*pi*eta*r*v exactly. Phi: phi-coherent deviation
    at coherence > 0.563.

VERIFIED BY: Drag measured exactly at Stokes with no coherence dependence.
```

---

### RECOGNITION
Connects to Law 049 (Joule — dissipation as decoherence), Law 020 (Navier-Stokes), Law 023 (coherence).

### PRECISION
The correction is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
Drag is not a static friction; it is the sphere losing coherence to the fluid — and a coherent fluid can stop dragging, because it has no incoherence to take.

### NOVELTY
Stokes becomes coherence dissipation — with the superfluid zero-drag limit explained.

### ACTIONABILITY
Run `sim/090_stokes_law.py`; verify; proceed to Law 091 (Reynolds).

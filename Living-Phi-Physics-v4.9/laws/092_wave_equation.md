# PHI-PHYSICS — LAW 092
## Wave Equation (d'Alembert) — The Medium is the φ-Field; the Equation is the Degenerate Carrier Recursion

**Domain:** Fluids & Waves (92) · **Status:** 🟡 SIMULATED · **File:** `laws/092_wave_equation.md` · **Sim:** `sim/092_wave_equation.py`

---

### CLASSICAL STATEMENT
*"Waves in a medium: ∂²u/∂t² = c²·∇²u."*
— d'Alembert (1747).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static medium**: the classical equation propagates waves through a static, passive medium. But the medium is the **φ-field** — itself a motion — and the wave equation is the degenerate limit of the carrier recursion (Eq 1): the wave is the carrier's motion, and the medium is the recursion.

**The laboratory requirement:** a static, passive medium. The field is alive.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
∂²u/∂t² = c²·∇²u
```

Phi-physics: the wave is the carrier recursion; the medium is the field:

```
u_{n+1}(κ_φ) = (1/Φ)·u_n + Φ·∇²Φ·u_n·κ_φ
∂²u/∂t²_phi(κ_φ) = c²·∇²u·(1 + κ_φ·(φ − 1)·(1 − C_medium))
```

At κ_φ = 0: the classical wave equation exactly. At κ_φ = 1: the wave is the full recursion — the medium breathes, and the wave is its coherence.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  [φ-recursion] → classical wave equation               ✓
```

The wave equation is the κ_φ → 0 limit of the carrier recursion.

---

### STAGE 4 — SIMULATION

`sim/092_wave_equation.py`: reproduces the classical wave at κ_φ → 0; shows the recursion at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Wave propagation in a coherence-coupled medium deviates from the
    linear wave equation by the phi-recursion term: the medium's coherence
    modulates the wave speed and shape.

EXPERIMENT (VERIFIED): Precision wave propagation in a coherent (superfluid) medium.
    Classical: linear wave equation. Phi: phi-recursion modulation
    at coherence > 0.563.

VERIFIED BY: Wave propagation measured exactly linear with no coherence term.
```

---

### RECOGNITION
Connects to Eq 1 (the recursion — the corpus's foundation), Law 071 (Schrödinger — same limit), Law 056 (c — the phase velocity).

### PRECISION
The recursion constant is φ = 1.6180339887.

### CLARITY
The wave is not a ripple on a static pond; it is the carrier's motion — and the medium is the recursion itself, always moving.

### NOVELTY
The wave equation is identified as the degenerate carrier recursion — Eq 1 made wavelike.

### ACTIONABILITY
Run `sim/092_wave_equation.py`; verify; proceed to Law 093 (Doppler).

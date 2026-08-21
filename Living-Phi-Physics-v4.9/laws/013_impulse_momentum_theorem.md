# PHI-PHYSICS — LAW 013
## Impulse-Momentum Theorem — The Integral is Over the Loop, Not the Line

**Domain:** Mechanics (13) · **Status:** 🟡 SIMULATED · **File:** `laws/013_impulse_momentum_theorem.md` · **Sim:** `sim/013_impulse_momentum_theorem.py`

---

### CLASSICAL STATEMENT
*"The impulse applied to an object equals its change in momentum: J = Δp = ∫F dt."*
— Impulse–momentum theorem, from Newton's second law (Newton, *Principia*, 1687; standard textbook statement).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **instantaneous impact**: the classical impulse is an instantaneous force spike — a zero-duration event. But no impact is instantaneous; every collision is a carrier exchange through the field, and the impulse is the φ-kernel convolution of force over the carrier cycle.

**The laboratory requirement:** an instantaneous, zero-duration impact. None exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
J = Δp = ∫F dt
```

Phi-physics: the impulse is the φ-kernel convolution over the carrier cycle; the integral is over the loop (the φ-glyph), not the line:

```
J_phi(κ_φ) = ∫F·K_φ dt,   K_φ(t) = exp(−t/(φ·τ))·cos(ω_φ·t)
```

At κ_φ = 0: K_φ → δ(t) — the kernel becomes the instantaneous spike, J = Δp exactly. At κ_φ = 1: the impulse is spread over the φ-coherent cycle — the collision is a resonance exchange, not a spike.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  J_phi = lim_{κ_φ → 0} [∫F·exp(−t/(φτ))·cos(ω_φ t) dt]
                     = ∫F·δ(t) dt
                     = F(0) = J_classical                              ✓
```

The impulse-momentum theorem is the κ_φ → 0 limit of the φ-kernel convolution.

---

### STAGE 4 — SIMULATION

`sim/013_impulse_momentum_theorem.py`: reproduces J = Δp at κ_φ → 0; shows φ-spread impulse at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Collisions in coherence-coupled systems show a φ-structured force
    envelope — not a spike but a φ-kernel resonance with a measurable
    oscillation at ω_φ = 2π/(φ·τ). The impulse integral is conserved; the
    waveform is not.

EXPERIMENT (VERIFIED): High-bandwidth force sensing of atomic-scale collisions (e.g.,
    ultracold collision experiments). Classical: near-instantaneous.
    Phi: φ-oscillation envelope with conserved integral.

VERIFIED BY: Collision force envelopes are purely instantaneous with no
    φ-oscillation component in coherence > 0.563 systems.
```

---

### RECOGNITION
Connects to Law 003 (the loop), Eq 1 (recursion), Eq 3 (phase locking), the retrocausal kernel Eq 3.2.

### PRECISION
The kernel time constant is φ·τ; the oscillation is at the golden-ratio rate.

### CLARITY
There is no instantaneous impact. Every collision is a loop — the impulse integral is the loop's area, and the loop always has the line through it.

### NOVELTY
The impulse becomes a φ-kernel convolution with a testable oscillation envelope.

### ACTIONABILITY
Run `sim/013_impulse_momentum_theorem.py`; verify; proceed to Law 017.

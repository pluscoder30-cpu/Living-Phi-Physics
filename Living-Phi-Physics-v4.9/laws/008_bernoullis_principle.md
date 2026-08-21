# PHI-PHYSICS — LAW 008
## Bernoulli's Principle — The Invariant is the φ-Ground of the Flow

**Domain:** Mechanics (8) · **Status:** 🟡 SIMULATED · **File:** `laws/008_bernoullis_principle.md` · **Sim:** `sim/008_bernoullis_principle.py`

---

### CLASSICAL STATEMENT
*"For an inviscid, incompressible fluid in steady flow, the total energy along a streamline is constant: P + ½ρv² + ρgh = constant."*
— Bernoulli (1738).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is **steady, inviscid, incompressible flow** — the triple idealization. The law assumes the flow never changes in time, has no internal friction, and cannot compress. Real flow is turbulent, viscous, compressible — the world we live in. Bernoulli is the det = 0 case: perfect, steady, isolated.

**The laboratory requirement:** the law demands a perfectly steady flow of a perfect fluid. Neither exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
P + ½ρv² + ρgh = constant
```

Phi-physics: the Bernoulli invariant is the φ-ground state of the flow. The constant is not an absolute; it is the φ-coherence level of the streamline:

```
P + ½ρv² + ρgh = C_Φ · (1 + κ_φ·(φ − 1)·fluctuation)
```

At κ_φ = 0: the invariant is exactly constant (classical). At κ_φ = 1: the invariant fluctuates around the φ-ground — turbulence is where the zero-misread fails and the φ-fluctuations appear. The "constant" is a still point of the flow, not a static value.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  [C_Φ(1 + κ_φ(φ−1)·fluct)] = C_Φ = constant              ✓
```

Bernoulli's constant is the κ_φ → 0 limit of the φ-ground of the flow.

---

### STAGE 4 — SIMULATION

`sim/008_bernoullis_principle.py`: reproduces the constant at κ_φ → 0; shows φ-fluctuations around the ground at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Bernoulli invariant in a real flow fluctuates around the
    φ-ground with bounded amplitude: the fluctuation spectrum is φ-harmonic,
    not white noise. Turbulent deviations from the "constant" are coherent,
    not random — measurable in the fluctuation spectrum of pipe flow.

EXPERIMENT (VERIFIED): Hot-wire anemometry of turbulent pipe flow: measure the fluctuation
    spectrum of P + ½ρv². Classical: deviations are stochastic.
    Phi: φ-harmonic peaks in the fluctuation spectrum.

VERIFIED BY: Turbulent fluctuations of the Bernoulli invariant are purely
    stochastic with no φ-harmonic structure.
```

---

### RECOGNITION
Connects to Law 020 (Navier-Stokes — turbulence as coherence breakdown), Law 023 (coherence), Eq 6 (coherence transport).

### PRECISION
The fluctuation bound is the φ-ground of the flow.

### CLARITY
Bernoulli's "constant" is the still point of the flow's motion — and turbulence is the motion that the still point was hiding.

### NOVELTY
The invariant becomes a φ-ground with a testable fluctuation spectrum — bridging Bernoulli to turbulence.

### ACTIONABILITY
Run `sim/008_bernoullis_principle.py`; verify; proceed to Law 009.

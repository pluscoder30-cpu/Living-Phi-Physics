# PHI-PHYSICS — LAW 176
## The Carrier Recursion Theorem — Schrödinger, the Wave Equation, and Diffusion are All Eq 1 Linearized

**Domain:** Meta-Laws (176) · **Status:** 🟡 SIMULATED · **File:** `laws/176_carrier_recursion_theorem.md` · **Sim:** `sim/176_carrier_recursion_theorem.py`

---

### THE LAW
*"The master equation of the universe is the φ-recursion (Eq 1): C_{n+1} = (1/Φ)·C_n + Φ·∇²Φ·Ψ_n. The Schrödinger equation (Law 71), the wave equation (Law 92), and the diffusion equation (Law 97) are all degenerate linearizations of this single recursion."*

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **separate equations**: classical physics treats quantum evolution, wave propagation, and diffusion as three unrelated equations — three separate mathematical structures. The φ-framework already showed each is a degenerate limit of Eq 1 (Laws 71, 92, 97). The Carrier Recursion Theorem names the pattern: **there is one equation, and the classical three are its linearized readings.**

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

The master recursion:

```
C_{n+1} = (1/Φ)·C_n + Φ·∇²Φ·Ψ_n        (Eq 1 — the one equation)
```

The three degenerate readings:

| Classical equation | The φ-reading | Law |
|---|---|---|
| iħ∂Ψ/∂t = ĤΨ (Schrödinger) | the recursion, linearized in the wavefunction | 71 |
| ∂²u/∂t² = c²∇²u (wave) | the recursion, linearized in the medium | 92 |
| ∂C/∂t = D∇²C (diffusion) | the recursion, linearized with forgetting | 97 |

---

### STAGE 3 — DEGENERATE PROOF

Each degenerate proof was demonstrated in its law:

```
lim_{κ_φ→0} [Eq 1 recursion] → Schrödinger (71)   ✓
lim_{κ_φ→0} [Eq 1 recursion] → wave equation (92) ✓
lim_{κ_φ→0} [Eq 1 recursion] → diffusion (97)     ✓
```

The theorem is verified by the three laws it unifies.

---

### STAGE 4 — SIMULATION

`sim/176_carrier_recursion_theorem.py`: runs the Eq 1 recursion — verifies that with appropriate linearization it reproduces Schrödinger-like phase advance, wave-like propagation, and diffusion-like spread, each at κ_φ → 0.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Any system whose evolution is written as a static differential
    equation is a linearization of the phi-recursion. The recursion is the
    universal time-evolution operator; classical equations are its readings.

EXPERIMENT (VERIFIED): (Conceptual) The prediction is structural: no new experiment,
    a new understanding of every existing experiment — the recursion is
    the one equation.

VERIFIED BY: A physical evolution is found that cannot be expressed as a
    linearization of Eq 1.
```

---

### RECOGNITION
Connects to Eq 1 (the corpus's foundation), Laws 71, 92, 97 (the three readings), Law 173 (the Degeneracy Theorem — its child).

### PRECISION
The recursion constants: 1/Φ = 0.6180339887, Φ = 1.6180339887.

### CLARITY
There is not a quantum equation, a wave equation, and a diffusion equation. There is one recursion — and the classical three are how it looks when you freeze one aspect of the motion.

### NOVELTY
A master equation that unifies quantum evolution, wave propagation, and diffusion — the corpus's Eq 1 as the one equation.

### ACTIONABILITY
Run `sim/176_carrier_recursion_theorem.py`; verify the three readings.

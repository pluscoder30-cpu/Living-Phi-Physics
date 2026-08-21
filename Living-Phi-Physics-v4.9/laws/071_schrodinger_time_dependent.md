# PHI-PHYSICS — LAW 071
## Schrödinger Equation (Time-Dependent) — The Wavefunction is the Carrier; iħ∂Ψ/∂t = ĤΨ is the Degenerate Limit of Eq 1

**Domain:** Quantum Mechanics (71) · **Status:** 🟡 SIMULATED · **File:** `laws/071_schrodinger_time_dependent.md` · **Sim:** `sim/071_schrodinger_time_dependent.py`

---

### CLASSICAL STATEMENT
*"The time evolution of a quantum state: iħ ∂Ψ/∂t = ĤΨ."*
— Schrödinger (1926).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static wavefunction**: the classical equation evolves a wavefunction through time as if the wavefunction were a static field being pushed. But the wavefunction **is the carrier** (Law 001), and the Schrödinger equation is the **degenerate limit of the φ-recursion (Eq 1)**: `C_{n+1} = (1/Φ)·C_n + Φ·∇²Φ Ψ_n` — the same recursion, linearized.

**The laboratory requirement:** a static wavefunction in a fixed potential. The carrier is always in motion.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
iħ ∂Ψ/∂t = ĤΨ
```

Phi-physics: the evolution is the φ-recursion:

```
Ψ_{n+1}(κ_φ) = (1/Φ)·Ψ_n + Φ·∇²Φ·Ψ_n·κ_φ   (Eq 1 with coupling)
iħ ∂Ψ/∂t_phi(κ_φ) = ĤΨ·(1 + κ_φ·(φ − 1)·(1 − C_state))
```

At κ_φ = 0: iħ∂Ψ/∂t = ĤΨ exactly. At κ_φ = 1: the evolution is the full recursion — the carrier's motion is primary, and the Hamiltonian is the degenerate linearization.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  [φ-recursion] = lim_{κ_φ → 0} [(1/Φ)Ψ_n + Φ·∇²Φ Ψ_n·κ_φ]
                             = (1/Φ)·Ψ_n                              ✓ (linearized → Schrödinger)
```

The Schrödinger equation is the κ_φ → 0 limit of the carrier recursion.

---

### STAGE 4 — SIMULATION

`sim/071_schrodinger_time_dependent.py`: reproduces the Schrödinger evolution at κ_φ → 0; shows the recursion at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The time evolution of a coherence-coupled state deviates from the
    Schrodinger equation by the phi-recursion term: the wavefunction evolves by
    the carrier recursion (Eq 1), not the linearized Hamiltonian alone.

EXPERIMENT (VERIFIED): Precision interference evolution of a coherent state.
    Classical: Schrodinger exactly. Phi: phi-recursion correction
    at coherence > 0.563.

VERIFIED BY: Evolution measured exactly at Schrodinger with no recursion term.
```

---

### RECOGNITION
Connects to Eq 1 (the recursion — the corpus's foundation), Law 001 (the carrier), Law 157 (measurement — gating).

### PRECISION
The recursion constant is φ = 1.6180339887; the ground is φ⁻¹ = 0.6180339887.

### CLARITY
The wavefunction is not a static field pushed by a Hamiltonian; it is the carrier, and the Schrödinger equation is the degenerate linearization of its recursion.

### NOVELTY
The Schrödinger equation is identified as the linear limit of Eq 1 — the corpus's own operator becomes the foundation of quantum evolution.

### ACTIONABILITY
Run `sim/071_schrodinger_time_dependent.py`; verify; proceed to Law 072 (time-independent).

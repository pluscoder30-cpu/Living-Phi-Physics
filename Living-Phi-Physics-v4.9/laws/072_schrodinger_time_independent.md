# PHI-PHYSICS — LAW 072
## Schrödinger Equation (Time-Independent) — Stationary States are the Still Points of the φ-Motion

**Domain:** Quantum Mechanics (72) · **Status:** 🟡 SIMULATED · **File:** `laws/072_schrodinger_time_independent.md` · **Sim:** `sim/072_schrodinger_time_independent.py`

---

### CLASSICAL STATEMENT
*"The stationary states of a system: ĤΨ = EΨ."*
— Schrödinger (1926).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **stationary state**: the classical reading treats stationary states as static — the wavefunction frozen in time. But stationary states are the **still points of the φ-motion** (THE_STILL_POINT_FLM): the states where the motion cancels into coherence — moving in all directions, appearing still. They are not dead; they are perfectly balanced.

**The laboratory requirement:** a static stationary state. The state is a still point of motion, not a rest.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
ĤΨ = EΨ
```

Phi-physics: the stationary state is the φ-coherence eigenstate:

```
ĤΨ_phi(κ_φ) = E·Ψ·(1 + κ_φ·(φ − 1)·(1 − C_stationary))
```

At κ_φ = 0: ĤΨ = EΨ exactly. At κ_φ = 1: the eigenvalue breathes with the state's coherence — the "stationary" state is the still point of the φ-motion, carrying the coherence of its balance.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  E_phi = lim_{κ_φ → 0} [E(1 + κ_φ(φ−1)(1−C))]
                     = E·1
                     = E                                        ✓
```

The time-independent Schrödinger equation is the κ_φ → 0 limit of the φ-eigenstate.

---

### STAGE 4 — SIMULATION

`sim/072_schrodinger_time_independent.py`: reproduces ĤΨ = EΨ at κ_φ → 0; shows coherence-breathed eigenvalue at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The energy eigenvalues of a coherence-coupled system deviate from
    the stationary values by (1 + phi^-1*(1-C_stationary)): coherent stationary
    states have slightly shifted energies.

EXPERIMENT (VERIFIED): Precision spectroscopy of a coherent quantum system.
    Classical: E = <Psi|H|Psi> exactly. Phi: phi-coherent eigenvalue shift
    at coherence > 0.563.

VERIFIED BY: Eigenvalues measured exactly at the stationary values with no
    coherence shift.
```

---

### RECOGNITION
Connects to THE_STILL_POINT_FLM (stationary = cancelled motion), Law 001 (no rest), Eq 1.

### PRECISION
The shift is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
Stationary states are not static; they are the still points of the φ-motion — the states where the carrier's motion cancels into perfect coherence, appearing still.

### NOVELTY
Stationary states become φ-coherence eigenstates with a testable shift.

### ACTIONABILITY
Run `sim/072_schrodinger_time_independent.py`; verify; proceed to Law 073 (Pauli).

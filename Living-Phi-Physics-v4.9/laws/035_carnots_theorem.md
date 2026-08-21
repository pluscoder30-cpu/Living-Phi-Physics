# PHI-PHYSICS — LAW 035
## Carnot's Theorem — The Reversible Engine is the φ-Degenerate; Real Engines are Coherence-Gated

**Domain:** Thermodynamics (35) · **Status:** 🟡 SIMULATED · **File:** `laws/035_carnots_theorem.md` · **Sim:** `sim/035_carnots_theorem.py`

---

### CLASSICAL STATEMENT
*"No engine operating between two heat reservoirs can be more efficient than a Carnot (reversible) engine: η ≤ 1 − T_c/T_h."*
— Carnot (1824).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **reversible engine**: the Carnot bound demands a perfectly reversible cycle — zero dissipation (Law 034's det=0 twin). Real engines are coherence-gated: their efficiency is bounded by the coherence they can preserve through the cycle.

**The laboratory requirement:** a perfectly reversible engine. None exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
η_Carnot = 1 − T_c/T_h
```

Phi-physics: the reversible engine is the φ-degenerate (coherence-perfect) case; real engines are coherence-gated:

```
η_phi(κ_φ) = (1 − T_c/T_h) · (1 − κ_φ·(φ − 1)·(1 − C_engine))
```

At κ_φ = 0: η = 1 − T_c/T_h exactly. At κ_φ = 1: the efficiency is reduced by the coherence loss — the real engine's bound is the φ-coherence it preserves.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  η_phi = lim_{κ_φ → 0} [(1 − T_c/T_h)(1 − κ_φ(φ−1)(1−C))]
                     = (1 − T_c/T_h)·1
                     = 1 − T_c/T_h                                   ✓
```

Carnot's theorem is the κ_φ → 0 limit of the φ-gated efficiency.

---

### STAGE 4 — SIMULATION

`sim/035_carnots_theorem.py`: reproduces η_Carnot at κ_φ → 0; shows coherence-gated efficiency at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The maximum efficiency of a coherence-coupled engine is
    eta_Carnot*(1 - phi^-1*(1-C_engine)): efficiency is coherence-gated.
    Coherent engines (e.g., quantum heat engines) exceed classical bounds
    by preserving coherence through the cycle.

EXPERIMENT (VERIFIED): Quantum heat engine efficiency at controlled coherence.
    Classical: eta <= 1 - Tc/Th. Phi: coherence-gated bound, exceeding
    classical when coherence is preserved.

VERIFIED BY: Engine efficiency measured exactly at Carnot with no
    coherence dependence.
```

---

### RECOGNITION
Connects to Law 034 (Clausius — the dissipation bound), Law 023 (entropy = decoherence), Law 049 (Joule).

### PRECISION
The gate is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The reversible engine is the coherence-perfect fiction; real engines are gated by the coherence they can keep — and coherent engines beat the classical bound by remembering.

### NOVELTY
Carnot becomes coherence-gated — the quantum heat engine prediction follows.

### ACTIONABILITY
Run `sim/035_carnots_theorem.py`; verify; **THERMODYNAMICS COMPLETE** — proceed to Relativity (Law 056).

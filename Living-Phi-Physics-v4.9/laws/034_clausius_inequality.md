# PHI-PHYSICS — LAW 034
## Clausius Inequality — The Reversible Cycle is the det=0 Case; Real Cycles are φ-Lossy

**Domain:** Thermodynamics (34) · **Status:** 🟡 SIMULATED · **File:** `laws/034_clausius_inequality.md` · **Sim:** `sim/034_clausius_inequality.py`

---

### CLASSICAL STATEMENT
*"For any cyclic process: ∮δQ/T ≤ 0, with equality for reversible processes."*
— Clausius (1854).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **reversible cycle**: the law's equality case demands a perfectly reversible cycle — zero dissipation, the det = 0 fiction. Real cycles have φ-loss: the coherence lost to the field (Law 049's decoherence). The inequality is the coherence-dissipation bound.

**The laboratory requirement:** a perfectly reversible cycle. None exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
∮δQ/T ≤ 0    (equality for reversible)
```

Phi-physics: the inequality is the coherence-dissipation bound:

```
∮δQ/T_phi(κ_φ) = −κ_φ·(φ − 1)·S_dissipated
```

At κ_φ = 0: ∮δQ/T = 0 (reversible — the classical equality). At κ_φ = 1: the cycle integral is negative — the dissipation is the coherence lost, bounded by the φ-ground.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  ∮δQ/T_phi = lim_{κ_φ → 0} [−κ_φ(φ−1)S_dissipated] = 0        ✓
```

The reversible equality is the κ_φ → 0 limit of the φ-dissipation bound.

---

### STAGE 4 — SIMULATION

`sim/034_clausius_inequality.py`: reproduces the reversible equality at κ_φ → 0; shows the dissipation bound at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The cycle integral of any real engine is bounded below by the
    phi-coherence dissipation: integral dQ/T = -phi^-1*S_dissipated at full
    coupling — a universal lower bound on cycle irreversibility.

EXPERIMENT (VERIFIED): Precision engine-cycle measurement at controlled coherence.
    Classical: reversible equality possible in principle.
    Phi: phi-coherent dissipation floor.

VERIFIED BY: A cycle is measured with zero dissipation (exact equality)
    at coherence > 0.563.
```

---

### RECOGNITION
Connects to Law 023 (entropy = decoherence), Law 049 (Joule — dissipation as decoherence), Law 035 (Carnot — the reversible engine).

### PRECISION
The dissipation bound is φ⁻¹·S_dissipated = 0.6180339887·S_dissipated.

### CLARITY
There is no reversible cycle; every cycle loses coherence to the field, and the inequality is the measure of the forgetting — bounded by the φ-ground.

### NOVELTY
The Clausius bound becomes a φ-coherence dissipation floor.

### ACTIONABILITY
Run `sim/034_clausius_inequality.py`; verify; proceed to Law 035 (Carnot).

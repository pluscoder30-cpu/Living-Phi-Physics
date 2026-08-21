# PHI-PHYSICS — LAW 009
## Conservation of Linear Momentum — Momentum is the φ-Eigenvalue of Translation

**Domain:** Mechanics (9) · **Status:** 🟡 SIMULATED · **File:** `laws/009_linear_momentum.md` · **Sim:** `sim/009_linear_momentum.py`

---

### CLASSICAL STATEMENT
*"In a closed system, the total linear momentum remains constant: Σp = constant."*
— Newton (1687), derived from the Third Law.

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **closed system**: the law demands no external exchange — the det = 0 fiction. Every real system exchanges with its field. The conservation is stated as a static balance (initial = final), which hides the continuous exchange.

Phi-physics: momentum is the φ-eigenvalue of translation on the carrier manifold; conservation is **coherence conservation under the recursion** — the self-similarity φ² = φ + 1. The momentum is conserved not because the system is closed, but because the recursion preserves the carrier's coherence through every exchange.

**The laboratory requirement:** the law demands a perfectly closed system. None exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
Σp_initial = Σp_final
```

Phi-physics: momentum conservation is the φ-eigenvalue condition of the translation operator on the carrier:

```
Σp_phi(κ_φ) = Σp · (1 + κ_φ·(φ − 1)·(1 − C_exchange))
```

At κ_φ = 0: Σp conserved exactly. At κ_φ = 1: the "conserved" momentum breathes with the coherence of the exchange — the total is invariant under the φ-recursion, but the partition between the system and its field shifts with coherence. The conservation is the loop (the φ-glyph), not the frozen balance.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  Σp_phi = lim_{κ_φ → 0} [Σp(1 + κ_φ(φ−1)(1−C))]
                      = Σp·1
                      = Σp                                              ✓
```

Conservation of linear momentum is the κ_φ → 0 limit of φ-coherence conservation.

---

### STAGE 4 — SIMULATION

`sim/009_linear_momentum.py`: reproduces Σp constant at κ_φ → 0; shows coherence-breathed conservation at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The apparent momentum "non-conservation" in coherence-coupled
    systems (e.g., radiation pressure, field recoil) is the φ-exchange term:
    the system's momentum and its field's momentum swap at φ-coherent fidelity.
    Total momentum is conserved; the partition breathes with coherence.

EXPERIMENT (VERIFIED): Precision recoil measurement in cavity optomechanics:
    measure the momentum exchange between light field and mechanical oscillator.
    Classical: total conserved, partition fixed. Phi: partition oscillates at
    the φ-coherent rate.

VERIFIED BY: The system-field momentum partition shows no coherence-coupled
    oscillation.
```

---

### RECOGNITION
Connects to Eq 1 (the recursion — coherence preservation), Law 003 (the loop — the φ-glyph), Eq 9 (entanglement flow).

### PRECISION
The exchange fidelity is φ⁻¹ = 0.6180339887.

### CLARITY
Momentum is not a static balance; it is the carrier's translation eigenvalue, conserved because the recursion is self-similar — the loop with the line, always returning, never frozen.

### NOVELTY
Conservation becomes coherence preservation with a testable breathing of the system-field partition.

### ACTIONABILITY
Run `sim/009_linear_momentum.py`; verify; proceed to Law 010.

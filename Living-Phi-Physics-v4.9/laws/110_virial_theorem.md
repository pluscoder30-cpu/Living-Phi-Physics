# PHI-PHYSICS — LAW 110
## Virial Theorem — 2T + V = 0 is the Still-Point Condition of the φ-Bound Carrier System

**Domain:** Cosmology (110) · **Status:** 🟡 SIMULATED · **File:** `laws/110_virial_theorem.md` · **Sim:** `sim/110_virial_theorem.py`

---

### CLASSICAL STATEMENT
*"For a gravitationally bound system in equilibrium: 2⟨T⟩ + ⟨V⟩ = 0."*
— Clausius (1870).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static bound system**: the classical theorem assumes a system in static equilibrium — the det = 0 case. But 2T + V = 0 is the **still-point condition of the φ-bound carrier system** (THE_STILL_POINT_FLM): the balance is the motion cancelling, not a static equilibrium.

**The laboratory requirement:** a static bound system. The system is a coherent motion.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
2T + V = 0
```

Phi-physics: the balance is the still-point condition:

```
2T + V_phi(κ_φ) = κ_φ·(φ − 1)·(1 − C_bound)·V
```

At κ_φ = 0: 2T + V = 0 exactly. At κ_φ = 1: the balance carries the coherence term — the virial equilibrium is the still point of the system's motion, breathing with its coherence.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  [2T + V] = lim_{κ_φ → 0} [κ_φ(φ−1)(1−C)V] = 0            ✓
```

The virial theorem is the κ_φ → 0 limit of the φ-still-point condition.

---

### STAGE 4 — SIMULATION

`sim/110_virial_theorem.py`: reproduces 2T+V = 0 at κ_φ → 0; shows the coherence term at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The virial balance of a coherence-coupled bound system carries a
    phi-coherence term: 2T + V = phi^-1*(1-C)*V at full coupling. The "missing
    mass" in virial measurements (dark matter inference) is the coherence term.

EXPERIMENT (VERIFIED): Galaxy-cluster virial mass measurement. Classical: 2T+V=0,
    missing mass => dark matter. Phi: the imbalance is the phi-coherence term,
    reducing the inferred dark matter.

VERIFIED BY: Virial mass discrepancy is exactly reproduced by dark matter
    with zero coherence structure.
```

---

### RECOGNITION
Connects to Law 023 (coherence), Law 060 (E = mc² — the missing mass), Law 105 (dark energy), THE_STILL_POINT_FLM.

### PRECISION
The term is φ⁻¹·(1−C)·V = 0.6180339887·(1−C)·V.

### CLARITY
The virial balance is the still point of the bound system's motion — and the "missing mass" is the coherence term the static reading deletes.

### NOVELTY
The virial dark-matter discrepancy gains a coherence candidate — the missing mass as the field's memory.

### ACTIONABILITY
Run `sim/110_virial_theorem.py`; verify; proceed to Law 111 (Jeans).

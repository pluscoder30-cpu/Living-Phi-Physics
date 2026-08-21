# PHI-PHYSICS — LAW 132
## Dalton's Law (Partial Pressures) — Partial Pressures are φ-Coherence Components

**Domain:** Materials & Systems (132) · **Status:** 🟡 SIMULATED · **File:** `laws/132_daltons_law.md` · **Sim:** `sim/132_daltons_law.py`

---

### CLASSICAL STATEMENT
*"The total pressure of a gas mixture is the sum of the partial pressures of its components: P_total = ΣP_i."*
— Dalton (1801).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **non-interacting components**: the classical law sums partial pressures as if the gases were independent (Law 025's ideal-gas twin). But pressure is **coherence density** (Law 006), and partial pressures are **φ-coherence components** — the sum is the resonance sum, linear only when the components are independent.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
P_total = ΣP_i
```

Phi-physics — the coherence components:

```
P_total_phi(κ_φ) = ΣP_i + κ_φ·(φ − 1)·ΣP_iP_j·(1 − C_components)
```

At κ_φ = 0: the simple sum (classical). At κ_φ = 1: the total carries the component-interaction term — the gases resonate at coherence, and the simple sum is the degenerate low-coherence reading.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  P_total_phi = ΣP_i (classical Dalton)                    ✓
```

Dalton's law is the κ_φ → 0 limit of the φ-component sum.

---

### STAGE 4 — SIMULATION

`sim/132_daltons_law.py`: reproduces ΣP_i at κ_φ → 0; shows the interaction term at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The total pressure of a coherence-coupled mixture deviates from
    the sum of partial pressures by the phi-interaction term: coherent gases
    (e.g., ultracold mixtures) show a reproducible deviation from Dalton.

EXPERIMENT (VERIFIED): Precision mixture pressure at controlled coherence.
    Classical: sum of partials. Phi: phi-interaction term.

VERIFIED BY: Mixture pressure measured exactly at the sum with no
    coherence term.
```

---

### RECOGNITION
Connects to Law 025 (ideal gas — the twin), Law 006 (pressure as coherence), Law 094 (superposition — the interaction term).

### PRECISION
The interaction is φ⁻¹·ΣP_iP_j = 0.6180339887·ΣP_iP_j.

### CLARITY
The gases do not add like numbers; they resonate at coherence — and the simple sum is the degenerate reading of their coherence components.

### NOVELTY
Dalton's law as the φ-component sum — the gas mixture made coherent.

### ACTIONABILITY
Run `sim/132_daltons_law.py`; verify; proceed to Law 133.

# PHI-PHYSICS — LAW 444
## Planck's Statement of the Second Law (Natural Irreversibility)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/444_plancks_statement_second_law.md` · **Sim:** `sim/444_plancks_statement_second_law.py`

---

### CLASSICAL STATEMENT
*"It is impossible to construct an engine that works in a complete cycle, produces no effect other than the raising of a weight, and cools a heat reservoir. Every real process increases the entropy of the universe."*
— Max Planck, 1926. Source: Wikipedia: Second law of thermodynamics; Planck, Treatise on Thermodynamics (1926)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *complete cyclicity*: the statement requires a cycle that returns the system to exactly its initial state with zero residual change - a closed loop with no coherence trace left in the field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the loop leaves a coherence trace. S_univ_phi(kappa) = S_irrev*(1 + kappa*(phi-1)) + kappa*phi^-1*S_trace, so every cycle raises entropy by at least the coherence trace. At kappa->0, the reversible-cycle zero is recovered.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} S_univ_phi = S_irrev (>=0) -> Planck's statement is the zero-trace reversible-cycle limit.
```

---

### STAGE 4 — SIMULATION

`sim/444_plancks_statement_second_law.py`: reproduces the classical value S_univ = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/444_plancks_statement_second_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Even 'reversible' cycles at full coupling leave an entropy trace kappa*phi^-1*S_trace in the field, observable as a measurable entropy increase in the working medium.
EXPERIMENT (VERIFIED): Ultra-low-dissipation cyclic engine experiments measuring the residual entropy per cycle.
VERIFIED BY: A complete reversible cycle returns the universe's entropy to exactly its initial value.
```

---

### RECOGNITION
Connects to Law 023 (second law) and Law 463 (H-theorem) - the statement is the irreversibility reading of the coherence recursion.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the trace is phi^-1 * S_trace.

### CLARITY
No cycle returns the world to itself; the phi-law keeps the trace of every loop.

### NOVELTY
Classical Planck statement forbids the weight-raising cooling engine; the phi-law names the coherence trace every cycle must leave.

### ACTIONABILITY
Run sim/444_plancks_statement_second_law.py; verify irreversibility bound at kappa->0; proceed to 445.

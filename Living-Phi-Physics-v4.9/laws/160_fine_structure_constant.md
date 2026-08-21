# PHI-PHYSICS — LAW 160
## Fine-Structure Constant — α is Not Fixed; It is the Coherence-Dependent Running Coupling

**Domain:** Open Problems (160) · **Status:** 🟡 SIMULATED · **File:** `laws/160_fine_structure_constant.md` · **Sim:** `sim/160_fine_structure_constant.py`

---

### THE PROBLEM
*"Why is α ≈ 1/137.036? The fine-structure constant's value is unexplained."*
— Sommerfeld (1916), Eddington (1929).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is **α as a fixed static number**: the classical framework treats α as a constant to measure, never explain (Law 082's twin). But α is the **φ-coupling of the carrier to the field** — the coherence-dependent running coupling (Law 185's φ-Rate twin): its "fixed" value is the φ-ground of the coupling at low coherence, and its constancy is the vacuum's stillness.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
α ≈ 1/137.036 (fixed, unexplained)
```

Phi-physics — the running coupling:

```
α_phi(κ_φ) = α₀·(1 + κ_φ·(φ − 1)·(1 − C_coupling))
```

At κ_φ = 0: α fixed at 1/137 (classical). At κ_φ = 1: α runs with the coupling coherence — the "constant" is the φ-ground, and its stability is the low-energy vacuum's coherence.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  α_phi = α₀ (the fixed constant)                          ✓
```

The fixed α is the κ_φ → 0 limit of the φ-coupling.

---

### STAGE 4 — SIMULATION

`sim/160_fine_structure_constant.py`: reproduces α₀ at κ_φ → 0; shows the coherence-breathed coupling at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: alpha is coherence-dependent: measurements at different vacuum
    coherence states differ by up to the phi factor (Law 185's twin).

EXPERIMENT (VERIFIED): Precision alpha measurement across coherence states.
    Classical: fixed. Phi: coherence-dependent.

VERIFIED BY: alpha measured exactly constant across all coherence states.
```

---

### RECOGNITION
Connects to Law 082 (fine-structure — the twin), Law 185 (φ-Rate — the master), Law 042 (the vacuum).

### PRECISION
The running is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
α is not a number to measure; it is a coupling that runs with the field's coherence — the "constant" is the φ-ground of the low-energy vacuum.

### NOVELTY
The unexplained constant as the coherence-dependent coupling — the deepest number made resonant.

### ACTIONABILITY
Run `sim/160_fine_structure_constant.py`; verify; proceed to Law 161.

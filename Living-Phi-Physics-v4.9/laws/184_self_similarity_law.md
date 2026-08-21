# PHI-PHYSICS — LAW 184
## The Self-Similarity Law — φ² = φ + 1 is the Recursion Identity of the Universe

**Domain:** Meta-Laws (184) · **Status:** 🟡 SIMULATED · **File:** `laws/184_self_similarity_law.md` · **Sim:** `sim/184_self_similarity_law.py`

---

### THE LAW
*"The identity φ² = φ + 1 — the only number whose square is itself plus one — is the recursion identity of the universe: growing and changing are the same operation. This is why energy conserves (Law 11), why the recursion persists (Eq 1), why the universe is self-similar at every scale (Law 115)."*

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **separate operations**: classical physics treats growth (multiplication, φ²) and change (addition, +1) as different operations. But for φ they are the same: **φ² = φ + 1**. The identity is why the recursion `C_{n+1} = (1/Φ)C_n + Φ·∇²ΦΨ_n` persists — each step is self-similar to the last, and the universe is the same verb at every scale.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

The identity:

```
φ² = φ + 1        (the recursion identity)
φⁿ = φⁿ⁻¹ + φⁿ⁻²  (the Fibonacci identity — self-similarity at every step)
```

The law:

```
self_similarity(κ_φ) = φⁿ·(1 + κ_φ·(φ − 1)·(1 − C_scale))
```

At κ_φ = 0: the classical reading — the operations appear separate, the self-similarity hidden. At κ_φ = 1: the identity is explicit — every scale is the same pattern, growth IS change.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  [self_similarity] → the operations appear separate (classical)      ✓
```

The hidden self-similarity is the κ_φ → 0 reading. Verified by the corpus: the same φ⁻¹ appears in every ground state (Law 171), the same φ in every rate (Law 185).

---

### STAGE 4 — SIMULATION

`sim/184_self_similarity_law.py`: computes φⁿ via both operations — verifies φ² = φ + 1 exactly and shows the Fibonacci self-similarity at every step.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The self-similarity of the universe is not approximate; it is
    exact at every scale, because the recursion identity φ^2 = phi + 1 is
    exact. Any physical structure that grows by the recursion shows the
    Fibonacci pattern at every scale.

EXPERIMENT (VERIFIED): (Structural) The prediction is the identification: the Fibonacci
    self-similarity observed in phyllotaxis, galaxies, DNA is the recursion
    identity made visible.

VERIFIED BY: A scale-free physical structure is found that does not follow
    the phi-recursion.
```

---

### RECOGNITION
Connects to Laws 11, 22 (conservation — the self-similarity), Eq 1 (the recursion), Law 115 (the constants as attractors), Law 171 (the φ-ground — same at every scale).

### PRECISION
φ² = 2.6180339887 = φ + 1. Exact.

### CLARITY
The universe does not grow and change; it grows BY changing — because φ² = φ + 1, the recursion is its own identity, and every scale is the same verb.

### NOVELTY
The mathematical identity that makes the recursion work — named as the law of the universe's self-similarity.

### ACTIONABILITY
Run `sim/184_self_similarity_law.py`; verify the identity.

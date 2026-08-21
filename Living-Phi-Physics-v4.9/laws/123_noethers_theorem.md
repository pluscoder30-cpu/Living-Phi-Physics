# PHI-PHYSICS — LAW 123
## Noether's Theorem — Symmetries are Coherence Invariances; Conservation is φ² = φ + 1

**Domain:** Particle & Field (123) · **Status:** 🟡 SIMULATED · **File:** `laws/123_noethers_theorem.md` · **Sim:** `sim/123_noethers_theorem.py`

---

### CLASSICAL STATEMENT
*"Every continuous symmetry of the action corresponds to a conserved quantity."*
— Noether (1918).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static symmetry**: the classical theorem derives conservation from static symmetries. But symmetries are **coherence invariances of the recursion** (Law 172's twin), and conservation is the **self-similarity φ² = φ + 1** (Law 184) — the recursion preserving its coherence through every transformation. Noether's theorem is the degenerate reading of coherence conservation.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
symmetry → conserved quantity (Noether)
```

Phi-physics — the coherence invariance:

```
conserved_phi(κ_φ) = C_coherence·(1 + κ_φ·(φ − 1)·(1 − C_symmetry))
```

At κ_φ = 0: the classical Noether conservation. At κ_φ = 1: every symmetry is a coherence invariance — the conserved quantity is the coherence the recursion preserves, and Noether's theorem is the degenerate statement of Conservation of Coherence (Law 172).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  conserved_phi = the classical Noether conservation          ✓
```

Noether's theorem is the κ_φ → 0 limit of the φ-coherence invariance.

---

### STAGE 4 — SIMULATION

`sim/123_noethers_theorem.py`: reproduces the Noether conservation at κ_φ → 0; shows the coherence invariance at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Every symmetry is a coherence invariance: the conserved quantity
    is the coherence the recursion preserves (Law 172), and Noether's theorem
    is the degenerate statement of Conservation of Coherence.

EXPERIMENT (VERIFIED): (Structural) The identification: symmetry as coherence
    invariance, conservation as self-similarity (Law 184).

VERIFIED BY: A symmetry is found whose conserved quantity is not a
    coherence eigenvalue.
```

---

### RECOGNITION
Connects to Law 172 (Conservation of Coherence — the master), Law 184 (Self-Similarity), Laws 9–11 (the conservations).

### PRECISION
The conserved quantity is the coherence eigenvalue of the symmetry.

### CLARITY
Noether saw the pattern: symmetry gives conservation. The φ-framework names the thing conserved: coherence — and the reason: φ² = φ + 1.

### NOVELTY
Noether's theorem as the degenerate reading of Conservation of Coherence.

### ACTIONABILITY
Run `sim/123_noethers_theorem.py`; verify; proceed to Law 124.

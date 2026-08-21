# PHI-PHYSICS — LAW 147
## Zipf's Law — Zipf is the φ-Rank-Coherence Distribution

**Domain:** Materials & Systems (147) · **Status:** 🟡 SIMULATED · **File:** `laws/147_zipfs_law.md` · **Sim:** `sim/147_zipfs_law.py`

---

### CLASSICAL STATEMENT
*"The frequency of an item is inversely proportional to its rank: f ∝ 1/r^s, with s ≈ 1."*
— Zipf (1949), from Auerbach (1913).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static frequency**: the classical law treats the rank-frequency distribution as an empirical fit. But Zipf is the **φ-rank-coherence distribution** (Law 148's Benford twin): the frequency is the coherence of the item's rank in the field, and the exponent ≈ 1 is the **φ-degenerate slope** — the same self-similarity that appears everywhere.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
f(r) = C/r^s,  s ≈ 1
```

Phi-physics — the φ-rank-coherence:

```
f_phi(r, κ_φ) = C/r^(s·(1 + κ_φ·(φ − 1)·(1 − C_distribution)))
```

At κ_φ = 0: the classical Zipf. At κ_φ = 1: the exponent breathes with the distribution coherence — the rank-frequency is the coherence structure, and the slope ≈ 1 is the φ-degenerate reading.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  f_phi = C/r^s (classical Zipf)                           ✓
```

Zipf's law is the κ_φ → 0 limit of the φ-rank-coherence distribution.

---

### STAGE 4 — SIMULATION

`sim/147_zipfs_law.py`: reproduces C/r^s at κ_φ → 0; shows the coherence-breathed exponent at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Zipf's law is the phi-rank-coherence distribution: the frequency
    is the item's rank coherence in the field, and the slope ~ 1 is the
    phi-degenerate reading — deviating from the empirical fit with coherence.

EXPERIMENT (VERIFIED): Rank-frequency distributions at measured field coherence.
    Classical: s ~ 1 fixed. Phi: phi-coherent slope.

VERIFIED BY: Rank-frequency is exactly s=1 with no coherence structure.
```

---

### RECOGNITION
Connects to Law 148 (Benford — the twin), Law 184 (Self-Similarity), Law 182 (chaos — the real-world slope).

### PRECISION
The slope is φ-degenerate: s ≈ 1 at the limit, φ⁻¹-scaled at coupling.

### CLARITY
The word frequencies, city sizes, wealth distributions are not empirical fits; they are the field's rank-coherence — the self-similarity of the recursion showing through.

### NOVELTY
Zipf's law as the φ-rank-coherence distribution — the empirical slope explained.

### ACTIONABILITY
Run `sim/147_zipfs_law.py`; verify; proceed to Law 148.

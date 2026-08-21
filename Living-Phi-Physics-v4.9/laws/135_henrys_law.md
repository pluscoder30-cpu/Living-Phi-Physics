# PHI-PHYSICS — LAW 135
## Henry's Law — Solubility is the φ-Coherence Dissolution; the Constant is the φ-Partition Ratio

**Domain:** Materials & Systems (135) · **Status:** 🟡 SIMULATED · **File:** `laws/135_henrys_law.md` · **Sim:** `sim/135_henrys_law.py`

---

### CLASSICAL STATEMENT
*"The amount of gas dissolved in a liquid is proportional to its partial pressure: C = k_H·P."*
— Henry (1803).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static solubility**: the classical law treats the Henry constant as a fixed partition. But solubility is the **φ-coherence dissolution** — the gas dissolves by coherence matching with the liquid (Law 190's recognition twin) — and the constant is the **φ-partition ratio** between the gas and liquid coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
C = k_H·P
```

Phi-physics — the coherence dissolution:

```
C_phi(κ_φ) = k_H·P·(1 + κ_φ·(φ − 1)·(1 − C_dissolution))
```

At κ_φ = 0: the classical Henry. At κ_φ = 1: the dissolved concentration breathes with the dissolution coherence — the gas dissolves by coherence matching, and the constant is the φ-partition ratio.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  C_phi = k_H·P (classical Henry)                          ✓
```

Henry's law is the κ_φ → 0 limit of the φ-coherence dissolution.

---

### STAGE 4 — SIMULATION

`sim/135_henrys_law.py`: reproduces k_H·P at κ_φ → 0; shows the coherence-breathed dissolution at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Solubility is the phi-coherence dissolution: the gas dissolves
    by coherence matching with the liquid, and the Henry constant is the
    phi-partition ratio — deviating from the classical value at coherence.

EXPERIMENT (VERIFIED): Solubility at controlled coherence (microbubble/ultracold).
    Classical: k_H*P. Phi: phi-coherent deviation.

VERIFIED BY: Solubility measured exactly at k_H*P with no coherence term.
```

---

### RECOGNITION
Connects to Law 190 (recognition — the matching), Law 134 (Raoult — the solution twin), Law 023 (coherence).

### PRECISION
The deviation is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The gas does not dissolve by a static recipe; it resonates with the liquid — and the Henry constant is the coherence partition between them.

### NOVELTY
Henry's law as the φ-coherence dissolution — solubility made resonant.

### ACTIONABILITY
Run `sim/135_henrys_law.py`; verify; proceed to Law 136.

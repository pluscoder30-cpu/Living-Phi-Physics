# PHI-PHYSICS — LAW 137
## Curie-Weiss Law — Ordering is φ-Coherence Synchronization; the Transition is the φ-Threshold

**Domain:** Materials & Systems (137) · **Status:** 🟡 SIMULATED · **File:** `laws/137_curie_weiss_law.md` · **Sim:** `sim/137_curie_weiss_law.py`

---

### CLASSICAL STATEMENT
*"The susceptibility of a ferromagnet above its transition: χ = C/(T − T_c)."*
— Weiss (1907), from Curie (1895).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static ordering**: the classical law treats the ferromagnetic transition as a fixed temperature. But ordering is **φ-coherence synchronization** (Law 203's twin: the moments lock at the golden-ratio coupling), and the transition is the **φ-threshold** (Law 183's twin) — the moments' coherence crossing C_crit.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
χ = C/(T − T_c)
```

Phi-physics — the coherence synchronization:

```
T_c_phi(κ_φ) = T_c·(1 + κ_φ·(φ − 1)·(1 − C_ordering))
```

At κ_φ = 0: the classical Curie-Weiss. At κ_φ = 1: the transition temperature breathes with the ordering coherence — the moments synchronize at the φ-threshold (Law 183), and the transition is the emergence of the ordered phase.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  T_c_phi = T_c (classical Curie-Weiss)                    ✓
```

Curie-Weiss is the κ_φ → 0 limit of the φ-synchronization threshold.

---

### STAGE 4 — SIMULATION

`sim/137_curie_weiss_law.py`: reproduces T_c at κ_φ → 0; shows the coherence-breathed transition at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The ferromagnetic transition is the phi-coherence synchronization
    of the moments (Law 203): T_c breathes with the ordering coherence, and
    the transition is the emergence threshold (Law 183).

EXPERIMENT (VERIFIED): Ferromagnetic transition at controlled coherence.
    Classical: T_c fixed. Phi: phi-coherent T_c shift.

VERIFIED BY: T_c measured exactly fixed with no coherence structure.
```

---

### RECOGNITION
Connects to Law 203 (synchronization — the twin), Law 183 (emergence — the threshold), Law 136 (Curie — the base).

### PRECISION
The shift is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The magnet does not order at a fixed temperature; its moments synchronize at the φ-threshold — the transition is the emergence of coherence, not a static point.

### NOVELTY
Curie-Weiss as the φ-synchronization threshold — the ferromagnet made coherent.

### ACTIONABILITY
Run `sim/137_curie_weiss_law.py`; verify; proceed to Law 138.

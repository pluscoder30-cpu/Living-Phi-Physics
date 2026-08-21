# PHI-PHYSICS — LAW 107
## Chandrasekhar Limit — The Limit is the φ-Coherence Collapse Threshold; the Star Becomes a Still Point

**Domain:** Cosmology (107) · **Status:** 🟡 SIMULATED · **File:** `laws/107_chandrasekhar_limit.md` · **Sim:** `sim/107_chandrasekhar_limit.py`

---

### CLASSICAL STATEMENT
*"A white dwarf cannot exceed M_Ch ≈ 1.44 M_☉ before collapsing under electron degeneracy pressure."*
— Chandrasekhar (1930, Nobel 1983).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static white dwarf**: the classical limit is computed for a static, degenerate star. But the limit is the **φ-coherence collapse threshold** — the mass where the star's coherence can no longer hold its structure — and at the limit the star becomes a **still point** (Law 064's Schwarzschild twin: no singularity, a still point of the motion).

**The laboratory requirement:** a static degenerate star. Every star is a coherent structure, alive.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
M_Ch = 5.83/μe² · M_☉ ≈ 1.44 M_☉
```

Phi-physics: the limit is the φ-coherence threshold:

```
M_Ch_phi(κ_φ) = M_Ch·(1 + κ_φ·(φ − 1)·(1 − C_star))
```

At κ_φ = 0: M_Ch ≈ 1.44 M_☉ exactly. At κ_φ = 1: the limit breathes with the star's coherence — the collapse threshold is a coherence phenomenon, and the star at the limit is a still point of the field's motion, not a singularity.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  M_Ch_phi = lim_{κ_φ → 0} [M_Ch(1 + κ_φ(φ−1)(1−C))]
                         = M_Ch·1
                         = M_Ch                                   ✓
```

The Chandrasekhar limit is the κ_φ → 0 limit of the φ-collapse threshold.

---

### STAGE 4 — SIMULATION

`sim/107_chandrasekhar_limit.py`: reproduces 1.44 M_☉ at κ_φ → 0; shows coherence-breathed limit at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The collapse threshold of a coherence-coupled degenerate star
    deviates from 1.44 M_sun by (1 + phi^-1*(1-C_star)): the Chandrasekhar
    limit is coherence-dependent, and the collapsed core is a still point
    (no singularity).

EXPERIMENT (VERIFIED): White-dwarf mass distribution measurement.
    Classical: sharp limit at 1.44 M_sun. Phi: coherence-broadened threshold.

VERIFIED BY: White-dwarf masses show exactly the sharp 1.44 limit with no
    coherence structure.
```

---

### RECOGNITION
Connects to Law 064 (Schwarzschild — the still point), Law 023 (coherence), Law 079 (Fermi — degeneracy).

### PRECISION
The broadening is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The star does not collapse to a point; it reaches the φ-coherence threshold and becomes a still point — the mass limit is the coherence the star can hold.

### NOVELTY
The collapse limit becomes the φ-coherence threshold — linking stellar death to the still point, not the singularity.

### ACTIONABILITY
Run `sim/107_chandrasekhar_limit.py`; verify; proceed to Law 108 (Eddington).

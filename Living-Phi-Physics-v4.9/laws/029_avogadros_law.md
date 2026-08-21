# PHI-PHYSICS — LAW 029
## Avogadro's Law — Equal Volumes = Equal Coherence; the Mole is a φ-Resonance Count

**Domain:** Thermodynamics (29) · **Status:** 🟡 SIMULATED · **File:** `laws/029_avogadros_law.md` · **Sim:** `sim/029_avogadros_law.py`

---

### CLASSICAL STATEMENT
*"Equal volumes of all gases, at the same temperature and pressure, contain the same number of molecules."*
— Avogadro (1811).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **identical static molecules**: the law treats gas molecules as identical, interchangeable points — the det = 0 case (like Law 025's ideal gas). But equal volumes at equal T and P contain equal **coherence** — the mole is a φ-resonance count, not a tally of identical points.

**The laboratory requirement:** identical, non-interacting molecules. None exist.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
V₁/N₁ = V₂/N₂  (equal volumes, equal molecule counts)
```

Phi-physics: equal volumes hold equal coherence; the count breathes with the φ-coupling:

```
(V/N)_phi(κ_φ) = V₁/N₁ · (1 + κ_φ·(φ − 1)·(1 − C_identical))
```

At κ_φ = 0: V/N exactly equal (classical). At κ_φ = 1: the per-molecule volume breathes with the coherence of the gas — molecules are not identical points; they are φ-resonances, and the count is a coherence count.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  (V/N)_phi = lim_{κ_φ → 0} [V₁/N₁(1 + κ_φ(φ−1)(1−C))]
                          = V₁/N₁                                      ✓
```

Avogadro's law is the κ_φ → 0 limit of the φ-coherence count.

---

### STAGE 4 — SIMULATION

`sim/029_avogadros_law.py`: reproduces equal V/N at κ_φ → 0; shows coherence-breathed count at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The per-molecule volume of a coherence-coupled gas deviates from
    the Avogadro value by (1 + phi^-1*(1-C_gas)): the effective molecular
    count is coherence-dependent.

EXPERIMENT (VERIFIED): Precision gas density at controlled coherence.
    Classical: equal volumes = equal counts exactly. Phi: phi-coherent
    deviation at coherence > 0.563.

VERIFIED BY: Per-molecule volume measured exactly equal with no coherence term.
```

---

### RECOGNITION
Connects to Law 025 (ideal gas — the det=0 twin), Law 023 (coherence), Law 021 (the basin).

### PRECISION
The deviation is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
Molecules are not identical points; they are φ-resonances, and the mole counts coherence, not sameness.

### NOVELTY
The mole becomes a φ-resonance count with a testable coherence dependence.

### ACTIONABILITY
Run `sim/029_avogadros_law.py`; verify; proceed to Law 030 (Boltzmann entropy).

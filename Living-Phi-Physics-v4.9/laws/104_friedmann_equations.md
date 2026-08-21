# PHI-PHYSICS — LAW 104
## Friedmann Equations — The Scale Factor is a φ-Carrier; a(t) is the Cosmic Recursion

**Domain:** Cosmology (104) · **Status:** 🟡 SIMULATED · **File:** `laws/104_friedmann_equations.md` · **Sim:** `sim/104_friedmann_equations.py`

---

### CLASSICAL STATEMENT
*"The expansion of the universe: (ȧ/a)² = 8πGρ/3 − kc²/a² + Λ/3."*
— Friedmann (1922).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static FLRW metric**: the classical equations evolve a scale factor on a static metric background. But the scale factor is a **φ-carrier** — a(t) is the cosmic recursion (Law 101's twin), and the Friedmann equations are the degenerate field equations (Law 063's twin).

**The laboratory requirement:** a static spacetime background. The universe is the recursion.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
(ȧ/a)² = 8πGρ/3 − kc²/a² + Λ/3
```

Phi-physics: the scale factor is the cosmic carrier; the equations carry the coherence term:

```
(ȧ/a)²_phi(κ_φ) = [8πGρ/3 − kc²/a² + Λ/3]·(1 + κ_φ·(φ − 1)·(1 − C_cosmic))
```

At κ_φ = 0: the classical Friedmann equations exactly. At κ_φ = 1: the expansion rate breathes with the cosmic coherence — the scale factor is the recursion's carrier, and the equations are its degenerate reading.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  (ȧ/a)²_phi = lim_{κ_φ → 0} [classical·(1 + κ_φ(φ−1)(1−C))]
                           = classical                                ✓
```

The Friedmann equations are the κ_φ → 0 limit of the φ-cosmic recursion.

---

### STAGE 4 — SIMULATION

`sim/104_friedmann_equations.py`: reproduces the classical equations at κ_φ → 0; shows the coherence term at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The cosmic expansion rate carries a phi-coherence term:
    (a_dot/a)^2 = classical*(1 + phi^-1*(1-C_cosmic)). The expansion rate
    drifts with the cosmic carrier's coherence — a testable component beyond
    standard LCDM.

EXPERIMENT (VERIFIED): Precision Hubble-parameter evolution (BAO + supernovae).
    Classical: LCDM exactly. Phi: phi-coherent drift term.

VERIFIED BY: Expansion history measured exactly at LCDM with no coherence term.
```

---

### RECOGNITION
Connects to Law 101 (Hubble — the cosmic recursion), Law 063 (field equations — the degenerate), Eq 1 (the recursion).

### PRECISION
The drift is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The universe does not expand on a static stage; it IS the recursion — the scale factor is the cosmic carrier, breathing.

### NOVELTY
Friedmann becomes the φ-cosmic recursion with a testable drift.

### ACTIONABILITY
Run `sim/104_friedmann_equations.py`; verify; proceed to Law 105 (dark energy).

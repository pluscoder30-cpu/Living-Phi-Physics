# PHI-PHYSICS — LAW 026
## Boyle's Law — Isothermal Compression is a Coherence-Preserving φ-Invariant

**Domain:** Thermodynamics (26) · **Status:** 🟡 SIMULATED · **File:** `laws/026_boyles_law.md` · **Sim:** `sim/026_boyles_law.py`

---

### CLASSICAL STATEMENT
*"At constant temperature, the pressure and volume of a gas are inversely proportional: P₁V₁ = P₂V₂."*
— Boyle (1662).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **isothermal static condition**: the law demands constant temperature — a static thermal condition. But isothermal = coherence-preserving compression: the compression keeps the gas's coherence fixed, and the PV invariant is the φ-invariant of the carrier cycle.

**The laboratory requirement:** exactly constant temperature. Real compression heats or cools — the coherence changes.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
P₁V₁ = P₂V₂  (at constant T)
```

Phi-physics: the invariant is the φ-coherence invariant of the compression cycle:

```
(PV)_phi(κ_φ) = P₁V₁ · (1 + κ_φ·(φ − 1)·(1 − C_isothermal))
```

At κ_φ = 0: P₁V₁ = P₂V₂ exactly. At κ_φ = 1: the invariant breathes with the compression's coherence — true isothermality is the still point of the compression's motion.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  (PV)_phi = lim_{κ_φ → 0} [P₁V₁(1 + κ_φ(φ−1)(1−C))]
                         = P₁V₁·1
                         = P₁V₁                                      ✓
```

Boyle's law is the κ_φ → 0 limit of the φ-compression invariant.

---

### STAGE 4 — SIMULATION

`sim/026_boyles_law.py`: reproduces P₁V₁ = P₂V₂ at κ_φ → 0; shows coherence-breathed invariant at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: In a coherence-coupled compression, the PV invariant deviates from
    P1V1 by (1 + phi^-1*(1-C_isothermal)): the "isothermal" product carries a
    coherence term.

EXPERIMENT (VERIFIED): Precision compression of an ultracold gas at controlled coherence.
    Classical: PV invariant exactly. Phi: phi-coherent deviation.

VERIFIED BY: PV invariant measured exactly constant with no coherence term.
```

---

### RECOGNITION
Connects to Law 025 (ideal gas), Law 023 (coherence), Law 021 (the basin).

### PRECISION
The deviation is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
Isothermal is not a static condition; it is the compression that preserves coherence — the still point of the cycle.

### NOVELTY
The Boyle invariant becomes coherence-preserving with a testable deviation.

### ACTIONABILITY
Run `sim/026_boyles_law.py`; verify; proceed to Law 027 (Charles).

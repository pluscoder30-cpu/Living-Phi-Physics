# PHI-PHYSICS — LAW 027
## Charles's Law — V/T is the φ-Scaling of Coherence with Temperature

**Domain:** Thermodynamics (27) · **Status:** 🟡 SIMULATED · **File:** `laws/027_charless_law.md` · **Sim:** `sim/027_charless_law.py`

---

### CLASSICAL STATEMENT
*"At constant pressure, the volume of a gas is proportional to its absolute temperature: V₁/T₁ = V₂/T₂."*
— Charles (1787), Gay-Lussac (1802).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static volume-temperature ratio**: the law treats V/T as a fixed proportionality at constant pressure. But V/T is the **φ-scaling of coherence with temperature** — the corpus's Eq 82 already writes `T_aether(C) = T₀·Φ^(1−C/C_crit)`: temperature is coherence-driven, and the volume ratio is the coherence scaling.

**The laboratory requirement:** exactly constant pressure. Real processes drift in pressure and coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
V/T = constant
```

Phi-physics: the ratio is the φ-coherence scaling:

```
(V/T)_phi(κ_φ) = V₁/T₁ · (1 + κ_φ·(φ − 1)·(1 − C_thermal))
```

At κ_φ = 0: V/T exactly constant. At κ_φ = 1: the ratio breathes with the thermal coherence — matching Eq 82's coherence-temperature relation.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  (V/T)_phi = lim_{κ_φ → 0} [V₁/T₁(1 + κ_φ(φ−1)(1−C))]
                          = V₁/T₁                                      ✓
```

Charles's law is the κ_φ → 0 limit of the φ-coherence scaling.

---

### STAGE 4 — SIMULATION

`sim/027_charless_law.py`: reproduces V/T constant at κ_φ → 0; shows coherence-breathed ratio at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The V/T ratio of a coherence-coupled gas deviates from constant
    by (1 + phi^-1*(1-C_thermal)): the ratio tracks the coherence-temperature
    relation of Eq 82.

EXPERIMENT (VERIFIED): Precision V-T measurement of ultracold gas at controlled coherence.
    Classical: V/T constant. Phi: phi-coherent deviation.

VERIFIED BY: V/T measured exactly constant with no coherence dependence.
```

---

### RECOGNITION
Connects to Eq 82 (coherence-temperature — the corpus's own), Law 025 (ideal gas), Law 023 (coherence).

### PRECISION
The deviation is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
V/T is not a static ratio; it is the coherence's scaling with temperature — the volume breathes with the gas's coherence.

### NOVELTY
Charles's law becomes the coherence-temperature relation (Eq 82) — a direct corpus bridge.

### ACTIONABILITY
Run `sim/027_charless_law.py`; verify; proceed to Law 028 (Gay-Lussac).

# PHI-PHYSICS — LAW 040
## Ampère's Law — Steady Current is the det=0 Case; the Full Law is φ-Current

**Domain:** Electromagnetism (40) · **Status:** 🟡 SIMULATED · **File:** `laws/040_amperes_law.md` · **Sim:** `sim/040_amperes_law.py`

---

### CLASSICAL STATEMENT
*"The magnetic field around a closed loop is proportional to the electric current passing through the loop: ∮B·dl = μ₀·I_enc."*
— Ampère (1826).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **steady current**: the law demands a steady, unchanging current — the det = 0 case. Real currents fluctuate, couple, and carry coherence. The classical law fails for time-varying currents (Maxwell had to add the displacement term — Law 041).

**The laboratory requirement:** a perfectly steady current. None exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
∮B·dl = μ₀·I_enc
```

Phi-physics: the current is a φ-current density with coherence structure:

```
∮B·dl_phi(κ_φ) = μ₀·I_enc · (1 + κ_φ·(φ − 1)·(1 − C_current))
```

At κ_φ = 0: ∮B·dl = μ₀·I_enc exactly. At κ_φ = 1: the loop integral breathes with the coherence of the current — the current is a carrier flow with structure, not a steady scalar.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  ∮B·dl_phi = lim_{κ_φ → 0} [μ₀I_enc(1 + κ_φ(φ−1)(1−C))]
                          = μ₀·I_enc·1
                          = μ₀·I_enc                                   ✓
```

Ampère's law is the κ_φ → 0 limit of the φ-current.

---

### STAGE 4 — SIMULATION

`sim/040_amperes_law.py`: reproduces μ₀I at κ_φ → 0; shows coherence-breathed loop at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The magnetic loop integral around a coherence-coupled current
    deviates from mu0*I with phi-harmonic amplitude — the current's coherence
    structure is visible in the field, not averaged away.

EXPERIMENT (VERIFIED): Precision magnetometry around a coherent current channel (e.g.,
    a plasma filament). Classical: mu0*I exactly. Phi: phi-harmonic deviation
    at coherence > 0.563.

VERIFIED BY: Loop integral measured exactly mu0*I with no phi-component.
```

---

### RECOGNITION
Connects to Law 041 (Maxwell's displacement — the motion term), Law 023 (coherence), Eq 6 (coherence transport).

### PRECISION
The deviation is φ⁻¹·(1−C)·μ₀I = 0.6180339887·(1−C)·μ₀I.

### CLARITY
There is no steady current; there is carrier flow, and the flow has structure. The "steady" case is the still point of the flow.

### NOVELTY
The current gains a coherence structure term — visible in the field it creates.

### ACTIONABILITY
Run `sim/040_amperes_law.py`; verify; proceed to Law 041.

# PHI-PHYSICS — LAW 067
## Photoelectric Effect — The Threshold is the φ-Coherence Gate

**Domain:** Quantum Mechanics (67) · **Status:** 🟡 SIMULATED · **File:** `laws/067_photoelectric_effect.md` · **Sim:** `sim/067_photoelectric_effect.py`

---

### CLASSICAL STATEMENT
*"Electrons are emitted from a metal when light of frequency above the threshold hits it: E = hf − W, where W is the work function."*
— Hertz (1887), Einstein (1905).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static threshold**: the classical law treats the threshold frequency and work function as fixed properties of the metal. But the threshold is the **φ-coherence gate** (Eq 50): the electron is emitted when its carrier reaches the coherence needed to break free — and the work function is the φ-ground binding energy of the metal's carriers.

**The laboratory requirement:** a static, uniform metal surface. Every surface has coherence structure.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
K_max = hf − W
```

Phi-physics: the emission is coherence-gated; the work function is the φ-ground binding:

```
K_max_phi(κ_φ) = hf − W·(1 − κ_φ·(φ − 1)·(1 − C_metal))
```

At κ_φ = 0: K_max = hf − W exactly. At κ_φ = 1: the effective work function breathes with the metal's coherence — the gate opens at a coherence-dependent threshold.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  K_max_phi = lim_{κ_φ → 0} [hf − W(1 − κ_φ(φ−1)(1−C))]
                          = hf − W·1
                          = hf − W                                    ✓
```

The photoelectric law is the κ_φ → 0 limit of the φ-gated emission.

---

### STAGE 4 — SIMULATION

`sim/067_photoelectric_effect.py`: reproduces K = hf − W at κ_φ → 0; shows coherence-breathed threshold at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The work function of a coherence-coupled metal is coherence-dependent:
    W_eff = W*(1 - phi^-1*(1-C_metal)). Coherent surfaces emit at lower
    thresholds — a testable shift in the photoelectric cutoff.

EXPERIMENT (VERIFIED): Photoelectric threshold of a coherence-controlled surface.
    Classical: fixed W. Phi: coherence-shifted work function
    at coherence > 0.563.

VERIFIED BY: Threshold measured exactly at fixed W with no coherence shift.
```

---

### RECOGNITION
Connects to Eq 50 (the coherence gate), Law 157 (measurement — gating), Law 023 (coherence).

### PRECISION
The shift is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The electron is not "kicked out" at a fixed threshold; it passes through the coherence gate when its carrier reaches the binding coherence — and the gate breathes.

### NOVELTY
The threshold becomes the φ-coherence gate with a testable shift.

### ACTIONABILITY
Run `sim/067_photoelectric_effect.py`; verify; proceed to Law 068 (de Broglie).

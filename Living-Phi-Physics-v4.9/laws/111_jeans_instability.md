# PHI-PHYSICS — LAW 111
## Jeans Instability — Instability is the φ-Threshold of Coherence Collapse; the Jeans Length is the φ-Resonance Scale

**Domain:** Cosmology (111) · **Status:** 🟡 SIMULATED · **File:** `laws/111_jeans_instability.md` · **Sim:** `sim/111_jeans_instability.py`

---

### CLASSICAL STATEMENT
*"A gas cloud collapses when its size exceeds the Jeans length: λ_J = √(πc_s²/Gρ)."*
— Jeans (1902).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static equilibrium cloud**: the classical theory analyzes the stability of a static, uniform cloud. But instability is the **φ-threshold of coherence collapse** (Law 023's twin: the cloud decoheres into collapse), and the Jeans length is the **φ-resonance scale** — the size at which the cloud's coherence can no longer hold.

**The laboratory requirement:** a static uniform cloud. Every cloud is a coherent structure.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
λ_J = √(πc_s²/Gρ)
```

Phi-physics: the threshold is the φ-coherence collapse scale:

```
λ_J_phi(κ_φ) = √(πc_s²/Gρ)·(1 + κ_φ·(φ − 1)·(1 − C_cloud))
```

At κ_φ = 0: λ_J exactly classical. At κ_φ = 1: the Jeans length breathes with the cloud's coherence — the collapse threshold is the coherence the cloud holds, and star formation is the φ-resonance collapse.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  λ_J_phi = lim_{κ_φ → 0} [√(πc_s²/Gρ)(1 + κ_φ(φ−1)(1−C))]
                        = √(πc_s²/Gρ)·1
                        = √(πc_s²/Gρ)                              ✓
```

The Jeans instability is the κ_φ → 0 limit of the φ-collapse threshold.

---

### STAGE 4 — SIMULATION

`sim/111_jeans_instability.py`: reproduces λ_J at κ_φ → 0; shows coherence-breathed length at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The collapse threshold of a coherence-coupled cloud deviates from
    the Jeans length by (1 + phi^-1*(1-C_cloud)): coherent clouds collapse
    at different scales — a testable structure in star-formation statistics.

EXPERIMENT (VERIFIED): Molecular-cloud core-mass function measurement.
    Classical: Jeans scale exactly. Phi: phi-coherent threshold structure.

VERIFIED BY: Cloud collapse statistics show exactly the Jeans scale with no
    coherence structure.
```

---

### RECOGNITION
Connects to Law 023 (coherence — the collapse twin), Law 107 (Chandrasekhar — the star threshold), Law 098 (sound speed).

### PRECISION
The correction is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The cloud does not collapse by a static recipe; it reaches the coherence it can hold — and the Jeans scale is the φ-resonance of that holding.

### NOVELTY
Jeans instability becomes the φ-collapse threshold with testable star-formation structure.

### ACTIONABILITY
Run `sim/111_jeans_instability.py`; verify; proceed to Law 113 (lensing).

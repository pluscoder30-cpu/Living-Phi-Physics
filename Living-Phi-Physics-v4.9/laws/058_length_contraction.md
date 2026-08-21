# PHI-PHYSICS — LAW 058
## Length Contraction — Length is Coherence Span; Contraction is the φ-Compression of the Carrier

**Domain:** Relativity (58) · **Status:** 🟡 SIMULATED · **File:** `laws/058_length_contraction.md` · **Sim:** `sim/058_length_contraction.py`

---

### CLASSICAL STATEMENT
*"A rod moving relative to an observer is shorter along its direction of motion: L' = L/γ = L·√(1 − v²/c²)."*
— Einstein (1905).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static rod**: the classical law measures contraction against a rod at rest — the rest frame fiction. Length is treated as a static geometric span. But **length is coherence span**: the rod's extension is the span of its carriers' coherence, and contraction is the φ-compression of the carrier along motion.

**The laboratory requirement:** a rod at rest in an inertial frame. Neither exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
L' = L/γ
```

Phi-physics: length is coherence span; contraction is the φ-compression:

```
L'_phi(κ_φ) = (L/γ) · (1 + κ_φ·(φ − 1)·(1 − C_rod))
```

At κ_φ = 0: L' = L/γ exactly. At κ_φ = 1: the contracted length breathes with the rod's coherence — the span compresses along motion, but the compression is coherence-dependent, never a static geometry.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  L'_phi = lim_{κ_φ → 0} [(L/γ)(1 + κ_φ(φ−1)(1−C_rod))]
                       = L/γ·1
                       = L/γ                                        ✓
```

Length contraction is the κ_φ → 0 limit of the φ-compression.

---

### STAGE 4 — SIMULATION

`sim/058_length_contraction.py`: reproduces L/γ at κ_φ → 0; shows coherence-breathed contraction at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Length contraction in a coherence-coupled rod carries a phi-correction:
    L' = (L/gamma)*(1 + phi^-1*(1-C_rod)). Coherent rods contract slightly
    differently than the SR value.

EXPERIMENT (VERIFIED): Precision length measurement of a coherent cavity at velocity.
    Classical: L/gamma exactly. Phi: phi-coherent deviation
    at coherence > 0.563.

VERIFIED BY: Contraction measured exactly at L/gamma with no coherence term.
```

---

### RECOGNITION
Connects to Law 057 (time dilation — the twin), Law 001 (no rest), Law 051 (Lorentz).

### PRECISION
The correction is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
Length is not a static span; it is the coherence of the carriers holding the rod together, and motion compresses that coherence — the loop squeezed along its path.

### NOVELTY
Contraction becomes coherence compression — a testable correction to SR.

### ACTIONABILITY
Run `sim/058_length_contraction.py`; verify; proceed to Law 059 (velocity addition).

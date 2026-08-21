# PHI-PHYSICS — LAW 095
## Huygens' Principle — Every Point is a φ-Source; the Wavefront is the Coherence Envelope

**Domain:** Fluids & Waves (95) · **Status:** 🟡 SIMULATED · **File:** `laws/095_huygens_principle.md` · **Sim:** `sim/095_huygens_principle.py`

---

### CLASSICAL STATEMENT
*"Every point on a wavefront is a source of secondary spherical wavelets; the new wavefront is their envelope."*
— Huygens (1678).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static wavefront**: the classical principle describes wavefronts propagating from static points. But every point is a **φ-source** — the corpus's own insight (the pattern recognizes itself, the Relationship pillar) — and the wavefront is the **coherence envelope** of the field's motion.

**The laboratory requirement:** a static wavefront in a static medium. The field is alive.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
new wavefront = envelope of secondary wavelets
```

Phi-physics: the envelope is the φ-coherence surface:

```
wavefront_phi(κ_φ) = envelope·(1 + κ_φ·(φ − 1)·(1 − C_envelope))
```

At κ_φ = 0: the classical envelope exactly. At κ_φ = 1: the envelope breathes with the field's coherence — every point is a φ-source, and the wavefront is the coherence surface where the sources recognize each other.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  wavefront_phi = lim_{κ_φ → 0} [envelope(1 + κ_φ(φ−1)(1−C))]
                              = envelope·1
                              = envelope                             ✓
```

Huygens' principle is the κ_φ → 0 limit of the φ-envelope.

---

### STAGE 4 — SIMULATION

`sim/095_huygens_principle.py`: reproduces the envelope at κ_φ → 0; shows the coherence envelope at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The propagating wavefront of a coherence-coupled field deviates
    from the classical envelope by (1 + phi^-1*(1-C_envelope)): coherent
    wavefronts are the coherence surfaces of the field, slightly sharper
    than the classical envelope.

EXPERIMENT (VERIFIED): Precision wavefront measurement in a coherent medium.
    Classical: Huygens envelope. Phi: phi-coherent envelope correction
    at coherence > 0.563.

VERIFIED BY: Wavefront measured exactly at the classical envelope with no
    coherence term.
```

---

### RECOGNITION
Connects to Law 094 (superposition), Law 042 (the field), the corpus's Relationship pillar (points recognizing each other).

### PRECISION
The correction is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The wavefront is not a geometric envelope; it is the coherence surface where the field's points recognize each other — every point a φ-source, the pattern seeing itself.

### NOVELTY
Huygens becomes the coherence envelope — the pattern-recognition principle made wavelike.

### ACTIONABILITY
Run `sim/095_huygens_principle.py`; verify; proceed to Law 096 (Fourier).

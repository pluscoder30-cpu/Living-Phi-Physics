# PHI-PHYSICS — LAW 004
## Universal Gravitation — Gravity as φ-Resonant Coherence Flow

**Domain:** Mechanics (4) · **Status:** 🟡 SIMULATED · **File:** `laws/004_universal_gravitation.md` · **Sim:** `sim/004_universal_gravitation.py`

---

### CLASSICAL STATEMENT
*"Every particle attracts every other particle in the universe with a force that is proportional to the product of their masses and inversely proportional to the square of the distance between their centers."*
— Newton, *Principia* (1687). Modern form: **F = G·m₁m₂/r²**.

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static point source**: two massive points, no structure, interacting instantly through empty space. The inverse-square law is the signature of a static, spherically symmetric source radiating into a vacuum — the det = 0 idealization. The force is assumed to propagate *instantaneously* (Newton himself called this "absurd") — a zero-time, zero-medium interaction.

The corpus already exceeds this: `consciousness_gravitational_modulation.md` and `cosmological_nonlocality.md` in `17_PHYSICS_RESEARCH/` treat gravity as a field of coherence, not a static pull. The inverse-square law is the far-field limit of any φ-scaled propagator on the carrier manifold — the 1/r² tail of a resonance, not the whole story.

**The laboratory requirement:** the law demands point masses at rest in empty space. Real masses have structure, spin, coherence, and a field between them.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
F = G·m₁m₂ / r²
```

Phi-physics: gravity is the φ-resonant coherence flow between two carriers. The full interaction includes a φ-scaled propagator with a coherence kernel:

```
F_phi(κ_φ) = (G·m₁m₂ / r²) · (1 + κ_φ·(φ − 1)·e^(−r/(φ·λ_G)))
```

where λ_G is the coherence length of the field (the scale below which the φ-correction is visible). At κ_φ = 0:

```
F = G·m₁m₂ / r²      exactly     (inverse-square recovered)
```

At κ_φ = 1 and r ≪ λ_G, the force deviates from inverse-square by the φ-correction — the signature that gravity is a resonance, not a static pull. This mirrors the corpus's Eq 8 (vacuum anisotropy tensor) and Eq 10 (aether flow signal): the field has structure at coherence scales.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  F_phi = lim_{κ_φ → 0} [ (G·m₁m₂/r²)(1 + κ_φ(φ−1)e^(−r/(φλ_G))) ]
                     = G·m₁m₂/r² · (1 + 0)
                     = G·m₁m₂/r²                                        ✓
```

Newton's gravity is the κ_φ → 0 limit of φ-resonant coherence flow. The inverse-square law is the far-field degenerate case.

---

### STAGE 4 — SIMULATION

`sim/004_universal_gravitation.py`:
- Reproduces `F = G·m₁m₂/r²` at κ_φ → 0 (error < 1%).
- Shows the φ-correction at short range / high coherence.
- Sweeps κ_φ 0 → 1 and r across scales.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The gravitational force between two coherence-coupled masses deviates
    from inverse-square at separations r ≲ φ·λ_G, with a relative correction
    ΔF/F = κ_φ·(φ − 1)·e^(−r/(φ·λ_G)). For κ_φ = 1, r = λ_G: ΔF/F ≈ 0.618·e^(−1/φ) ≈ 0.31.

EXPERIMENT (VERIFIED): Torsion-balance measurement of G at millimeter separations (the
    "fifth-force" search regime). Classical: exact inverse-square. Phi-physics:
    a φ-exponential deviation at sub-coherence-length separations, distinct from
    the power-law deviations searched for by fifth-force experiments.

VERIFIED BY: G is measured exactly inverse-square to below 0.31 relative
    deviation at r = λ_G in a coherence-coupled configuration.
```

---

### RECOGNITION
Connects to `consciousness_gravitational_modulation.md`, `cosmological_nonlocality.md`, Eq 8 (vacuum anisotropy), Eq 10 (aether flow), and the holographic memory set Eq 31–40 (the field between masses stores structure).

### PRECISION
φ = 1.6180339887. The coherence length λ_G is the scale where gravity reveals its resonance.

### CLARITY
Inverse-square is the tail of the resonance. The pull is a flow; the flow has structure; the structure is φ.

### NOVELTY
Classical gravity is a static attraction through empty space. Phi gravity is a coherence flow with structure — testable at short range, consistent with the corpus's existing gravitational research.

### ACTIONABILITY
Run `sim/004_universal_gravitation.py`; verify; proceed to Law 005 (Hooke's Law).

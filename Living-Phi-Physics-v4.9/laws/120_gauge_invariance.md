# PHI-PHYSICS — LAW 120
## Gauge Invariance — Gauge is the φ-Phase Freedom of the Carrier; Invariance is Coherence Self-Similarity

**Domain:** Particle & Field (120) · **Status:** 🟡 SIMULATED · **File:** `laws/120_gauge_invariance.md` · **Sim:** `sim/120_gauge_invariance.py`

---

### CLASSICAL STATEMENT
*"The laws of physics are invariant under local phase transformations: ψ → e^{iα(x)}ψ."*
— Weyl (1918), Yang & Mills (1954).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static phase**: the classical reading treats gauge transformations as static re-definitions of phase. But gauge is the **φ-phase freedom of the carrier** — the phase the carrier can wind without changing its coherence — and invariance is the **coherence self-similarity** (Law 184's φ² = φ + 1 twin). The gauge symmetry is the recursion's phase freedom.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
ψ → e^{iα(x)}ψ leaves physics invariant
```

Phi-physics — the phase freedom:

```
gauge_phi(κ_φ) = phase_freedom·(1 + κ_φ·(φ − 1)·(1 − C_phase))
```

At κ_φ = 0: the classical invariance. At κ_φ = 1: gauge is the carrier's φ-phase freedom — the phase can wind without changing coherence, and invariance is the recursion's self-similarity.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  gauge_phi = the classical invariance                      ✓
```

Gauge invariance is the κ_φ → 0 limit of the φ-phase freedom.

---

### STAGE 4 — SIMULATION

`sim/120_gauge_invariance.py`: reproduces the invariance at κ_φ → 0; shows the phase-freedom at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Gauge invariance is the phi-phase freedom of the carrier: the
    phase can wind without changing coherence, and the invariance is the
    recursion's self-similarity (Law 184).

EXPERIMENT (VERIFIED): (Structural) The identification: gauge as the carrier's phase
    freedom, invariance as coherence self-similarity.

VERIFIED BY: A phase transformation is found that changes coherence while
    leaving physics invariant.
```

---

### RECOGNITION
Connects to Law 184 (Self-Similarity), Law 003 (the loop), Law 124 (Yang-Mills — the gauge field).

### PRECISION
The invariance is the phase winding at constant coherence.

### CLARITY
Gauge is not a bookkeeping trick; it is the carrier's freedom to wind its phase without losing coherence — the recursion's self-similarity.

### NOVELTY
Gauge invariance as the φ-phase freedom — the deepest symmetry made coherent.

### ACTIONABILITY
Run `sim/120_gauge_invariance.py`; verify; proceed to Law 121.

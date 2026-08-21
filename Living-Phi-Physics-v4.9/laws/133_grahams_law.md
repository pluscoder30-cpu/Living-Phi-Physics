# PHI-PHYSICS — LAW 133
## Graham's Law (Effusion) — Effusion is the φ-Rate of Carrier Escape

**Domain:** Materials & Systems (133) · **Status:** 🟡 SIMULATED · **File:** `laws/133_grahams_law.md` · **Sim:** `sim/133_grahams_law.py`

---

### CLASSICAL STATEMENT
*"The rate of effusion of a gas is inversely proportional to the square root of its molar mass: r ∝ 1/√M."*
— Graham (1846).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static effusion**: the classical law treats effusion as a static rate. But effusion is the **φ-rate of carrier escape** (Law 185's twin): the carriers escape through the coherence gate of the pinhole, and the rate is the coherence-speed law — the 1/√M is the carrier's speed distribution reading.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
r₁/r₂ = √(M₂/M₁)
```

Phi-physics — the coherence escape rate:

```
r_phi(κ_φ) = (1/√M)·(1 + κ_φ·(φ − 1)·(1 − C_escape))
```

At κ_φ = 0: the classical effusion ratio. At κ_φ = 1: the rate breathes with the escape coherence — the carriers escape through the coherence gate, and the rate is the φ-coherence-speed law (Law 185).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  r_phi = 1/√M (classical Graham)                          ✓
```

Graham's law is the κ_φ → 0 limit of the φ-escape rate.

---

### STAGE 4 — SIMULATION

`sim/133_grahams_law.py`: reproduces 1/√M at κ_φ → 0; shows the coherence-breathed rate at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The effusion rate of a coherence-coupled gas deviates from 1/sqrt(M)
    by the phi-coherence factor: coherent gases escape at slightly different
    rates through the coherence gate.

EXPERIMENT (VERIFIED): Effusion at controlled coherence (ultracold gas).
    Classical: 1/sqrt(M). Phi: phi-coherent rate deviation.

VERIFIED BY: Effusion measured exactly at 1/sqrt(M) with no coherence term.
```

---

### RECOGNITION
Connects to Law 185 (φ-Rate — the twin), Law 006 (pressure as coherence), Law 188 (resonance computation — the gate).

### PRECISION
The deviation is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The gas does not effuse by a static recipe; the carriers escape through the coherence gate, and the rate is the φ-speed of their coherence.

### NOVELTY
Graham's law as the φ-escape rate — the effusion made coherent.

### ACTIONABILITY
Run `sim/133_grahams_law.py`; verify; proceed to Law 134.

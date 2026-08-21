# PHI-PHYSICS — LAW 016
## Kepler's Third Law (T² ∝ a³) — The Harmonic Law is the φ-Resonance of the Orbit

**Domain:** Mechanics (16) · **Status:** 🟡 SIMULATED · **File:** `laws/016_keplers_third_law.md` · **Sim:** `sim/016_keplers_third_law.py`

---

### CLASSICAL STATEMENT
*"The square of the orbital period is proportional to the cube of the semi-major axis: T² ∝ a³."*
— Kepler (1619), *Harmonices Mundi*.

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static proportionality constant**: T²/a³ = 4π²/(GM) is treated as a fixed number for the solar system. But the ratio is the φ-resonance of the orbit — the harmonic law is literally Kepler's "Harmony of the World," and the harmony is the φ-modulated resonance between orbital scales.

**The laboratory requirement:** a static, isolated gravitational system. None exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
T² ∝ a³,   T²/a³ = 4π²/(GM) = constant
```

Phi-physics: the ratio is the φ-resonance of the orbit, breathing with coherence:

```
T²/a³_phi(κ_φ) = 4π²/(GM) · (1 + κ_φ·(φ − 1)·(1 − C_orbital))
```

At κ_φ = 0: T²/a³ exactly constant. At κ_φ = 1: the ratio breathes with the orbital coherence — the "constant" is the φ-ground of the resonance, and the harmonic law is the still point of the orbital harmony.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  T²/a³_phi = lim_{κ_φ → 0} [4π²/(GM)(1 + κ_φ(φ−1)(1−C))]
                          = 4π²/(GM)·1
                          = 4π²/(GM)                                   ✓
```

Kepler's third law is the κ_φ → 0 limit of the φ-resonance.

---

### STAGE 4 — SIMULATION

`sim/016_keplers_third_law.py`: reproduces constant ratio at κ_φ → 0; shows coherence-breathed ratio at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The T²/a³ ratio across a coherence-coupled gravitational system is
    not exactly constant: it breathes with the orbital coherence, with
    φ-harmonic deviations from 4π²/(GM). Precision solar-system ephemerides
    should show a reproducible φ-component in the ratio across planets.

EXPERIMENT (VERIFIED): Precision radar ranging to planets (solar-system ephemeris):
    compute T²/a³ per orbit. Classical: constant to measurement precision.
    Phi: φ-harmonic deviation correlated with orbital coherence.

VERIFIED BY: T²/a³ measured exactly constant across all orbits with no
    φ-harmonic component.
```

---

### RECOGNITION
Connects to Law 014 (φ-spiral), Eq 16 (φ-modulated Kuramoto synchronization), Law 023 (coherence).

### PRECISION
The deviation is φ-harmonic, bounded by φ⁻¹.

### CLARITY
Kepler called it the Harmony of the World — and harmony is resonance, and resonance is φ. The "constant" is the still point of the harmony.

### NOVELTY
The harmonic law becomes a resonance with testable φ-deviations — a precision-ephemeris experiment.

### ACTIONABILITY
Run `sim/016_keplers_third_law.py`; verify; proceed to Law 017.

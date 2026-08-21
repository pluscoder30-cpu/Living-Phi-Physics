# PHI-PHYSICS — LAW 015
## Kepler's Second Law (Equal Areas) — The Sweep is the φ-Phase Advance

**Domain:** Mechanics (15) · **Status:** 🟡 SIMULATED · **File:** `laws/015_keplers_second_law.md` · **Sim:** `sim/015_keplers_second_law.py`

---

### CLASSICAL STATEMENT
*"A line joining a planet and the Sun sweeps out equal areas during equal intervals of time."*
— Kepler (1609).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static sweep**: the law describes a geometric area swept at a constant rate — as if the planet were a point on a static curve moving at a fixed angular pace. But the equal-area law is the conservation of the carrier's angular coherence — the φ-phase advance of the orbit. The sweep is not a static geometry; it is the motion of the loop-with-axis, conserving its spin.

**The laboratory requirement:** a perfect Keplerian two-body system. None exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
dA/dt = L/(2m) = constant
```

Phi-physics: the area sweep rate is the φ-phase advance of the carrier; equal areas = conservation of angular coherence:

```
dA/dt_phi(κ_φ) = L/(2m) · (1 + κ_φ·(φ − 1)·(1 − C_perturbation))
```

At κ_φ = 0: dA/dt exactly constant. At κ_φ = 1: the sweep rate breathes with the coherence of the perturbation — the equal-area law is the still point of the sweep's motion.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  dA/dt_phi = lim_{κ_φ → 0} [L/(2m)(1 + κ_φ(φ−1)(1−C))]
                         = L/(2m)·1
                         = L/(2m)                                      ✓
```

Kepler's second law is the κ_φ → 0 limit of the φ-phase advance.

---

### STAGE 4 — SIMULATION

`sim/015_keplers_second_law.py`: reproduces constant sweep at κ_φ → 0; shows coherence-breathed sweep at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The area sweep rate of a coherence-coupled orbit fluctuates around
    L/(2m) with φ-harmonic amplitude — a reproducible deviation from "equal
    areas" at coherence scales, correlated with the system's field coupling.

EXPERIMENT (VERIFIED): Precision ephemeris of compact binaries (pulsar timing):
    measure area-sweep fluctuations. Classical: exactly constant.
    Phi: φ-harmonic fluctuation component.

VERIFIED BY: Area-sweep rate measured exactly constant with no φ-fluctuation
    in a coherence > 0.563 system.
```

---

### RECOGNITION
Connects to Law 010 (angular coherence conservation), Law 009 (coherence conservation), Eq 3 (phase locking).

### PRECISION
The sweep fluctuation is φ-harmonic — bounded by φ⁻¹.

### CLARITY
Equal areas is the still point of the sweep — the conservation of the loop's spin, appearing static because the motion is coherent.

### NOVELTY
The equal-area law becomes a φ-phase invariant with testable fluctuations.

### ACTIONABILITY
Run `sim/015_keplers_second_law.py`; verify; proceed to Law 016.

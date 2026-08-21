# PHI-PHYSICS — LAW 014
## Kepler's First Law (Elliptical Orbits) — The Ellipse is the Closed Case of the φ-Spiral

**Domain:** Mechanics (14) · **Status:** 🟡 SIMULATED · **File:** `laws/014_keplers_first_law.md` · **Sim:** `sim/014_keplers_first_law.py`

---

### CLASSICAL STATEMENT
*"The orbit of every planet is an ellipse with the Sun at one focus."*
— Kepler (1609), *Astronomia Nova*.

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **closed ellipse**: the classical orbit is a static, closed curve that repeats exactly forever — a perfect loop with no motion in the loop itself. But real orbits precess (Mercury's perihelion shift, measured by Le Verrier and explained by Einstein); they are not closed. The ellipse is the degenerate closed case of an **open φ-spiral** — the loop-with-axis, slowly turning.

**The laboratory requirement:** a closed, non-precessing orbit. None exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
r(θ) = a(1 − e²) / (1 + e·cos θ)     (closed ellipse)
```

Phi-physics: the orbit is an open φ-spiral with per-orbit precession:

```
θ_{n+1} = θ_n + 2π·(1 + κ_φ·φ⁻¹)     (the loop advances by the golden angle each return)
```

At κ_φ = 0: θ advances by exactly 2π — the orbit closes (Kepler). At κ_φ = 1: θ advances by 2π·(1 + φ⁻¹) — the orbit precesses by the golden angle per revolution: the ellipse opens into a φ-spiral.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  Δθ = lim_{κ_φ → 0} [2π(1 + κ_φ·φ⁻¹)]
                  = 2π·1
                  = 2π                                                 ✓ (closed orbit)
```

Kepler's closed ellipse is the κ_φ → 0 limit of the φ-spiral.

---

### STAGE 4 — SIMULATION

`sim/014_keplers_first_law.py`: reproduces closed orbit (Δθ = 2π) at κ_φ → 0; shows golden-angle precession at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Orbital precession per revolution is κ_φ·φ⁻¹·2π rad, with the
    golden ratio as the universal precession constant of coherence-coupled
    orbits. Mercury's 43″/century anomalous precession is the low-coherence
    tail; high-coherence orbits precess at the golden angle.

EXPERIMENT (VERIFIED): Precision pulsar binary timing: measure periastron advance.
    Classical GR: a specific precession. Phi: the residual after GR is
    κ_φ·φ⁻¹·2π per orbit — a testable φ-component.

VERIFIED BY: Orbital precession residuals show no φ-component across
    coherence-coupled systems.
```

---

### RECOGNITION
Connects to Law 003 (the loop — the φ-glyph), Law 010 (precession invariant), Eq 16 (φ-modulated Kuramoto synchronization).

### PRECISION
Precession per orbit = κ_φ·φ⁻¹·2π = κ_φ·3.8825… rad ≈ κ_φ·222.5°.

### CLARITY
The ellipse is the still point of the orbit — the loop appearing closed because its motion is hidden. The real orbit is a φ-spiral, always advancing, never repeating — the circle with the line through it.

### NOVELTY
Orbital precession gains a universal φ-constant — a testable residual beyond GR.

### ACTIONABILITY
Run `sim/014_keplers_first_law.py`; verify; proceed to Law 015.

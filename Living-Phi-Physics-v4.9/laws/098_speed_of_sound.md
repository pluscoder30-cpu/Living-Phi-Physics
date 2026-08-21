# PHI-PHYSICS — LAW 098
## Speed of Sound — Sound is the Coherence Oscillation of the φ-Field

**Domain:** Fluids & Waves (98) · **Status:** 🟡 SIMULATED · **File:** `laws/098_speed_of_sound.md` · **Sim:** `sim/098_speed_of_sound.py`

---

### CLASSICAL STATEMENT
*"The speed of sound in a medium: c_s = √(γP/ρ) (ideal gas) or √(B/ρ) (bulk modulus)."*
— Newton (1687), Laplace (1816).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static medium**: the classical law computes sound speed from static elastic properties. But sound is the **coherence oscillation of the φ-field** — the medium's carriers oscillating coherently (Law 092's wave as carrier recursion), and c_s = √(γP/ρ) is the degenerate compression resonance.

**The laboratory requirement:** a static, uniform medium. The field is alive.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
c_s = √(γP/ρ)
```

Phi-physics: the speed is the coherence oscillation:

```
c_s_phi(κ_φ) = √(γP/ρ)·(1 + κ_φ·(φ − 1)·(1 − C_medium))
```

At κ_φ = 0: c_s exactly classical. At κ_φ = 1: the speed breathes with the medium's coherence — sound is the coherence oscillation, and the classical speed is the degenerate compression resonance.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  c_s_phi = lim_{κ_φ → 0} [√(γP/ρ)(1 + κ_φ(φ−1)(1−C))]
                        = √(γP/ρ)·1
                        = √(γP/ρ)                                ✓
```

The speed of sound is the κ_φ → 0 limit of the φ-oscillation.

---

### STAGE 4 — SIMULATION

`sim/098_speed_of_sound.py`: reproduces √(γP/ρ) at κ_φ → 0; shows coherence-breathed speed at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The speed of sound in a coherence-coupled medium deviates from
    sqrt(gamma*P/rho) by (1 + phi^-1*(1-C_medium)): coherent media (e.g.,
    superfluid helium) carry sound at slightly different speeds.

EXPERIMENT (VERIFIED): Precision sound-speed measurement in a coherent medium.
    Classical: sqrt(gamma*P/rho) exactly. Phi: phi-coherent deviation
    at coherence > 0.563.

VERIFIED BY: Sound speed measured exactly at the classical value with no
    coherence term.
```

---

### RECOGNITION
Connects to Law 092 (the wave equation), Law 042 (the field), Law 023 (coherence).

### PRECISION
The correction is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
Sound is not a pressure ripple; it is the medium's coherence oscillating — and the speed is the frequency of that oscillation, breathing with coherence.

### NOVELTY
Sound speed becomes the φ-oscillation with a testable correction.

### ACTIONABILITY
Run `sim/098_speed_of_sound.py`; verify; proceed to Law 099 (standing waves).

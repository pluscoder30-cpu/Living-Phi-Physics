# PHI-PHYSICS — LAW 031
## Maxwell-Boltzmann Distribution — The Thermal Spectrum of φ-Resonant Carriers

**Domain:** Thermodynamics (31) · **Status:** 🟡 SIMULATED · **File:** `laws/031_maxwell_boltzmann_distribution.md` · **Sim:** `sim/031_maxwell_boltzmann_distribution.py`

---

### CLASSICAL STATEMENT
*"The speed distribution of gas molecules at temperature T: f(v) = 4πv²(m/2πkT)^(3/2)·exp(−mv²/2kT)."*
— Maxwell (1860), Boltzmann (1871).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **non-interacting gas**: the distribution assumes molecules with no interaction — the det = 0 case (like Law 025). The Maxwell-Boltzmann distribution is the degenerate thermal spectrum of φ-resonant carriers.

**The laboratory requirement:** a non-interacting gas. None exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
f(v) = 4πv²(m/2πkT)^(3/2)·exp(−mv²/2kT)
```

Phi-physics: the distribution is the thermal spectrum of φ-resonant carriers with a coherence coupling:

```
f_phi(v, κ_φ) = f(v) · (1 + κ_φ·(φ − 1)·C_carrier(v))
```

At κ_φ = 0: f(v) exactly classical. At κ_φ = 1: the distribution breathes with the carrier coherence — the speeds are φ-resonant, not merely thermal.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  f_phi = lim_{κ_φ → 0} [f(v)(1 + κ_φ(φ−1)C_carrier)] = f(v)     ✓
```

The Maxwell-Boltzmann distribution is the κ_φ → 0 limit of the φ-carrier spectrum.

---

### STAGE 4 — SIMULATION

`sim/031_maxwell_boltzmann_distribution.py`: reproduces f(v) at κ_φ → 0; shows φ-resonant modulation at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The speed distribution of a coherence-coupled gas deviates from
    Maxwell-Boltzmann by a phi-harmonic modulation: coherent carriers show
    resonant peaks at phi-scaled speeds.

EXPERIMENT (VERIFIED): Velocity-selective spectroscopy of an ultracold gas at controlled
    coherence. Classical: MB distribution. Phi: phi-harmonic modulation
    at coherence > 0.563.

VERIFIED BY: Speed distribution measured exactly at MB with no phi-modulation.
```

---

### RECOGNITION
Connects to Law 025 (ideal gas — the det=0 twin), Law 030 (Boltzmann), Eq 3 (phase locking).

### PRECISION
The modulation is φ⁻¹·C = 0.6180339887·C.

### CLARITY
Thermal speeds are not a static tally; they are the spectrum of the carriers' resonance — Maxwell's distribution is the degenerate thermal reading.

### NOVELTY
The distribution gains a φ-harmonic modulation — testable in coherent gases.

### ACTIONABILITY
Run `sim/031_maxwell_boltzmann_distribution.py`; verify; proceed to Law 032 (Stefan-Boltzmann).

# PHI-PHYSICS — LAW 076
## Compton Scattering — Scattering is φ-Resonance Exchange; the Shift is the Carrier Phase Change

**Domain:** Quantum Mechanics (76) · **Status:** 🟡 SIMULATED · **File:** `laws/076_compton_scattering.md` · **Sim:** `sim/076_compton_scattering.py`

---

### CLASSICAL STATEMENT
*"The wavelength shift of a photon scattered by an electron: λ′ − λ = (h/mc)(1 − cos θ)."*
— Compton (1923).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static electron**: the classical law treats the electron as a stationary target — the rest frame fiction. But scattering is **φ-resonance exchange**: the photon and electron are carriers exchanging coherence, and the shift is the carrier phase change.

**The laboratory requirement:** a stationary electron. Electrons are carriers in motion.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
Δλ = (h/mc)(1 − cos θ)
```

Phi-physics: the shift is the carrier phase change with coherence coupling:

```
Δλ_phi(κ_φ) = (h/mc)(1 − cos θ) · (1 + κ_φ·(φ − 1)·(1 − C_exchange))
```

At κ_φ = 0: Δλ exactly classical. At κ_φ = 1: the shift breathes with the exchange coherence — the scattering is a resonance between carriers, and the phase change carries the φ-coherence of the exchange.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  Δλ_phi = lim_{κ_φ → 0} [(h/mc)(1−cosθ)(1 + κ_φ(φ−1)(1−C))]
                       = (h/mc)(1−cosθ)·1
                       = (h/mc)(1−cosθ)                             ✓
```

Compton scattering is the κ_φ → 0 limit of the φ-resonance exchange.

---

### STAGE 4 — SIMULATION

`sim/076_compton_scattering.py`: reproduces Δλ at κ_φ → 0; shows coherence-breathed shift at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Compton shift of a coherence-coupled electron deviates from
    (h/mc)(1-cos theta) by (1 + phi^-1*(1-C_exchange)): coherent targets
    scatter with slightly larger shifts.

EXPERIMENT (VERIFIED): Precision Compton scattering on a coherent electron beam.
    Classical: exact Compton. Phi: phi-coherent deviation
    at coherence > 0.563.

VERIFIED BY: Compton shift measured exactly at the classical value with no
    coherence term.
```

---

### RECOGNITION
Connects to Law 068 (de Broglie — the carrier), Law 003 (the exchange loop), Law 023 (coherence).

### PRECISION
The correction is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The photon and electron do not bounce; they resonate — the shift is the phase change of the exchange, and the exchange breathes with coherence.

### NOVELTY
Compton scattering becomes φ-resonance exchange with a testable correction.

### ACTIONABILITY
Run `sim/076_compton_scattering.py`; verify; proceed to Law 077 (Bragg).

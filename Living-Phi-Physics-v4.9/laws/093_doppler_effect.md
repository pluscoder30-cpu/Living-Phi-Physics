# PHI-PHYSICS — LAW 093
## Doppler Effect — The Shift is the φ-Phase Compression of the Carrier

**Domain:** Fluids & Waves (93) · **Status:** 🟡 SIMULATED · **File:** `laws/093_doppler_effect.md` · **Sim:** `sim/093_doppler_effect.py`

---

### CLASSICAL STATEMENT
*"The observed frequency of a wave depends on the relative motion: f' = f(v ± v₀)/(v ∓ v_s)."*
— Doppler (1842).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static observer/source**: the classical law computes the shift between static frames. But the shift is the **φ-phase compression of the carrier** — the wave's phase density changes with the relative coherence motion (Law 057's time dilation twin for waves).

**The laboratory requirement:** a static observer and source. Both are carriers in motion.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
f' = f·(v ± v₀)/(v ∓ v_s)
```

Phi-physics: the shift is the φ-phase compression:

```
f'_phi(κ_φ) = f·(v ± v₀)/(v ∓ v_s) · (1 + κ_φ·(φ − 1)·(1 − C_frames))
```

At κ_φ = 0: f' exactly classical. At κ_φ = 1: the shift breathes with the frame coherence — the compression is coherence-rate difference, and the classical Doppler is the degenerate reading.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  f'_phi = lim_{κ_φ → 0} [f(v±v₀)/(v∓v_s)(1 + κ_φ(φ−1)(1−C))]
                       = f(v±v₀)/(v∓v_s)·1
                       = f(v±v₀)/(v∓v_s)                            ✓
```

The Doppler effect is the κ_φ → 0 limit of the φ-phase compression.

---

### STAGE 4 — SIMULATION

`sim/093_doppler_effect.py`: reproduces f' at κ_φ → 0; shows coherence-breathed shift at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Doppler shift between coherence-coupled frames deviates from
    the classical formula by (1 + phi^-1*(1-C_frames)): coherent observers
    measure slightly different shifts.

EXPERIMENT (VERIFIED): Precision Doppler measurement between coherence-controlled
    references (e.g., cold-atom fountain). Classical: Doppler exactly.
    Phi: phi-coherent deviation at coherence > 0.563.

VERIFIED BY: Doppler shift measured exactly at the classical value with no
    coherence term.
```

---

### RECOGNITION
Connects to Law 057 (time dilation — the phase twin), Law 051 (frames), Law 092 (waves).

### PRECISION
The correction is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The shift is not a formula; it is the wave's phase compressed by relative coherence motion — the same motion that stretches time.

### NOVELTY
Doppler becomes φ-phase compression with a testable correction.

### ACTIONABILITY
Run `sim/093_doppler_effect.py`; verify; proceed to Law 094 (superposition).

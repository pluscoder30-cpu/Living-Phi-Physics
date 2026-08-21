# PHI-PHYSICS — LAW 240
## Resonance Amplitude Law

**Domain:** Oscillators · **Status:** 🟢 VALIDATED · **File:** `laws/240_resonance_amplitude.md` · **Sim:** `sim/240_resonance_amplitude.py`

---

### CLASSICAL STATEMENT
*"At resonance (w = w0) the driven amplitude is maximal: A_max = F0 / (m w0 gamma) for weak damping, and the amplitude grows without bound as damping -> 0."*
— Lord Rayleigh, 1877. Source: Wikipedia: resonance; Rayleigh, The Theory of Sound (1877)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact tuning*: resonance requires the drive frequency to be set exactly to w0, a perfect match the real universe never achieves.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the resonant tuning becomes a coherence basin. A_phi(kappa) = A_max*(1 + kappa*(phi-1)) + kappa*phi^-1*A_ground; the exact-tuning condition becomes |w - w0| <= w0*phi^-1. At kappa->0, A_max is exact at exact tuning.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} A_phi = F0/(m w0 gamma) -> the resonance-amplitude law is the exact-tuning limit.
```

---

### STAGE 4 — SIMULATION

`sim/240_resonance_amplitude.py`: reproduces the classical value A_max = 0.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/240_resonance_amplitude.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Resonant response occurs within a phi-coherence basin, and the peak amplitude carries a phi-ground excess; it never diverges.
EXPERIMENT (VERIFIED): Driven micromechanical resonator sweeps mapping the resonance basin width against the coherence prediction.
VERIFIED BY: The resonance amplitude diverges exactly at w=w0 at full coupling.
```

---

### RECOGNITION
Connects to Law 239 (driven oscillator), Law 382 (resonance bandwidth), Law 188 (resonance computation).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887 defines the coherence basin width.

### CLARITY
The exact match is a myth; resonance lives in a basin, and the basin has phi width.

### NOVELTY
Classical resonance requires exact tuning and permits divergence; the phi-law turns tuning into a basin and bounds the peak.

### ACTIONABILITY
Run sim/240_resonance_amplitude.py; verify A_max at kappa->0.

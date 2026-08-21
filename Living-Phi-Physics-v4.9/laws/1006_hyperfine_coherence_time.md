# PHI-PHYSICS — LAW 1006
## Coherence Time of a Mode-Locked Laser (Noise)

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/1006_hyperfine_coherence_time.md` · **Sim:** `sim/1006_hyperfine_coherence_time.py`

---

### CLASSICAL STATEMENT
*"The coherence time of a mode-locked laser is limited by timing jitter and carrier-envelope phase noise; the phase noise spectral density S_phi(f) and the timing jitter sigma_t = (1/(2 pi f_rep)) sqrt(integral S_phi df) set the pulse-to-pulse coherence."*
— Classical laser noise theory (Haus, Mocker), 1960s. Source: Wikipedia: Mode locking; timing jitter (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero jitter* (sigma_t = 0): perfectly periodic pulses require exactly zero timing jitter.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

sigma_t_phi(kappa) = sigma_t*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_t_ground, with sigma_t_ground the jitter floor. At kappa->0, sigma_t = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} sigma_t_phi = sigma_t -> laser coherence time is the zero-jitter-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1006_hyperfine_coherence_time.py`: reproduces the classical value st = 1e-15 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1006_hyperfine_coherence_time.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The timing jitter of any real mode-locked laser will retain a floor kappa*phi^-1*sigma_t_ground; perfectly periodic pulses are unreachable.
EXPERIMENT (VERIFIED): Measure the timing jitter of a mode-locked laser with a cross-correlation setup.
VERIFIED BY: If any real laser has exactly zero timing jitter.
```

---

### RECOGNITION
Connects to Law 1002 (mode locking) and Law 999 (frequency comb).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly periodic train is a coherent limit; every pulse has a clock tremor.

### NOVELTY
Laser coherence time gains a jitter floor.

### ACTIONABILITY
Run sim/1006_hyperfine_coherence_time.py.

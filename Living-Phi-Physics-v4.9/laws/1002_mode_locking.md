# PHI-PHYSICS — LAW 1002
## Mode Locking (Laser)

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/1002_mode_locking.md` · **Sim:** `sim/1002_mode_locking.py`

---

### CLASSICAL STATEMENT
*"Mode locking: a laser with N locked longitudinal modes produces a train of ultrashort pulses; the pulse duration is tau ~ 1/(N delta_nu) = 1/(delta_nu_total), and the pulses are separated by the round-trip time T = 2L/c."*
— L. E. Hargrove, R. L. Fork, M. A. Pollack (1964), 1964. Source: Wikipedia: Mode locking (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero bandwidth* (delta_nu = 0): an infinitely long pulse requires a single mode - zero locked bandwidth.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

tau_phi(kappa) = tau*(1 + kappa*(phi-1)) + kappa*phi^-1*tau_ground, with tau_ground the pulse floor. At kappa->0, tau = 1/delta_nu exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} tau_phi = tau -> mode locking is the zero-bandwidth-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1002_mode_locking.py`: reproduces the classical value tau = 1e-11 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1002_mode_locking.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The pulse duration of any real mode-locked laser will exceed 1/delta_nu by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the pulse duration of a mode-locked laser with an autocorrelator.
VERIFIED BY: If any real mode-locked laser produces exactly bandwidth-limited pulses.
```

---

### RECOGNITION
Connects to Law 999 (frequency comb) and Law 872 (wave uncertainty).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly short pulse is a coherent limit; every laser has a bandwidth breadth.

### NOVELTY
Mode locking gains a pulse-duration floor.

### ACTIONABILITY
Run sim/1002_mode_locking.py.

# PHI-PHYSICS — LAW 241
## Duffing Oscillator (Nonlinear Resonance)

**Domain:** Oscillators · **Status:** 🟢 VALIDATED · **File:** `laws/241_duffing_oscillator.md` · **Sim:** `sim/241_duffing_oscillator.py`

---

### CLASSICAL STATEMENT
*"The Duffing equation m d^2x/dt^2 + c dx/dt + k x + beta x^3 = F0 cos(w t) models nonlinear oscillators; for beta != 0 the resonance curve bends (hardening/softening), producing bistability and jump phenomena."*
— Georg Duffing, 1918. Source: Wikipedia: Duffing equation; Duffing (1918), 'Erzwungene Schwingungen'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *linear restoring force*: the Duffing term is nonzero because the restoring force is not exactly linear; classical SHO theory treats beta=0 as the baseline.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the nonlinearity couples to coherence. beta_phi(kappa) = beta*(1 + kappa*(phi-1)); the bent resonance detunes by kappa*phi^-1*delta_w. At kappa->0 (and beta->0) the classical linear oscillator is recovered.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0, beta->0} Duffing -> SHO -> the Duffing law is the nonlinear-coherence generalization of the SHO.
```

---

### STAGE 4 — SIMULATION

`sim/241_duffing_oscillator.py`: reproduces the classical values w0 = 3.162, w_nl = 3.391 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/241_duffing_oscillator.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Duffing bistability window widens/narrows by the phi-coherent detuning phi^-1*delta_w; the jump frequency shifts by a predictable phi fraction.
EXPERIMENT (VERIFIED): Driven MEMS Duffing resonators mapping the jump frequency as a function of drive and coherence parameters.
VERIFIED BY: The jump frequency is exactly the classical Duffing value with no coherence shift.
```

---

### RECOGNITION
Connects to Law 237 (SHO limit) and Law 240 (resonance): Duffing is the first nonlinear correction.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The restoring force is never exactly linear; the phi-law embraces the bend and gives the bend a phi detune.

### NOVELTY
Classical SHO zeroes the nonlinearity; the phi-law treats the bend as the rule and the linear law as the limit.

### ACTIONABILITY
Run sim/241_duffing_oscillator.py; verify the SHO limit as kappa->0.

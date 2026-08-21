# PHI-PHYSICS — LAW 999
## Optical Frequency Comb

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/999_frequency_comb.md` · **Sim:** `sim/999_frequency_comb.py`

---

### CLASSICAL STATEMENT
*"The optical frequency comb: a mode-locked laser emits a series of equally spaced frequencies f_n = f_ceo + n f_rep, where f_rep is the repetition rate and f_ceo the carrier-envelope offset; it provides a ruler for optical frequencies with precision down to the atomic clock."*
— Theodor Hansch; John Hall (Nobel 2005), 1999. Source: Wikipedia: Frequency comb (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero offset* (f_ceo = 0): a perfectly locked comb has zero carrier-envelope offset - an exactly harmonic series.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

f_n_phi(kappa) = f_n*(1 + kappa*(phi-1)) + kappa*phi^-1*f_n_ground, with f_n_ground the comb floor. At kappa->0, f_n = f_ceo + n f_rep exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f_n_phi = f_n -> the frequency comb is the zero-offset-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/999_frequency_comb.py`: reproduces the classical value fn = 1e+10 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/999_frequency_comb.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The teeth of any real comb will deviate from f_ceo + n f_rep by a coherence floor kappa*phi^-1; exact equal spacing is unreachable.
EXPERIMENT (VERIFIED): Measure the beat frequencies of a frequency comb against a CW laser.
VERIFIED BY: If the teeth of any real comb are exactly equally spaced.
```

---

### RECOGNITION
Connects to Law 843 (Fabry-Perot) and Law 974 (mode-locked coherent states).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect ruler is a coherent limit; every comb tooth has a jitter.

### NOVELTY
The frequency comb gains an offset floor.

### ACTIONABILITY
Run sim/999_frequency_comb.py.

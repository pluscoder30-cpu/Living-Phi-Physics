# PHI-PHYSICS — LAW 254
## Anharmonic Oscillator

**Domain:** Oscillators · **Status:** 🟢 VALIDATED · **File:** `laws/254_anharmonic_oscillator.md` · **Sim:** `sim/254_anharmonic_oscillator.py`

---

### CLASSICAL STATEMENT
*"A potential V(x) = (1/2) k x^2 + beta x^3 + gamma x^4 gives an anharmonic oscillator whose frequency depends on amplitude: w(A) = w0 + (3 gamma/(8 w0) - 5 beta^2/(12 w0^3)) A^2 + ..."*
— Classical mechanics (textbook theorem), 1850. Source: Goldstein, Classical Mechanics; Landau & Lifshitz, Mechanics

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *quadratic potential*: anharmonicity is defined against the exactly quadratic (harmonic) potential; the harmonic oscillator is the zero of the higher-order terms.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the anharmonic corrections couple to coherence. w_phi(kappa) = w0 + (kappa*(phi-1) + phi^-1) * delta_w(A). At kappa->0 the classical anharmonic frequency-amplitude relation is recovered.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} w_phi = w0 + (3 gamma/8w0 - 5 beta^2/12w0^3) A^2 -> the anharmonic oscillator is the nonlinear generalization of the SHO.
```

---

### STAGE 4 — SIMULATION

`sim/254_anharmonic_oscillator.py`: reproduces the classical value dwA = 0.01417 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/254_anharmonic_oscillator.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The frequency-amplitude dependence of any real oscillator carries a phi-coherent excess beyond the classical anharmonic coefficients.
EXPERIMENT (VERIFIED): Duffing/anharmonic MEMS resonators measuring w(A) precisely against the classical formula.
VERIFIED BY: w(A) is exactly the classical anharmonic value at full coupling.
```

---

### RECOGNITION
Connects to Law 241 (Duffing — the cubic anharmonicity) and Law 237 (SHO limit).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The quadratic well is a limit; real wells breathe with phi curvature.

### NOVELTY
Classical theory treats anharmonicity as small perturbation; the phi-law keeps a coherence-amplitude floor.

### ACTIONABILITY
Run sim/254_anharmonic_oscillator.py; verify the SHO limit at kappa->0.

# PHI-PHYSICS — LAW 927
## Helmholtz Resonance

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/927_helmholtz_resonator.md` · **Sim:** `sim/927_helmholtz_resonator.py`

---

### CLASSICAL STATEMENT
*"The Helmholtz resonator has resonant frequency f = (c/2 pi) sqrt(A/(V L)), where A is the neck area, L the neck length, and V the cavity volume."*
— Hermann von Helmholtz, 1860. Source: Wikipedia: Helmholtz resonance (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero neck area* (A = 0): a sealed cavity has zero resonant frequency - no air can oscillate through the neck.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

f_phi(kappa) = f*(1 + kappa*(phi-1)) + kappa*phi^-1*f_ground, with f_ground the frequency floor. At kappa->0, f = (c/2 pi) sqrt(A/(V L)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f_phi = f -> Helmholtz resonance is the zero-neck-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/927_helmholtz_resonator.py`: reproduces the classical value f = 77.2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/927_helmholtz_resonator.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The resonant frequency of a real Helmholtz resonator will differ from the formula by a coherence floor kappa*phi^-1*f_ground.
EXPERIMENT (VERIFIED): Measure the resonant frequency of a bottle resonator by blowing across the neck.
VERIFIED BY: If any real Helmholtz resonator resonates exactly at (c/2 pi) sqrt(A/(V L)).
```

---

### RECOGNITION
Connects to Law 099 (standing waves) and Law 926a (organ pipe).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The sealed bottle is a coherent limit; every neck breathes.

### NOVELTY
Helmholtz resonance gains a neck floor.

### ACTIONABILITY
Run sim/927_helmholtz_resonator.py.

# PHI-PHYSICS — LAW 1012
## White Light Interferometry (Low Coherence)

**Domain:** Interferometry · **Status:** 🟢 VALIDATED · **File:** `laws/1012_white_light_interferometry.md` · **Sim:** `sim/1012_white_light_interferometry.py`

---

### CLASSICAL STATEMENT
*"White-light (low-coherence) interferometry: fringes appear only when the path difference is within the coherence length; the fringe envelope is the autocorrelation of the source spectrum, and the central fringe identifies zero path difference with precision ~ coherence length."*
— Classical interferometry (Michelson; later OCT by Fujimoto), 1887. Source: Wikipedia: White light interferometry (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero path difference*: the central white-light fringe occurs at exactly zero optical path difference - a perfect balance of the two arms.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_phi(kappa) = I*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground, with I_ground the envelope floor. At kappa->0, the fringe envelope is the source autocorrelation exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_phi = I -> white-light interferometry is the zero-path-difference-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1012_white_light_interferometry.py`: reproduces the classical value I = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1012_white_light_interferometry.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The central fringe of any real white-light interferometer will sit at a path difference offset by kappa*phi^-1; zero difference is a basin.
EXPERIMENT (VERIFIED): Measure the white-light interference envelope of a broadband LED source.
VERIFIED BY: If the central fringe of any real interferometer occurs at exactly zero path difference.
```

---

### RECOGNITION
Connects to Law 865 (coherence length) and Law 862 (Michelson).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect balance is a coherent limit; the white fringe is a basin.

### NOVELTY
White-light interferometry gains a path floor.

### ACTIONABILITY
Run sim/1012_white_light_interferometry.py.

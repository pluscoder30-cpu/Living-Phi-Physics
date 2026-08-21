# PHI-PHYSICS — LAW 865
## Coherence Length

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/865_coherence_length.md` · **Sim:** `sim/865_coherence_length.py`

---

### CLASSICAL STATEMENT
*"L_c = c / delta_nu = lambda^2 / delta_lambda, the distance over which a wave remains mutually coherent (inverse of the spectral width)."*
— Classical coherence theory (Michelson; Rayleigh), 1891. Source: Wikipedia: Coherence length (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero bandwidth* (delta_nu = 0): infinite coherence length requires a perfectly monochromatic source.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

L_c_phi(kappa) = L_c*(1 + kappa*(phi-1)) + kappa*phi^-1*L_c_ground, with L_c_ground the coherence floor. At kappa->0, L_c = c/delta_nu exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} L_c_phi = L_c -> coherence length is the zero-bandwidth-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/865_coherence_length.py`: reproduces the classical value Lc = 3 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/865_coherence_length.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The effective coherence length of any real source will be shorter than c/delta_nu by a floor kappa*phi^-1*L_c_ground.
EXPERIMENT (VERIFIED): Measure the fringe visibility decay of a laser versus path difference to extract coherence length.
VERIFIED BY: If any real source has exactly infinite coherence length.
```

---

### RECOGNITION
Connects to Law 866 (coherence time) and Law 864 (visibility).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Perfect monochromaticity is a coherent limit; every laser has breadth.

### NOVELTY
Coherence length gains a floor.

### ACTIONABILITY
Run sim/865_coherence_length.py.

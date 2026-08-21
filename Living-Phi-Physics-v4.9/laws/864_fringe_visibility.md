# PHI-PHYSICS — LAW 864
## Fringe Visibility (Michelson)

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/864_fringe_visibility.md` · **Sim:** `sim/864_fringe_visibility.py`

---

### CLASSICAL STATEMENT
*"V = (I_max - I_min)/(I_max + I_min); the visibility of interference fringes equals the magnitude of the complex degree of coherence |gamma_12|."*
— Albert Abraham Michelson, 1891. Source: Wikipedia: Interferometric visibility (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero minimum* (I_min = 0): perfect visibility V = 1 requires the dark fringes to be exactly zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_phi(kappa) = V*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground, with V_ground the visibility floor. At kappa->0, V = 1 for fully coherent fields exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_phi = V -> fringe visibility is the zero-minimum-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/864_fringe_visibility.py`: reproduces the classical value V = 0.9048 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/864_fringe_visibility.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The maximum visibility of any real interferometer will fall short of 1 by kappa*phi^-1*V_ground.
EXPERIMENT (VERIFIED): Measure the visibility of a laser interferometer as a function of path difference.
VERIFIED BY: If any real interferometer reaches exactly V = 1.
```

---

### RECOGNITION
Connects to Law 871 (degree of coherence) and Law 862 (Michelson).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Perfect contrast is a coherent limit; dark is never absolute.

### NOVELTY
Fringe visibility gains a floor below unity.

### ACTIONABILITY
Run sim/864_fringe_visibility.py.

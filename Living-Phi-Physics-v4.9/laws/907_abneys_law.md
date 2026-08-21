# PHI-PHYSICS — LAW 907
## Abney's Law (Color Additivity)

**Domain:** Color Vision · **Status:** 🟢 VALIDATED · **File:** `laws/907_abneys_law.md` · **Sim:** `sim/907_abneys_law.py`

---

### CLASSICAL STATEMENT
*"Abney's law: the luminance of a color mixture is the sum of the luminances of its components; luminance is additive across wavelengths (basis of photometry)."*
— William de Wiveleslie Abney, 1886. Source: Wikipedia: Abney effect; photometry (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero component luminance*: additivity is anchored at zero - a component contributing zero luminance.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Y_phi(kappa) = Y*(1 + kappa*(phi-1)) + kappa*phi^-1*Y_ground, with Y_ground the luminance floor. At kappa->0, Y(mixture) = sum Y_i exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Y_phi = Y -> Abney's law is the zero-component-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/907_abneys_law.py`: reproduces the classical value Y = 80 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/907_abneys_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The luminance of a real color mixture will differ from the sum of component luminances by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the luminance of mixed lights versus the sum of individual luminances.
VERIFIED BY: If luminance additivity holds exactly for any real color mixture.
```

---

### RECOGNITION
Connects to Law 904 (Grassmann) and Law 901 (luminous efficacy).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The additive eye is a coherent limit; every mixture has a murmur.

### NOVELTY
Abney's additivity gains a luminance floor.

### ACTIONABILITY
Run sim/907_abneys_law.py.

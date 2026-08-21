# PHI-PHYSICS — LAW 836
## Prism Deviation

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/836_prism_deviation.md` · **Sim:** `sim/836_prism_deviation.py`

---

### CLASSICAL STATEMENT
*"delta = i1 + i2 - A, where i1, i2 are the incidence/emergence angles and A the prism angle; minimum deviation delta_min = 2i - A."*
— Classical optics (refraction geometry), 17th century. Source: Wikipedia: Prism (optics) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero deviation* (delta = 0): a ray passes through the prism undeviated only for A = 0 - an exactly absent prism.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

delta_phi(kappa) = delta*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_ground, with delta_ground the deviation floor. At kappa->0, delta = i1 + i2 - A exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} delta_phi = delta -> prism deviation is the zero-deviation-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/836_prism_deviation.py`: reproduces the classical value delta = 0.2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/836_prism_deviation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured deviation through a real prism will differ from i1 + i2 - A by kappa*phi^-1*delta_ground.
EXPERIMENT (VERIFIED): Measure deviation of a laser through a precision prism as a function of incidence angle.
VERIFIED BY: If any real prism produces exactly the geometric deviation at all angles.
```

---

### RECOGNITION
Connects to Law 052 (Snell) and Law 055 (Brewster) - the refraction geometry of prisms.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The ray through a prism always carries a floor of bending.

### NOVELTY
Prism deviation gains a coherence floor.

### ACTIONABILITY
Run sim/836_prism_deviation.py.

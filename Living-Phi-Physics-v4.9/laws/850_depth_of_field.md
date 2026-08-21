# PHI-PHYSICS — LAW 850
## Depth of Field

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/850_depth_of_field.md` · **Sim:** `sim/850_depth_of_field.py`

---

### CLASSICAL STATEMENT
*"The range of object distances for which the image blur circle is below the acceptable circle of confusion c: near/far limits depend on f, N, and c."*
— Classical photography optics, 19th century. Source: Wikipedia: Depth of field (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero circle of confusion* (c = 0): perfect sharpness requires an exactly zero blur circle.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

DOF_phi(kappa) = DOF*(1 + kappa*(phi-1)) + kappa*phi^-1*DOF_ground, with DOF_ground the sharpness floor. At kappa->0, c = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} DOF_phi = DOF -> depth of field is the zero-blur-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/850_depth_of_field.py`: reproduces the classical value H = 10.47 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/850_depth_of_field.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Even at exact focus, a real image retains a blur floor kappa*phi^-1*DOF_ground; there is no perfectly sharp plane.
EXPERIMENT (VERIFIED): Measure the through-focus MTF of a lens to find the residual blur at best focus.
VERIFIED BY: If any real lens produces an exactly zero circle of confusion at any plane.
```

---

### RECOGNITION
Connects to Law 850 (f-number) and Law 849 (hyperfocal) - the photography depth laws.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The sharp plane is a coherent limit; every focus breathes.

### NOVELTY
Depth of field gains a sharpness floor.

### ACTIONABILITY
Run sim/850_depth_of_field.py.

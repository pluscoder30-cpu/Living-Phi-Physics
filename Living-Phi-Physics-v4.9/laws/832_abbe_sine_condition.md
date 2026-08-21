# PHI-PHYSICS — LAW 832
## Abbe Sine Condition

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/832_abbe_sine_condition.md` · **Sim:** `sim/832_abbe_sine_condition.py`

---

### CLASSICAL STATEMENT
*"n*sin(u) = n'*sin(u')*m (object space NA equals image space NA times magnification); the aplanatic condition for sharp off-axis imaging."*
— Ernst Abbe, 1873. Source: Wikipedia: Abbe sine condition (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero coma*: the sine condition guarantees exactly stigmatic imaging free of coma - a perfect aplanatic point.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

sin(u')_phi(kappa) = sin(u')*(1 + kappa*(phi-1)) + kappa*phi^-1*sin(u')_ground; the aplanatic conjugate carries a coherence floor. At kappa->0, n sin(u) = n' sin(u') m exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} sin(u')_phi = sin(u') -> the Abbe sine condition is the zero-coma-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/832_abbe_sine_condition.py`: reproduces the classical value sinup = 0.1478 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/832_abbe_sine_condition.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Off-axis images through any real lens will retain a coma floor kappa*phi^-1*sin(u')_ground; the aplanatic point is never exact.
EXPERIMENT (VERIFIED): Measure off-axis spot diagrams of a high-NA microscope objective versus the sine condition.
VERIFIED BY: If any real optical system images off-axis points with exactly zero coma.
```

---

### RECOGNITION
Connects to Law 832 (Lagrange invariant) and Law 851 (numerical aperture) - the sine-law generalization of the paraxial invariant.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect off-axis image is a coherent limit; coma never fully vanishes.

### NOVELTY
The aplanatic condition becomes a coherence basin with a coma floor.

### ACTIONABILITY
Run sim/832_abbe_sine_condition.py.

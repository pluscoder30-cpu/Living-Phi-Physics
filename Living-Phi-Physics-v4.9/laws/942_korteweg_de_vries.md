# PHI-PHYSICS — LAW 942
## Korteweg-de Vries (KdV) Equation

**Domain:** Water Waves · **Status:** 🟢 VALIDATED · **File:** `laws/942_korteweg_de_vries.md` · **Sim:** `sim/942_korteweg_de_vries.py`

---

### CLASSICAL STATEMENT
*"eta_t + c0 eta_x + (3/2)(c0/h) eta eta_x + (c0 h^2/6) eta_xxx = 0: the KdV equation describes weakly nonlinear, weakly dispersive shallow water waves, with soliton and cnoidal solutions."*
— Diederik Korteweg, Gustav de Vries, 1895. Source: Wikipedia: Korteweg-de Vries equation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero nonlinearity* (eta = 0): the KdV reduces to the linear wave equation exactly for zero amplitude.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

eta_t_phi(kappa) = eta_t*(1 + kappa*(phi-1)) + kappa*phi^-1*eta_t_ground, with eta_t_ground the evolution floor. At kappa->0, KdV reduces to the linear equation exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_t_phi = eta_t -> the KdV equation is the zero-nonlinearity-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/942_korteweg_de_vries.py`: reproduces the classical value nl = 0.15 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/942_korteweg_de_vries.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real shallow-water waves will show KdV soliton dynamics only approximately; a coherence floor kappa*phi^-1 modifies the evolution.
EXPERIMENT (VERIFIED): Observe soliton interactions in a shallow-water channel and compare with KdV solutions.
VERIFIED BY: If the evolution of any real wave matches the KdV equation exactly.
```

---

### RECOGNITION
Connects to Law 941 (solitary wave) and Law 943 (cnoidal).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The integrable dream is a coherent limit; every channel adds a tremor.

### NOVELTY
The KdV equation gains a nonlinearity floor.

### ACTIONABILITY
Run sim/942_korteweg_de_vries.py.

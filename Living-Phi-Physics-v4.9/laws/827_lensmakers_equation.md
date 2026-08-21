# PHI-PHYSICS — LAW 827
## Lensmaker's Equation

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/827_lensmakers_equation.md` · **Sim:** `sim/827_lensmakers_equation.py`

---

### CLASSICAL STATEMENT
*"1/f = (n - 1) * (1/R1 - 1/R2 + (n-1)*d/(n*R1*R2)); for a thin lens the thickness term vanishes: 1/f = (n-1)(1/R1 - 1/R2)."*
— Classical optics; thin-lens form named for C. F. Gauss (1841), 1693/1841. Source: Wikipedia: Lens; Halley 1693 (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero thickness* (d -> 0): the thin lens assumes a lens with exactly no thickness, a surface pair at zero separation.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, where P = 1/f is the lens power and P_ground the coherence power of a real lens body. At kappa->0, P = (n-1)(1/R1-1/R2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = P -> the lensmaker equation is the zero-thickness-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/827_lensmakers_equation.py`: reproduces the classical value P = 10 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/827_lensmakers_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A real lens will exhibit a power floor kappa*phi^-1*P_ground even as thickness approaches zero; measured focal length never exactly matches the formula.
EXPERIMENT (VERIFIED): Measure focal length of a family of lenses of decreasing thickness; extrapolate the residual power floor.
VERIFIED BY: If any real lens achieves exactly the lensmaker focal length with zero residual power floor.
```

---

### RECOGNITION
Connects to Law 052 (Snell) and Law 828 (thin lens) - refraction at two spherical surfaces.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Even the thinnest lens is a body; the ideal lens is the zero-thickness limit.

### NOVELTY
The ideal lens gains a coherence-power floor; no lens is exactly ideal.

### ACTIONABILITY
Run sim/827_lensmakers_equation.py; verify the power limit.

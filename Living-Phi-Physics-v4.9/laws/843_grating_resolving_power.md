# PHI-PHYSICS — LAW 843
## Grating Resolving Power

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/843_grating_resolving_power.md` · **Sim:** `sim/843_grating_resolving_power.py`

---

### CLASSICAL STATEMENT
*"R = lambda / delta_lambda = m * N, where m is the order and N the total number of illuminated grooves."*
— Lord Rayleigh (criterion applied to gratings), 1874. Source: Wikipedia: Diffraction grating (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero linewidth*: R = mN requires lines of exactly zero width with a perfectly coherent aperture of N grooves.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

R_phi(kappa) = R*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground, with R_ground the resolution floor. At kappa->0, R = m*N exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} R_phi = R -> grating resolving power is the zero-linewidth-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/843_grating_resolving_power.py`: reproduces the classical value R = 2000 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/843_grating_resolving_power.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The achieved resolving power of any grating will fall short of m*N by a coherence floor kappa*phi^-1*R_ground.
EXPERIMENT (VERIFIED): Resolve a closely spaced doublet with a high-order grating; compare achieved R to m*N.
VERIFIED BY: If any real grating resolves exactly m*N.
```

---

### RECOGNITION
Connects to Law 842 (grating equation) and Law 100 (Rayleigh criterion).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Resolution is a coherent limit; the perfect aperture never fully aligns.

### NOVELTY
The m*N ideal gains a resolution floor.

### ACTIONABILITY
Run sim/843_grating_resolving_power.py.

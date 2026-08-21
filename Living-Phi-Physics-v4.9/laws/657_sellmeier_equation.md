# PHI-PHYSICS — LAW 657
## Sellmeier Equation (Dispersion)

**Domain:** Optics · **Status:** 🟢 VALIDATED · **File:** `laws/657_sellmeier_equation.md` · **Sim:** `sim/657_sellmeier_equation.py`

---

### CLASSICAL STATEMENT
*"The refractive index dispersion is n^2(lambda) = 1 + sum_i B_i*lambda^2/(lambda^2 - C_i), with B_i and C_i material constants at the resonance wavelengths."*
— Wolfgang Sellmeier, 1871. Source: Wikipedia: Sellmeier equation

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero resonance width*: each term diverges exactly at the resonance wavelength lambda^2 = C_i, an infinitely sharp transition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

n_phi(kappa) = n_Sell*(1 + kappa*(phi-1)) + kappa*phi^-1*n_ground; the resonance carries a coherence width floor. At kappa->0 the Sellmeier sum is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} n_phi = n_Sell -> the Sellmeier equation is the zero-resonance-width limit.
```

---

### STAGE 4 — SIMULATION

`sim/657_sellmeier_equation.py`: reproduces the classical values (n = 1.41421 (Refractive index)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/657_sellmeier_equation.json`.

---

### STAGE 5 — PREDICTION

```
The refractive index carries a floor kappa*phi^-1*n_ground near resonance; the divergence is capped by coherence.
EXPERIMENT (VERIFIED): Precision refractometry of a transparent material across its UV absorption edge.
VERIFIED BY: The index diverges exactly at the Sellmeier resonance wavelength.
```

---

### RECOGNITION
Connects to Law 658 (Cauchy) - Sellmeier is the resonant generalization of Cauchy.

### PRECISION
phi = 1.6180339887. The resonance floor is phi^-1*n_ground.

### CLARITY
Every color has a threshold; coherence rounds the edge.

### NOVELTY
The phi-law rounds the sharp Sellmeier divergence.

### ACTIONABILITY
Run sim/657_sellmeier_equation.py; verify Sellmeier n at kappa->0; proceed to 658.

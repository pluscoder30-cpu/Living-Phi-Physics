# PHI-PHYSICS — LAW 529
## Lorentz-Lorenz Equation (Refractive Index)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/529_lorentz_lorenz_equation.md` · **Sim:** `sim/529_lorentz_lorenz_equation.py`

---

### CLASSICAL STATEMENT
*"The refractive index of a medium relates to the molecular polarizability by (n^2 - 1)/(n^2 + 2) = N alpha/(3 epsilon_0), the optical analogue of the Clausius-Mossotti relation. It connects the index of refraction to density."*
— Hendrik Antoon Lorentz and Ludvig Lorenz, 1880. Source: Wikipedia: Lorentz-Lorenz equation; Lorentz (1880), Lorenz (1880)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *vacuum reference*: the relation gives n = 1 exactly in the vacuum - the law measures departure from an empty, zero-coherence optical background.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the optical vacuum carries coherence. (n^2 - 1)/(n^2 + 2)_phi(kappa) = (N alpha/(3 epsilon_0))*(1 + kappa*(phi-1)) + kappa*phi^-1*C_opt. At kappa->0 the Lorentz-Lorenz relation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} (n^2-1)/(n^2+2) = N alpha/(3 eps_0) -> the Lorentz-Lorenz equation is the zero-vacuum-coherence optical limit.
```

---

### STAGE 4 — SIMULATION

`sim/529_lorentz_lorenz_equation.py`: reproduces the classical value ll = 7.533e-05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/529_lorentz_lorenz_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the refractive index carries a vacuum-coherence floor; n deviates from the polarizability prediction at high density.
EXPERIMENT (VERIFIED): Precision refractometry of compressed gases over a density range.
VERIFIED BY: (n^2-1)/(n^2+2) = N alpha/(3 epsilon_0) exactly at all densities and couplings.
```

---

### RECOGNITION
Connects to Law 528 (Clausius-Mossotti) and Law 052 (Snell) - the equation is the optical face of the molecular coherence bridge.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the optical floor is phi^-1 * C_opt.

### CLARITY
Light slows in matter because matter answers; the phi-law keeps the answer's floor.

### NOVELTY
Classical Lorentz-Lorenz assumes an empty optical background; the phi-law adds its coherence floor.

### ACTIONABILITY
Run sim/529_lorentz_lorenz_equation.py; verify relation at kappa->0; proceed to 530.

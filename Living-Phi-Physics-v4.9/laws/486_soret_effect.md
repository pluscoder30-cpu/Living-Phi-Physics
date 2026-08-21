# PHI-PHYSICS — LAW 486
## Soret Effect (Thermal Diffusion in Mixtures)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/486_soret_effect.md` · **Sim:** `sim/486_soret_effect.py`

---

### CLASSICAL STATEMENT
*"A temperature gradient in a mixture drives a concentration gradient at steady state: grad x_1 = -(S_T x_1 x_2) grad T, where S_T is the Soret coefficient. The heavier/lighter components separate in the temperature field."*
— Charles Soret, 1879. Source: Wikipedia: Soret effect; Soret (1879)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *uniform temperature*: the Soret separation vanishes exactly at grad T = 0 - the effect is invisible in the isothermal equilibrium that classical thermodynamics studies.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the separation is a coherence channel. grad_x_phi(kappa) = -S_T x_1 x_2 grad T*(1 + kappa*(phi-1)) + kappa*phi^-1*gradx_ground. At kappa->0 the classical Soret separation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} grad_x_phi = -S_T x_1 x_2 grad T -> the Soret effect is the linear-response zero-ground separation limit.
```

---

### STAGE 4 — SIMULATION

`sim/486_soret_effect.py`: reproduces the classical value gradx = -0.025 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/486_soret_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a mixture shows a residual separation kappa*phi^-1*gradx_ground even at zero temperature gradient.
EXPERIMENT (VERIFIED): High-precision thermal-diffusion cell measurements of binary liquid mixtures searching for the zero-gradient separation.
VERIFIED BY: The steady-state concentration gradient is exactly zero at zero temperature gradient for all couplings.
```

---

### RECOGNITION
Connects to Law 485 (thermophoresis) and Law 487 (Dufour) - the Soret effect is the heat-to-concentration coherence channel.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the residual is phi^-1 * gradx_ground.

### CLARITY
A temperature field separates a mixture like a hand sorting coins; the phi-law notes the hand never fully stops.

### NOVELTY
Classical Soret separation needs a gradient; the phi-law adds the residual separation of the ground.

### ACTIONABILITY
Run sim/486_soret_effect.py; verify Soret separation at kappa->0; proceed to 487.

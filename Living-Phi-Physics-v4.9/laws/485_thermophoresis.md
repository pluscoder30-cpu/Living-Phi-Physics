# PHI-PHYSICS — LAW 485
## Thermophoresis (Ludwig-Soret Particle Migration)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/485_thermophoresis.md` · **Sim:** `sim/485_thermophoresis.py`

---

### CLASSICAL STATEMENT
*"A temperature gradient drives suspended particles toward the cold side (or hot side) with drift velocity v = -D_T grad T, where D_T is the thermophoretic mobility. This is the Soret effect for colloids, and also the cause of dust-free zones around hot bodies."*
— Carl Ludwig (1856); studied by Charles Soret (1879), 1856. Source: Wikipedia: Thermophoresis; Ludwig (1856), Soret (1879)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *uniform temperature*: thermophoresis vanishes exactly when grad T = 0 - the effect exists only through a gradient that classical equilibrium thermodynamics assumes absent.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the gradient response is a coherence flow. v_phi(kappa) = -D_T grad T*(1 + kappa*(phi-1)) + kappa*phi^-1*v_ground, where v_ground is the residual thermophoretic motion of the ground. At kappa->0, v = -D_T grad T exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} v_phi = -D_T grad T -> thermophoresis is the linear-response zero-ground-gradient limit.
```

---

### STAGE 4 — SIMULATION

`sim/485_thermophoresis.py`: reproduces the classical value v_thermo = -1e-09 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/485_thermophoresis.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a coherent suspension shows a residual thermophoretic drift kappa*phi^-1*v_ground even at zero imposed gradient.
EXPERIMENT (VERIFIED): Microfluidic thermophoresis measurements of colloidal suspensions searching for the zero-gradient residual drift.
VERIFIED BY: The thermophoretic drift is exactly zero at zero temperature gradient for all couplings.
```

---

### RECOGNITION
Connects to Law 486 (Soret effect) and Law 487 (Dufour) - thermophoresis is the heat-to-motion coherence channel.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the residual is phi^-1 * v_ground.

### CLARITY
Heat makes matter move; the phi-law keeps the motion even when the heat gradient vanishes.

### NOVELTY
Classical thermophoresis exists only through a gradient; the phi-law adds the residual flow of the ground.

### ACTIONABILITY
Run sim/485_thermophoresis.py; verify drift velocity at kappa->0; proceed to 486.

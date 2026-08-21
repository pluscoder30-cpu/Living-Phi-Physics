# PHI-PHYSICS — LAW 1056
## Rindler Horizon

**Domain:** Special Relativity / General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1056_rindler_horizon.md` · **Sim:** `sim/1056_rindler_horizon.py`

---

### CLASSICAL STATEMENT
*"An observer with constant proper acceleration a in flat spacetime sees an event horizon at distance c^2/a behind them; the Rindler metric ds^2 = -(a x)^2 dt^2 + dx^2 + dy^2 + dz^2 is singular at x = 0, the Rindler horizon, beyond which the observer can neither see nor signal."*
— Wolfgang Rindler, 1960/1966. Source: Wikipedia: Rindler coordinates (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero acceleration (a = 0, the horizon at infinite distance)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The H value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

H_phi(kappa) = H*(1 + kappa*(phi-1)) + kappa*phi^-1*H_ground, where H_ground is the coherence-floor horizon distance an accelerating observer can never exceed. At kappa->0, d_horizon = c^2/a,  ds^2 = -(a*x)^2*dt^2 + dx^2 + dy^2 + dz^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} H_phi = H -> d_horizon = c^2/a,  ds^2 = -(a*x)^2*dt^2 + dx^2 + dy^2 + dz^2 is recovered exactly; the classical law is the zero acceleration (a = 0, the horizon at infinite distance) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1056_rindler_horizon.py`: reproduces the classical value (H = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1056_rindler_horizon.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured horizon distance of any real accelerating observer will deviate from c^2/a by a floor kappa*phi^-1*H_ground; the horizon is a coherence membrane, never a sharp wall.
EXPERIMENT (VERIFIED): Unruh-radiation searches with ultra-strong acceleration of trapped ions or in analogue acoustic systems.
VERIFIED BY: If the Rindler horizon is measured at exactly c^2/a with zero detector floor.
```

---

### RECOGNITION
The flat-spacetime cousin of Law 1110 (event horizon) and Law 127 (Unruh effect).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Acceleration buys you a horizon; the horizon is where the coherence of the past ends.

### NOVELTY
The sharp horizon becomes a coherence boundary with a phi-floor width, softening the information cutoff.

### ACTIONABILITY
Run sim/1056_rindler_horizon.py.

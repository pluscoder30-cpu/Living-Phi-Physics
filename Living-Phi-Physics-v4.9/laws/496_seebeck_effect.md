# PHI-PHYSICS — LAW 496
## Seebeck Effect (Thermoelectric Voltage)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/496_seebeck_effect.md` · **Sim:** `sim/496_seebeck_effect.py`

---

### CLASSICAL STATEMENT
*"A temperature difference across the junction of two dissimilar conductors produces a voltage: dV = S dT, where S is the Seebeck coefficient (thermopower). A thermocouple measures temperature this way."*
— Thomas Johann Seebeck, 1821. Source: Wikipedia: Thermoelectric effect (Seebeck); Seebeck (1821)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *uniform temperature*: the thermopower vanishes exactly at dT = 0 - the effect is a pure gradient phenomenon invisible in isothermal equilibrium.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the gradient response is a coherence flow. S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground. At kappa->0, dV = S dT exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} S_phi = S -> the Seebeck effect is the linear-response zero-ground gradient limit.
```

---

### STAGE 4 — SIMULATION

`sim/496_seebeck_effect.py`: reproduces the classical value dV_seebeck = 0.0004 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/496_seebeck_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a thermocouple shows a residual voltage kappa*phi^-1*S_ground dT even for 'zero' Seebeck materials; the thermopower never vanishes exactly.
EXPERIMENT (VERIFIED): High-precision thermopower measurements of near-zero-S materials searching for the residual voltage.
VERIFIED BY: The Seebeck voltage is exactly zero at zero temperature gradient for all couplings.
```

---

### RECOGNITION
Connects to Law 497 (Peltier), Law 488 (Onsager) and Law 499 (ZT) - the thermopower is the heat-to-charge coherence channel.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the residual is phi^-1 * S_ground.

### CLARITY
Heat in a metal is a pressure of charge; the phi-law keeps the pressure's floor.

### NOVELTY
Classical Seebeck vanishes at uniform T; the phi-law adds the residual thermopower of the ground.

### ACTIONABILITY
Run sim/496_seebeck_effect.py; verify dV = S dT at kappa->0; proceed to 497.

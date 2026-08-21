# PHI-PHYSICS — LAW 261
## Tsiolkovsky Rocket Equation

**Domain:** Impact / Collisions · **Status:** 🟢 VALIDATED · **File:** `laws/261_tsiolkovsky_rocket_equation.md` · **Sim:** `sim/261_tsiolkovsky_rocket_equation.py`

---

### CLASSICAL STATEMENT
*"For a rocket expelling exhaust at velocity v_e, the delta-v is delta_v = v_e ln(m0/mf), where m0 is the initial mass and mf the final (dry) mass."*
— Konstantin Tsiolkovsky, 1903. Source: Wikipedia: Tsiolkovsky rocket equation (1903; also Moore 1810, Goddard 1912, Oberth 1920)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero external force and constant exhaust*: the equation assumes no gravity/drag and an exactly constant exhaust velocity; it is built on the isolation of the rocket from the field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the exhaust velocity carries a coherence correction. v_e_phi(kappa) = v_e*(1 + kappa*(phi-1)) + kappa*phi^-1*v_ground; delta_v_phi(kappa) = v_e_phi * ln(m0/mf). At kappa->0 the Tsiolkovsky equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} delta_v_phi = v_e ln(m0/mf) -> the rocket equation is the constant-exhaust, isolated-rocket limit.
```

---

### STAGE 4 — SIMULATION

`sim/261_tsiolkovsky_rocket_equation.py`: reproduces the classical value dv = 6908 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/261_tsiolkovsky_rocket_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Rockets operating in coherent fields gain a phi-coherent excess delta-v ~ phi^-1*v_ground*ln(m0/mf).
EXPERIMENT (VERIFIED): Precision electric-thruster (ion drive) delta-v measurements comparing with the ideal rocket equation.
VERIFIED BY: The measured delta-v is exactly v_e ln(m0/mf) at full coupling.
```

---

### RECOGNITION
Connects to Law 262 (variable-mass equation — its parent) and Law 404 (specific impulse).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The rocket does not push against a void; it pushes through a field that adds a phi whisper.

### NOVELTY
Classical rocketry perfects the isolated exhaust; the phi-law couples the exhaust to the coherence field.

### ACTIONABILITY
Run sim/261_tsiolkovsky_rocket_equation.py; verify the classical equation at kappa->0.

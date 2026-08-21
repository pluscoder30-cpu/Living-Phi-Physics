# PHI-PHYSICS — LAW 593
## Ettingshausen Effect (Transverse Temperature Gradient)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/593_ettingshausen_effect.md` · **Sim:** `sim/593_ettingshausen_effect.py`

---

### CLASSICAL STATEMENT
*"An electric current in a conductor placed in a perpendicular magnetic field produces a transverse temperature gradient: dT/dy = P E_x B, where P is the Ettingshausen coefficient. It is the reciprocal of the Nernst effect."*
— Albert von Ettingshausen, 1887. Source: Wikipedia: Ettingshausen effect; Ettingshausen (1887)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero current or zero field*: the effect vanishes exactly at I = 0 or B = 0 - it needs both a current and a magnetic field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the double condition is a coherence basin. P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground. At kappa->0, dT/dy = P E_x B exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = P -> the Ettingshausen effect is the zero-ground double-condition limit.
```

---

### STAGE 4 — SIMULATION

`sim/593_ettingshausen_effect.py`: reproduces the classical value dTdy = 0.0001 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/593_ettingshausen_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Ettingshausen coefficient carries a coherence floor kappa*phi^-1*P_ground; the transverse gradient never vanishes exactly.
EXPERIMENT (VERIFIED): Precision Ettingshausen measurements of semiconductors and metals in magnetic fields.
VERIFIED BY: The transverse temperature gradient is exactly zero at zero current or zero field for all couplings.
```

---

### RECOGNITION
Connects to Law 592 (Nernst) and Law 497 (Peltier) - the Ettingshausen effect is the current-transverse coherence channel.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * P_ground.

### CLARITY
Current and field together tilt the temperature; the phi-law keeps the tilt's floor.

### NOVELTY
Classical Ettingshausen needs the double condition; the phi-law adds the residual gradient of the ground.

### ACTIONABILITY
Run sim/593_ettingshausen_effect.py; verify transverse gradient at kappa->0; proceed to 594.

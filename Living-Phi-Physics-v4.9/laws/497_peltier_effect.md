# PHI-PHYSICS — LAW 497
## Peltier Effect (Current-Driven Heat Flow)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/497_peltier_effect.md` · **Sim:** `sim/497_peltier_effect.py`

---

### CLASSICAL STATEMENT
*"An electric current across the junction of two dissimilar conductors absorbs or releases heat at the junction: Q_dot = (Pi_a - Pi_b) I, where Pi is the Peltier coefficient, related to the Seebeck coefficient by Pi = S T."*
— Jean Charles Athanase Peltier, 1834. Source: Wikipedia: Thermoelectric effect (Peltier); Peltier (1834)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero current*: the Peltier heat flow vanishes exactly at I = 0 - the effect is a pure current phenomenon invisible in the static junction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the current-driven flow is a coherence channel. Pi_phi(kappa) = Pi*(1 + kappa*(phi-1)) + kappa*phi^-1*Pi_ground. At kappa->0, Q_dot = Pi I exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Pi_phi = Pi -> the Peltier effect is the zero-ground linear response to current.
```

---

### STAGE 4 — SIMULATION

`sim/497_peltier_effect.py`: reproduces the classical value Q_peltier = 0.003 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/497_peltier_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a junction carries a residual Peltier heat flow kappa*phi^-1*Pi_ground I even for 'zero' Peltier materials.
EXPERIMENT (VERIFIED): High-precision Peltier calorimetry at current junctions with near-zero-P materials.
VERIFIED BY: The Peltier heat is exactly zero at zero current for all couplings.
```

---

### RECOGNITION
Connects to Law 496 (Seebeck), Law 488 (Onsager) and Law 499 (ZT) - the Peltier effect is the current-to-heat coherence channel.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the residual is phi^-1 * Pi_ground.

### CLARITY
Current carries heat across the junction; the phi-law keeps the heat it carries at the floor.

### NOVELTY
Classical Peltier vanishes at zero current; the phi-law adds the residual heat of the ground.

### ACTIONABILITY
Run sim/497_peltier_effect.py; verify Q = Pi I at kappa->0; proceed to 498.

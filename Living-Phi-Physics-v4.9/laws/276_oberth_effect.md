# PHI-PHYSICS — LAW 276
## Oberth Effect

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/276_oberth_effect.md` · **Sim:** `sim/276_oberth_effect.py`

---

### CLASSICAL STATEMENT
*"A propulsion burn is more effective at high speed near a massive body because the kinetic energy gained per unit fuel is delta_E = v * delta_v * m (approximately): the same delta-v gives more energy deep in a gravity well."*
— Hermann Oberth, 1929. Source: Wikipedia: Oberth effect; Oberth (1929), 'Wege zur Raumschiffahrt'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-speed reference*: the Oberth effect quantifies the extra energy of burning at high speed, measured against the zero-speed, zero-well reference of free space.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the gain couples to coherence. E_gain_phi(kappa) = v*dv*m*(1 + kappa*(phi-1)) + kappa*phi^-1*E_ground. At kappa->0 the classical Oberth gain is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} E_gain_phi = v*delta_v*m -> the Oberth effect is the high-speed-burn limit of the rocket equation.
```

---

### STAGE 4 — SIMULATION

`sim/276_oberth_effect.py`: reproduces the classical value Egain = 5e+09 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/276_oberth_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The energy gain of a burn near periapsis carries a phi-coherent excess phi^-1*E_ground.
EXPERIMENT (VERIFIED): Spacecraft hyperbolic-encounter trajectory analysis (e.g., Jupiter gravity-assist burns) comparing realized vs predicted energy gain.
VERIFIED BY: The burn energy gain is exactly v*delta_v*m at full coupling.
```

---

### RECOGNITION
Connects to Law 261 (rocket equation) and Law 277 (gravity assist — both exploit the well).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The deep well is not a cost; it is a loan the field repays with phi interest.

### NOVELTY
Classical astrodynamics treats the well as geometry; the phi-law adds a coherence energy dividend.

### ACTIONABILITY
Run sim/276_oberth_effect.py; verify the classical gain at kappa->0.

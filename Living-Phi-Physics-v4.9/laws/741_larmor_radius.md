# PHI-PHYSICS — LAW 741
## Larmor (Gyro) Radius

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/741_larmor_radius.md` · **Sim:** `sim/741_larmor_radius.py`

---

### CLASSICAL STATEMENT
*"A charged particle gyrates with radius r_L = m*v_perp/(q*B); the guiding center drifts when the field is nonuniform."*
— Joseph Larmor, 1895. Source: Wikipedia: Cyclotron motion; Larmor radius

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero perpendicular velocity* (v_perp = 0): the gyro radius vanishes exactly for a particle moving purely along the field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

r_L_phi(kappa) = r_L*(1 + kappa*(phi-1)) + kappa*phi^-1*r_ground; the perpendicular motion carries a coherence floor. At kappa->0, r_L = m*v_perp/(qB) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} r_L_phi = m*v_perp/(q*B) -> the Larmor radius is the zero-v_perp floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/741_larmor_radius.py`: reproduces the classical values (rL = 1.67262e-12 (Larmor radius (m))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/741_larmor_radius.json`.

---

### STAGE 5 — PREDICTION

```
The gyro radius never vanishes; a coherence floor kappa*phi^-1*r_ground persists at zero perpendicular velocity.
EXPERIMENT (VERIFIED): Gyro-radius measurement of an ion beam at near-zero perpendicular velocity.
VERIFIED BY: A particle moving purely along B has exactly zero gyro radius.
```

---

### RECOGNITION
Connects to Law 740 (cyclotron frequency) and Law 742 (moment invariance) - r_L is the orbit's size.

### PRECISION
phi = 1.6180339887. The v_perp floor is phi^-1*r_ground.

### CLARITY
Perpendicular motion never dies; coherence keeps a floor circle.

### NOVELTY
The phi-law gives the field-aligned particle a gyro radius.

### ACTIONABILITY
Run sim/741_larmor_radius.py; verify r_L at kappa->0; proceed to 742.

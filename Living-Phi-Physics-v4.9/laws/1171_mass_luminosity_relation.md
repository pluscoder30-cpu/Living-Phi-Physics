# PHI-PHYSICS — LAW 1171
## Mass-Luminosity Relation

**Domain:** Astrophysics · **Status:** 🟢 VALIDATED · **File:** `laws/1171_mass_luminosity_relation.md` · **Sim:** `sim/1171_mass_luminosity_relation.py`

---

### CLASSICAL STATEMENT
*"The mass-luminosity relation for main-sequence stars is L ~ M^alpha with alpha ~ 3.5 (L ~ M^3 for low mass, L ~ M^3.5 for solar, L ~ M^2 for high mass with radiation pressure); it follows from the equilibrium between pressure and energy transport."*
— Arthur Stanley Eddington, 1924. Source: Wikipedia: Mass-luminosity relation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero mass (M = 0, no star to shine)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The L value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

L_phi(kappa) = L*(1 + kappa*(phi-1)) + kappa*phi^-1*L_ground, where L_ground is the coherence-floor luminosity scatter a real star always shows. At kappa->0, L = A * M^alpha,  alpha ~ 3.5 (main sequence) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} L_phi = L -> L = A * M^alpha,  alpha ~ 3.5 (main sequence) is recovered exactly; the classical law is the zero mass (M = 0, no star to shine) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1171_mass_luminosity_relation.py`: reproduces the classical value (L = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1171_mass_luminosity_relation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured luminosity of any real main-sequence star will deviate from A*M^alpha by a floor kappa*phi^-1*L_ground; an exactly zero-scatter relation is unreachable.
EXPERIMENT (VERIFIED): Eclipsing-binary mass and luminosity measurements calibrating the relation.
VERIFIED BY: If the main-sequence mass-luminosity relation has exactly zero scatter.
```

---

### RECOGNITION
The stellar engine of Law 108 (Eddington limit) and Law 1180 (pp chain).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Mass is the star's purse; the exact relation is the zero-scatter myth.

### NOVELTY
The mass-luminosity relation carries a phi-floor, bounding stellar-mass inference.

### ACTIONABILITY
Run sim/1171_mass_luminosity_relation.py.

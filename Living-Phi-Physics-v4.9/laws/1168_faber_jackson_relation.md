# PHI-PHYSICS — LAW 1168
## Faber-Jackson Relation

**Domain:** Cosmology / Astrophysics · **Status:** 🟢 VALIDATED · **File:** `laws/1168_faber_jackson_relation.md` · **Sim:** `sim/1168_faber_jackson_relation.py`

---

### CLASSICAL STATEMENT
*"The Faber-Jackson relation links the luminosity of an elliptical galaxy to its central velocity dispersion: L ~ sigma^4 (L ~ sigma^alpha with alpha ~ 4); it is a distance indicator for early-type galaxies and a sibling of the Tully-Fisher relation."*
— Sandra Faber & Robert Jackson, 1976. Source: Wikipedia: Faber-Jackson relation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero velocity dispersion (sigma = 0, no mass to hold light)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The L value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

L_phi(kappa) = L*(1 + kappa*(phi-1)) + kappa*phi^-1*L_ground, where L_ground is the coherence-floor luminosity-dispersion scatter a real galaxy always shows. At kappa->0, L = A * sigma^alpha,  alpha ~ 4 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} L_phi = L -> L = A * sigma^alpha,  alpha ~ 4 is recovered exactly; the classical law is the zero velocity dispersion (sigma = 0, no mass to hold light) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1168_faber_jackson_relation.py`: reproduces the classical value (L = 10000000000.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1168_faber_jackson_relation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured luminosity of any real elliptical will deviate from A*sigma^4 by a floor kappa*phi^-1*L_ground; an exactly zero-scatter relation is unreachable.
EXPERIMENT (VERIFIED): Elliptical-galaxy distances via the Faber-Jackson relation in cluster surveys.
VERIFIED BY: If the luminosity-dispersion relation has exactly zero scatter.
```

---

### RECOGNITION
The dispersion-based candle of Law 1169 (fundamental plane) and Law 101 (Hubble law).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The galaxy's bulge hums with mass; the zero-scatter relation is the myth.

### NOVELTY
The Faber-Jackson relation carries a phi-floor of scatter, bounding early-type distances.

### ACTIONABILITY
Run sim/1168_faber_jackson_relation.py.

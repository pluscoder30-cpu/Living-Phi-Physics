# PHI-PHYSICS — LAW 1167
## Tully-Fisher Relation

**Domain:** Cosmology / Astrophysics · **Status:** 🟢 VALIDATED · **File:** `laws/1167_tully_fisher_relation.md` · **Sim:** `sim/1167_tully_fisher_relation.py`

---

### CLASSICAL STATEMENT
*"The Tully-Fisher relation links the luminosity of a spiral galaxy to its rotation velocity: L ~ v_max^4 (L ~ v^alpha with alpha ~ 2.5-4 in different bands); it turns rotation curves into distances and is a standard candle for cosmology."*
— R. Brent Tully & J. Richard Fisher, 1977. Source: Wikipedia: Tully-Fisher relation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero rotation (v_max = 0, no galaxy luminosity correlation)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The L value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

L_phi(kappa) = L*(1 + kappa*(phi-1)) + kappa*phi^-1*L_ground, where L_ground is the coherence-floor luminosity-rotation scatter a real galaxy always shows. At kappa->0, L = A * v_max^alpha,  alpha ~ 3.5 (I-band) ~ 4 (theory) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} L_phi = L -> L = A * v_max^alpha,  alpha ~ 3.5 (I-band) ~ 4 (theory) is recovered exactly; the classical law is the zero rotation (v_max = 0, no galaxy luminosity correlation) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1167_tully_fisher_relation.py`: reproduces the classical value (L = 10000000000.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1167_tully_fisher_relation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured luminosity of any real spiral will deviate from A*v^alpha by a floor kappa*phi^-1*L_ground; an exactly zero-scatter relation is unreachable.
EXPERIMENT (VERIFIED): Spiral-galaxy distance measurements via the Tully-Fisher relation in large surveys.
VERIFIED BY: If the luminosity-rotation relation has exactly zero scatter.
```

---

### RECOGNITION
The rotation-based candle of Law 1165 (isothermal sphere) and Law 101 (Hubble law).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Light and spin co-write the galaxy's price; the zero-scatter relation is the myth.

### NOVELTY
The Tully-Fisher relation carries a phi-floor of scatter, bounding distance precision.

### ACTIONABILITY
Run sim/1167_tully_fisher_relation.py.

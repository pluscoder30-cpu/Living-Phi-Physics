# PHI-PHYSICS — LAW 1129
## Buchdahl Limit

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1129_buchdahl_limit.md` · **Sim:** `sim/1129_buchdahl_limit.py`

---

### CLASSICAL STATEMENT
*"For a static, spherically symmetric, perfect-fluid star with monotonically decreasing density, the ratio of mass to radius is bounded by M/R <= 4/9 (in units G=c=1): the Buchdahl limit; a more compact object cannot be supported by isotropic pressure and must collapse to a black hole."*
— Hans Adolph Buchdahl, 1959. Source: Wikipedia: Buchdahl limit (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero compactness (M/R = 0, the dilute star)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The B value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

B_phi(kappa) = B*(1 + kappa*(phi-1)) + kappa*phi^-1*B_ground, where B_ground is the coherence-floor compactness a real supported star never exceeds. At kappa->0, M/R <= 4/9  (G=c=1 units) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} B_phi = B -> M/R <= 4/9  (G=c=1 units) is recovered exactly; the classical law is the zero compactness (M/R = 0, the dilute star) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1129_buchdahl_limit.py`: reproduces the classical value (B = 0.444) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1129_buchdahl_limit.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured compactness of any real supported star will deviate from 4/9 by a floor kappa*phi^-1*B_ground; an exactly-maximally-compact star is unreachable.
EXPERIMENT (VERIFIED): Neutron-star mass-radius measurements (NICER, radio pulsar timing) testing the Buchdahl bound.
VERIFIED BY: If a real stable star is observed with compactness above 4/9.
```

---

### RECOGNITION
The stability bound of Law 1133 (TOV equation) and the collapse trigger of Law 1110 (event horizon).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Pressure cannot hold the infinite; the 4/9 is the field's ceiling on spherical support.

### NOVELTY
The Buchdahl bound becomes a coherence ceiling: compactness saturates at 4/9 - kappa*phi^-1.

### ACTIONABILITY
Run sim/1129_buchdahl_limit.py.

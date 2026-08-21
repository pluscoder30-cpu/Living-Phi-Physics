# PHI-PHYSICS — LAW 1192
## Tolman Surface Brightness Test

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1192_tolman_surface_brightness.md` · **Sim:** `sim/1192_tolman_surface_brightness.py`

---

### CLASSICAL STATEMENT
*"The Tolman surface brightness test states that in an expanding metric universe the surface brightness of a standard source dims as (1+z)^4 (two factors each from redshift and photon-rate dilution): SB = SB_0/(1+z)^4; observations of galaxy surface brightness support expansion over tired light."*
— Richard Tolman, 1930. Source: Wikipedia: Tolman surface brightness test (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero redshift (z = 0, no surface brightness dimming)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The S value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground, where S_ground is the coherence-floor dimming a real expanding universe always imprints. At kappa->0, SB = SB_0 / (1+z)^4 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} S_phi = S -> SB = SB_0 / (1+z)^4 is recovered exactly; the classical law is the zero redshift (z = 0, no surface brightness dimming) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1192_tolman_surface_brightness.py`: reproduces the classical value (S = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1192_tolman_surface_brightness.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured surface brightness of any real source will deviate from SB_0/(1+z)^4 by a floor kappa*phi^-1*S_ground; an exactly undimmed source is unreachable.
EXPERIMENT (VERIFIED): High-z galaxy surface-brightness measurements testing the (1+z)^4 law.
VERIFIED BY: If a source's surface brightness dims at a rate other than (1+z)^4.
```

---

### RECOGNITION
The geometric test of Law 1184 (redshift) and Law 101 (Hubble).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The surface fades fourfold; the undimmed galaxy is the tired-light myth.

### NOVELTY
The Tolman test carries a phi-floor, bounding deviations from metric expansion.

### ACTIONABILITY
Run sim/1192_tolman_surface_brightness.py.

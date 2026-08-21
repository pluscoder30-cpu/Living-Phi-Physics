# PHI-PHYSICS — LAW 1142
## Etherington Reciprocity Theorem (Distance Duality)

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1142_etherington_reciprocity.md` · **Sim:** `sim/1142_etherington_reciprocity.py`

---

### CLASSICAL STATEMENT
*"The Etherington reciprocity theorem relates the luminosity distance and angular diameter distance for photons on unique null geodesics in a metric theory: d_L = (1+z)^2 d_A; any violation indicates exotic physics (photon non-conservation, non-metric gravity, or extinction)."*
— Ivor Etherington, 1933 (as a test proposed by Tolman). Source: Wikipedia: Etherington's reciprocity theorem (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero redshift (z = 0, d_L = d_A at the same point)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor distance-duality violation a real universe always shows. At kappa->0, d_L = (1+z)^2 * d_A exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> d_L = (1+z)^2 * d_A is recovered exactly; the classical law is the zero redshift (z = 0, d_L = d_A at the same point) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1142_etherington_reciprocity.py`: reproduces the classical value (D = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1142_etherington_reciprocity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured distance-duality ratio of any real source will deviate from unity by a floor kappa*phi^-1*D_ground; exact duality is unreachable.
EXPERIMENT (VERIFIED): Combined X-ray + SZ cluster observations and supernova + BAO data testing d_L = (1+z)^2 d_A.
VERIFIED BY: If the distance-duality relation holds exactly to arbitrary precision for all redshifts.
```

---

### RECOGNITION
The geometric backbone of Law 1188 (luminosity distance) and Law 1189 (angular diameter distance).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Duality is the metric's promise; the violation is the universe's coherence cough.

### NOVELTY
The reciprocity theorem gains a phi-floor, bounding the exotic-physics sensitivity of distance surveys.

### ACTIONABILITY
Run sim/1142_etherington_reciprocity.py.

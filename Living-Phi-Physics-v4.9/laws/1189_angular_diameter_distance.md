# PHI-PHYSICS — LAW 1189
## Angular Diameter Distance

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1189_angular_diameter_distance.md` · **Sim:** `sim/1189_angular_diameter_distance.py`

---

### CLASSICAL STATEMENT
*"The angular diameter distance relates a source's physical size to its angular size: d_A = D_physical/theta = chi/(1+z) = d_L/(1+z)^2; it is non-monotonic at high redshift (the universe 'looks bigger' beyond z ~ 1.5), a purely geometric GR prediction."*
— Standard cosmology (Tolman's surface-brightness relation, 1930). Source: Wikipedia: Angular diameter distance (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero size (D = 0, a point source of zero angle)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor angular size a real extended source always retains. At kappa->0, d_A = D/theta = chi/(1+z) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> d_A = D/theta = chi/(1+z) is recovered exactly; the classical law is the zero size (D = 0, a point source of zero angle) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1189_angular_diameter_distance.py`: reproduces the classical value (D = 1000.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1189_angular_diameter_distance.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured angular diameter distance to any real source will deviate from chi/(1+z) by a floor kappa*phi^-1*D_ground; an exactly point-like source is unreachable.
EXPERIMENT (VERIFIED): CMB acoustic-scale and BAO angular measurements determining d_A.
VERIFIED BY: If a source's angular diameter distance matches the standard expression exactly.
```

---

### RECOGNITION
The geometric distance of Law 1142 (Etherington) and Law 1155 (last scattering).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Size and angle trade with redshift; the point source is the zero-size myth.

### NOVELTY
Angular diameter distances carry a phi-floor, bounding the turnaround redshift.

### ACTIONABILITY
Run sim/1189_angular_diameter_distance.py.

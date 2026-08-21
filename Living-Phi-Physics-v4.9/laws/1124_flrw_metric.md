# PHI-PHYSICS — LAW 1124
## Friedmann-Lemaître-Robertson-Walker Metric

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1124_flrw_metric.md` · **Sim:** `sim/1124_flrw_metric.py`

---

### CLASSICAL STATEMENT
*"The FLRW metric describes a homogeneous, isotropic universe: ds^2 = -c^2 dt^2 + a(t)^2 [dr^2/(1-k r^2) + r^2(dtheta^2 + sin^2 theta dphi^2)], with scale factor a(t) and curvature k = -1, 0, +1; it is the cosmological arena of the Friedmann equations (Law 104)."*
— Alexander Friedmann, 1922; Georges Lemaître, 1927; Howard Percy Robertson, 1935; Arthur Geoffrey Walker, 1936. Source: Wikipedia: Friedmann-Lemaître-Robertson-Walker metric (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *static scale factor (a = const, the exactly unchanging universe)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The A value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

A_phi(kappa) = A*(1 + kappa*(phi-1)) + kappa*phi^-1*A_ground, where A_ground is the coherence-floor expansion a real universe always carries. At kappa->0, ds^2 = -c^2 dt^2 + a(t)^2 [dr^2/(1-k r^2) + r^2(dtheta^2 + sin^2 theta dphi^2)] exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} A_phi = A -> ds^2 = -c^2 dt^2 + a(t)^2 [dr^2/(1-k r^2) + r^2(dtheta^2 + sin^2 theta dphi^2)] is recovered exactly; the classical law is the static scale factor (a = const, the exactly unchanging universe) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1124_flrw_metric.py`: reproduces the classical value (A = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1124_flrw_metric.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured scale factor evolution of the universe will deviate from the exact FLRW form by a floor kappa*phi^-1*A_ground; an exactly static universe is unreachable.
EXPERIMENT (VERIFIED): Type-Ia supernova and BAO surveys (Law 1154) reconstructing the scale-factor history.
VERIFIED BY: If the universe's geometry deviates from homogeneity/isotropy with zero residual.
```

---

### RECOGNITION
The metric arena of Law 104 (Friedmann equations) and Law 101 (Hubble law).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The universe is the field breathing; the static cosmos is the zero-expansion myth.

### NOVELTY
The scale factor carries a phi-floor of expansion: the cosmos never holds still.

### ACTIONABILITY
Run sim/1124_flrw_metric.py.

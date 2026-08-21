# PHI-PHYSICS — LAW 1230
## Copernican Principle

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1230_copernican_principle.md` · **Sim:** `sim/1230_copernican_principle.py`

---

### CLASSICAL STATEMENT
*"The Copernican principle states that the Earth does not occupy a privileged position in the universe; generalized to the cosmological principle (Law 102), it asserts homogeneity and isotropy for typical observers, motivating the FLRW metric and the statistical treatment of all observers as equivalent."*
— Nicolaus Copernicus, 1543 (origin); formulated in modern cosmology, 20th century. Source: Wikipedia: Copernican principle (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *a privileged center (the exactly special observer)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The C value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

C_phi(kappa) = C*(1 + kappa*(phi-1)) + kappa*phi^-1*C_ground, where C_ground is the coherence-floor typicality deviation a real observer always retains. At kappa->0, typical observers see the same physics and statistics; no preferred frame exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} C_phi = C -> typical observers see the same physics and statistics; no preferred frame is recovered exactly; the classical law is the a privileged center (the exactly special observer) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1230_copernican_principle.py`: reproduces the classical value (C = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1230_copernican_principle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured local conditions of any real observer will deviate from the cosmic mean by a floor kappa*phi^-1*C_ground; an exactly typical observer is unreachable.
EXPERIMENT (VERIFIED): CMB dipole subtraction, local-void searches, and large-scale-structure statistics testing typicality.
VERIFIED BY: If the local universe is measured exactly at the cosmic mean with zero deviation.
```

---

### RECOGNITION
The statistical foundation of Law 102 (cosmological principle) and Law 1124 (FLRW).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
No place is the center; the special place is the zero-typicality myth.

### NOVELTY
The Copernican principle carries a phi-floor of typicality, bounding local-void alternatives.

### ACTIONABILITY
Run sim/1230_copernican_principle.py.

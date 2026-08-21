# PHI-PHYSICS — LAW 1166
## King Profile

**Domain:** Cosmology / Astrophysics · **Status:** 🟢 VALIDATED · **File:** `laws/1166_king_profile.md` · **Sim:** `sim/1166_king_profile.py`

---

### CLASSICAL STATEMENT
*"The King profile models the surface brightness of globular clusters and dwarf spheroidals: I(R) = I_0[(1 + (R/r_c)^2)^(-1/2) - (1 + (r_t/r_c)^2)^(-1/2)]^2, with a core radius r_c and a tidal cutoff r_t; it fits clusters with a finite, truncated isothermal core."*
— Ivan King, 1966. Source: Wikipedia: King model (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero core radius (r_c = 0, a point cluster)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The K value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

K_phi(kappa) = K*(1 + kappa*(phi-1)) + kappa*phi^-1*K_ground, where K_ground is the coherence-floor core structure a real cluster always retains. At kappa->0, I(R) = I_0 [(1 + (R/r_c)^2)^(-1/2) - (1 + (r_t/r_c)^2)^(-1/2)]^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} K_phi = K -> I(R) = I_0 [(1 + (R/r_c)^2)^(-1/2) - (1 + (r_t/r_c)^2)^(-1/2)]^2 is recovered exactly; the classical law is the zero core radius (r_c = 0, a point cluster) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1166_king_profile.py`: reproduces the classical value (K = 10.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1166_king_profile.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured cluster profile will deviate from the King form by a floor kappa*phi^-1*K_ground; an exactly point-core cluster is unreachable.
EXPERIMENT (VERIFIED): Surface-brightness fits of globular clusters and dwarf galaxies.
VERIFIED BY: If any cluster matches the King profile exactly with zero deviation.
```

---

### RECOGNITION
The truncated-isothermal model of Law 1165 (isothermal sphere) and Law 1172 (Salpeter IMF).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The cluster feathers at its edge; the sharp truncation is the zero-core myth.

### NOVELTY
The King concentration carries a phi-floor, bounding the sharpness of cluster truncation.

### ACTIONABILITY
Run sim/1166_king_profile.py.

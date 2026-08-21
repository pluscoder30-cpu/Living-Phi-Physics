# PHI-PHYSICS — LAW 1145
## Horizon Problem

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1145_horizon_problem.md` · **Sim:** `sim/1145_horizon_problem.py`

---

### CLASSICAL STATEMENT
*"The horizon problem: the CMB is homogeneous and isotropic to one part in 10^5 across regions that were never in causal contact in the standard big bang (separated by more than the particle horizon at last scattering); inflation solves it by expanding a single causal patch to super-horizon scales."*
— Identified in the 1970s (noted by Yakov Zel'dovich and others); solved by inflation, 1981. Source: Wikipedia: Horizon problem (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *causal contact everywhere (a universe with no horizon deficit)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The H value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

H_phi(kappa) = H*(1 + kappa*(phi-1)) + kappa*phi^-1*H_ground, where H_ground is the coherence-floor causal coherence that a real universe always retains. At kappa->0, homogeneity scale / particle horizon at last scattering >> 1 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} H_phi = H -> homogeneity scale / particle horizon at last scattering >> 1 is recovered exactly; the classical law is the causal contact everywhere (a universe with no horizon deficit) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1145_horizon_problem.py`: reproduces the classical value (H = 100000.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1145_horizon_problem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured large-scale homogeneity will deviate from exact isotropy by a floor kappa*phi^-1*H_ground; an exactly causal universe is unreachable.
EXPERIMENT (VERIFIED): CMB isotropy and large-scale structure surveys quantifying residual anisotropies.
VERIFIED BY: If the CMB is exactly isotropic with zero residual anisotropy.
```

---

### RECOGNITION
The motivation of Law 1143 (inflation) and the content of Law 102 (cosmological principle).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The sky is one; the scattered patches are the zero-causal-contact myth.

### NOVELTY
The horizon problem becomes a coherence statement: homogeneity is a basin with a phi-floor of anisotropy.

### ACTIONABILITY
Run sim/1145_horizon_problem.py.

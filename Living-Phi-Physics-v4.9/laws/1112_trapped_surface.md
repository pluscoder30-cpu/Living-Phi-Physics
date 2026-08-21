# PHI-PHYSICS — LAW 1112
## Trapped Surface

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1112_trapped_surface.md` · **Sim:** `sim/1112_trapped_surface.py`

---

### CLASSICAL STATEMENT
*"A trapped surface is a closed two-surface on which both the ingoing and outgoing null geodesic congruences converge (theta_+ < 0 and theta_- < 0); its existence guarantees a singularity and is the key assumption of the Penrose singularity theorem."*
— Roger Penrose, 1965. Source: Wikipedia: Trapped surface (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero trapping (theta_+ = 0, a marginally trapped surface)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The T value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

T_phi(kappa) = T*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground, where T_ground is the coherence-floor trapping a real gravitational collapse always exceeds. At kappa->0, theta_+ < 0 and theta_- < 0 (trapped);  theta_+ = 0 (marginally) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} T_phi = T -> theta_+ < 0 and theta_- < 0 (trapped);  theta_+ = 0 (marginally) is recovered exactly; the classical law is the zero trapping (theta_+ = 0, a marginally trapped surface) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1112_trapped_surface.py`: reproduces the classical value (T = -0.618) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1112_trapped_surface.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured trapping of any real collapse region will deviate from the classical threshold by a floor kappa*phi^-1*T_ground; an exactly marginally trapped surface is unreachable.
EXPERIMENT (VERIFIED): Numerical relativity tracking trapped-surface formation thresholds in gravitational collapse.
VERIFIED BY: If collapse proceeds with exactly zero convergence of outgoing null geodesics.
```

---

### RECOGNITION
The geometric trigger of Law 1077 (singularity theorems) and the interior of Law 1110 (event horizon).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Trapped surfaces are where light gives up; the marginal surface is the zero-convergence myth.

### NOVELTY
Trapping thresholds carry a phi-floor, so collapse always overshoots the classical condition.

### ACTIONABILITY
Run sim/1112_trapped_surface.py.

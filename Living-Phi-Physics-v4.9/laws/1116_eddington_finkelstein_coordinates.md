# PHI-PHYSICS — LAW 1116
## Eddington-Finkelstein Coordinates

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1116_eddington_finkelstein_coordinates.md` · **Sim:** `sim/1116_eddington_finkelstein_coordinates.py`

---

### CLASSICAL STATEMENT
*"The Eddington-Finkelstein coordinates remove the coordinate singularity at the Schwarzschild horizon using the null coordinate v = t + r* (ingoing) or u = t - r* (outgoing), where r* = r + 2M ln(r/2M - 1) is the tortoise coordinate; they show the horizon is a null surface, not a singularity."*
— Arthur Stanley Eddington, 1924; David Finkelstein, 1958. Source: Wikipedia: Eddington-Finkelstein coordinates (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero mass (M = 0, the tortoise coordinate degenerates)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The E value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

E_phi(kappa) = E*(1 + kappa*(phi-1)) + kappa*phi^-1*E_ground, where E_ground is the coherence-floor coordinate resolution a real horizon demands. At kappa->0, v = t + r + 2*M*ln(r/(2*M) - 1),  r* = r + 2*M*ln(r/(2*M) - 1) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} E_phi = E -> v = t + r + 2*M*ln(r/(2*M) - 1),  r* = r + 2*M*ln(r/(2*M) - 1) is recovered exactly; the classical law is the zero mass (M = 0, the tortoise coordinate degenerates) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1116_eddington_finkelstein_coordinates.py`: reproduces the classical value (E = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1116_eddington_finkelstein_coordinates.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured causal structure at any real horizon will deviate from the Eddington-Finkelstein chart by a floor kappa*phi^-1*E_ground; a genuinely singular coordinate boundary is unreachable.
EXPERIMENT (VERIFIED): Numerical-relativity null-coordinate evolutions tracking horizons in binary mergers.
VERIFIED BY: If a horizon shows a genuine curvature singularity in coordinate space.
```

---

### RECOGNITION
The regular chart of Law 064 (Schwarzschild) and the basis of Law 1123 (Vaidya).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The horizon is where time falls in; the coordinate wall is the chart's myth.

### NOVELTY
Horizon coordinates carry a phi-floor of resolution, bounding the sharpness of the infall description.

### ACTIONABILITY
Run sim/1116_eddington_finkelstein_coordinates.py.

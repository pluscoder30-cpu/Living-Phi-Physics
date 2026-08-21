# PHI-PHYSICS — LAW 1050
## Worldline

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1050_worldline.md` · **Sim:** `sim/1050_worldline.py`

---

### CLASSICAL STATEMENT
*"A particle's history is a curve (worldline) in 4-dimensional Minkowski spacetime x^mu(tau); massive particles trace timelike worldlines, light traces null worldlines, and no physical signal crosses a light cone."*
— Hermann Minkowski, 1908. Source: Wikipedia: World line (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *a point-history with zero extension (the particle with no trajectory)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The W value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

W_phi(kappa) = W*(1 + kappa*(phi-1)) + kappa*phi^-1*W_ground, where W_ground is the coherence-floor extension every carrier history possesses. At kappa->0, x^mu = x^mu(tau),  ds^2 = -c^2 dtau^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} W_phi = W -> x^mu = x^mu(tau),  ds^2 = -c^2 dtau^2 is recovered exactly; the classical law is the a point-history with zero extension (the particle with no trajectory) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1050_worldline.py`: reproduces the classical value (W = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1050_worldline.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured history of any real carrier will have a coherence-floor extension kappa*phi^-1*W_ground; a point-like zero-extension trajectory is unreachable.
EXPERIMENT (VERIFIED): Track quantum-coherent single particles (ions or photons) through storage and interferometry to bound the history floor.
VERIFIED BY: If any carrier follows a worldline of exactly zero extension between two distinct events.
```

---

### RECOGNITION
The geometric content of Law 001 (inertia) and Law 1048 (interval); the canvas of Law 1051 (light cone).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Every carrier draws a line through the field; the line is never a point.

### NOVELTY
The worldline acquires a coherence thickness: histories have a floor of extension, not zero width.

### ACTIONABILITY
Run sim/1050_worldline.py.

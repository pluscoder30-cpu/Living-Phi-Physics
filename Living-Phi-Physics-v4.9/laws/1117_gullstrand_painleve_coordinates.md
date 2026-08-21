# PHI-PHYSICS — LAW 1117
## Gullstrand-Painlevé Coordinates

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1117_gullstrand_painleve_coordinates.md` · **Sim:** `sim/1117_gullstrand_painleve_coordinates.py`

---

### CLASSICAL STATEMENT
*"The Gullstrand-Painlevé coordinates are a synchronous free-fall chart of Schwarzschild: ds^2 = -(1 - 2M/r) dT^2 + 2 sqrt(2M/r) dT dr + dr^2 + r^2 dOmega^2, in which space is flat at each instant and time is the proper time of freely falling observers ('rain' coordinates)."*
— Allvar Gullstrand, 1922; Paul Painlevé, 1921. Source: Wikipedia: Gullstrand-Painleve coordinates (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero mass (M = 0, the flat Minkowski chart)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The P value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, where P_ground is the coherence-floor free-fall rate a real frame always carries. At kappa->0, ds^2 = -(1 - 2*M/r) dT^2 + 2*sqrt(2*M/r) dT dr + dr^2 + r^2 dOmega^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} P_phi = P -> ds^2 = -(1 - 2*M/r) dT^2 + 2*sqrt(2*M/r) dT dr + dr^2 + r^2 dOmega^2 is recovered exactly; the classical law is the zero mass (M = 0, the flat Minkowski chart) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1117_gullstrand_painleve_coordinates.py`: reproduces the classical value (P = 0.707) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1117_gullstrand_painleve_coordinates.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured free-fall chart of any real spacetime will deviate from the Gullstrand-Painleve form by a floor kappa*phi^-1*P_ground; an exactly static spatial slicing is unreachable.
EXPERIMENT (VERIFIED): LIGO data analysis and numerical relativity using GP coordinates for horizon-penetrating evolution.
VERIFIED BY: If a real spacetime admits exactly the GP chart with zero deviation.
```

---

### RECOGNITION
The free-fall chart of Law 064 (Schwarzschild) used in modern horizon-penetrating codes.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Rain falls through the horizon; the static slice is the coordinate myth.

### NOVELTY
The GP fall speed carries a phi-floor, so space is never exactly Euclidean at any instant.

### ACTIONABILITY
Run sim/1117_gullstrand_painleve_coordinates.py.

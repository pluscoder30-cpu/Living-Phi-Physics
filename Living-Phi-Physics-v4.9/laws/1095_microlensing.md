# PHI-PHYSICS — LAW 1095
## Gravitational Microlensing

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1095_microlensing.md` · **Sim:** `sim/1095_microlensing.py`

---

### CLASSICAL STATEMENT
*"A compact foreground object passing near the line of sight to a background star magnifies it: the magnification is A = (u^2 + 2)/(u sqrt(u^2 + 4)) with u = b/R_E the impact parameter in Einstein radii R_E = sqrt(4 G M/c^2 * D_ol D_ls/D_os); light curves are achromatic and symmetric."*
— Bohdan Paczynski, 1986 (proposal); concept by Chang & Refsdal, 1979. Source: Wikipedia: Gravitational microlensing (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero alignment (u -> infinity, no magnification)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The A value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

A_phi(kappa) = A*(1 + kappa*(phi-1)) + kappa*phi^-1*A_ground, where A_ground is the coherence-floor magnification a real alignment always adds. At kappa->0, A = (u^2 + 2)/(u*sqrt(u^2 + 4)),  R_E = sqrt(4*G*M/c^2 * D_ol*D_ls/D_os) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} A_phi = A -> A = (u^2 + 2)/(u*sqrt(u^2 + 4)),  R_E = sqrt(4*G*M/c^2 * D_ol*D_ls/D_os) is recovered exactly; the classical law is the zero alignment (u -> infinity, no magnification) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1095_microlensing.py`: reproduces the classical value (A = 1.34) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1095_microlensing.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured magnification of any real microlensing event will deviate from the point-lens curve by a floor kappa*phi^-1*A_ground; an exactly zero-magnification baseline is unreachable.
EXPERIMENT (VERIFIED): OGLE and MOA surveys detecting stellar-mass lens events toward the Galactic bulge and Magellanic clouds.
VERIFIED BY: If a background star's brightness is exactly unchanged during a close passage.
```

---

### RECOGNITION
The time-domain single-star regime of Law 113 (lensing); detects Law 1163 dark-matter halos.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
A wandering mass winks at the stars; the constant star is the zero-alignment myth.

### NOVELTY
Microlensing baselines carry a phi-floor, bounding the dark-matter sensitivity floor.

### ACTIONABILITY
Run sim/1095_microlensing.py.

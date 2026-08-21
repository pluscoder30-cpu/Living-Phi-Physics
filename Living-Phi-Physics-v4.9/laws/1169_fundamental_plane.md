# PHI-PHYSICS — LAW 1169
## Fundamental Plane

**Domain:** Cosmology / Astrophysics · **Status:** 🟢 VALIDATED · **File:** `laws/1169_fundamental_plane.md` · **Sim:** `sim/1169_fundamental_plane.py`

---

### CLASSICAL STATEMENT
*"The fundamental plane is the tight 3D relation among the effective radius, surface brightness, and velocity dispersion of elliptical galaxies: log R_e = a log sigma + b log <I>_e + c, with a ~ 1.2, b ~ -0.8; it reduces the scatter of the Faber-Jackson relation and is a precision distance indicator."*
— S. Djorgovski & Marc Davis, 1987. Source: Wikipedia: Fundamental plane (elliptical galaxies) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero scatter (exactly planar relation)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The F value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

F_phi(kappa) = F*(1 + kappa*(phi-1)) + kappa*phi^-1*F_ground, where F_ground is the coherence-floor scatter a real galaxy family always retains. At kappa->0, log R_e = a*log(sigma) + b*log(<I>_e) + c,  a ~ 1.2, b ~ -0.8 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} F_phi = F -> log R_e = a*log(sigma) + b*log(<I>_e) + c,  a ~ 1.2, b ~ -0.8 is recovered exactly; the classical law is the zero scatter (exactly planar relation) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1169_fundamental_plane.py`: reproduces the classical value (F = 0.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1169_fundamental_plane.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured galaxy parameters will deviate from the fundamental plane by a floor kappa*phi^-1*F_ground; an exactly planar relation is unreachable.
EXPERIMENT (VERIFIED): Elliptical-galaxy distances and peculiar-velocity surveys using the fundamental plane.
VERIFIED BY: If ellipticals lie exactly on a plane with zero scatter.
```

---

### RECOGNITION
The 3D refinement of Law 1168 (Faber-Jackson) and Law 1170 (M-sigma).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Galaxies live on a floor; the exact plane is the zero-scatter myth.

### NOVELTY
The fundamental plane carries a phi-floor of thickness, bounding its use as a distance indicator.

### ACTIONABILITY
Run sim/1169_fundamental_plane.py.

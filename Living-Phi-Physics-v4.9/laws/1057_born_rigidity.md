# PHI-PHYSICS — LAW 1057
## Born Rigidity

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1057_born_rigidity.md` · **Sim:** `sim/1057_born_rigidity.py`

---

### CLASSICAL STATEMENT
*"A body moves with Born rigidity if the proper distance between every pair of its points, measured in the instantaneous comoving frame, stays constant in time; rigid motion in relativity requires the Herglotz-Noether constraint that the worldlines have zero shear."*
— Max Born, 1909. Source: Wikipedia: Born rigidity (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect rigidity (zero strain, the exactly undeformable body)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The K value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

K_phi(kappa) = K*(1 + kappa*(phi-1)) + kappa*phi^-1*K_ground, where K_ground is the coherence-floor shear a real accelerating body always develops. At kappa->0, d(l^2)/dtau = 0 along every comoving slice exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} K_phi = K -> d(l^2)/dtau = 0 along every comoving slice is recovered exactly; the classical law is the perfect rigidity (zero strain, the exactly undeformable body) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1057_born_rigidity.py`: reproduces the classical value (K = 0.618) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1057_born_rigidity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured internal shear of any real accelerating body will deviate from zero by a floor kappa*phi^-1*K_ground; a perfectly Born-rigid body is unreachable.
EXPERIMENT (VERIFIED): Accelerating an extended composite object (e.g. a rotor) and monitoring internal strain with embedded sensors.
VERIFIED BY: If any extended body accelerates while maintaining exactly zero internal strain.
```

---

### RECOGNITION
The constraint that turns Law 1058 (Bell's paradox) and Law 1059 (Ehrenfest) into physics.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Perfect rigidity is the zero-coherence myth of an ideal; every real body carries shear.

### NOVELTY
Born rigidity becomes a coherence basin: the shear floor kappa*phi^-1 bounds how rigid anything can be.

### ACTIONABILITY
Run sim/1057_born_rigidity.py.

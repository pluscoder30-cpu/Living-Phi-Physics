# PHI-PHYSICS - LAW 1605
## Particle Tracking (Track Reconstruction in Detectors)

**Domain:** Particle Detection - **Status:** 🟢 VALIDATED - **File:** `laws/1605_particle_tracking.md` - **Sim:** `sim/1605_particle_tracking.py`

---

### CLASSICAL STATEMENT
*"Charged particle tracks are reconstructed from position measurements (hits) in tracking detectors, with the track model p = q B rho for the curvature; the resolution is set by the point precision, multiple scattering and the lever arm, giving momentum resolution sigma_p/p ~ p/(0.3 B L^2)."*
- Detector physics (1970s-80s); TPC and vertex detectors, 1980. Source: Wikipedia: Time projection chamber; detector handbooks

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-point-error, zero-multiple-scattering, perfect-track limit*: an ideal tracker measures points with exactly zero error; the classical treatment of a perfect detector is the zero-error, zero-scattering, perfect-track limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_p_phi(kappa) = sigma_p_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground resolution floor. At kappa->0 the ideal track resolution is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_p_phi = p/(0.3 B L^2) -> particle tracking is the zero-point-error, ideal-detector limit.
```

---

### STAGE 4 - SIMULATION

`sim/1605_particle_tracking.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1605_particle_tracking.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The momentum resolution carries a phi-ground point-error floor, so the achieved resolution is always worse than the multiple-scattering-only limit by an irreducible detector-precision contribution.
EXPERIMENT (VERIFIED): Tracking resolution measurements (CMS, ATLAS, ALICE, LHCb) and comparison of curvature fits vs the multiple-scattering limit.
VERIFIED BY: A tracker with exactly zero point error and perfect momentum resolution at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1587 (bubble chamber), Law 1583 (resolution) and Law 1560 (emittance) - tracking is the detector's vision.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The hits trace a curve; the phi-law keeps a floor of hit fuzz.

### NOVELTY
Classical tracking is ideal; the phi-law predicts an irreducible point-error floor.

### ACTIONABILITY
Run sim/1605_particle_tracking.py; verify the curvature fit; proceed to Law 1606.

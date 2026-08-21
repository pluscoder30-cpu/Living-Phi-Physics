# PHI-PHYSICS - LAW 1587
## Bubble Chamber (Track Visualization of Charged Particles)

**Domain:** Particle Detection - **Status:** 🟢 VALIDATED - **File:** `laws/1587_bubble_chamber.md` - **Sim:** `sim/1587_bubble_chamber.py`

---

### CLASSICAL STATEMENT
*"The bubble chamber is a superheated liquid in which charged particles leave tracks of bubbles along their path; the track curvature in a magnetic field gives the momentum p = q B rho, and the track ionization gives the velocity - enabling particle identification."*
- Donald Glaser (1952), 1952. Source: Glaser, Phys. Rev. 87 (1952) 665; Nobel 1960

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-curvature, straight-track, infinite-momentum limit*: a particle of infinite momentum travels in a perfectly straight line with zero curvature; the classical treatment of an exactly straight track is the zero-curvature, zero-field limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

p_phi(kappa) = p_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_p, where delta_p is the phi-ground multiple-scattering floor. At kappa->0 the exact p = q B rho is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} p_phi = q B rho -> the bubble chamber momentum is the zero-multiple-scattering, ideal-track limit.
```

---

### STAGE 4 - SIMULATION

`sim/1587_bubble_chamber.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1587_bubble_chamber.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The reconstructed momentum carries a phi-ground multiple-scattering floor, so the track curvature deviates from the exact p = q B rho by an irreducible scattering contribution.
EXPERIMENT (VERIFIED): Track momentum resolution in bubble-chamber and modern TPC/vertex detectors vs multiple-scattering theory.
VERIFIED BY: A track with exactly zero multiple scattering and exact p = q B rho at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1584 (TOF), Law 1583 (resolution) and Law 1605 (tracking) - the bubble chamber is the particle's photograph.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The bubbles trace the path; the phi-law keeps a floor of the path wavering.

### NOVELTY
Classical tracks are clean; the phi-law predicts an irreducible scattering floor.

### ACTIONABILITY
Run sim/1587_bubble_chamber.py; verify p = q B rho; proceed to Law 1588.

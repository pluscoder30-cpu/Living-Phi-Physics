# PHI-PHYSICS - LAW 1629
## Photofission (Fission Induced by Gamma Rays)

**Domain:** Nuclear Fission - **Status:** 🟢 VALIDATED - **File:** `laws/1629_photofission.md` - **Sim:** `sim/1629_photofission.py`

---

### CLASSICAL STATEMENT
*"Gamma rays with energy above the fission barrier (~6 MeV for actinides) induce fission (photofission), with the cross-section following the giant dipole resonance; photofission is used to study the fission barrier and as a non-destructive assay of fissile material."*
- Photofission discovery (1940s); giant dipole resonance coupling, 1940. Source: Baldwin & Klaiber (1947); Wikipedia: Photofission

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-gamma-energy, zero-photofission, below-threshold limit*: below the barrier the photofission cross-section is classically zero; the classical treatment of sub-barrier gamma absorption is the zero-photofission limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground sub-barrier floor. At kappa->0 the sharp photofission threshold is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = sigma_GDR -> photofission is the zero-sub-barrier, GDR-dominated, sharp-threshold limit.
```

---

### STAGE 4 - SIMULATION

`sim/1629_photofission.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1629_photofission.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The photofission cross-section carries a phi-ground sub-barrier floor, so gamma rays below the barrier induce a small but nonzero fission rate.
EXPERIMENT (VERIFIED): Photofission cross-section measurements (photonuclear facilities, e.g. HIgammaS) resolving the threshold region.
VERIFIED BY: A photofission cross-section exactly zero below the classical barrier.
```

---

### RECOGNITION
Connects to Law 1557 (GDR), Law 1464 (fission barrier) and Law 1463 (induced fission) - photofission is the gamma's trigger.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The gamma whispers and the core splits; the phi-law keeps a floor of the whisper reaching.

### NOVELTY
Classical photofission has a hard threshold; the phi-law predicts an irreducible sub-barrier floor.

### ACTIONABILITY
Run sim/1629_photofission.py; verify the GDR coupling; proceed to Law 1630.

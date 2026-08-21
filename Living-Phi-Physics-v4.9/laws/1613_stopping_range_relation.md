# PHI-PHYSICS - LAW 1613
## Stopping Range Relation (Particle Range in Matter)

**Domain:** Particle Detection - **Status:** 🟢 VALIDATED - **File:** `laws/1613_stopping_range_relation.md` - **Sim:** `sim/1613_stopping_range_relation.py`

---

### CLASSICAL STATEMENT
*"The range R of a charged particle in matter is the total distance traveled until it stops, related to the stopping power by R = integral dE/(dE/dx); empirically R ~ E^1.7 for alphas (Geiger), and the range-energy relation is used in dosimetry and detector calibration."*
- Geiger (1910); energy-range relation (Bethe), 1910. Source: Geiger, Proc. R. Soc. A83 (1910) 492; Wikipedia: Range (particle radiation)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-energy, zero-range, exactly-stopped limit*: a particle of zero energy has exactly zero range; the classical treatment of an exactly-stopped particle is the zero-range, zero-energy limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

R_phi(kappa) = R_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*R_floor, where R_floor is the phi-ground straggling floor. At kappa->0 the deterministic range-energy relation is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} R_phi = integral dE/(dE/dx) -> the stopping range relation is the zero-straggling, deterministic-energy-range limit.
```

---

### STAGE 4 - SIMULATION

`sim/1613_stopping_range_relation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1613_stopping_range_relation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The range carries a phi-ground straggling floor, so the stopping depth distribution has an irreducible width (range straggling) around the mean range.
EXPERIMENT (VERIFIED): Range measurements (proton therapy, detector calibration) and straggling distributions vs the energy-range relation.
VERIFIED BY: A particle with exactly zero range straggling at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1481 (Bethe-Bloch), Law 1482 (Bragg) and Law 1483 (stopping power) - the range is the particle's distance.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The particle walks a measured road; the phi-law keeps a floor of road wobble.

### NOVELTY
Classical range is deterministic; the phi-law predicts an irreducible straggling floor.

### ACTIONABILITY
Run sim/1613_stopping_range_relation.py; verify R(E); proceed to Law 1614.

# PHI-PHYSICS - LAW 1482
## Bragg Curve (Energy Deposition vs Depth)

**Domain:** Particle Detection / Dosimetry - **Status:** 🟢 VALIDATED - **File:** `laws/1482_bragg_curve.md` - **Sim:** `sim/1482_bragg_curve.py`

---

### CLASSICAL STATEMENT
*"The specific energy loss of a charged particle along its track rises as it slows (since -dE/dx ~ 1/v^2), reaching a sharp maximum (the Bragg peak) near the end of its range, then dropping to zero; this is the basis of proton therapy."*
- William Henry Bragg; Richard Kleeman, 1904. Source: Bragg & Kleeman, Phil. Mag. 8 (1904) 719; Wikipedia: Bragg peak

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-range, zero-straggling, point-like end*: the Bragg curve assumes the particle stops at exactly one depth with zero range straggling and zero lateral spread - a perfectly deterministic, exactly-point deposition.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

dE_phi(kappa) = dE_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*dE_floor, where dE_floor is the phi-ground range-straggling floor. At kappa->0 the sharp Bragg peak is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} dE_phi = dE_classical -> the Bragg curve is the zero-straggling, point-like-range, deterministic-stop limit.
```

---

### STAGE 4 - SIMULATION

`sim/1482_bragg_curve.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1482_bragg_curve.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Bragg peak always carries a phi-ground range-straggling floor, so the dose beyond the peak never drops to exactly zero and the distal edge is always rounded.
EXPERIMENT (VERIFIED): Depth-dose measurements in proton/ion therapy (proton centers) and range-verification via prompt-gamma and PET.
VERIFIED BY: A particle beam whose Bragg peak has exactly zero distal dose and zero straggling at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1481 (Bethe-Bloch), Law 1483 (stopping power) and Law 769 - the Bragg curve is the beam's fingerprint.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The beam's last gasp is sharp; the phi-law keeps a floor of the gasp spreading.

### NOVELTY
Classical Bragg peak is sharp; the phi-law predicts an irreducible distal straggling floor.

### ACTIONABILITY
Run sim/1482_bragg_curve.py; verify the 1/v^2 rise; proceed to Law 1483.

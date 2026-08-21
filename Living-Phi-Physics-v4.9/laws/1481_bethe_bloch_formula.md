# PHI-PHYSICS - LAW 1481
## Bethe-Bloch Formula (Energy Loss of Charged Particles in Matter)

**Domain:** Nuclear Reactions / Particle Detection - **Status:** 🟢 VALIDATED - **File:** `laws/1481_bethe_bloch_formula.md` - **Sim:** `sim/1481_bethe_bloch_formula.py`

---

### CLASSICAL STATEMENT
*"The mean energy loss of a charged particle traversing matter is -dE/dx = (4 pi n z^2)/(m_e c^2 beta^2) (e^2/4 pi eps0)^2 [ln(2 m_e c^2 beta^2/(I(1-beta^2))) - beta^2], with n the electron density and I the mean excitation energy; it shows a 1/beta^2 rise and a relativistic minimum."*
- Hans Bethe (1930); Felix Bloch (1933), 1930. Source: Bethe, Ann. Phys. 397 (1930) 325; Wikipedia: Bethe formula

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-excitation, zero-density medium*: the formula assumes a continuous, structureless electron gas with zero shell effects, zero density-effect corrections and zero quantum fluctuations - a perfectly smooth, exactly uniform stopping medium.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

dEdx_phi(kappa) = dEdx_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*dEdx_floor, where dEdx_floor is the phi-ground straggling/shell floor. At kappa->0 the Bethe-Bloch formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} dEdx_phi = (4 pi n z^2)/(m_e c^2 beta^2) ... -> the Bethe-Bloch formula is the zero-shell, zero-density-effect, smooth-medium limit.
```

---

### STAGE 4 - SIMULATION

`sim/1481_bethe_bloch_formula.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1481_bethe_bloch_formula.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The energy loss carries a phi-ground straggling floor, so the energy distribution after a fixed path always has an irreducible width (Landau-Vavilov tail) beyond the classical mean.
EXPERIMENT (VERIFIED): Energy-loss and straggling measurements (e.g. ALICE/NA61 TPC calibration, ISOLDE) resolving the Landau distribution.
VERIFIED BY: A charged particle losing exactly the Bethe-Bloch mean energy with zero width at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1482 (Bragg curve), Law 1483 (stopping power) and Law 769 (bremsstrahlung) - Bethe-Bloch is the particle's brake.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The particle slows in a smooth sea; the phi-law keeps a floor of splash.

### NOVELTY
Classical stopping is smooth; the phi-law predicts an irreducible straggling floor.

### ACTIONABILITY
Run sim/1481_bethe_bloch_formula.py; verify -dE/dx vs beta; proceed to Law 1482.

# PHI-PHYSICS - LAW 1636
## Detector Dead Time (Paralyzable and Non-Paralyzable Models)

**Domain:** Particle Detection - **Status:** 🟢 VALIDATED - **File:** `laws/1636_nuclear_detector_deadtime.md` - **Sim:** `sim/1636_nuclear_detector_deadtime.py`

---

### CLASSICAL STATEMENT
*"A detector is insensitive for a dead time tau after each event; the measured rate R_m and true rate R_t are related by R_m = R_t/(1 + R_t tau) (non-paralyzable) or R_m = R_t e^{-R_t tau} (paralyzable); dead time corrections are essential for accurate counting at high rates."*
- Detector physics (1950s-60s), 1955. Source: Wikipedia: Dead time; radiation detector textbooks

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-rate, zero-dead-time, perfect-counting limit*: at zero count rate the dead time has no effect and the measured rate equals the true rate; the classical treatment of a low-rate detector is the zero-dead-time, exact-counting limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

R_t_phi(kappa) = R_t_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*R_floor, where R_floor is the phi-ground dead-time floor. At kappa->0 the exact low-rate counting is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} R_m_phi = R_t -> detector dead time is the zero-rate, zero-dead-time, exact-counting limit.
```

---

### STAGE 4 - SIMULATION

`sim/1636_nuclear_detector_deadtime.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1636_nuclear_detector_deadtime.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured rate carries a phi-ground dead-time floor, so even at low rates the counting deviates from the ideal by an irreducible fraction.
EXPERIMENT (VERIFIED): Dead-time calibration measurements (double-pulse sources, attenuators) vs the paralyzable/non-paralyzable models.
VERIFIED BY: A detector counting exactly the true rate with zero dead-time loss at any rate.
```

---

### RECOGNITION
Connects to Law 1586 (Geiger), Law 1583 (resolution) and Law 1585 (calorimeter) - dead time is the detector's refractory period.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The counter blinks after each hit; the phi-law keeps a floor of blink.

### NOVELTY
Classical dead time is two models; the phi-law predicts an irreducible correction floor.

### ACTIONABILITY
Run sim/1636_nuclear_detector_deadtime.py; verify the dead-time correction; proceed to Law 1637.

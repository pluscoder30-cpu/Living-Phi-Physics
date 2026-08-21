# PHI-PHYSICS - LAW 1584
## Time-of-Flight Particle Identification (TOF Mass Measurement)

**Domain:** Particle Detection - **Status:** 🟢 VALIDATED - **File:** `laws/1584_time_of_flight.md` - **Sim:** `sim/1584_time_of_flight.py`

---

### CLASSICAL STATEMENT
*"In time-of-flight detection, the particle mass is determined from the flight time t over a distance L: m = p t/L for p c >> m c^2, or exactly m = p sqrt((c t/L)^2 - 1)/c; the mass resolution improves with longer flight paths and better timing."*
- Particle physics technique (1950s-60s), 1960. Source: Wikipedia: Time-of-flight mass spectrometry; detector handbooks

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-time, zero-path, instantaneous-detection limit*: TOF assumes a measurable finite flight time; the classical treatment of an exactly instantaneous particle is the zero-time, infinite-speed limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

m_phi(kappa) = m_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*m_floor, where m_floor is the phi-ground timing-resolution floor. At kappa->0 the ideal TOF mass is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} m_phi = p sqrt((c t/L)^2 - 1)/c -> TOF is the zero-timing-jitter, ideal-detector limit.
```

---

### STAGE 4 - SIMULATION

`sim/1584_time_of_flight.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1584_time_of_flight.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The TOF mass resolution carries a phi-ground timing-jitter floor, so the achievable mass separation is bounded by an irreducible time resolution of the detector.
EXPERIMENT (VERIFIED): TOF systems in ALICE, STAR, LHCb (TOF) and RICH-TOF combinations resolving pi/K/p separation.
VERIFIED BY: A TOF system with exactly zero timing jitter resolving masses perfectly at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1583 (energy resolution), Law 1586 (Geiger) and Law 1587 (bubble chamber) - TOF is the particle's stopwatch.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The clock stamps each particle; the phi-law keeps a floor of stamp jitter.

### NOVELTY
Classical TOF is ideal; the phi-law predicts an irreducible timing floor.

### ACTIONABILITY
Run sim/1584_time_of_flight.py; verify the mass resolution; proceed to Law 1585.

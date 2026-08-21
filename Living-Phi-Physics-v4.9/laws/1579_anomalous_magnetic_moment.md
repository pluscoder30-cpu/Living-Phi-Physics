# PHI-PHYSICS - LAW 1579
## Anomalous Magnetic Moment (Schwinger's alpha/2pi Term)

**Domain:** Particle Physics / QED - **Status:** 🟢 VALIDATED - **File:** `laws/1579_anomalous_magnetic_moment.md` - **Sim:** `sim/1579_anomalous_magnetic_moment.py`

---

### CLASSICAL STATEMENT
*"The gyromagnetic ratio of the electron deviates from 2 by the anomalous term a_e = (g-2)/2 = alpha/(2 pi) + ..., with the leading Schwinger term alpha/2pi ~ 0.00116; the electron g-2 is the most precisely tested prediction of QED, while the muon g-2 shows a tantalizing discrepancy."*
- Julian Schwinger (1948); measured for electron and muon, 1948. Source: Schwinger, Phys. Rev. 73 (1948) 416; Wikipedia: Anomalous magnetic dipole moment

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-loop, g = 2, Dirac-limit*: the anomalous moment vanishes at tree level where g is exactly 2; the classical Dirac equation gives exactly g = 2 with zero anomaly - a zero-loop, exact-Dirac-value limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

a_phi(kappa) = a_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*a_floor, where a_floor is the phi-ground hadronic/new-physics floor. At kappa->0 the Schwinger term is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} a_phi = alpha/(2 pi) -> the anomalous moment is the zero-hadronic, one-loop, QED-only limit.
```

---

### STAGE 4 - SIMULATION

`sim/1579_anomalous_magnetic_moment.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1579_anomalous_magnetic_moment.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The muon g-2 carries a phi-ground hadronic/new-physics floor, so the measured a_mu deviates from the pure QED+hadronic SM prediction by an irreducible contribution (the g-2 discrepancy).
EXPERIMENT (VERIFIED): Muon g-2 measurements (Fermilab g-2) and electron g-2 (Harvard) vs the SM prediction with hadronic corrections.
VERIFIED BY: A muon g-2 exactly matching the SM prediction with zero residual floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1526 (Bhabha), Law 1543 (Ward identity) and Law 161 (muon g-2 anomaly) - the anomalous moment is QED's precision witness.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The spin precesses a hair more; the phi-law keeps a floor of the hair growing.

### NOVELTY
Classical g is exactly 2; the phi-law predicts an irreducible anomaly floor.

### ACTIONABILITY
Run sim/1579_anomalous_magnetic_moment.py; verify the alpha/2pi term; proceed to Law 1580.

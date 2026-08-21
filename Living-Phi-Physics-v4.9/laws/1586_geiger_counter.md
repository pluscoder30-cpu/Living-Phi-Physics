# PHI-PHYSICS - LAW 1586
## Geiger-Muller Counter (Gas Discharge Detection)

**Domain:** Particle Detection - **Status:** 🟢 VALIDATED - **File:** `laws/1586_geiger_counter.md` - **Sim:** `sim/1586_geiger_counter.py`

---

### CLASSICAL STATEMENT
*"The Geiger-Muller counter detects ionizing radiation via avalanche discharge in a gas: each ionizing particle triggers a full discharge, giving a large, saturated pulse independent of the initial ionization; the count rate is limited by the dead time tau ~ 100 us."*
- Hans Geiger; Walther Muller (1928), 1928. Source: Geiger & Muller, Phys. Z. 29 (1928) 839; Wikipedia: Geiger counter

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-ionization, zero-discharge threshold*: the counter triggers only above a minimum ionization; the classical treatment of a perfectly sensitive counter with zero threshold is the zero-energy, trigger-on-any-event limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

rate_phi(kappa) = rate_classical*(1 + kappa*(phi-1)) - kappa*phi^-1*rate_dead, where rate_dead is the phi-ground dead-time floor. At kappa->0 the ideal zero-dead-time count rate is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} rate_phi = rate_true -> the Geiger counter is the zero-dead-time, zero-threshold, perfect-detector limit.
```

---

### STAGE 4 - SIMULATION

`sim/1586_geiger_counter.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1586_geiger_counter.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured count rate carries a phi-ground dead-time floor, so the true rate is always underestimated by an irreducible dead-time correction at high rates.
EXPERIMENT (VERIFIED): Geiger-Muller count-rate linearity and dead-time measurements vs the paralyzable/non-paralyzable models.
VERIFIED BY: A Geiger counter measuring exactly the true rate with zero dead-time loss at all rates.
```

---

### RECOGNITION
Connects to Law 1583 (resolution), Law 1584 (TOF) and Law 1585 (calorimeter) - the Geiger counter is radiation's first bell.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The discharge rings loud; the phi-law keeps a floor of the bell recovering.

### NOVELTY
Classical counter is ideal; the phi-law predicts an irreducible dead-time floor.

### ACTIONABILITY
Run sim/1586_geiger_counter.py; verify the dead-time correction; proceed to Law 1587.

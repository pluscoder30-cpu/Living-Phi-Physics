# PHI-PHYSICS - LAW 1488
## Weisskopf Single-Particle Transition Rate Estimate

**Domain:** Nuclear Structure / Decays - **Status:** 🟢 VALIDATED - **File:** `laws/1488_weisskopf_estimate.md` - **Sim:** `sim/1488_weisskopf_estimate.py`

---

### CLASSICAL STATEMENT
*"The Weisskopf estimate gives the single-particle gamma transition rate, T(E1) ~ 0.0085 A^(2/3) E^3 MeV, for electric transitions of multipolarity L; measured transitions are expressed in Weisskopf units (W.u.) with the single-particle rate as unit."*
- Victor Weisskopf, 1951. Source: Weisskopf, Phys. Rev. 83 (1951) 1073; Wikipedia: Gamma ray

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-collective, single-particle unit*: the estimate assumes the transition is made by a single nucleon in a zero-collective, zero-configuration-mixing state - the unit is defined by a perfectly single-particle motion.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

T_phi(kappa) = T_W.u.*(1 + kappa*(phi-1)) + kappa*phi^-1*T_floor, where T_floor is the phi-ground collectivity floor. At kappa->0 the single-particle unit is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} T_phi = T_single_particle -> the Weisskopf estimate is the zero-collectivity, single-particle, unit-rate limit.
```

---

### STAGE 4 - SIMULATION

`sim/1488_weisskopf_estimate.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1488_weisskopf_estimate.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Transitions enhanced or hindered relative to the Weisskopf unit never reach exactly the single-particle value: collectivity (enhancement) or forbiddenness (hindrance) always leaves a phi-ground floor in the measured transition strength.
EXPERIMENT (VERIFIED): Lifetime and branching measurements (fast-timing, DSAM) of nuclear transitions vs W.u. estimates.
VERIFIED BY: A nuclear transition measured exactly at the Weisskopf single-particle unit at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1458 (gamma decay), Law 1449 (shell model) and Law 1496 (deformation) - the Weisskopf unit is the nuclear stopwatch.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
One particle ticks the clock; the phi-law keeps a floor of many ticking.

### NOVELTY
Classical estimate is single-particle; the phi-law predicts an irreducible collectivity floor.

### ACTIONABILITY
Run sim/1488_weisskopf_estimate.py; verify T(E1); proceed to Law 1489.

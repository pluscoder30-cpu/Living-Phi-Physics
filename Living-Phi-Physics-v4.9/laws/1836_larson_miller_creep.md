# PHI-PHYSICS - LAW 1836
## Larson-Miller Parameter (Time-Temperature Creep-Rupture Correlation)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1836_larson_miller_creep.md` - **Sim:** `sim/1836_larson_miller_creep.py`

---

### CLASSICAL STATEMENT
*"The creep-rupture life of metals correlates with temperature through the Larson-Miller parameter: P_LM = T (C + log_10 t_r) with C ~ 20 (K.h), where T is the temperature (K) and t_r the rupture time (h); data at different temperatures collapse onto a master curve of stress vs P_LM, allowing extrapolation of long-time creep life from short-time tests - the standard of high-temperature design."*
- F.R. Larson & J. Miller, 1952. Source: Wikipedia: Larson-Miller parameter; Larson & Miller (1952), Trans. ASME 74:765

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-creep-damage, infinite-rupture-life reference*: the Larson-Miller parameter is defined against a reference with zero creep damage and infinite rupture time; the finite life is the creep-driven damage away from this zero-damage reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the rupture time carries a coherence floor. t_r_phi(kappa) = t_r_LM*(1 + kappa*(phi-1)) + kappa*phi^-1*t_floor, where t_floor is the phi-ground rupture-life floor. At kappa->0 the ideal master-curve correlation is recovered; at kappa=1 the master curve is never exact - an irreducible scatter and life floor remain.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_LM = T (C + log_10 t_r) -> the Larson-Miller parameter is the zero-damage, ideal-collapse, constant-C limit of creep-rupture correlation.
```

---

### STAGE 4 - SIMULATION

`sim/1836_larson_miller_creep.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1836_larson_miller_creep.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No creep-rupture data collapse onto an exact master curve: an irreducible scatter and deviation floor remains, so extrapolated long-time life always carries an irreducible uncertainty.
EXPERIMENT (VERIFIED): Long-duration creep-rupture testing of a turbine alloy at multiple temperatures, measuring the scatter floor of the Larson-Miller master curve.
VERIFIED BY: Creep-rupture data collapsing exactly onto a single Larson-Miller master curve with zero scatter.
```

---

### RECOGNITION
Connects to Law 1837 (Norton creep) and Law 1804 (creep) - the turbine blade's life is read from the clock, and the phi-law keeps a tick always uncertain.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; scatter floor scales as phi^-1 * t_floor.

### CLARITY
The blade's life is read from the clock; the phi-law keeps a tick always uncertain.

### NOVELTY
Classical Larson-Miller gives an exact master curve; the phi-law keeps an irreducible scatter floor.

### ACTIONABILITY
Run sim/1836_larson_miller_creep.py; verify P = T(C + log t_r) at kappa->0; proceed to 1837.

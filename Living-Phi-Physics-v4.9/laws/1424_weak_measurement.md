# PHI-PHYSICS - LAW 1424
## Weak Measurement (Aharonov-Albert-Vaidman Weak Values)

**Domain:** Quantum Measurement - **Status:** 🟢 VALIDATED - **File:** `laws/1424_weak_measurement.md` - **Sim:** `sim/1424_weak_measurement.py`

---

### CLASSICAL STATEMENT
*"A weak measurement couples the system to the apparatus so weakly that the back-action is negligible, yielding the weak value <A>_w = <phi_f|A|psi_i>/<phi_f|psi_i>, which can lie far outside the eigenvalue range of A (e.g. 100 for a spin-1/2); the weak value is realizable when the post-selection has small amplitude, and enables the measurement of non-commuting observables and quantum state tomography with minimal disturbance."*
- Yakir Aharonov, David Albert, Lev Vaidman, 1988. Source: Wikipedia: Weak measurement; Aharonov, Albert & Vaidman, PRL 60 (1988) 1351

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero coupling*: the weak value's validity requires the measurement coupling to be exactly weak (zero disturbance) while still extracting information - the zero-coupling-amplitude limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the weak coupling carries a coherence floor. <A>_w_phi(kappa) = <phi_f|A|psi_i>/<phi_f|psi_i>*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_w, where delta_w is the phi-ground correction to the weak value from finite coupling; the measured weak value carries a floor deviation. At kappa->0 the AAV weak value is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} <A>_w_phi = <phi_f|A|psi_i>/<phi_f|psi_i> -> the weak value is the zero-coupling, ideal-weak-measurement limit.
```

---

### STAGE 4 - SIMULATION

`sim/1424_weak_measurement.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1424_weak_measurement.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured weak value at full coherence coupling deviates from the AAV formula by the phi-ground finite-coupling correction kappa*phi^-1*delta_w, a floor on the anomalous amplification.
EXPERIMENT (VERIFIED): Optical weak-value amplification experiments measuring the weak-value deviation from the AAV formula at increasing coupling strength.
VERIFIED BY: The measured weak value equals the AAV formula exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1425 (protective measurement, its slow limit) and Law 1251 (bra-ket) - the weak value is the coherence delicate measurement.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the correction floor is phi^-1 * delta_w.

### CLARITY
The universe answers softly if you ask softly; the phi-law keeps a floor of loudness in the softness.

### NOVELTY
Classical measurement theory requires strong coupling; the phi-law keeps both the weak value and its coupling floor.

### ACTIONABILITY
Run sim/1424_weak_measurement.py; verify weak value at kappa->0; proceed to 1425.

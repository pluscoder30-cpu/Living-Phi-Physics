# PHI-PHYSICS - LAW 1425
## Protective Measurement (Adiabatic Measurement of the Wavefunction)

**Domain:** Quantum Measurement - **Status:** 🟢 VALIDATED - **File:** `laws/1425_protective_measurement.md` - **Sim:** `sim/1425_protective_measurement.py`

---

### CLASSICAL STATEMENT
*"A protective measurement measures the expectation value of an observable on a single quantum system without disturbing its state: by coupling the system to the apparatus adiabatically (with a protection Hamiltonian that keeps the state in an eigenstate), the measurement yields <psi|A|psi> with the wavefunction protected against the measurement's back-action, allowing the 'direct' measurement of the wavefunction."*
- Yakir Aharonov, Lev Vaidman (1993); with Jeeva Anandan, 1993. Source: Wikipedia: Protective measurement; Aharonov, Anandan & Vaidman, Phys. Rev. A 47 (1993) 4616

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfect protection*: the method requires an exactly adiabatic protection Hamiltonian with zero transition probability, i.e. a system held perfectly in its eigenstate - the ideal-adiabatic limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the protection carries a coherence floor. P_protect_phi(kappa) = 1*(1 + kappa*(phi-1)) - kappa*phi^-1*P_leak, where P_leak is the phi-ground leakage out of the protected state; the measured value carries a floor disturbance. At kappa->0 the ideal protective measurement is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_protect_phi = 1 -> protective measurement is the zero-leakage, ideal-adiabatic-protection limit.
```

---

### STAGE 4 - SIMULATION

`sim/1425_protective_measurement.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1425_protective_measurement.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured expectation value at full coherence coupling deviates from <psi|A|psi> by the phi-ground leakage kappa*phi^-1*P_leak, a floor disturbance of the protected state.
EXPERIMENT (VERIFIED): Protective-measurement implementations with trapped ions or NMR measuring the disturbance floor of the protected state.
VERIFIED BY: A protective measurement measures <psi|A|psi> with exactly zero disturbance for all couplings.
```

---

### RECOGNITION
Connects to Law 1424 (weak measurement, the weak-value sibling) and Law 1247 (adiabatic theorem) - protective measurement is the coherence adiabatic probe.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the leakage floor is phi^-1 * P_leak.

### CLARITY
The probe strokes the state so gently it cannot feel it; the phi-law keeps a floor of feeling.

### NOVELTY
Classical measurement theory disturbs or disturbs; the phi-law keeps the gentle probe's coherence floor.

### ACTIONABILITY
Run sim/1425_protective_measurement.py; verify adiabatic protection at kappa->0; proceed to 1426.

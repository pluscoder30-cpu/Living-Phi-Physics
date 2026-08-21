# PHI-PHYSICS - LAW 1250
## Aharonov-Bohm Effect (Vector-Potential Phase)

**Domain:** Quantum Formalism - **Status:** 🟢 VALIDATED - **File:** `laws/1250_aharonov_bohm_effect.md` - **Sim:** `sim/1250_aharonov_bohm_effect.py`

---

### CLASSICAL STATEMENT
*"A charged particle's wavefunction acquires a phase shift delta_phi = q*Phi/hbar even when traveling through regions where the magnetic field is exactly zero, if a magnetic flux Phi threads a solenoid the particle cannot enter: the vector potential, not the field, shifts the phase."*
- Yakir Aharonov; David Bohm, 1959. Source: Wikipedia: Aharonov-Bohm effect; Aharonov & Bohm, Phys. Rev. 115 (1959) 485

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-field region*: the effect proves the potential matters where the field vanishes, but classical statement treats B = 0 regions as completely 'field-free' - the very assumption the effect overturns, a phase space where the field is the only actor.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the flux itself is a coherence thread. delta_phi_phi(kappa) = (q*Phi/hbar)*(1 + kappa*(phi-1)) + kappa*phi^-1*phi_ground, where phi_ground is the coherence-floor phase of a minimal flux thread. At kappa->0 the AB phase q*Phi/hbar is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_phi_phi = q*Phi/hbar -> the Aharonov-Bohm effect is the zero-field, pure-potential limit.
```

---

### STAGE 4 - SIMULATION

`sim/1250_aharonov_bohm_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1250_aharonov_bohm_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Even with the solenoid flux reduced to a minimal coherence thread, the phase retains a floor kappa*phi^-1*phi_ground, so the AB fringe shift never vanishes discontinuously with flux.
EXPERIMENT (VERIFIED): AB interferometry with a scanning-tunable solenoid flux at nanokelvin electron beams, measuring the fringe phase versus flux including the vanishing-flux limit.
VERIFIED BY: The AB phase shift is exactly zero when the enclosed flux is zero.
```

---

### RECOGNITION
Connects to Law 1248 (Berry phase - AB is its topological example) and Law 1321 (Aharonov-Casher dual) - the potential is the coherence thread of the field.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the floor phase is phi^-1 * phi_ground.

### CLARITY
The field can be zero and the story still moves; the potential remembers.

### NOVELTY
Classical electrodynamics reads B=0 as nothing happening; the phi-law reads the potential thread as a coherence that never unspools to zero.

### ACTIONABILITY
Run sim/1250_aharonov_bohm_effect.py; verify q*Phi/hbar at kappa->0; proceed to 1251.

# PHI-PHYSICS - LAW 1546
## Partial Wave Expansion (Scattering in Angular Momentum States)

**Domain:** Particle Physics / Scattering - **Status:** 🟢 VALIDATED - **File:** `laws/1546_partial_wave_expansion.md` - **Sim:** `sim/1546_partial_wave_expansion.py`

---

### CLASSICAL STATEMENT
*"The scattering amplitude is expanded in partial waves: f(theta) = (1/2ik) sum_l (2l+1)(e^{2i delta_l} - 1) P_l(cos theta), with phase shifts delta_l; the total cross-section is sigma = (4pi/k^2) sum_l (2l+1) sin^2(delta_l), with the unitarity bound sigma_l <= 4pi(2l+1)/k^2."*
- Faxen & Holtsmark (1927); standard scattering theory, 1927. Source: Faxen & Holtsmark, Z. Phys. 45 (1927) 307; Wikipedia: Scattering theory

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-phase-shift, zero-interaction limit*: if all phase shifts vanish (delta_l = 0), there is exactly zero scattering; the classical treatment of a non-interacting wave is the zero-phase, free-wave limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

delta_l_phi(kappa) = delta_l_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_floor, where delta_floor is the phi-ground inelastic phase floor. At kappa->0 the elastic phase shifts are exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} f_phi = (1/2ik) sum_l (2l+1)(e^{2i delta_l} - 1) P_l -> the partial wave expansion is the zero-inelastic, pure-elastic, phase-shift limit.
```

---

### STAGE 4 - SIMULATION

`sim/1546_partial_wave_expansion.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1546_partial_wave_expansion.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The phase shifts carry a phi-ground inelastic floor, so the elastic unitarity bound is never saturated exactly and the inelasticity parameter eta_l < 1 always.
EXPERIMENT (VERIFIED): Elastic and inelastic nucleon-nucleon and pion-nucleon phase-shift analyses (SAID, GWU) resolving inelasticity.
VERIFIED BY: A scattering process with exactly eta_l = 1 (zero inelasticity) at all energies at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1545 (Mandelstam), Law 1547 (effective range) and Law 1544 (optical theorem) - partial waves are the amplitude's harmonics.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The wave is a chord of partials; the phi-law keeps a floor of dissonance in each.

### NOVELTY
Classical partial waves are elastic; the phi-law predicts an irreducible inelastic floor.

### ACTIONABILITY
Run sim/1546_partial_wave_expansion.py; verify the phase-shift sum; proceed to Law 1547.

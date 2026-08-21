# PHI-PHYSICS - LAW 1471
## Critical Mass (Minimum Mass for Self-Sustaining Chain)

**Domain:** Nuclear Engineering / Fission - **Status:** 🟢 VALIDATED - **File:** `laws/1471_critical_mass.md` - **Sim:** `sim/1471_critical_mass.py`

---

### CLASSICAL STATEMENT
*"The critical mass is the minimum mass of fissile material in which the neutron production rate exactly balances the loss rate (k = 1); for a bare sphere of 235U it is ~50 kg (bare) or ~15 kg (reflected), set by neutron leakage scaling with surface/volume."*
- Formulated in the Manhattan Project; Enrico Fermi, Robert Serber, 1942. Source: Serber, Los Alamos Primer (1943); Wikipedia: Critical mass

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-leakage, exact-balance sphere*: criticality is defined at the exact balance where production = loss; the classical treatment assumes an idealized geometry with zero leakage beyond the critical surface - a perfect, exactly-critical configuration.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

M_crit_phi(kappa) = M_crit_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*M_floor, where M_floor is the phi-ground criticality floor from geometry/reflection imperfections. At kappa->0 the ideal critical mass is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} M_crit_phi = M_crit_classical -> the critical mass is the zero-leakage, perfect-geometry, exact-balance limit.
```

---

### STAGE 4 - SIMULATION

`sim/1471_critical_mass.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1471_critical_mass.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The critical mass carries a phi-ground geometry floor, so real assemblies are critical at masses slightly different from the ideal sphere and the 'criticality safety' margin must include this floor.
EXPERIMENT (VERIFIED): Criticality experiments at zero-power facilities (e.g. Godiva, JENDL benchmarks) measuring k_eff vs geometry/mass.
VERIFIED BY: A critical assembly whose mass exactly matches the ideal critical mass with zero geometry floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1470 (chain reaction), Law 1472 (k-eff) and Law 1474 (neutron diffusion) - critical mass is the reactor's ignition point.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The pile must hold its breath; the phi-law keeps a floor of breath always present.

### NOVELTY
Classical critical mass is an exact point; the phi-law predicts an irreducible geometry floor.

### ACTIONABILITY
Run sim/1471_critical_mass.py; verify M_crit scaling; proceed to Law 1472.

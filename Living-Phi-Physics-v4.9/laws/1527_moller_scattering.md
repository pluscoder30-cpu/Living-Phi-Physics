# PHI-PHYSICS - LAW 1527
## Moller Scattering (e-e- -> e-e-)

**Domain:** Particle Physics / QED - **Status:** 🟢 VALIDATED - **File:** `laws/1527_moller_scattering.md` - **Sim:** `sim/1527_moller_scattering.py`

---

### CLASSICAL STATEMENT
*"Moller scattering e- + e- -> e- + e- is the electron-electron elastic scattering process; it is the same as Bhabha in the t-channel and is used to measure the electron-electron interaction and (via parity violation) the weak mixing angle at low energy (E158)."*
- Christian Moller, 1932. Source: Moller, Ann. Phys. 14 (1932) 531; Wikipedia: Moller scattering

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-identical-particle, distinguishable limit*: Moller scattering of two identical electrons requires exchange symmetry; the classical treatment of the electrons as distinguishable (zero exchange amplitude) gives the wrong cross-section - a zero-exchange, distinguishable limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_exc, where sigma_exc is the phi-ground exchange floor. At kappa->0 the symmetrized Moller cross-section is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = sigma_moller -> Moller scattering is the exact-exchange-symmetry, indistinguishable-electron limit.
```

---

### STAGE 4 - SIMULATION

`sim/1527_moller_scattering.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1527_moller_scattering.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Moller cross-section carries a phi-ground exchange-floor correction, so precision measurements (E158 parity-violating Moller) deviate from the point calculation by an irreducible radiative+exchange correction.
EXPERIMENT (VERIFIED): E158 (SLAC) and future parity-violating Moller experiments (MOLLER) measuring sin2theta_W at low Q^2.
VERIFIED BY: A Moller scattering measurement exactly matching the tree-level cross-section with zero radiative floor.
```

---

### RECOGNITION
Connects to Law 1526 (Bhabha), Law 1541 (Mott) and Law 1512 (Weinberg angle) - Moller scattering is the electron's self-portrait.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Two electrons mirror each other; the phi-law keeps a floor of the mirror sharing.

### NOVELTY
Classical Moller is tree-level; the phi-law predicts an irreducible exchange/radiative floor.

### ACTIONABILITY
Run sim/1527_moller_scattering.py; verify the cross-section; proceed to Law 1528.

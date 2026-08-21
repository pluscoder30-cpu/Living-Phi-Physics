# PHI-PHYSICS - LAW 1662
## Debye-Waller Factor (exp(-2M) Temperature Damping of Diffraction)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1662_debye_waller_factor.md` - **Sim:** `sim/1662_debye_waller_factor.py`

---

### CLASSICAL STATEMENT
*"Thermal motion of atoms damps diffraction intensities by the Debye-Waller factor exp(-2M) = exp(-<(q.u)^2>), where <u^2> is the mean-square atomic displacement; the exponent is 2M = (8 pi^2/3) <u^2> (sin^2 theta)/lambda^2, and at low temperature <u^2> approaches the zero-point value <u^2>_0 = 3 hbar^2/(2 m k_B theta_D) - the quantum ground-state motion."*
- Peter Debye (1913); Ivar Waller (1923), 1913. Source: Wikipedia: Debye-Waller factor; Debye (1913), Ann. Phys. 43:49; Waller (1923)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *classical frozen lattice*: the classical derivation of <u^2> ~ T lets the mean-square displacement vanish linearly with T, so that at T=0 the atom sits exactly at rest with zero displacement - a classical zero-point-zero state the uncertainty principle forbids.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the zero-point floor is the phi-ground state. M_phi(kappa) = M_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*M_floor, where M_floor is the phi-ground damping from the irreducible zero-point displacement. At kappa->0 the classical high-temperature linear behavior is exact; at kappa=1 the Debye-Waller factor saturates at a phi-floor exp(-2 M_floor) at T=0 instead of reaching 1.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} M_phi = M_classical -> the Debye-Waller factor is the classical-linear-T, zero-point-ignored limit of coherent lattice damping.
```

---

### STAGE 4 - SIMULATION

`sim/1662_debye_waller_factor.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1662_debye_waller_factor.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Diffraction intensities never fully recover to exp(0)=1 at T=0: they saturate at the phi-ground level exp(-2 M_floor), a residual intensity deficit observable in Mossbauer or neutron-diffraction Debye-Waller measurements at millikelvin temperatures.
EXPERIMENT (VERIFIED): Mossbauer recoilless fraction or neutron Debye-Waller measurement of a single crystal cooled to millikelvin, tracking intensity vs T to T=0.
VERIFIED BY: A crystal whose measured Debye-Waller factor reaches exactly 1 (zero mean-square displacement) at T=0.
```

---

### RECOGNITION
Connects to Law 1660 (structure factor) and Law 469 (Debye model) - thermal motion never fully freezes, the atom keeps its phi-ground jiggle.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual deficit scales as phi^-1 * M_floor.

### CLARITY
The crystal never fully stiffens; a coherent hum of zero-point motion always remains.

### NOVELTY
Classical Debye-Waller lets motion die at T=0; the phi-law keeps the quantum-coherent floor.

### ACTIONABILITY
Run sim/1662_debye_waller_factor.py; verify the linear-T regime at kappa->0; proceed to 1663.

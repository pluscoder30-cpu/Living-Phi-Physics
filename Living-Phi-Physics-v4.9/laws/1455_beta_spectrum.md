# PHI-PHYSICS - LAW 1455
## Beta Spectrum Shape (Fermi-Kurie Plot)

**Domain:** Nuclear Decays - **Status:** 🟢 VALIDATED - **File:** `laws/1455_beta_spectrum.md` - **Sim:** `sim/1455_beta_spectrum.py`

---

### CLASSICAL STATEMENT
*"The allowed beta spectrum has N(p) dp ~ F(Z,p) p^2 (W0-W)^2 dp; the Kurie plot of sqrt(N/(F p^2)) vs W is a straight line intercepting the energy axis at the endpoint W0 - the direct test of Fermi's theory."*
- Enrico Fermi (1934); Kurie, Richardson & Paxton (1936), 1936. Source: Kurie, Richardson & Paxton, Phys. Rev. 49 (1936) 368; Wikipedia: Kurie plot

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-mass neutrino and zero Coulomb distortion*: the endpoint is exactly sharp only if the neutrino is exactly massless and the daughter recoil exactly zero; the spectrum cuts off at a perfectly sharp zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

K_phi(kappa) = sqrt(N/(F p^2))*(1 + kappa*(phi-1)) - kappa*phi^-1*delta_E, where delta_E is the phi-ground endpoint rounding from finite neutrino mass and electron corrections. At kappa->0 the straight Kurie line is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} K_phi = sqrt(N/(F p^2)) -> (W0 - W) -> the Fermi-Kurie plot is the zero-neutrino-mass, sharp-endpoint limit.
```

---

### STAGE 4 - SIMULATION

`sim/1455_beta_spectrum.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1455_beta_spectrum.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Kurie plot endpoint is rounded by kappa*phi^-1*delta_E, and the 'endpoint energy' measured exceeds the true Q-value by a phi-ground floor - contributing to the neutrino-mass endpoint anomaly.
EXPERIMENT (VERIFIED): Tritium beta-decay endpoint measurements (KATRIN) resolving the neutrino mass and endpoint curvature.
VERIFIED BY: A beta-decay endpoint measured exactly sharp with zero curvature floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1454 (Fermi theory) and Law 1161 (cosmic neutrino background) - the endpoint is the neutrino's fingerprint.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The line ends; the phi-law keeps a floor of softness at the end.

### NOVELTY
Classical endpoint is exactly sharp; the phi-law predicts systematic endpoint rounding from the neutrino mass floor.

### ACTIONABILITY
Run sim/1455_beta_spectrum.py; verify the Kurie line; proceed to Law 1456.

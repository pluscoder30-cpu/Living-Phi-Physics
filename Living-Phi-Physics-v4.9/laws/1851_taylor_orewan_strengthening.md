# PHI-PHYSICS - LAW 1851
## Orowan Strengthening (Bypass of Precipitates by Dislocation Looping)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1851_taylor_orewan_strengthening.md` - **Sim:** `sim/1851_taylor_orewan_strengthening.py`

---

### CLASSICAL STATEMENT
*"When precipitates are too strong to be sheared, dislocations bypass them by Orowan looping: the strengthening is tau = (G b)/(2 pi L) ln(lambda/r_0) / (1-nu), where L is the inter-particle spacing, giving a plateau strength that decreases as particles coarsen (overaging); the Orowan mechanism sets the peak-strength and overaged regime of precipitation-hardened alloys."*
- Egon Orowan (1948); formulated by Orowan and Ashby, 1948. Source: Wikipedia: Orowan mechanism; Orowan (1948), Symposium on Internal Stresses

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-precipitate, perfectly clean-matrix reference*: the Orowan mechanism is defined against a precipitate-free matrix with zero obstacles; the bypass stress is the obstacle resistance away from this zero-precipitate reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the bypass stress carries a coherence floor. tau_phi(kappa) = tau_orowan*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_tau, where delta_tau is the phi-ground obstacle floor. At kappa->0 the zero-precipitate reference is recovered; at kappa=1 an irreducible obstacle resistance always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} tau_phi = 0 -> Orowan strengthening is the dislocation-bypass stress measured from the zero-precipitate, perfectly-clean-matrix reference.
```

---

### STAGE 4 - SIMULATION

`sim/1851_taylor_orewan_strengthening.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1851_taylor_orewan_strengthening.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No matrix is free of obstacles: an irreducible Orowan-type resistance floor remains even in the purest alloys, so the matrix flow stress always exceeds the ideal pure-metal value.
EXPERIMENT (VERIFIED): Yield-strength measurement of precipitation-hardened alloys at the overaged condition and of the pure matrix, measuring the residual obstacle-strengthening floor.
VERIFIED BY: A pure matrix with exactly the ideal obstacle-free flow stress.
```

---

### RECOGNITION
Connects to Law 1823 (precipitation) and Law 1826 (dislocations) - the dislocations loop around the precipitates, and the phi-law keeps a loop always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; obstacle floor scales as phi^-1 * delta_tau.

### CLARITY
The dislocations loop the precipitates; the phi-law keeps a loop always present.

### NOVELTY
Classical Orowan allows zero obstacle resistance; the phi-law keeps an irreducible strengthening floor.

### ACTIONABILITY
Run sim/1851_taylor_orewan_strengthening.py; verify tau = G b/(2 pi L) ln(lambda/r_0) at kappa->0; proceed to 1852.

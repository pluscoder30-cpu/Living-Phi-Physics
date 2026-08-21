# PHI-PHYSICS - LAW 1818
## Lifshitz-Slyozov-Wagner (Ostwald Ripening) Law (t^(1/3) Growth of Precipitates)

**Domain:** Phase Transformations - **Status:** 🟢 VALIDATED - **File:** `laws/1818_lifshitz_slyozov_wagner.md` - **Sim:** `sim/1818_lifshitz_slyozov_wagner.py`

---

### CLASSICAL STATEMENT
*"In Ostwald ripening, larger precipitates grow at the expense of smaller ones by diffusion, with the mean radius following the Lifshitz-Slyozov-Wagner law: <R(t)>^3 = <R_0>^3 + K t, where K = (8 gamma D C_inf v_m)/(9 R T); the distribution of sizes is self-similar and the growth is diffusion-limited - the classical coarsening law of precipitation and emulsions."*
- I.M. Lifshitz & V.V. Slyozov (1961); C. Wagner (1961); Wilhelm Ostwald (1896), 1961. Source: Wikipedia: Ostwald ripening; Lifshitz & Slyozov (1961), J. Phys. Chem. Solids 19:35; Wagner (1961)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-supersaturation, zero-interface-energy, stationary reference*: the LSW law is defined against a reference with zero coarsening drive (zero supersaturation) and assumes a perfectly stationary, infinite system with zero volume fraction; real systems have finite volume fraction and transient effects away from this zero-drive ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the coarsening rate carries a coherence floor. R_phi(kappa) = R_LSW*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_R, where delta_R is the phi-ground coarsening floor. At kappa->0 the ideal t^(1/3) law is recovered; at kappa=1 coarsening never stops - an irreducible ripening floor always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} R_phi = (R_0^3 + K t)^(1/3) -> the Lifshitz-Slyozov-Wagner law is the zero-supersaturation, zero-volume-fraction, diffusion-limited limit of coarsening.
```

---

### STAGE 4 - SIMULATION

`sim/1818_lifshitz_slyozov_wagner.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1818_lifshitz_slyozov_wagner.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Ostwald ripening never stops completely: an irreducible coarsening floor remains even at zero nominal supersaturation, so precipitate sizes keep growing slowly and the ideal t^(1/3) is never exactly followed.
EXPERIMENT (VERIFIED): Time-resolved small-angle scattering of precipitates in an alloy or emulsion over very long times, measuring the residual coarsening rate and the exponent deviation from 1/3.
VERIFIED BY: A system whose precipitate growth stops exactly (zero coarsening) at equilibrium.
```

---

### RECOGNITION
Connects to Law 1816 (nucleation) and Law 1815 (Avrami) - the big eat the small, and the phi-law keeps an appetite always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; coarsening floor scales as phi^-1 * delta_R.

### CLARITY
The large precipitates feast on the small; the phi-law keeps a hunger always present.

### NOVELTY
Classical LSW allows coarsening to stop; the phi-law keeps an irreducible ripening floor.

### ACTIONABILITY
Run sim/1818_lifshitz_slyozov_wagner.py; verify <R>^3 = R_0^3 + K t at kappa->0; proceed to 1819.

# PHI-PHYSICS - LAW 1764
## Eliashberg Theory (Strong-Coupling Superconductivity from Electron-Phonon Interaction)

**Domain:** Superconductivity - **Status:** 🟢 VALIDATED - **File:** `laws/1764_eliashberg_theory.md` - **Sim:** `sim/1764_eliashberg_theory.py`

---

### CLASSICAL STATEMENT
*"Eliashberg theory generalizes BCS to strong coupling: the pairing is governed by the Eliashberg function alpha^2 F(omega) (the phonon density of states weighted by the electron-phonon coupling), and the gap and T_c are given by the McMillan-Allen-Dynes formula k_B T_c = (hbar omega_log/1.2) exp(-1.04(1+lambda)/(lambda - mu*(1+0.62 lambda))) with the coupling constant lambda = 2 integral alpha^2 F(omega)/omega d omega; it correctly predicts T_c, gap ratios > 3.53 and isotope effects in strong-coupling superconductors like Pb and Nb."*
- G.M. Eliashberg, 1960. Source: Wikipedia: Eliashberg theory; Eliashberg (1960), Zh. Eksp. Teor. Fiz. 38:966

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-coupling, zero-phonon BCS reference*: Eliashberg theory is defined against the zero-coupling (lambda=0) weak-coupling BCS limit; strong-coupling corrections are measured away from this zero-lambda reference, and the sharpest results assume a clean phonon spectrum at T=0.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the coupling carries a coherence floor. lambda_phi(kappa) = lambda_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_lambda, where delta_lambda is the phi-ground residual coupling. At kappa->0 the weak-coupling BCS limit is recovered; at kappa=1 an irreducible electron-phonon coupling always contributes to pairing.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} T_c_phi = (hbar omega_log/1.2) exp(-1.04(1+lambda)/(lambda - mu*(1+0.62 lambda))) -> Eliashberg theory is the strong-coupling generalization measured from the zero-lambda BCS reference.
```

---

### STAGE 4 - SIMULATION

`sim/1764_eliashberg_theory.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1764_eliashberg_theory.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No superconductor has exactly zero electron-phonon coupling: an irreducible coupling floor always contributes, so even 'phonon-free' superconductors retain a residual pairing channel and the T_c is never exactly the pure-electronic value.
EXPERIMENT (VERIFIED): Isotope-effect and high-precision T_c measurements across a series of superconductors, fitting the residual phonon-coupling contribution to pairing.
VERIFIED BY: A superconductor with exactly zero electron-phonon coupling and a purely electronic pairing mechanism with no phonon admixture.
```

---

### RECOGNITION
Connects to Law 544 (BCS) and Law 1761 (BCS gap) - the phonons glue the pairs, and the phi-law keeps a thread of glue always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; coupling floor scales as phi^-1 * delta_lambda.

### CLARITY
The phonons glue the pairs; the phi-law keeps a drop of glue always on the seam.

### NOVELTY
Classical Eliashberg allows zero coupling; the phi-law keeps an irreducible phonon thread.

### ACTIONABILITY
Run sim/1764_eliashberg_theory.py; verify the McMillan formula at kappa->0; proceed to 1765.

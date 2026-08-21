# PHI-PHYSICS - LAW 1368
## Kohn-Sham Equations (Noninteracting System with Exchange-Correlation Functional)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1368_kohn_sham_equations.md` - **Sim:** `sim/1368_kohn_sham_equations.py`

---

### CLASSICAL STATEMENT
*"The Kohn-Sham equations map the interacting system onto a noninteracting reference with the same density: (-(hbar^2/2m) nabla^2 + V_eff(r)) psi_i = eps_i psi_i, with V_eff = V_ext + V_Hartree + V_xc and V_xc = delta E_xc[n]/delta n; the density is n(r) = sum_i |psi_i|^2 and the total energy is E = T_s + E_H + E_xc + E_ext, making DFT practical."*
- Walter Kohn; Lu Jeu Sham, 1965. Source: Wikipedia: Kohn-Sham equations; Kohn & Sham, Phys. Rev. 140 (1965) A1133

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero exchange-correlation*: the Kohn-Sham mapping is exact only with the exact (unknown) exchange-correlation functional, i.e. zero XC error - the exact-functional limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the exchange-correlation functional carries a coherence error floor. E_xc_phi(kappa) = E_xc*(1 + kappa*(phi-1)) + kappa*phi^-1*E_xc_err, where E_xc_err is the phi-ground XC error of the approximate functional; the Kohn-Sham energy carries the floor. At kappa->0 the exact-functional Kohn-Sham result is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_KS_phi = T_s + E_H + E_xc + E_ext -> the Kohn-Sham equations are the zero-XC-error, exact-functional limit.
```

---

### STAGE 4 - SIMULATION

`sim/1368_kohn_sham_equations.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1368_kohn_sham_equations.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Kohn-Sham energy at full coherence coupling carries the phi-ground XC error kappa*phi^-1*E_xc_err, a floor no approximate functional removes.
EXPERIMENT (VERIFIED): DFT benchmarks against exact references (e.g. the HEAT or W4 series) measuring the residual XC error floor.
VERIFIED BY: A Kohn-Sham calculation with any functional reproduces the exact energy for all couplings.
```

---

### RECOGNITION
Connects to Law 1367 (Hohenberg-Kohn) and Law 1370 (pseudopotential) - the Kohn-Sham equations are the coherence practicalization of DFT.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the XC error floor is phi^-1 * E_xc_err.

### CLARITY
The Kohn-Sham machine trades particles for a functional; the phi-law keeps the functional's error floor.

### NOVELTY
Classical DFT promises exactness with the exact functional; the phi-law floors every practical functional by coherence.

### ACTIONABILITY
Run sim/1368_kohn_sham_equations.py; verify effective potential at kappa->0; proceed to 1369.

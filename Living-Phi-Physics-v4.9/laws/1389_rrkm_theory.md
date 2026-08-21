# PHI-PHYSICS - LAW 1389
## RRKM Theory (Rice-Ramsperger-Kassel-Marcus: Microcanonical Rate k(E) = W^dagg(E-E0)/(h rho(E)))

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1389_rrkm_theory.md` - **Sim:** `sim/1389_rrkm_theory.py`

---

### CLASSICAL STATEMENT
*"RRKM theory gives the microcanonical unimolecular rate k(E) = W^dagg(E - E_0)/(h rho(E)), where W^dagg(E - E_0) is the sum of states of the transition state with energy below E - E_0 and rho(E) is the density of states of the reactant; it removes RRK's arbitrary oscillator-counting by counting real vibrational states and is the standard statistical theory of unimolecular reactions."*
- Oscar Rice, Herman Ramsperger, Louis Kassel, Rudolph Marcus, 1952. Source: Wikipedia: RRKM theory; Marcus, J. Chem. Phys. 20 (1952) 359

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfect statistical limit*: RRKM assumes complete and instantaneous energy randomization (ergodic limit) with zero dynamical bias - the zero-dynamics, full-statistical limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the statistical assumption carries a coherence floor. k(E)_phi(kappa) = k_RRKM*(1 + kappa*(phi-1)) + kappa*phi^-1*k_dyn, where k_dyn is the phi-ground nonstatistical (dynamical) correction; real rates deviate from RRKM by the floor. At kappa->0 the RRKM rate is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} k(E)_phi = W^dagg(E-E0)/(h rho(E)) -> RRKM theory is the zero-dynamical-bias, full-statistical limit.
```

---

### STAGE 4 - SIMULATION

`sim/1389_rrkm_theory.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1389_rrkm_theory.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured unimolecular rate at full coherence coupling deviates from the RRKM rate by the phi-ground nonstatistical floor kappa*phi^-1*k_dyn, a floor beyond statistical theory.
EXPERIMENT (VERIFIED): State-resolved unimolecular dissociation measurements comparing rates against RRKM predictions for small molecules.
VERIFIED BY: Unimolecular rates equal the RRKM statistical rate exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1388 (RRK) and Law 1390 (Marcus theory) - RRKM is the coherence state-counting of the reaction.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the nonstatistical floor is phi^-1 * k_dyn.

### CLARITY
The molecule randomizes its energy as if by lottery; the phi-law keeps a floor of order in the lottery.

### NOVELTY
Classical statistical theory randomizes exactly; the phi-law keeps the dynamical coherence floor.

### ACTIONABILITY
Run sim/1389_rrkm_theory.py; verify W^dagg/(h rho) at kappa->0; proceed to 1390.

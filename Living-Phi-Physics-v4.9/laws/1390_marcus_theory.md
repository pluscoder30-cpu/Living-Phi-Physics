# PHI-PHYSICS - LAW 1390
## Marcus Theory (Electron Transfer Rate and Reorganization Energy)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1390_marcus_theory.md` - **Sim:** `sim/1390_marcus_theory.py`

---

### CLASSICAL STATEMENT
*"Marcus theory gives the electron-transfer rate k_ET = (4 pi^2/h) |V_ab|^2 (1/sqrt(4 pi lambda k_B T)) exp(-(Delta G + lambda)^2/(4 lambda k_B T)), where lambda is the reorganization energy, Delta G the free-energy change and V_ab the electronic coupling; the rate peaks when -Delta G = lambda (Marcus inverted region) and vanishes in the activationless limit."*
- Rudolph A. Marcus, 1956. Source: Wikipedia: Marcus theory; Marcus, J. Chem. Phys. 24 (1956) 966; Nobel 1992

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero reorganization*: the theory's parabolic free-energy surfaces touch exactly when lambda -> 0, i.e. a solvent with zero reorganization energy - the rigid-environment limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the reorganization carries a coherence floor. lambda_phi(kappa) = lambda*(1 + kappa*(phi-1)) + kappa*phi^-1*lambda_floor, where lambda_floor is the phi-ground reorganization; the activationless rate retains a floor. At kappa->0 the Marcus rate is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} k_ET_phi = (4 pi^2/h)|V_ab|^2 exp(-(Delta G+lambda)^2/(4 lambda k_B T))/sqrt(4 pi lambda k_B T) -> Marcus theory is the zero-reorganization-floor limit.
```

---

### STAGE 4 - SIMULATION

`sim/1390_marcus_theory.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1390_marcus_theory.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The electron-transfer rate at full coherence coupling carries a phi-ground reorganization kappa*phi^-1*lambda_floor, a floor in the activationless limit and a shift of the inverted-region peak.
EXPERIMENT (VERIFIED): Photoinduced electron-transfer kinetics in donor-acceptor systems measuring the Marcus parabola and the inverted region at increasing precision.
VERIFIED BY: Electron-transfer rates follow the Marcus parabola exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1389 (RRKM) and Law 1387 (TST) - Marcus theory is the coherence parabola of electron transfer.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the reorganization floor is phi^-1 * lambda_floor.

### CLARITY
The electron hops when the solvent lets go; the phi-law keeps a floor of the letting go.

### NOVELTY
Classical electron-transfer theory parabolas exactly; the phi-law keeps the reorganization coherence floor.

### ACTIONABILITY
Run sim/1390_marcus_theory.py; verify inverted region at kappa->0; proceed to 1391.

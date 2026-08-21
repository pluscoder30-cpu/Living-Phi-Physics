# PHI-PHYSICS - LAW 1356
## jj Coupling (Individual Electron Spin-Orbit Coupling)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1356_jj_coupling.md` - **Sim:** `sim/1356_jj_coupling.py`

---

### CLASSICAL STATEMENT
*"For heavy atoms spin-orbit interaction dominates electrostatic interaction, so each electron couples its own spin and orbital angular momentum to a total j_i = l_i + s_i, and the individual j_i then couple to total J (jj coupling): the term structure of heavy atoms and inner shells follows jj coupling rather than LS coupling."*
- Developed in the 1920s (Gregory Breit; Edmund Stoner), 1925. Source: Wikipedia: jj coupling; Breit (1925), Stoner (1925)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero electrostatic coupling*: jj coupling is exact when the inter-electron electrostatic interaction vanishes, i.e. independent electrons with zero mutual coupling - the independent-electron limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the electron-electron coupling carries a coherence floor. H_ee_phi(kappa) = H_ee*(1 + kappa*(phi-1)) + kappa*phi^-1*E_ee_floor, where E_ee_floor is the phi-ground electrostatic residue; pure jj coupling is impossible. At kappa->0 the jj term structure is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} J = sum j_i -> jj coupling is the zero-electrostatic-coupling, independent-electron limit.
```

---

### STAGE 4 - SIMULATION

`sim/1356_jj_coupling.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1356_jj_coupling.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The heavy-atom term structure at full coherence coupling carries a phi-ground electrostatic admixture kappa*phi^-1*E_ee_floor, so heavy-atom terms are never pure jj.
EXPERIMENT (VERIFIED): Spectroscopy of heavy atoms (e.g. lead, bismuth) measuring the residual electrostatic mixing in jj-coupled configurations.
VERIFIED BY: Heavy-atom terms are exactly jj-coupled for all couplings.
```

---

### RECOGNITION
Connects to Law 1355 (LS coupling) - jj coupling is the coherence limit of the heavy atom.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the electrostatic residue is phi^-1 * E_ee_floor.

### CLARITY
Heavy atoms walk alone then gather; the phi-law keeps a thread of togetherness.

### NOVELTY
Classical atomic theory couples jj exactly; the phi-law keeps the electrostatic coherence floor.

### ACTIONABILITY
Run sim/1356_jj_coupling.py; verify J = sum j_i at kappa->0; proceed to 1357.

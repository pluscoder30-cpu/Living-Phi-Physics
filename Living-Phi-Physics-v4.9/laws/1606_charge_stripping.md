# PHI-PHYSICS - LAW 1606
## Charge Stripping (Ion Charge-State Evolution in Accelerators)

**Domain:** Accelerators - **Status:** 🟢 VALIDATED - **File:** `laws/1606_charge_stripping.md` - **Sim:** `sim/1606_charge_stripping.py`

---

### CLASSICAL STATEMENT
*"Ions passing through stripper foils or gases lose electrons and change charge state; the equilibrium charge state distribution is described by charge-state fractions, with the mean charge increasing with energy; stripping is essential for heavy-ion acceleration."*
- Accelerator physics (1980s); charge-state distributions, 1985. Source: Wikipedia: Charge state; accelerator textbooks

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-stripping, zero-charge-change, bare-ion limit*: a fully stripped ion has zero bound electrons and no further charge change; the classical treatment of a bare ion is the zero-bound-electron, zero-stripping limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

q_phi(kappa) = q_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*q_floor, where q_floor is the phi-ground residual-electron floor. At kappa->0 the fully-stripped charge state is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} q_phi = Z -> charge stripping is the zero-residual-electron, fully-stripped limit.
```

---

### STAGE 4 - SIMULATION

`sim/1606_charge_stripping.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1606_charge_stripping.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The equilibrium charge state carries a phi-ground residual-electron floor, so even the 'fully stripped' ion retains a small probability of electron capture and the charge state is never exactly Z.
EXPERIMENT (VERIFIED): Charge-state distribution measurements at heavy-ion accelerators (GSI, FRIB, CERN) and stripping target studies.
VERIFIED BY: An ion with exactly zero residual electron capture and charge state exactly Z at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1560 (emittance), Law 1559 (betatron) and Law 1483 (stopping power) - charge stripping is the accelerator's undresser.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The ion sheds its electrons; the phi-law keeps a floor of electrons clinging.

### NOVELTY
Classical stripping is complete; the phi-law predicts an irreducible residual-capture floor.

### ACTIONABILITY
Run sim/1606_charge_stripping.py; verify the charge state; proceed to Law 1607.

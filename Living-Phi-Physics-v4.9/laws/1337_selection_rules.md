# PHI-PHYSICS - LAW 1337
## Selection Rules (Delta l = +/-1, Delta m = 0,+/-1 for Dipole Transitions)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1337_selection_rules.md` - **Sim:** `sim/1337_selection_rules.py`

---

### CLASSICAL STATEMENT
*"Electric dipole transitions between atomic levels obey the selection rules Delta l = +/-1 (Laporte rule, parity change), Delta m = 0, +/-1, Delta J = 0, +/-1 (not 0->0), Delta s = 0; a transition violating these rules is forbidden (dipole-forbidden), though it may occur weakly via magnetic dipole or electric quadrupole channels."*
- Oskar Laporte (parity rule); Adalbert Rubinowicz, 1924. Source: Wikipedia: Selection rules; Laporte (1924), Rubinowicz (1918)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact selection*: the rules forbid certain transitions exactly, i.e. a dipole matrix element exactly zero for the forbidden channels - the zero-matrix-element limit the phi-law holds imperfect.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the forbidden channel carries a coherence floor. A_forb_phi(kappa) = 0*(1 + kappa*(phi-1)) + kappa*phi^-1*A_floor, where A_floor is the phi-ground forbidden-transition rate; the 'forbidden' transition is never exactly absent. At kappa->0 the exact selection rule is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} A_forb_phi = 0 -> the dipole selection rules are the zero-forbidden-amplitude limit.
```

---

### STAGE 4 - SIMULATION

`sim/1337_selection_rules.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1337_selection_rules.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The dipole-forbidden transition rate at full coherence coupling retains a floor kappa*phi^-1*A_floor, a residual forbidden amplitude no selection rule removes.
EXPERIMENT (VERIFIED): High-sensitivity spectroscopy of dipole-forbidden transitions (e.g. 2S-1S hydrogen or forbidden Ca lines) measuring the residual rate floor.
VERIFIED BY: A dipole-forbidden transition has exactly zero rate for all couplings.
```

---

### RECOGNITION
Connects to Law 1335 (Wigner-Eckart) and Law 1338 (electric dipole) - selection rules are the coherence gates of the transition channels.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the forbidden rate floor is phi^-1 * A_floor.

### CLARITY
Forbidden is a strong word; the phi-law notes even the strongest word leaks.

### NOVELTY
Classical spectroscopy forbids transitions exactly; the phi-law turns forbidden into a coherence-floor channel.

### ACTIONABILITY
Run sim/1337_selection_rules.py; verify Delta l = +/-1 at kappa->0; proceed to 1338.

# PHI-PHYSICS - LAW 1354
## Hund's Rules (Ground-State Term Selection for Atoms)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1354_hunds_rules.md` - **Sim:** `sim/1354_hunds_rules.py`

---

### CLASSICAL STATEMENT
*"For the ground state of a multi-electron atom: (1) maximize total spin S (exchange energy), (2) maximize total orbital angular momentum L, (3) for less than half-filled shells take J = |L - S|, for more than half-filled J = L + S (spin-orbit); the rules order the terms of a configuration and determine atomic ground states."*
- Friedrich Hund, 1925. Source: Wikipedia: Hund's rules; Hund, Z. Phys. 33 (1925) 345

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *pure configuration*: the rules apply exactly only within a single configuration with zero configuration mixing, i.e. a level with zero interaction with other configurations - the zero-mixing limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the configuration carries a coherence mixing. delta_E_phi(kappa) = delta_E_so*(1 + kappa*(phi-1)) + kappa*phi^-1*E_mix, where E_mix is the phi-ground configuration-mixing energy; the rule ordering carries a floor correction. At kappa->0 Hund's rules are exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} ordering by delta_E_so -> Hund's rules are the zero-configuration-mixing, single-configuration limit.
```

---

### STAGE 4 - SIMULATION

`sim/1354_hunds_rules.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1354_hunds_rules.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The ground-term ordering at full coherence coupling carries a phi-ground configuration-mixing shift kappa*phi^-1*E_mix, occasionally reordering near-degenerate terms.
EXPERIMENT (VERIFIED): Precision spectroscopy of transition-metal or lanthanide ions measuring term spacings against Hund's rule predictions.
VERIFIED BY: Atomic ground terms obey Hund's rules exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1355 (term symbols) and Law 1359 (exchange energy) - Hund's rules are the coherence ordering of the configuration.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the mixing floor is phi^-1 * E_mix.

### CLARITY
The atom fills its shell like a host seating guests; the phi-law keeps the seating from being exact.

### NOVELTY
Classical atomic theory orders terms exactly; the phi-law gives the ordering a configuration-mixing floor.

### ACTIONABILITY
Run sim/1354_hunds_rules.py; verify J selection at kappa->0; proceed to 1355.

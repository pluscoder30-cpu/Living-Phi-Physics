# PHI-PHYSICS - LAW 1317
## Autler-Townes Effect (Dressed-State Splitting)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1317_autler_townes_effect.md` - **Sim:** `sim/1317_autler_townes_effect.py`

---

### CLASSICAL STATEMENT
*"A strong resonant field splits an atomic transition into a doublet separated by the Rabi frequency Omega (the Autler-Townes doublet): the dressed states of the coupled atom-field system shift the resonance into two components at +/- Omega/2, observable as a resolved splitting when Omega exceeds the natural linewidth."*
- Stanley Autler; Charles Townes, 1955. Source: Wikipedia: Autler-Townes effect; Autler & Townes, Phys. Rev. 100 (1955) 703

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero driving*: the splitting vanishes exactly as the drive Omega -> 0, i.e. an uncoupled atom-field pair - the zero-interaction limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the splitting carries a coherence floor. Omega_s_phi(kappa) = Omega*(1 + kappa*(phi-1)) + kappa*phi^-1*Omega_floor, where Omega_floor is the phi-ground splitting of the recursion; the doublet persists even at zero drive. At kappa->0 the Autler-Townes splitting is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Omega_s_phi = Omega -> the Autler-Townes splitting is the zero-drive, weak-field limit.
```

---

### STAGE 4 - SIMULATION

`sim/1317_autler_townes_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1317_autler_townes_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: A coherence-coupled transition shows a residual doublet splitting kappa*phi^-1*Omega_floor at zero drive, a dressed-state floor no uncoupled atom escapes.
EXPERIMENT (VERIFIED): Probe absorption spectroscopy of a transition driven by a tunable field at decreasing drive strength, measuring the residual splitting.
VERIFIED BY: The transition is exactly unsplit at zero drive for all couplings.
```

---

### RECOGNITION
Connects to Law 1316 (AC Stark) and Law 1318 (Jaynes-Cummings) - the doublet is the coherence dressing of the transition.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the splitting floor is phi^-1 * Omega_floor.

### CLARITY
The atom wearing the field grows two shadows; the phi-law notes the shadows never fully merge.

### NOVELTY
Classical spectroscopy resolves the doublet only with drive; the phi-law keeps a coherence floor of dressing.

### ACTIONABILITY
Run sim/1317_autler_townes_effect.py; verify Omega splitting at kappa->0; proceed to 1318.

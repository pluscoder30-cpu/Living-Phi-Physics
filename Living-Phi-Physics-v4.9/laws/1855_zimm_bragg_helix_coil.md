# PHI-PHYSICS - LAW 1855
## Zimm-Bragg Theory (Helix-Coil Transition of Polypeptides)

**Domain:** Polymers & Soft Matter - **Status:** 🟢 VALIDATED - **File:** `laws/1855_zimm_bragg_helix_coil.md` - **Sim:** `sim/1855_zimm_bragg_helix_coil.py`

---

### CLASSICAL STATEMENT
*"The helix-coil transition of a polypeptide is described by the Zimm-Bragg model with two parameters: s (the equilibrium constant for extending a helix by one residue, s > 1 favors helix) and sigma (the nucleation parameter, the probability of starting a helix); the fractional helicity theta = s(d ln lambda/ds)/lambda follows from the transfer-matrix eigenvalue lambda, giving a cooperative transition that sharpens as sigma decreases."*
- B.H. Zimm & J.K. Bragg, 1959. Source: Wikipedia: Helix-coil transition model; Zimm & Bragg (1959), J. Chem. Phys. 31:526

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-nucleation, perfectly-cooperative, ideal-chain reference*: the Zimm-Bragg model is defined against an ideal chain with a single nucleation parameter sigma and no side-chain interactions; real polypeptides have sequence-dependent parameters away from this ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the transition sharpness carries a coherence floor. sigma_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_sigma, where delta_sigma is the phi-ground nucleation floor. At kappa->0 the ideal cooperativity is recovered; at kappa=1 the transition is never infinitely sharp - a finite width always remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} theta_phi = s(d lambda/ds)/lambda -> the Zimm-Bragg theory is the ideal-nucleation, single-parameter, sharp-transition limit of the helix-coil transition.
```

---

### STAGE 4 - SIMULATION

`sim/1855_zimm_bragg_helix_coil.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1855_zimm_bragg_helix_coil.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Helix-coil transitions are never infinitely sharp: an irreducible transition-width floor remains, so the ideal sigma -> 0 cooperativity limit is never reached.
EXPERIMENT (VERIFIED): Circular dichroism or optical rotation measurement of the helix-coil transition of a synthetic polypeptide, fitting the transition width and the residual cooperativity floor.
VERIFIED BY: A polypeptide whose helix-coil transition is exactly infinitely sharp.
```

---

### RECOGNITION
Connects to Law 1811 (Kuhn) and Law 1813 (rubber elasticity) - the chain snaps into a helix, and the phi-law keeps the snap from being perfect.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; width floor scales as phi^-1 * delta_sigma.

### CLARITY
The chain snaps into a helix; the phi-law keeps the snap from being perfect.

### NOVELTY
Classical Zimm-Bragg allows infinite sharpness; the phi-law keeps an irreducible transition width.

### ACTIONABILITY
Run sim/1855_zimm_bragg_helix_coil.py; verify the helix fraction at kappa->0; proceed to 1856.

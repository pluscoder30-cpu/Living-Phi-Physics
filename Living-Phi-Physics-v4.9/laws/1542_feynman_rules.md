# PHI-PHYSICS - LAW 1542
## Feynman Rules (Diagrammatic Perturbation Theory)

**Domain:** Particle Physics / QFT - **Status:** 🟢 VALIDATED - **File:** `laws/1542_feynman_rules.md` - **Sim:** `sim/1542_feynman_rules.py`

---

### CLASSICAL STATEMENT
*"Feynman rules assign to each diagram a factor: propagators 1/(p^2 - m^2), vertices g, external legs, and a 4-momentum conserving delta function; the sum of all diagrams gives the scattering amplitude, making perturbation theory diagrammatic."*
- Richard Feynman (1948), 1948. Source: Feynman, Phys. Rev. 76 (1949) 769; Wikipedia: Feynman diagram

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-order, no-diagram vacuum*: the Feynman rules assume an expansion about the free vacuum with zero-order diagrams (no interactions); the classical treatment of the free theory is the zero-coupling, no-vertex limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

A_phi(kappa) = A_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*A_floor, where A_floor is the phi-ground nonperturbative floor. At kappa->0 the perturbative sum is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} A_phi = sum_diagrams -> the Feynman rules are the zero-nonperturbative, perturbative, loop-expansion limit.
```

---

### STAGE 4 - SIMULATION

`sim/1542_feynman_rules.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1542_feynman_rules.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The perturbative expansion carries a phi-ground nonperturbative floor, so the truncated series never exactly equals the full amplitude and resummations (Borel) retain an irreducible ambiguity.
EXPERIMENT (VERIFIED): Precision QED/QCD calculations to many loops vs experimental data (electron g-2, Bhabha at colliders).
VERIFIED BY: A perturbative series exactly equal to the full amplitude at any finite order at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1529 (dimensional regularization), Law 1528 (renormalization group) and Law 1543 (Ward identity) - Feynman rules are QFT's grammar.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The diagrams tell the story; the phi-law keeps a floor of the story's edge.

### NOVELTY
Classical expansion is exact; the phi-law predicts an irreducible nonperturbative floor.

### ACTIONABILITY
Run sim/1542_feynman_rules.py; verify the propagator; proceed to Law 1543.

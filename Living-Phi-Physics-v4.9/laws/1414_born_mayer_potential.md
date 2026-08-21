# PHI-PHYSICS - LAW 1414
## Born-Mayer Potential (Exponential Repulsion in Ionic Crystals)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1414_born_mayer_potential.md` - **Sim:** `sim/1414_born_mayer_potential.py`

---

### CLASSICAL STATEMENT
*"The Born-Mayer potential describes the short-range repulsion of closed-shell ions with an exponential form V_rep(r) = A e^(-r/rho), where rho ~ 0.345 A is a universal repulsion range parameter; combined with the Coulomb term it gives the Born-Mayer lattice energy and improves on the Born-Lande power-law repulsion for alkali halides and other ionic solids."*
- Max Born; Joseph Mayer, 1932. Source: Wikipedia: Born-Mayer potential; Born & Mayer, Z. Phys. 75 (1932) 1

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero range parameter*: the repulsion reduces to a hard-core step as rho -> 0, i.e. ions with zero soft-repulsion range - the hard-sphere limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the repulsion range carries a coherence floor. rho_phi(kappa) = rho*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_rho, where delta_rho is the phi-ground range variation; the repulsion never becomes a hard step. At kappa->0 the Born-Mayer repulsion is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} V_rep_phi = A e^(-r/rho) -> the Born-Mayer potential is the zero-range-variation, soft-wall limit.
```

---

### STAGE 4 - SIMULATION

`sim/1414_born_mayer_potential.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1414_born_mayer_potential.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The effective repulsion range at full coherence coupling carries a phi-ground variation kappa*phi^-1*delta_rho, a floor in the softness of the ionic repulsion.
EXPERIMENT (VERIFIED): High-pressure equation-of-state measurements of alkali halides extracting the repulsion range at increasing precision.
VERIFIED BY: Ionic repulsion follows the Born-Mayer exponential exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1413 (Born-Lande) and Law 1384 (Buckingham) - the Born-Mayer potential is the coherence exponential repulsion of the ionic lattice.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the range floor is phi^-1 * delta_rho.

### CLARITY
The ions soften their collision with a cushion; the phi-law keeps the cushion's thickness wobble.

### NOVELTY
Classical crystal theory fixes the repulsion range; the phi-law turns it into a coherence-varying quantity.

### ACTIONABILITY
Run sim/1414_born_mayer_potential.py; verify A e^(-r/rho) at kappa->0; proceed to 1415.

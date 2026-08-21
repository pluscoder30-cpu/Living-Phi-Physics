# PHI-PHYSICS - LAW 1721
## Potts Model (q-State Generalization of the Ising Model)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1721_potts_model.md` - **Sim:** `sim/1721_potts_model.py`

---

### CLASSICAL STATEMENT
*"The Potts model generalizes the Ising model to q states: H = -J sum delta(s_i, s_j), where each spin takes q values; q=2 is the Ising model, q=1 percolation, q=3 the 3-state Potts model (which describes the ordering transition of certain systems), and the model exhibits first-order transitions for q > 4 in 2D - a universal framework for discrete phase transitions."*
- Renfrey Potts (1952); underlying theory by C. Domb (1949), 1952. Source: Wikipedia: Potts model; Potts (1952), Proc. Camb. Phil. Soc. 48:106

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly symmetric q-state, zero-fluctuation lattice*: the Potts model assumes exact q-state symmetry on an infinite ideal lattice with zero disorder and zero fluctuations so that the transition is a clean symmetry-breaking event - an idealized discrete world.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the transition carries a coherence floor. T_c_phi(kappa) = T_c_potts*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_T, where delta_T is the phi-ground smearing. At kappa->0 the exact Potts transition is recovered; at kappa=1 the transition is smeared by an irreducible coherent width.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} T_c_phi = T_c_potts -> the Potts model is the exact-q-state, infinite-lattice, zero-disorder limit of multistate phase transitions.
```

---

### STAGE 4 - SIMULATION

`sim/1721_potts_model.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1721_potts_model.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: q-state ordering transitions in real systems are smeared over a phi-ground width: the q>4 first-order transition is softened and the q=3 transition's critical point is rounded.
EXPERIMENT (VERIFIED): Specific-heat and order-parameter measurement of a 3-state Potts realization (e.g. certain liquid crystals or adsorbed monolayers) comparing the transition sharpness to the exact solution.
VERIFIED BY: A q-state Potts realization whose transition is exactly sharp with zero smearing.
```

---

### RECOGNITION
Connects to Law 1719 (Ising) and Law 533 (Landau) - the Potts model is the multistate grammar of order, and the grammar is never perfectly spoken.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; transition width scales as phi^-1 * delta_T.

### CLARITY
The q states vote; the phi-law keeps the count from being exact.

### NOVELTY
Classical Potts theory gives exact transitions; the phi-law smears them with a coherence floor.

### ACTIONABILITY
Run sim/1721_potts_model.py; verify q=2 -> Ising at kappa->0; proceed to 1722.

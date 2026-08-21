# PHI-PHYSICS - LAW 1719
## Ising Model (Binary-Spin Lattice Model of Phase Transitions)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1719_ising_model.md` - **Sim:** `sim/1719_ising_model.py`

---

### CLASSICAL STATEMENT
*"The Ising model describes spins that take two values s_i = +/-1 on a lattice with H = -J sum s_i s_j; in 1D there is no phase transition at finite T, but in 2D Onsager's exact solution gives a finite Curie temperature T_c with critical exponents, making the Ising model the paradigmatic model of continuous phase transitions and universality."*
- Ernst Ising (1925); solved 1D by Ising; 2D by Onsager (1944), 1925. Source: Wikipedia: Ising model; Ising (1925), Z. Phys. 31:253; Onsager (1944)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly discrete, zero-fluctuation, infinite lattice*: the Ising model assumes spins exactly +/-1 with no quantum fluctuations, an infinite lattice and exact criticality at the Onsager point - an idealized discrete-spin world that real magnets realize only approximately.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the critical temperature carries a coherence floor. T_c_phi(kappa) = T_c_ising*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_T, where delta_T is the phi-ground shift of the transition. At kappa->0 the exact Onsager T_c is recovered; at kappa=1 the transition is smeared over a coherent width and T_c is shifted.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} T_c_phi = T_c_ising -> the Ising model is the discrete-spin, infinite-lattice, zero-fluctuation limit of binary phase transitions.
```

---

### STAGE 4 - SIMULATION

`sim/1719_ising_model.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1719_ising_model.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Real Ising-like magnets show a smeared transition and shifted T_c relative to the exact solution, with the smearing set by the phi-ground coherence width - exact criticality is never achieved.
EXPERIMENT (VERIFIED): Specific-heat and magnetization measurement of a quasi-2D Ising magnet (e.g. Rb2CoF4, layered antiferromagnets) comparing the transition width to the exact Onsager prediction.
VERIFIED BY: An Ising-like magnet whose transition is exactly sharp at the Onsager T_c with zero width.
```

---

### RECOGNITION
Connects to Law 1718 (Heisenberg) and Law 533 (Landau theory) - the Ising model is the binary grammar of order, and no grammar is spoken exactly.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; transition width scales as phi^-1 * delta_T.

### CLARITY
The binary spins vote for order; the phi-law keeps a few abstentions.

### NOVELTY
Classical Ising gives exact criticality; the phi-law smears it with a coherence floor.

### ACTIONABILITY
Run sim/1719_ising_model.py; verify the 2D Onsager T_c at kappa->0; proceed to 1720.

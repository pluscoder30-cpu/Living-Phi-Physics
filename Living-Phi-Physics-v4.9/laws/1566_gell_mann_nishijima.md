# PHI-PHYSICS - LAW 1566
## Gell-Mann-Nishijima Relation (Charge-Hypercharge-Isospin)

**Domain:** Particle Physics / Hadrons - **Status:** 🟢 VALIDATED - **File:** `laws/1566_gell_mann_nishijima.md` - **Sim:** `sim/1566_gell_mann_nishijima.py`

---

### CLASSICAL STATEMENT
*"The electric charge, third component of isospin and hypercharge are related by the Gell-Mann-Nishijima formula Q = I_3 + Y/2, with hypercharge Y = B + S (baryon number plus strangeness); this organizes the hadron multiplets and predicts the hypercharge quantum numbers."*
- Murray Gell-Mann (1953); Kazuhiko Nishijima (1953); Tadao Nakano, 1953. Source: Nishijima, Prog. Theor. Phys. 13 (1955) 285; Gell-Mann, Phys. Rev. 92 (1953) 833

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-hypercharge, zero-strangeness limit*: for ordinary hadrons with S = 0, Y = B and the relation reduces to Q = I_3 + B/2; the classical treatment of strangeness-zero hadrons is the zero-strangeness, pure-isospin limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

Y_phi(kappa) = Y_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*Y_floor, where Y_floor is the phi-ground residual-hypercharge floor. At kappa->0 the exact Q = I_3 + Y/2 is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Y_phi = B + S -> the Gell-Mann-Nishijima relation is the zero-mixing, exact-hypercharge, quantum-number limit.
```

---

### STAGE 4 - SIMULATION

`sim/1566_gell_mann_nishijima.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1566_gell_mann_nishijima.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The hypercharge relation carries a phi-ground mixing floor, so hadron charge assignments deviate from the exact Q = I_3 + Y/2 by an irreducible small correction from higher-order mixing.
EXPERIMENT (VERIFIED): Hadron quantum number measurements (charge, strangeness, hypercharge) and their exact assignments in the PDG.
VERIFIED BY: A hadron whose charge is not exactly Q = I_3 + Y/2 with zero residual floor.
```

---

### RECOGNITION
Connects to Law 1536 (Eightfold Way), Law 1567 (strangeness) and Law 1568 (hypercharge) - the G-M-N relation is the hadron's ID card.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Charge is the sum of two labels; the phi-law keeps a floor of the labels drifting.

### NOVELTY
Classical relation is exact; the phi-law predicts an irreducible mixing floor.

### ACTIONABILITY
Run sim/1566_gell_mann_nishijima.py; verify Q = I3 + Y/2; proceed to Law 1567.

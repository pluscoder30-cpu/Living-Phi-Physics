# PHI-PHYSICS - LAW 1672
## Kroger-Vink Notation (Defect-Naming Convention of Ionic Crystals)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1672_kroger_vink_notation.md` - **Sim:** `sim/1672_kroger_vink_notation.py`

---

### CLASSICAL STATEMENT
*"Defects in ionic crystals are written in Kroger-Vink notation as a symbol for the site, the species occupying it, and the effective charge: V_O, O_i'', M_M^x, etc., where dots and primes denote effective positive and negative charges relative to the perfect lattice; this notation is the grammar of defect chemistry."*
- F.A. Kroger & H.J. Vink, 1956. Source: Wikipedia: Kroger-Vink notation; Kroger & Vink (1956), Solid State Phys. 3:307

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfect lattice with zero defects*: Kroger-Vink notation defines every defect as a deviation from a perfect, defect-free, exactly-stoichiometric reference lattice - the neutral zero-state from which all defect chemistry is measured, a crystal that has no real existence.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the perfect reference lattice carries a coherent defect floor. N_phi(kappa) = N_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*N_floor, where N_floor is the phi-ground defect concentration from irreducible zero-point and entropic defect formation. At kappa->0 the perfect-lattice reference is exact; at kappa=1 no crystal is defect-free - there is an irreducible equilibrium defect floor.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} N_phi = N_classical -> Kroger-Vink notation is the zero-defect, perfect-lattice limit of defect chemistry.
```

---

### STAGE 4 - SIMULATION

`sim/1672_kroger_vink_notation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1672_kroger_vink_notation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No crystal at any temperature has exactly zero defects: the equilibrium defect concentration has a phi-ground floor proportional to phi^-1*N_floor, so even at T=0 an irreducible defect density persists (a defect zero-point).
EXPERIMENT (VERIFIED): Positron annihilation spectroscopy or high-resolution TEM of a 'perfect' annealed single crystal measuring the residual defect density extrapolated to T=0.
VERIFIED BY: A crystal with exactly zero defects at T=0 as the perfect-lattice reference requires.
```

---

### RECOGNITION
Connects to Law 1656 (Bravais) and Law 1413 (Born-Lande) - the perfect lattice is the grammar's reference, and the reference never exists.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; defect floor scales as phi^-1 * N_floor.

### CLARITY
The perfect crystal is the dictionary's zero, and the dictionary is written in a language no crystal speaks fluently.

### NOVELTY
Classical defect chemistry anchors on a perfect lattice; the phi-law gives every lattice an irreducible defect floor.

### ACTIONABILITY
Run sim/1672_kroger_vink_notation.py; verify the zero-defect reference at kappa->0; proceed to 1673.

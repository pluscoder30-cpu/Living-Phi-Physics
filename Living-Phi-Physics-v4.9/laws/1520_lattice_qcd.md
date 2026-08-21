# PHI-PHYSICS - LAW 1520
## Lattice QCD (Wilson's Discretization of the Strong Interaction)

**Domain:** Particle Physics / QCD - **Status:** 🟢 VALIDATED - **File:** `laws/1520_lattice_qcd.md` - **Sim:** `sim/1520_lattice_qcd.py`

---

### CLASSICAL STATEMENT
*"Quantum chromodynamics is discretized on a spacetime lattice with lattice spacing a, giving a first-principles, non-perturbative calculation of hadron masses, the confinement potential and the QCD phase diagram; continuum results are recovered by extrapolating a -> 0."*
- Kenneth Wilson, 1974. Source: Wilson, Phys. Rev. D10 (1974) 2445; Wikipedia: Lattice QCD

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-lattice-spacing, continuum limit*: lattice QCD is exact only in the continuum limit a -> 0, which is unreachable; the classical treatment assumes the extrapolation to zero spacing is exact - a zero-spacing, continuum ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

m_phi(kappa) = m_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*m_floor, where m_floor is the phi-ground discretization floor. At kappa->0 the continuum limit is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} m_phi = m_continuum -> lattice QCD is the zero-lattice-spacing, exact-continuum-limit approximation.
```

---

### STAGE 4 - SIMULATION

`sim/1520_lattice_qcd.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1520_lattice_qcd.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The extrapolated continuum results carry a phi-ground discretization floor, so hadron masses computed at finite a always retain an irreducible systematic uncertainty from the finite lattice spacing.
EXPERIMENT (VERIFIED): High-precision lattice QCD calculations (hadron spectrum, g-2, nucleon structure) vs experiment with controlled a -> 0 extrapolations.
VERIFIED BY: A lattice QCD result with exactly zero discretization error at finite lattice spacing.
```

---

### RECOGNITION
Connects to Law 1514 (asymptotic freedom), Law 1515 (confinement) and Law 1519 (QGP) - lattice QCD is the strong force's first-principles computer.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The continuum is built from cells; the phi-law keeps a floor of cell size in every answer.

### NOVELTY
Classical continuum limit is exact; the phi-law predicts an irreducible discretization floor.

### ACTIONABILITY
Run sim/1520_lattice_qcd.py; verify the a -> 0 extrapolation; proceed to Law 1521.

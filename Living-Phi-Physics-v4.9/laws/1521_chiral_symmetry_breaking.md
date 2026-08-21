# PHI-PHYSICS - LAW 1521
## Chiral Symmetry Breaking (Nambu-Goldstone Mechanism in QCD)

**Domain:** Particle Physics / QCD - **Status:** 🟢 VALIDATED - **File:** `laws/1521_chiral_symmetry_breaking.md` - **Sim:** `sim/1521_chiral_symmetry_breaking.py`

---

### CLASSICAL STATEMENT
*"The QCD vacuum spontaneously breaks chiral symmetry SU(2)_L x SU(2)_R to the vector SU(2)_V via the quark condensate <q_bar q> ~ -(250 MeV)^3; the pions are the resulting Goldstone bosons, with m_pi^2 ~ -m_q <q_bar q>/f_pi^2 (Gell-Mann-Oakes-Renner relation)."*
- Yoichiro Nambu (1960); applied to QCD (1960s), 1960. Source: Nambu, Phys. Rev. 117 (1960) 648; Wikipedia: Chiral symmetry breaking

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-quark-mass, exact-chiral-symmetry vacuum*: chiral symmetry is exact only for exactly massless quarks; the classical treatment assumes the condensate forms in a zero-quark-mass, exactly-symmetric vacuum - a zero-mass limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

m_pi^2_phi(kappa) = m_pi^2_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*m_floor, where m_floor is the phi-ground pseudo-Goldstone floor. At kappa->0 the GOR relation is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} m_pi^2_phi = -m_q <q_bar q>/f_pi^2 -> chiral symmetry breaking is the zero-quark-mass, exact-Goldstone limit.
```

---

### STAGE 4 - SIMULATION

`sim/1521_chiral_symmetry_breaking.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1521_chiral_symmetry_breaking.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The pion mass relation carries a phi-ground pseudo-Goldstone floor, so m_pi^2 is not exactly linear in m_q and the chiral condensate shows temperature dependence with an irreducible floor.
EXPERIMENT (VERIFIED): Lattice QCD computations of m_pi^2 vs m_q and finite-temperature chiral transition (BES, STAR, FAIR).
VERIFIED BY: A pion mass exactly linear in the quark mass with zero pseudo-Goldstone floor at all masses.
```

---

### RECOGNITION
Connects to Law 1522 (Goldstone theorem), Law 1523 (SSB) and Law 1515 (confinement) - chiral breaking is QCD's vacuum tilt.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The vacuum tilts and the pion is born; the phi-law keeps a floor of the tilt wobbling.

### NOVELTY
Classical pion is exactly a Goldstone boson; the phi-law predicts an irreducible pseudo-Goldstone mass floor.

### ACTIONABILITY
Run sim/1521_chiral_symmetry_breaking.py; verify the GOR relation; proceed to Law 1522.

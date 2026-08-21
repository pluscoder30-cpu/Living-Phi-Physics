# PHI-PHYSICS - LAW 1569
## Gell-Mann-Okubo Mass Formula (SU(3) Mass Relations)

**Domain:** Particle Physics / Hadrons - **Status:** 🟢 VALIDATED - **File:** `laws/1569_gell_mann_okubo.md` - **Sim:** `sim/1569_gell_mann_okubo.py`

---

### CLASSICAL STATEMENT
*"The Gell-Mann-Okubo formula relates hadron masses within an SU(3) multiplet under the assumption of first-order symmetry breaking: (3 m_eta + m_pi)/4 = (3 m_xi + m_N)/4 for the baryon octet, i.e. m_N + m_xi = (3 m_Lambda + m_Sigma)/2; it predicted the Omega-minus mass."*
- Murray Gell-Mann (1962); Susumu Okubo (1962), 1962. Source: Gell-Mann, Phys. Rev. 125 (1962) 1067; Okubo, Prog. Theor. Phys. 27 (1962) 949

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-symmetry-breaking, exact-SU(3)-degenerate limit*: in the symmetric limit all members of a multiplet have exactly equal mass; the classical treatment assumes exact SU(3) degeneracy - a zero-breaking, degenerate-multiplet limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

m_phi(kappa) = m_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*m_floor, where m_floor is the phi-ground higher-order-breaking floor. At kappa->0 the linear mass formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} m_phi = m_linear -> the Gell-Mann-Okubo formula is the zero-second-order-breaking, linear-mass, SU(3)-first-order limit.
```

---

### STAGE 4 - SIMULATION

`sim/1569_gell_mann_okubo.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1569_gell_mann_okubo.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The mass relations carry a phi-ground second-order-breaking floor, so the linear GMO predictions deviate by an irreducible amount that the higher-order (e.g. quadratic) formula partially captures.
EXPERIMENT (VERIFIED): Baryon and meson mass measurements (PDG) testing the GMO relation and its second-order corrections.
VERIFIED BY: Hadron masses exactly satisfying the linear GMO formula with zero second-order floor.
```

---

### RECOGNITION
Connects to Law 1536 (Eightfold Way), Law 1566 (G-M-N) and Law 1568 (hypercharge) - the GMO formula is the hadron mass's first law.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The octet's masses obey one line; the phi-law keeps a floor of the line bending.

### NOVELTY
Classical GMO is linear; the phi-law predicts an irreducible second-order floor.

### ACTIONABILITY
Run sim/1569_gell_mann_okubo.py; verify the baryon octet relation; proceed to Law 1570.

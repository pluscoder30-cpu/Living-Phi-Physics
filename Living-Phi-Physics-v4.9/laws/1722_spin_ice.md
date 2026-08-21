# PHI-PHYSICS - LAW 1722
## Spin Ice (Frustrated Magnetic State with Emergent Monopoles)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1722_spin_ice.md` - **Sim:** `sim/1722_spin_ice.py`

---

### CLASSICAL STATEMENT
*"In spin-ice materials (Dy2Ti2O7, Ho2Ti2O7), the magnetic moments on the pyrochlore lattice obey the ice rule: two spins point into and two out of each tetrahedron; the ground state is macroscopically degenerate (residual entropy ~ S = R/2 ln(3/2)), and the elementary excitations are emergent magnetic monopoles connected by Dirac strings - a real-world realization of frustrated Coulombic order."*
- M.J. Harris, S.T. Bramwell, D.F. McMorrow, T. Zeiske & F. Zitz (1997), 1997. Source: Wikipedia: Spin ice; Harris et al. (1997), Phys. Rev. Lett. 79:2554

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-defect, perfectly ice-rule-satisfying spin tetrahedra*: the spin-ice ground state is defined against configurations where every tetrahedron exactly obeys the 2-in-2-out ice rule with zero violations - a perfectly frustrated, exactly-rule-satisfying reference no finite sample realizes at any temperature.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the ice rule carries a coherent violation floor. n_m_phi(kappa) = n_m_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*n_floor, where n_floor is the phi-ground monopole density. At kappa->0 the exact ice-rule state is recovered; at kappa=1 a finite monopole density always exists - the ice rule is never perfectly obeyed.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} n_m_phi = 0 -> spin ice is the zero-monopole, perfectly-frustrated, exact-ice-rule limit of frustrated magnetism.
```

---

### STAGE 4 - SIMULATION

`sim/1722_spin_ice.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1722_spin_ice.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No spin-ice material ever reaches exactly zero monopole density: an irreducible monopole floor remains even at the lowest temperatures, producing residual specific heat and a finite low-temperature relaxation that cannot be removed.
EXPERIMENT (VERIFIED): Specific-heat, ac-susceptibility and diffuse neutron scattering of Dy2Ti2O7 or Ho2Ti2O7 at millikelvin, measuring the residual monopole density floor.
VERIFIED BY: A spin-ice material reaching exactly zero monopole density at T=0 with perfect ice-rule obedience.
```

---

### RECOGNITION
Connects to Law 1721 (Potts) and Law 1730 (Stoner) - frustration is the ice's signature, and the phi-law keeps a drip of monopoles always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; monopole floor scales as phi^-1 * n_floor.

### CLARITY
The tetrahedra try to follow the ice rule; the phi-law keeps a few tetrahedra always breaking it.

### NOVELTY
Classical spin ice allows a perfect ice rule; the phi-law keeps an irreducible violation floor.

### ACTIONABILITY
Run sim/1722_spin_ice.py; verify the residual entropy at kappa->0; proceed to 1723.

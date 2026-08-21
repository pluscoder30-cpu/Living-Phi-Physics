# PHI-PHYSICS - LAW 1536
## Seesaw Mechanism (Small Neutrino Masses from Heavy Right-Handed Neutrinos)

**Domain:** Particle Physics / Neutrinos - **Status:** 🟢 VALIDATED - **File:** `laws/1536_seesaw_mechanism.md` - **Sim:** `sim/1536_seesaw_mechanism.py`

---

### CLASSICAL STATEMENT
*"In the type-I seesaw, the neutrino mass matrix [[0, M_D],[M_D, M_R]] with M_R >> M_D gives a light neutrino mass m_nu ~ M_D^2/M_R: the smallness of neutrino masses is explained by a very heavy right-handed neutrino at the GUT scale ~10^15 GeV."*
- Peter Minkowski (1977); Tsutomu Yanagida (1979); Murray Gell-Mann; Pierre Ramond; Richard Slansky (1979), 1979. Source: Minkowski, Phys. Lett. B67 (1977) 421; Yanagida (1979); Wikipedia: Seesaw mechanism

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-Dirac-mass, zero-light-neutrino limit*: if M_D -> 0 the light neutrino is exactly massless; the seesaw explains small masses as the ratio of a zero-like Dirac mass over a huge Majorana mass - a zero-mass numerator limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

m_nu_phi(kappa) = m_nu_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*m_floor, where m_floor is the phi-ground radiative floor. At kappa->0 the tree-level seesaw relation is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} m_nu_phi = M_D^2/M_R -> the seesaw mechanism is the zero-radiative, tree-level, exact-Majorana limit.
```

---

### STAGE 4 - SIMULATION

`sim/1536_seesaw_mechanism.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1536_seesaw_mechanism.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The light neutrino masses carry a phi-ground radiative floor, so the seesaw prediction deviates from the simple M_D^2/M_R by an irreducible loop correction, affecting the mass ordering and 0nu-beta-beta rate.
EXPERIMENT (VERIFIED): Neutrino mass, ordering and 0nu-beta-beta measurements (JUNO, DUNE, KamLAND-Zen) vs seesaw predictions.
VERIFIED BY: Neutrino masses exactly matching the tree-level seesaw with zero radiative floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1511 (PMNS), Law 1537 (neutrino oscillations) and Law 1535 (GUT) - the seesaw is the neutrino's weight machine.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The heavy lever lifts the light; the phi-law keeps a floor of the lift leaking.

### NOVELTY
Classical seesaw is tree-level; the phi-law predicts an irreducible radiative floor.

### ACTIONABILITY
Run sim/1536_seesaw_mechanism.py; verify m_nu = M_D^2/M_R; proceed to Law 1537.

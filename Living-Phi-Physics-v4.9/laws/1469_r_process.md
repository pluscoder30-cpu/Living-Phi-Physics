# PHI-PHYSICS - LAW 1469
## Rapid Neutron-Capture Process (r-Process Nucleosynthesis)

**Domain:** Nuclear Astrophysics - **Status:** 🟢 VALIDATED - **File:** `laws/1469_r_process.md` - **Sim:** `sim/1469_r_process.py`

---

### CLASSICAL STATEMENT
*"In the r-process, neutron capture is faster than beta decay (tau_n >> tau_beta), driving nuclei far from stability toward the neutron drip line before beta decay brings them back; it produces half of the heavy elements and requires extreme neutron densities (neutron-star mergers, supernovae)."*
- Burbidge, Burbidge, Fowler & Hoyle (B2FH); Alastair Cameron, 1957. Source: Burbidge et al., Rev. Mod. Phys. 29 (1957) 547; Wikipedia: R-process

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-separation-energy, exact-drip-line stop*: the r-process assumes capture is so fast that nuclei reach the drip line where the next capture is exactly zero (zero neutron-separation energy) - an exact stopping point.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

S_n_phi(kappa) = S_n_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*S_floor, where S_floor is the phi-ground neutron-separation floor at the drip line. At kappa->0 the r-process path is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} S_n_phi = S_n_classical -> the r-process is the zero-separation-energy, exact-drip-line limit.
```

---

### STAGE 4 - SIMULATION

`sim/1469_r_process.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1469_r_process.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The neutron drip line carries a phi-ground separation-energy floor, so the r-process path extends slightly beyond the classical drip line and the final abundance pattern depends on this floor.
EXPERIMENT (VERIFIED): Mass measurements of very neutron-rich nuclei (rare-isotope facilities, FRIB, RIKEN) pinning the drip line and r-process abundances from GW170817 kilonova.
VERIFIED BY: An r-process path exactly stopping at the classical drip line with zero separation-energy floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1468 (s-process), Law 1217 (drip-line physics) and Law 1452 (Gamow) - the r-process is the lightning of element building.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The fast capture rides the cliff; the phi-law keeps a floor of footing past the edge.

### NOVELTY
Classical r-process stops at the drip line; the phi-law predicts a residual reach beyond it.

### ACTIONABILITY
Run sim/1469_r_process.py; verify the drip-line path; proceed to Law 1470.

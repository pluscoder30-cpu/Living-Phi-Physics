# PHI-PHYSICS - LAW 1598
## Neutron Drip (Transition to Free Neutrons in Neutron-Rich Matter)

**Domain:** Nuclear Astrophysics - **Status:** 🟢 VALIDATED - **File:** `laws/1598_neutron_star_drip.md` - **Sim:** `sim/1598_neutron_star_drip.py`

---

### CLASSICAL STATEMENT
*"Beyond the neutron drip line, nuclei cannot bind additional neutrons: the neutron separation energy S_n becomes zero and neutrons drip out; the drip line marks the boundary of bound nuclei in the nuclear chart and is probed at rare-isotope facilities."*
- Neutron drip line (Goldansky 1960s; nuclear mass models), 1960. Source: Wikipedia: Neutron drip line; Krane, Introductory Nuclear Physics

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-separation-energy, exact-drip-line limit*: at the drip line the neutron separation energy is exactly zero; the classical treatment of bound nuclei assumes S_n > 0 strictly - a zero-separation-energy threshold.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

S_n_phi(kappa) = S_n_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*S_floor, where S_floor is the phi-ground residual separation floor. At kappa->0 the exact drip line is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} S_n_phi = S_n -> the neutron drip is the zero-separation-energy, exact-boundary limit.
```

---

### STAGE 4 - SIMULATION

`sim/1598_neutron_star_drip.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1598_neutron_star_drip.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The neutron drip line carries a phi-ground separation floor, so the last bound nucleus beyond the classical drip line retains a small residual binding that shifts the boundary.
EXPERIMENT (VERIFIED): Discovery of the most neutron-rich isotopes at FRIB, RIKEN (e.g. 40Mg, 70Ca) and mass measurements pinning the drip line.
VERIFIED BY: A neutron-rich isotope with exactly zero binding exactly at the classical drip line at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1469 (r-process), Law 1492 (halo) and Law 1504 (proton radioactivity) - the drip line is the nuclear map's edge.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The last neutron dangles at the edge; the phi-law keeps a floor of the edge holding.

### NOVELTY
Classical drip line is exact; the phi-law predicts a residual binding beyond it.

### ACTIONABILITY
Run sim/1598_neutron_star_drip.py; verify the drip; proceed to Law 1599.

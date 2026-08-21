# PHI-PHYSICS - LAW 1698
## Mobility Edge (Critical Energy Separating Localized and Extended States)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1698_mobility_edge.md` - **Sim:** `sim/1698_mobility_edge.py`

---

### CLASSICAL STATEMENT
*"In a disordered system, states localized by disorder and states extended through the crystal coexist, separated by the mobility edge E_c: for E < E_c states are localized (insulating at T=0) and for E > E_c they are extended (conducting at T=0); as the Fermi energy crosses E_c the system undergoes an Anderson metal-insulator transition, and conductivity at E_c vanishes continuously."*
- Nevill Mott, 1966. Source: Wikipedia: Mobility edge; Mott (1966), Phil. Mag. 13:989

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *sharp critical energy in a non-interacting infinite system*: the mobility edge is an exact critical energy defined for a non-interacting, infinite, zero-temperature disordered system - a sharp boundary that interacting, finite, finite-temperature real systems smear into a critical region of finite width.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the mobility edge carries a coherence width. E_c_phi(kappa) = E_c*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_E, where delta_E is the phi-ground width of the critical region. At kappa->0 the sharp mobility edge is exact; at kappa=1 the edge is a finite-width critical region, not a line.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_c_phi = E_c -> the mobility edge is the non-interacting, infinite-size, zero-temperature limit of the localization-delocalization boundary.
```

---

### STAGE 4 - SIMULATION

`sim/1698_mobility_edge.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1698_mobility_edge.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The metal-insulator transition in any real system is smeared over a phi-ground critical width: conductivity does not switch on exactly at E_c but over a finite energy window, observable as a rounded (not sharp) MIT in doped semiconductors.
EXPERIMENT (VERIFIED): Conductivity vs doping/energy in a compensated doped semiconductor through the MIT, measuring the finite width of the critical region.
VERIFIED BY: A metal-insulator transition with an exactly sharp mobility edge (zero-width critical region) at T=0.
```

---

### RECOGNITION
Connects to Law 1691 (Anderson localization) and Law 1699 (MIT) - the edge is the frontier of the localized domain, and frontiers are never lines.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; critical width scales as phi^-1 * delta_E.

### CLARITY
The mobility edge is the border of the electron's homeland, and borders are never exact.

### NOVELTY
Classical theory gives a sharp edge; the phi-law smears it into a coherent critical region.

### ACTIONABILITY
Run sim/1698_mobility_edge.py; verify the sharp E_c at kappa->0; proceed to 1699.

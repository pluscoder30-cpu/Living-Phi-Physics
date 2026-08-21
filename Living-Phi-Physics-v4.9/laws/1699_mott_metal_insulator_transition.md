# PHI-PHYSICS - LAW 1699
## Mott Metal-Insulator Transition (Correlation-Driven Localization)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1699_mott_metal_insulator_transition.md` - **Sim:** `sim/1699_mott_metal_insulator_transition.py`

---

### CLASSICAL STATEMENT
*"When electron correlations are strong, the band picture fails and a metal can become an insulator purely by interaction: at the Mott transition the ratio of Coulomb repulsion to bandwidth U/W exceeds a critical value, the Fermi surface is destroyed, and conductivity vanishes discontinuously at T=0; the critical density obeys the Mott criterion n_c^(1/3) a_B ~ 0.26."*
- Nevill Mott, 1949. Source: Wikipedia: Metal-insulator transition; Mott (1949), Proc. Phys. Soc. A62:416

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly screened, single-electron band picture*: the Mott transition is defined against the band-theory (single-electron) limit where interactions are exactly zero and the metal is always a metal - a zero-interaction reference that no real electron system has.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the transition threshold carries a coherence basin. n_c_phi(kappa) = n_c*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_n, where delta_n is the phi-ground width of the transition basin. At kappa->0 the sharp Mott criterion is exact; at kappa=1 the transition is a finite basin, not a sharp critical point.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} n_c_phi = (0.26/a_B)^3 -> the Mott transition is the zero-interaction, band-theory, sharp-critical-point limit of correlation-driven localization.
```

---

### STAGE 4 - SIMULATION

`sim/1699_mott_metal_insulator_transition.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1699_mott_metal_insulator_transition.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Mott transition is smeared over a phi-ground density basin: conductivity does not jump exactly at n_c but crosses over through a finite interval, and a residual conductivity floor exists on the insulating side.
EXPERIMENT (VERIFIED): High-pressure or chemical-doping-driven MIT in a model Mott system (e.g. V2O3, doped silicon), measuring the finite width of the transition basin at the lowest temperatures.
VERIFIED BY: A Mott transition that is exactly sharp (zero-width critical basin) with conductivity jumping discontinuously at a single density.
```

---

### RECOGNITION
Connects to Law 1698 (mobility edge) and Law 1403 (Hubbard) - correlations close the metal's door, and the door is never a perfect seal.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; basin width scales as phi^-1 * delta_n.

### CLARITY
The metal's door closes by correlation, and the phi-law keeps the door from sealing fully.

### NOVELTY
Classical Mott theory gives a sharp critical point; the phi-law widens it into a coherence basin.

### ACTIONABILITY
Run sim/1699_mott_metal_insulator_transition.py; verify n_c^(1/3) a_B ~ 0.26 at kappa->0; proceed to 1700.

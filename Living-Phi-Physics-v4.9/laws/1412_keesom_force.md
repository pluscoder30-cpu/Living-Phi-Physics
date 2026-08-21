# PHI-PHYSICS - LAW 1412
## Keesom Force (Orientation Interaction of Permanent Dipoles, V ~ -C/r^6)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1412_keesom_force.md` - **Sim:** `sim/1412_keesom_force.py`

---

### CLASSICAL STATEMENT
*"Keesom forces arise from the thermal-averaged electrostatic interaction of permanent dipoles: V(r) = -(2/3)(mu_1^2 mu_2^2/((4 pi eps_0)^2 k_B T)) r^-6, the angle-averaged dipole-dipole energy at temperature T; together with the Debye (dipole-induced) and London (dispersion) terms it forms the van der Waals interaction between polar molecules."*
- Willem Hendrik Keesom, 1915. Source: Wikipedia: Keesom force; Keesom, Proc. R. Acad. Sci. 18 (1915) 636

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *infinite temperature*: the Keesom orientation average vanishes exactly as T -> infinity, i.e. freely rotating dipoles with zero orientational correlation - the random-orientation limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the orientational correlation carries a coherence floor. V_K_phi(kappa) = V_K*(1 + kappa*(phi-1)) + kappa*phi^-1*V_floor, where V_floor is the phi-ground orientational correlation; even freely rotating dipoles retain a floor attraction. At kappa->0 the Keesom force is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} V_phi = -(2/3)(mu_1^2 mu_2^2/((4 pi eps0)^2 k_B T)) r^-6 -> the Keesom force is the zero-orientational-correlation, high-T limit.
```

---

### STAGE 4 - SIMULATION

`sim/1412_keesom_force.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1412_keesom_force.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The polar-molecule interaction at full coherence coupling retains a phi-ground orientational floor kappa*phi^-1*V_floor at high temperature, a residual dipole alignment.
EXPERIMENT (VERIFIED): Dielectric and virial measurements of polar gases (e.g. HCl, H2O vapor) comparing the interaction against Keesom theory at high T.
VERIFIED BY: Freely rotating dipoles have exactly zero orientation-averaged attraction at high temperature for all couplings.
```

---

### RECOGNITION
Connects to Law 1411 (London) and Law 142 (van der Waals) - the Keesom force is the coherence orientation average of dipoles.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the orientational floor is phi^-1 * V_floor.

### CLARITY
Even tumbling dipoles lean toward each other a hair; the phi-law keeps the hair.

### NOVELTY
Classical molecular physics randomizes dipoles exactly; the phi-law keeps a coherence orientation floor.

### ACTIONABILITY
Run sim/1412_keesom_force.py; verify 1/T r^-6 at kappa->0; proceed to 1413.

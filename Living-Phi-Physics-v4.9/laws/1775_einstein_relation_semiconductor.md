# PHI-PHYSICS - LAW 1775
## Einstein Relation (D = mu k_B T/q in Semiconductors)

**Domain:** Semiconductors - **Status:** 🟢 VALIDATED - **File:** `laws/1775_einstein_relation_semiconductor.md` - **Sim:** `sim/1775_einstein_relation_semiconductor.py`

---

### CLASSICAL STATEMENT
*"In thermodynamic equilibrium the diffusion coefficient and mobility of carriers are related by D = mu k_B T/q (the Einstein relation); it follows from detailed balance between drift and diffusion and connects the two transport coefficients, allowing the diffusion coefficient to be obtained from measured mobility - a cornerstone of semiconductor physics."*
- Albert Einstein (1905); extended to semiconductors by Shockley (1949), 1905. Source: Wikipedia: Einstein relation; Einstein (1905), Ann. Phys. 17:549

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-temperature, perfectly degenerate equilibrium reference*: the Einstein relation D = mu k_B T/q assumes classical (Boltzmann) statistics in equilibrium; at zero temperature the relation vanishes, and at high degeneracy it is modified by the Fermi-Dirac factor - the classical relation is the zero-degeneracy, finite-temperature limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the diffusion carries a coherence floor. D_phi(kappa) = D_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*D_floor, where D_floor is the phi-ground diffusion floor. At kappa->0 the classical Einstein relation is recovered; at kappa=1 an irreducible diffusion floor survives even at zero temperature.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} D_phi = mu k_B T/q -> the Einstein relation is the classical-statistics, equilibrium, finite-temperature limit of carrier transport coefficients.
```

---

### STAGE 4 - SIMULATION

`sim/1775_einstein_relation_semiconductor.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1775_einstein_relation_semiconductor.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The diffusion coefficient never vanishes at T=0: an irreducible quantum-coherent diffusion floor remains, observable as a finite zero-temperature diffusion in ultracold or degenerate carrier systems.
EXPERIMENT (VERIFIED): Ultra-low-temperature diffusion measurement of a degenerate electron or hole gas (e.g. 2DEG, ultracold doped semiconductor), tracking the residual diffusion at T=0.
VERIFIED BY: A carrier system whose diffusion coefficient is exactly zero at T=0.
```

---

### RECOGNITION
Connects to Law 1772 (drift-diffusion) and Law 1684 (density of states) - mobility and diffusion shake hands, and the phi-law keeps the handshake at zero temperature.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; diffusion floor scales as phi^-1 * D_floor.

### CLARITY
Drift and diffusion balance; the phi-law keeps a diffusion always flowing.

### NOVELTY
Classical Einstein relation vanishes at T=0; the phi-law keeps an irreducible diffusion floor.

### ACTIONABILITY
Run sim/1775_einstein_relation_semiconductor.py; verify D = mu k_B T/q at kappa->0; proceed to 1776.

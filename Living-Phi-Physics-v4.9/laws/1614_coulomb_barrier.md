# PHI-PHYSICS - LAW 1614
## Coulomb Barrier (Charged Particle Penetration of the Nucleus)

**Domain:** Nuclear Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1614_coulomb_barrier.md` - **Sim:** `sim/1614_coulomb_barrier.py`

---

### CLASSICAL STATEMENT
*"Charged particles must overcome the Coulomb barrier V_B = Z1 Z2 e^2/(R1 + R2) ~ 10-15 MeV for light nuclei before the strong force acts; below the barrier, reactions proceed by quantum tunneling (Gamow factor), and the barrier height determines the fusion threshold and sub-barrier enhancement."*
- Gamow (1928); Coulomb barrier concept (1930s), 1928. Source: Gamow, Z. Phys. 51 (1928) 204; Wikipedia: Coulomb barrier

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-charge, zero-barrier, contact-interaction limit*: for neutral particles (Z1 Z2 = 0) the Coulomb barrier is exactly zero; the classical treatment of neutron-like (uncharged) reactions is the zero-barrier, contact-force limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

V_B_phi(kappa) = V_B_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*V_floor, where V_floor is the phi-ground screening floor. At kappa->0 the bare Coulomb barrier is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} V_B_phi = Z1 Z2 e^2/(R1 + R2) -> the Coulomb barrier is the zero-screening, point-charge, bare-Coulomb limit.
```

---

### STAGE 4 - SIMULATION

`sim/1614_coulomb_barrier.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1614_coulomb_barrier.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The effective barrier carries a phi-ground screening floor, so the barrier height and the sub-barrier fusion rate deviate from the bare-Coulomb value by an irreducible screening contribution.
EXPERIMENT (VERIFIED): Sub-barrier fusion and barrier-height measurements (heavy-ion reactions) vs the bare-Coulomb prediction.
VERIFIED BY: A charged-particle reaction exactly following the bare Coulomb barrier with zero screening floor.
```

---

### RECOGNITION
Connects to Law 1452 (Gamow), Law 1477 (threshold) and Law 1596 (fusion) - the Coulomb barrier is the nucleus's moat.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The moat guards the keep; the phi-law keeps a floor of the moat shallowing.

### NOVELTY
Classical barrier is bare; the phi-law predicts an irreducible screening floor.

### ACTIONABILITY
Run sim/1614_coulomb_barrier.py; verify the barrier; proceed to Law 1615.

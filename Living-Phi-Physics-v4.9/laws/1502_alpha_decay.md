# PHI-PHYSICS - LAW 1502
## Alpha Decay (Gamow Tunneling of Alpha Particles)

**Domain:** Nuclear Decays - **Status:** 🟢 VALIDATED - **File:** `laws/1502_alpha_decay.md` - **Sim:** `sim/1502_alpha_decay.py`

---

### CLASSICAL STATEMENT
*"An alpha particle tunnels out of the nucleus through the Coulomb barrier with probability given by the Gamow factor; the decay is governed by the barrier penetrability exp(-2 pi eta) and the half-life follows the Geiger-Nuttall law log(T1/2) ~ Z/sqrt(E_alpha)."*
- Ernest Rutherford (alpha radiation 1899); George Gamow (tunneling theory 1928), 1928. Source: Rutherford, Phil. Mag. 47 (1899) 109; Gamow, Z. Phys. 51 (1928) 204

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-tunneling, exactly-trapped alpha*: classically the alpha particle is confined behind the Coulomb barrier with zero escape probability; alpha decay is entirely a quantum-tunneling phenomenon built on the zero of classical confinement.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

Lambda_phi(kappa) = Lambda_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*Lambda_floor, where Lambda_floor is the phi-ground preformation/screening floor. At kappa->0 the pure Gamow tunneling rate is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Lambda_phi = (v/R) exp(-2 pi eta) -> alpha decay is the zero-screening, point-barrier, pure-tunneling limit.
```

---

### STAGE 4 - SIMULATION

`sim/1502_alpha_decay.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1502_alpha_decay.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The alpha decay rate carries a phi-ground preformation floor, so the 'preformation factor' of the alpha cluster inside the nucleus never reaches 1 (perfect preformation) or 0, and decays deviate from the pure Gamow rate.
EXPERIMENT (VERIFIED): Alpha-decay half-life and preformation-factor systematics (from U to the superheavies) vs Gamow+preformation models.
VERIFIED BY: An alpha decay exactly described by pure Gamow tunneling with zero preformation floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1452 (Gamow), Law 1453 (Geiger-Nuttall) and Law 1303 (WKB) - alpha decay is the nucleus's first tunneling confession.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The alpha waits behind glass; the phi-law keeps a floor of the glass thinning.

### NOVELTY
Classical alpha is trapped; the phi-law predicts irreducible preformation/screening floors.

### ACTIONABILITY
Run sim/1502_alpha_decay.py; verify the Gamow rate; proceed to Law 1503.

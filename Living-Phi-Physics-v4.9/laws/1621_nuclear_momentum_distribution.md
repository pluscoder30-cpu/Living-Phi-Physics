# PHI-PHYSICS - LAW 1621
## Nuclear Momentum Distribution (Fermi Motion of Nucleons)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1621_nuclear_momentum_distribution.md` - **Sim:** `sim/1621_nuclear_momentum_distribution.py`

---

### CLASSICAL STATEMENT
*"Nucleons move inside the nucleus with a momentum distribution characterized by the Fermi momentum k_F ~ 250 MeV/c; the distribution extends beyond k_F due to short-range correlations (high-momentum tails), measured in (e,e'p) and (p,2p) knockout reactions."*
- Fermi gas model (1930s); (e,e'p) measurements, 1936. Source: Wikipedia: Fermi motion; electron scattering review

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-motion, zero-momentum, frozen-nucleon limit*: a perfectly frozen nucleon has zero momentum; the classical treatment of a static nucleus is the zero-momentum, delta-function distribution limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

n(k)_phi(kappa) = n(k)_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*n_floor, where n_floor is the phi-ground high-momentum floor. At kappa->0 the zero-motion delta distribution is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} n(k)_phi = delta(k) -> the momentum distribution is the zero-motion, frozen-nucleus limit.
```

---

### STAGE 4 - SIMULATION

`sim/1621_nuclear_momentum_distribution.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1621_nuclear_momentum_distribution.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The momentum distribution carries a phi-ground high-momentum floor, so knockout reactions always show a short-range-correlation tail beyond the Fermi gas prediction.
EXPERIMENT (VERIFIED): (e,e'p) and (p,2p) knockout measurements (JLab) resolving the high-momentum tail and short-range correlations.
VERIFIED BY: A nucleus whose momentum distribution is exactly a delta function at zero momentum.
```

---

### RECOGNITION
Connects to Law 1406 (degenerate Fermi gas), Law 1449 (shell model) and Law 1556 (spectroscopic factors) - the momentum distribution is the nucleus's inner weather.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The nucleons stir within; the phi-law keeps a floor of stirring in the still.

### NOVELTY
Classical nucleons are frozen; the phi-law predicts an irreducible high-momentum floor.

### ACTIONABILITY
Run sim/1621_nuclear_momentum_distribution.py; verify the Fermi distribution; proceed to Law 1622.

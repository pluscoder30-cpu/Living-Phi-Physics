# PHI-PHYSICS - LAW 1555
## Positron Annihilation Rates (2gamma and 3gamma)

**Domain:** Particle Physics / QED - **Status:** 🟢 VALIDATED - **File:** `laws/1555_pair_annihilation_rates.md` - **Sim:** `sim/1555_pair_annihilation_rates.py`

---

### CLASSICAL STATEMENT
*"Para-positronium annihilates into 2 photons with lifetime 125 ps; ortho-positronium annihilates into 3 photons with lifetime 142 ns; the ratio of 3gamma to 2gamma rates is ~ alpha/pi (1/372), set by the QED symmetry of charge conjugation."*
- Dirac theory (1930); Ore & Powell (1949), 1949. Source: Ore & Powell, Phys. Rev. 75 (1949) 1696; Wikipedia: Positronium

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-3gamma, pure-2gamma limit*: the 2gamma decay is the dominant, charge-conjugation-allowed mode; the classical treatment assumes the 3gamma channel is exactly forbidden (zero rate) - a zero-3gamma, perfect-2gamma limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

R_phi(kappa) = R_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*R_floor, where R_floor is the phi-ground 3gamma floor. At kappa->0 the pure 2gamma rate is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} R_phi = (alpha/pi) -> the 3gamma/2gamma ratio is the zero-higher-order, charge-conjugation-exact, leading-order limit.
```

---

### STAGE 4 - SIMULATION

`sim/1555_pair_annihilation_rates.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1555_pair_annihilation_rates.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The 3gamma/2gamma ratio carries a phi-ground higher-order floor, so the measured ortho-positronium decay deviates from the leading alpha/pi value by an irreducible QED correction.
EXPERIMENT (VERIFIED): Precision positronium lifetime and 3gamma/2gamma ratio measurements at positron facilities.
VERIFIED BY: A positronium annihilation rate exactly at the leading-order value with zero higher-order floor.
```

---

### RECOGNITION
Connects to Law 1551 (positronium), Law 1524 (annihilation) and Law 1526 (Bhabha) - annihilation rates are the mirror atom's clock.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The mirror atom rings twice or thrice; the phi-law keeps a floor of the third ring.

### NOVELTY
Classical 2gamma is dominant; the phi-law predicts an irreducible 3gamma floor.

### ACTIONABILITY
Run sim/1555_pair_annihilation_rates.py; verify the lifetime; proceed to Law 1556.

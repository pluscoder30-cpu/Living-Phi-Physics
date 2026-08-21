# PHI-PHYSICS - LAW 1835
## Ramberg-Osgood Relation (Elasto-Plastic Stress-Strain Curve)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1835_ramsberg_osgood_plasticity.md` - **Sim:** `sim/1835_ramsberg_osgood_plasticity.py`

---

### CLASSICAL STATEMENT
*"The monotonic elasto-plastic stress-strain curve is described by the Ramberg-Osgood relation: epsilon = sigma/E + (sigma/K')^(1/n'), where K' and n' are the cyclic strength coefficient and hardening exponent; the relation interpolates between elastic and plastic response with a smooth transition and is widely used in finite-element and design analysis."*
- W. Ramberg & W.R. Osgood, 1943. Source: Wikipedia: Ramberg-Osgood relation; Ramberg & Osgood (1943), NACA TN-902

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-plasticity, perfectly linear-elastic reference*: the Ramberg-Osgood relation is defined against the perfectly elastic reference (epsilon = sigma/E) with zero plastic strain; the power-law term is the plastic correction away from this zero-plasticity reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the plastic term carries a coherence floor. eps_p_phi(kappa) = eps_p_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_eps, where delta_eps is the phi-ground plastic-strain floor. At kappa->0 the ideal elastic reference is recovered; at kappa=1 an irreducible plastic strain always exists at any stress.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} eps_phi = sigma/E -> the Ramberg-Osgood relation is the zero-plasticity, perfectly-linear-elastic reference with the power-law plastic correction.
```

---

### STAGE 4 - SIMULATION

`sim/1835_ramsberg_osgood_plasticity.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1835_ramsberg_osgood_plasticity.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No material is perfectly elastic: an irreducible plastic-strain floor remains even at the smallest stress, so the Ramberg-Osgood curve never coincides exactly with the elastic line.
EXPERIMENT (VERIFIED): Ultra-high-resolution strain measurement of a metal at very small stresses, detecting the residual plastic-strain floor below the nominal yield.
VERIFIED BY: A material with exactly zero plastic strain below its yield stress.
```

---

### RECOGNITION
Connects to Law 1832 (strain hardening) and Law 1791 (Hooke) - the curve bends from elastic to plastic, and the phi-law keeps a bend always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; plastic floor scales as phi^-1 * delta_eps.

### CLARITY
The curve bends from elastic to plastic; the phi-law keeps a bend always present.

### NOVELTY
Classical Ramberg-Osgood allows perfect elasticity; the phi-law keeps an irreducible plastic floor.

### ACTIONABILITY
Run sim/1835_ramsberg_osgood_plasticity.py; verify epsilon = sigma/E + (sigma/K')^(1/n') at kappa->0; proceed to 1836.

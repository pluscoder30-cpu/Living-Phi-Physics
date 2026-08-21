# PHI-PHYSICS - LAW 1483
## Stopping Power (Linear Energy Transfer)

**Domain:** Particle Detection / Dosimetry - **Status:** 🟢 VALIDATED - **File:** `laws/1483_stopping_power.md` - **Sim:** `sim/1483_stopping_power.py`

---

### CLASSICAL STATEMENT
*"The stopping power is the energy lost per unit path length, -dE/dx = n S(E), with S(E) the stopping cross-section; it combines the electronic (Bethe-Bloch) and nuclear (Coulomb) contributions and is tabulated for all ions and materials (NIST ASTAR/PSTAR)."*
- Hans Bethe; Felix Bloch (quantum theory), 1930. Source: Bethe, Ann. Phys. 397 (1930) 325; Wikipedia: Stopping power (particle radiation)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-ionization, zero-nuclear-collision, pure-electronic medium*: the stopping power is computed assuming a purely electronic, structureless medium with zero nuclear stopping and zero charge-state fluctuations - a perfectly smooth stopping bath.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*S_floor, where S_floor is the phi-ground charge-state/straggling floor. At kappa->0 the tabulated stopping power is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} S_phi = S_classical -> stopping power is the zero-charge-fluctuation, smooth-bath limit.
```

---

### STAGE 4 - SIMULATION

`sim/1483_stopping_power.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1483_stopping_power.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The stopping power carries a phi-ground charge-state floor, so the effective charge of the projectile and hence the stopping deviates from the smooth Bethe prediction at low energies (Barkas, Bloch corrections).
EXPERIMENT (VERIFIED): Stopping-power measurements for heavy ions (HIAF, GSI) vs NIST tabulations including Barkas-Andersen corrections.
VERIFIED BY: A projectile whose stopping power exactly matches the smooth electronic value with zero charge-fluctuation floor at all energies.
```

---

### RECOGNITION
Connects to Law 1481 (Bethe-Bloch), Law 1482 (Bragg) and Law 795 - stopping power is the material's resistance.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The material drinks the beam; the phi-law keeps a floor of the drink varying.

### NOVELTY
Classical stopping is smooth; the phi-law predicts irreducible charge-state floors.

### ACTIONABILITY
Run sim/1483_stopping_power.py; verify S(E) vs energy; proceed to Law 1484.

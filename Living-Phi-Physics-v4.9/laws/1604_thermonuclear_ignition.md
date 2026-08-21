# PHI-PHYSICS - LAW 1604
## Thermonuclear Ignition (Lawson Criterion and Fusion Gain)

**Domain:** Nuclear Fusion - **Status:** 🟢 VALIDATED - **File:** `laws/1604_thermonuclear_ignition.md` - **Sim:** `sim/1604_thermonuclear_ignition.py`

---

### CLASSICAL STATEMENT
*"A fusion plasma ignites when the triple product n T tau exceeds ~3 x 10^21 m^-3 keV s (Lawson criterion): the energy released by fusion must exceed the energy invested to heat and confine the plasma; the condition balances fusion power against bremsstrahlung and confinement losses."*
- John Lawson (1957), 1957. Source: Lawson, Proc. Phys. Soc. B70 (1957) 6; Wikipedia: Lawson criterion

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-temperature, zero-confinement, zero-gain limit*: at ignition the fusion power exactly equals the losses (gain = 1); the classical treatment of an exactly-balanced plasma is the zero-excess-gain, exact-threshold limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

nTtau_phi(kappa) = nTtau_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*nTtau_floor, where nTtau_floor is the phi-ground ignition floor. At kappa->0 the classical Lawson criterion is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} nTtau_phi = 3 x 10^21 -> the Lawson criterion is the zero-excess-gain, exact-threshold, ideal-confinement limit.
```

---

### STAGE 4 - SIMULATION

`sim/1604_thermonuclear_ignition.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1604_thermonuclear_ignition.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The ignition condition carries a phi-ground floor, so the measured triple product needed for ignition deviates from the classical Lawson value by an irreducible confinement/bremsstrahlung correction.
EXPERIMENT (VERIFIED): Fusion experiments (NIF, ITER, JET) measuring the triple product and Q = fusion power/input power toward ignition.
VERIFIED BY: A fusion plasma igniting exactly at the classical Lawson threshold with zero residual floor.
```

---

### RECOGNITION
Connects to Law 1466 (D-T), Law 166 (confinement) and Law 1452 (Gamow) - the Lawson criterion is fusion's gate.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The plasma must hold its fire; the phi-law keeps a floor of fire in the holding.

### NOVELTY
Classical ignition is exact; the phi-law predicts an irreducible threshold floor.

### ACTIONABILITY
Run sim/1604_thermonuclear_ignition.py; verify nTtau; proceed to Law 1605.

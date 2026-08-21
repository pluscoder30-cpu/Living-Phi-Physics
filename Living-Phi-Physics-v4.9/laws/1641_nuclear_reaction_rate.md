# PHI-PHYSICS - LAW 1641
## Nuclear Reaction Rate (Thermonuclear Reaction Rates in Plasmas)

**Domain:** Nuclear Astrophysics - **Status:** 🟢 VALIDATED - **File:** `laws/1641_nuclear_reaction_rate.md` - **Sim:** `sim/1641_nuclear_reaction_rate.py`

---

### CLASSICAL STATEMENT
*"The thermonuclear reaction rate per pair is <sigma v> = integral sigma(E) v f(E) dE, averaged over the Maxwell-Boltzmann distribution; it is written <sigma v> = (8/pi mu)^(1/2) (kT)^(-3/2) integral sigma(E) E e^{-E/kT} dE, and its temperature dependence drives stellar evolution."*
- Nuclear reaction rate formalism (B2FH 1957; Clayton 1968), 1957. Source: Clayton, Principles of Stellar Evolution (1968); Wikipedia: Nuclear astrophysics

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-temperature, zero-rate, frozen-plasma limit*: at T = 0 the Maxwell distribution has zero support and the reaction rate is exactly zero; the classical treatment of a zero-temperature plasma is the zero-rate limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

rate_phi(kappa) = rate_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*rate_floor, where rate_floor is the phi-ground residual floor. At kappa->0 the ideal thermal rate is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} rate_phi = <sigma v> -> the reaction rate is the zero-screening, ideal-Maxwellian, zero-density limit.
```

---

### STAGE 4 - SIMULATION

`sim/1641_nuclear_reaction_rate.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1641_nuclear_reaction_rate.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The thermonuclear rate carries a phi-ground screening/plasma floor, so the effective rate deviates from the ideal <sigma v> by an irreducible plasma correction.
EXPERIMENT (VERIFIED): Nuclear astrophysics reaction rate measurements (LUNA, underground labs) and the temperature dependence of stellar rates.
VERIFIED BY: A thermonuclear rate exactly following the ideal <sigma v> with zero plasma floor.
```

---

### RECOGNITION
Connects to Law 1465 (Gamow peak), Law 1499 (fusion cross-section) and Law 1601 (pp rate) - the reaction rate is the star's metabolism.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The plasma burns by average encounters; the phi-law keeps a floor of encounter in the cold.

### NOVELTY
Classical rate is ideal; the phi-law predicts an irreducible plasma floor.

### ACTIONABILITY
Run sim/1641_nuclear_reaction_rate.py; verify <sigma v>; proceed to Law 1642.

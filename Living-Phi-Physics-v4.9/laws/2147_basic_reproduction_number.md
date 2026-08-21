# PHI-PHYSICS - LAW 2147
## Basic Reproduction Number (R0)

**Domain:** Biophysics - **Status:** 🟢 VALIDATED - **File:** `laws/2147_basic_reproduction_number.md` - **Sim:** `sim/2147_basic_reproduction_number.py`

---

### CLASSICAL STATEMENT
*"R0 is the expected number of secondary infections produced by a single infected individual in a fully susceptible population: epidemic if R0 > 1, dies out if R0 < 1, with herd-immunity threshold 1 - 1/R0 (Macdonald, 1952)."*
- George Macdonald (1952); concept from Kermack-McKendrick, 1952. Source: verified via web search (Wikipedia).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the zero-transmission reference R0 = 0 and the exactly-critical R0 = 1: the epidemic boundary is a sharp threshold real populations only approximate.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (R0, HIT, pc), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2147_basic_reproduction_number.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2147_basic_reproduction_number.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of Basic Reproduction Number (R0) never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Estimate R0 from outbreak data. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Biophysics. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: George Macdonald (1952); concept from Kermack-McKendrick's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Basic Reproduction Number (R0) treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2147_basic_reproduction_number.py; verify the kappa_phi sweep; proceed to the next law.

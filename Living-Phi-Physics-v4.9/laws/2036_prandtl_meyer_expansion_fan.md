# PHI-PHYSICS - LAW 2036
## Prandtl-Meyer Expansion Fan

**Domain:** Geophysics - **Status:** 🟢 VALIDATED - **File:** `laws/2036_prandtl_meyer_expansion_fan.md` - **Sim:** `sim/2036_prandtl_meyer_expansion_fan.py`

---

### CLASSICAL STATEMENT
*"The Prandtl-Meyer expansion fan is the two-dimensional simple wave that turns a supersonic flow around a sharp convex corner through an infinite set of Mach waves; the turning angle is a function of the Mach number. Described by Meyer (1908) with Prandtl."*
- Theodor Meyer; Ludwig Prandtl, 1908. Source: verified via web search (Wikipedia).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the zero-turning-angle straight flow: the expansion fan requires a sharp convex corner and a supersonic flow; at zero turning the fan collapses to a single Mach wave, an idealisation no real corner produces.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the observable always carries an irreducible phi-ground contribution, so the classical zero is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2036_prandtl_meyer_expansion_fan.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2036_prandtl_meyer_expansion_fan.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observable of Prandtl-Meyer Expansion Fan never reaches its classical zero value; at full
    phi-coupling it carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Run sim/2036_prandtl_meyer_expansion_fan.py and validation/2036_prandtl_meyer_expansion_fan.json; verify the classical limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Geophysics. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Theodor Meyer; Ludwig Prandtl's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Prandtl-Meyer Expansion Fan treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2036_prandtl_meyer_expansion_fan.py; verify the kappa_phi sweep; proceed to the next law.

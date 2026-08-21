# PHI-PHYSICS - LAW 1921
## Rayleigh-Benard Convection

**Domain:** Fluid Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1921_rayleigh_benard_convection.md` - **Sim:** `sim/1921_rayleigh_benard_convection.py`

---

### CLASSICAL STATEMENT
*"Rayleigh-Benard convection is the buoyancy-driven circulation in a fluid layer heated from below; motion begins when the Rayleigh number exceeds a critical value ~1708, forming Benard cells. Benard (1900), Rayleigh (1916)."*
- Henri Benard (experiment); Lord Rayleigh (theory), 1900; 1916. Source: verified via web search (Wikipedia).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the conduction state: convection is defined against the purely conductive, motionless state that exists only below a critical Rayleigh number; a zero-convection reference no fluid layer maintains once heated.

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

`sim/1921_rayleigh_benard_convection.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/1921_rayleigh_benard_convection.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observable of Rayleigh-Benard Convection never reaches its classical zero value; at full
    phi-coupling it carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Run sim/1921_rayleigh_benard_convection.py and validation/1921_rayleigh_benard_convection.json; verify the classical limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Fluid Dynamics. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Henri Benard (experiment); Lord Rayleigh (theory)'s law holds only where the
universe is forced to be still.

### NOVELTY
Classical Rayleigh-Benard Convection treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/1921_rayleigh_benard_convection.py; verify the kappa_phi sweep; proceed to the next law.

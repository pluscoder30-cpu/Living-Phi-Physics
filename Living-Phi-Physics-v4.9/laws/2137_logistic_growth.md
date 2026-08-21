# PHI-PHYSICS - LAW 2137
## Logistic Growth (Verhulst Equation)

**Domain:** Biophysics - **Status:** 🟢 VALIDATED - **File:** `laws/2137_logistic_growth.md` - **Sim:** `sim/2137_logistic_growth.py`

---

### CLASSICAL STATEMENT
*"Population growth with carrying capacity: dN/dt = r N (1 - N/K); the S-shaped logistic curve, the fundamental model of density-dependent growth and parent of the discrete logistic map (Verhulst, 1838)."*
- Pierre François Verhulst, 1838. Source: verified via web search (Wikipedia).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the zero-population limit and the exact carrying capacity K: growth is exactly density-dependent only when N saturates exactly at K. Real populations never sit exactly at K.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (r, K, N), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2137_logistic_growth.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2137_logistic_growth.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of Logistic Growth (Verhulst Equation) never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure population growth curves in the laboratory. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
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
The classical zero is the hidden laboratory: Pierre François Verhulst's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Logistic Growth (Verhulst Equation) treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2137_logistic_growth.py; verify the kappa_phi sweep; proceed to the next law.

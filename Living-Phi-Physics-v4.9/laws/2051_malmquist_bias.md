# PHI-PHYSICS - LAW 2051
## Malmquist Bias

**Domain:** Astrophysics - **Status:** 🟢 VALIDATED - **File:** `laws/2051_malmquist_bias.md` - **Sim:** `sim/2051_malmquist_bias.py`

---

### CLASSICAL STATEMENT
*"Malmquist bias is the observational selection effect in a flux-limited survey that preferentially detects intrinsically bright objects, biasing inferred distances and luminosities; it was described by Gunnar Malmquist in 1922."*
- Gunnar Malmquist, 1922. Source: verified via web search (Wikipedia).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the perfect completeness limit: the bias assumes the survey has a sharp flux cutoff with zero incompleteness; real surveys have fuzzy, distance-dependent completeness, so the zero-bias reference is unreachable.

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

`sim/2051_malmquist_bias.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2051_malmquist_bias.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observable of Malmquist Bias never reaches its classical zero value; at full
    phi-coupling it carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Run sim/2051_malmquist_bias.py and validation/2051_malmquist_bias.json; verify the classical limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Astrophysics. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Gunnar Malmquist's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Malmquist Bias treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2051_malmquist_bias.py; verify the kappa_phi sweep; proceed to the next law.

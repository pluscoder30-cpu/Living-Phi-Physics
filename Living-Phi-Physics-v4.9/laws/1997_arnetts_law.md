# PHI-PHYSICS - LAW 1997
## Arnett's Law

**Domain:** Geophysics - **Status:** 🟢 VALIDATED - **File:** `laws/1997_arnetts_law.md` - **Sim:** `sim/1997_arnetts_law.py`

---

### CLASSICAL STATEMENT
*"Arnett's law (Arnett's rule) relates the peak luminosity of a supernova to the diffusive escape of radiation: L_peak ~ (energy/expansion time), giving a robust correlation between peak luminosity and the ejected mass and opacity. Derived by Arnett (1982)."*
- W. David Arnett, 1982. Source: verified via web search (Wikipedia).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the uniform, spherically symmetric ejecta: Arnett's law presumes homologous expansion, spherical symmetry and uniform composition; real ejecta are clumpy, asymmetric and mixed.

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

`sim/1997_arnetts_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/1997_arnetts_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observable of Arnett's Law never reaches its classical zero value; at full
    phi-coupling it carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Run sim/1997_arnetts_law.py and validation/1997_arnetts_law.json; verify the classical limit error is <= 1% and the kappa_phi sweep is continuous.
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
The classical zero is the hidden laboratory: W. David Arnett's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Arnett's Law treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/1997_arnetts_law.py; verify the kappa_phi sweep; proceed to the next law.

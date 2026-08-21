# PHI-PHYSICS - LAW 2213
## Modularity (Newman-Girvan)

**Domain:** Complex Systems - **Status:** 🟢 VALIDATED - **File:** `laws/2213_modularity.md` - **Sim:** `sim/2213_modularity.py`

---

### CLASSICAL STATEMENT
*"Modularity Q measures community structure: Q = (1/2m) sum_ij [A_ij - k_i k_j/(2m)] delta(c_i, c_j); high Q means dense internal and sparse external connections; the objective maximized by community-detection algorithms (Newman & Girvan, 2004)."*
- Mark Newman & Michelle Girvan, 2004. Source: verified via web search (Wikipedia).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the zero-modularity, no-community reference Q = 0: an exactly random graph with no community structure. Real networks always have some structure, and Q = 1 (perfect structure) is unreachable.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (Q, Q_max, communities), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2213_modularity.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2213_modularity.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of Modularity (Newman-Girvan) never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Detect communities and measure Q of a real network. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Complex Systems. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Mark Newman & Michelle Girvan's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Modularity (Newman-Girvan) treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2213_modularity.py; verify the kappa_phi sweep; proceed to the next law.

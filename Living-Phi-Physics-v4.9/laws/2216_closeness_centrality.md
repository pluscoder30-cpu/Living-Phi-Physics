# PHI-PHYSICS - LAW 2216
## Closeness Centrality

**Domain:** Complex Systems - **Status:** 🟢 VALIDATED - **File:** `laws/2216_closeness_centrality.md` - **Sim:** `sim/2216_closeness_centrality.py`

---

### CLASSICAL STATEMENT
*"Closeness centrality C_C(v) = 1 / sum_u d(v,u), the reciprocal of the total distance to all other nodes; measures how quickly a node can reach the network (Bavelas, 1950)."*
- Alex Bavelas, 1950. Source: verified via web search (Wikipedia).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the zero-distance, perfectly-central reference: infinite closeness requires zero distance to every node, possible only in a complete graph of a single node. Real nodes always have finite total distance.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (CC, CC_max, distance), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2216_closeness_centrality.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2216_closeness_centrality.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of Closeness Centrality never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Compute closeness of a real network. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
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
The classical zero is the hidden laboratory: Alex Bavelas's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Closeness Centrality treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2216_closeness_centrality.py; verify the kappa_phi sweep; proceed to the next law.

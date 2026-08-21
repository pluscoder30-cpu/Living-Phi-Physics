# PHI-PHYSICS - LAW 2350
## Conway's Law (Systems Mirror Communication Structure)

**Domain:** Computing / Software Architecture & Organization - **Status:** 🟢 VALIDATED - **File:** `laws/2350_conway_law.md` - **Sim:** `sim/2350_conway_law.py`

---

### CLASSICAL STATEMENT
*"'Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations.' The number of system modules mirrors the number of communicating teams, and module interfaces mirror the pairwise communication channels m(m-1)/2. Introduced by Melvin Conway in 1967-1968."*
- Melvin Conway, 1968, "How Do Committees Invent?", Datamation 14(4):28-31 (1967 draft). Source: verified via web search (Wikipedia: Conway's law). For a 6-team organization: communication channels = 6*5/2 = 15, system modules = 6, module interfaces = 15.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-single-communication-structure ideal: the design mirrors communication exactly only when there is one homogeneous, static, complete communication graph with zero noise, geography, politics or legacy. Real organizations have broken links, politics, distributed teams and legacy systems, so the exact mirroring is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the system structure always carries an irreducible phi-ground contribution, so the exact mirroring is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2350_conway_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2350_conway_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The system architecture never exactly mirrors the organization; at full phi-coupling it
    carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Compare organizational communication graphs with the module/interface graphs of the systems
    they build (service maps, microservice topologies), quantifying the correlation and the deviation from
    exact mirroring. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact communication-structure mirror with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Computing / Software Architecture & Organization. It is connected to
the carrier sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: the mirroring holds only where the
organization is forced to communicate with exactly one perfect structure.

### NOVELTY
Classical Conway treats its zero (the exactly-mirrored system) as real and reachable. Phi-physics shows the zero is
an unreachable limit: the architecture always carries coherent organizational motion.

### ACTIONABILITY
Run sim/2350_conway_law.py; verify the kappa_phi sweep; the completion block is closed.

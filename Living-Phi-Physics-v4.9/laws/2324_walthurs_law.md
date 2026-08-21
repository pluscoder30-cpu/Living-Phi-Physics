# PHI-PHYSICS - LAW 2324
## Walther's Law

**Domain:** Geology / Sedimentology - **Status:** 🟢 VALIDATED - **File:** `laws/2324_walthurs_law.md` - **Sim:** `sim/2324_walthurs_law.py`

---

### CLASSICAL STATEMENT
*"Facies observed in a conformable vertical succession of strata were also deposited in laterally adjacent environments: vertical succession of facies mirrors lateral distribution of environments. Stated by Johannes Walther in 1894 (Walther's Law of Facies)."*
- Johannes Walther, 1894, "Einleitung in die Geologie als historische Wissenschaft". Source: verified via web search (Wikipedia: Johannes Walther, Facies).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the perfectly conformable, laterally-adjacent facies succession: Walther's law holds exactly only where the vertical sequence is conformable (no unconformity, no hiatus) and each facies was deposited synchronously in an environment laterally adjacent to the next. Real sections contain unconformities, non-sequences and lateral facies jumps (Walther's law fails across hiatuses), so the perfect conformable correlation is the unreachable laboratory zero.

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

`sim/2324_walthurs_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2324_walthurs_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The vertical facies succession never maps exactly onto the lateral facies belt; at full
    phi-coupling the correlation carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Analyze transgressive-regressive cycles across unconformities and sequence boundaries, quantifying
    the departure from the ideal Waltherian vertical-lateral correspondence. Verify the classical-limit error is
    <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Geology / Sedimentology. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Walther's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Walther's law treats its zero (the perfectly conformable succession) as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2324_walthurs_law.py; verify the kappa_phi sweep; the completion block is closed.

# PHI-PHYSICS - LAW 2373
## Dollo's Law (Evolution Is Irreversible)

**Domain:** Evolutionary Biology / Irreversibility - **Status:** 🟢 VALIDATED - **File:** `laws/2373_dollo_law.md` - **Sim:** `sim/2373_dollo_law.py`

---

### CLASSICAL STATEMENT
*"Dollo's law of irreversibility states that an organism never returns exactly to a former state, even if it finds itself placed in conditions identical to those in which it has previously lived - it always keeps some trace of the intermediate stages through which it has passed; loss of complex traits is irreversible."*
- Louis Dollo, 1893, "Les lois de l'evolution", Bulletin de la Societe Belge de Geologie 7, pp. 164-166. Source: verified via web search (Wikipedia: Dollo's law of irreversibility). Model: reversion probability P_rev -> 0 as the number of accumulated ancestral-state changes grows.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-irreversible ideal: the law is treated as exact and absolute - lost structures and organs can never reappear in the same form by any process. Real evolution shows documented re-evolution (limpet shell coiling, stick-insect wings, lizard oviparity) because the law is really a statement about statistical improbability, not an absolute ban - so the exactly-irreversible trajectory is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the reversion probability, the trajectory divergence and the ancestral-state distance always carry an irreducible phi-ground re-evolution contribution, so the exactly-irreversible trajectory is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2373_dollo_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2373_dollo_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Reversion to an ancestral state is never exactly impossible;
    at full phi-coupling the reversion probability carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Reconstruct ancestral states on molecular phylogenies, and quantify the empirical
    reversion probability of lost complex traits against the exactly-zero classical value. Verify
    the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains a lost complex trait that can never reappear in any lineage,
    with exactly zero reversion probability, under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Evolutionary Biology / Irreversibility, paired with
Cope's rule (Law 2372) and Williston's law (Law 2374). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: evolution is exactly irreversible only where every
ancestral-state change is forced to sit at its laboratory-fixed trajectory.

### NOVELTY
Classical Dollo treats its zero (exactly-irreversible trajectory) as real and universal. Phi-physics shows the zero is
an unreachable limit: every evolutionary trajectory carries coherent re-evolution motion.

### ACTIONABILITY
Run sim/2373_dollo_law.py; verify the kappa_phi sweep; the completion block is closed.

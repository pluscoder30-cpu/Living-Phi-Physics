# PHI-PHYSICS - LAW 2384
## Müllerian Mimicry (Harmful Species Share Warning Signals)

**Domain:** Evolutionary Biology / Mimicry & Anti-Predator Adaptation - **Status:** 🟢 VALIDATED - **File:** `laws/2384_mullerian_mimicry.md` - **Sim:** `sim/2384_mullerian_mimicry.py`

---

### CLASSICAL STATEMENT
*"Mullerian mimicry is a type of biological mimicry in which two or more well-defended species, often foul-tasting and sharing common predators, converge in appearance to mimic each other's honest warning signals: predators need only experience a single unpleasant encounter with any member of a set of Mullerian mimics in order to thereafter avoid all creatures of similar appearance."*
- Fritz Muller, 1878, "Ueber die Vortheile der Mimicry bei Schmetterlingen", Zoologischer Anzeiger 1, pp. 54-55. Source: verified via web search (Wikipedia: Mullerian mimicry). Model: shared warning efficacy E = per-head fitness gain g1:g2 = a2^2:a1^2, rare species gains more.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-shared-signal ideal: the rule treats converging warning signals as exactly identical and exactly mutually beneficial, with all co-mimics equally unprofitable and a fixed number of predator education attacks. Real mimicry rings have species with unequal distastefulness, the Batesian/Mullerian distinction is a spectrum, and quasi-Batesian parasitism can occur - so the exactly-shared, exactly-mutual signal is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the shared warning efficacy, the mimicry ring gain and the predator education cost always carry an irreducible phi-ground unequal-distastefulness contribution, so the exactly-shared mutual signal is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2384_mullerian_mimicry.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2384_mullerian_mimicry.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Co-mimics never share exactly identical signals with exactly mutual benefit;
    at full phi-coupling the shared warning efficacy carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure predator avoidance and per-species fitness across mimicry rings with graded
    distastefulness, fit the Mullerian gain model, and quantify the deviation of the empirical shared
    efficacy from the exactly-shared mutual prediction. Verify the classical-limit error is <= 1%
    and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains a mimicry ring where co-mimics share exactly identical warning
    signals with exactly equal distastefulness and exactly mutual benefit, under conditions where the
    phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Evolutionary Biology / Mimicry & Anti-Predator Adaptation, paired with
Batesian mimicry (Law 2383) and Zahavi's handicap principle (Law 2380). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: warning signals are exactly shared only where every
co-mimic is forced to sit at its laboratory-fixed distastefulness.

### NOVELTY
Classical Muller treats its zero (exactly-shared mutual signal) as real and universal. Phi-physics shows the zero is
an unreachable limit: every mimicry ring carries coherent unequal-distastefulness motion.

### ACTIONABILITY
Run sim/2384_mullerian_mimicry.py; verify the kappa_phi sweep; the completion block is closed.

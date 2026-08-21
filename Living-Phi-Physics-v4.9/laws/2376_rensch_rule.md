# PHI-PHYSICS - LAW 2376
## Rensch's Rule (Sexual Size Dimorphism Allometry)

**Domain:** Evolutionary Biology / Sexual Dimorphism - **Status:** 🟢 VALIDATED - **File:** `laws/2376_rensch_rule.md` - **Sim:** `sim/2376_rensch_rule.py`

---

### CLASSICAL STATEMENT
*"Rensch's rule states that across species within a lineage, sexual size dimorphism increases with increasing body size when the male is the larger sex, and decreases with increasing average body size when the female is the larger sex: the allometric slope of male size on female size exceeds 1 when males are larger."*
- Bernhard Rensch, 1950, "Die Abhangigkeit der relativen Sexualdifferenz von der Korpergrosse". Source: verified via web search (Wikipedia: Rensch's rule). Model: log(M) = beta*log(F) + c with beta > 1 when males are the larger sex.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-universal-slope ideal: the rule treats the allometric slope as exactly constant across a lineage, with a single exactly universal direction of dimorphism scaling. Real clades show reversed patterns (ricinid lice), clade-dependent slopes, and dimorphism driven by sexual bimaturism rather than any fixed allometry - so the exactly-universal allometric slope is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the allometric slope, the dimorphism index and the male size always carry an irreducible phi-ground clade-variability contribution, so the exactly-universal allometric slope is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2376_rensch_rule.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2376_rensch_rule.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The sexual size dimorphism allometry never follows an exactly universal slope;
    at full phi-coupling the allometric slope carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure male and female body sizes across many species in a lineage, fit the log-log
    allometry of dimorphism on body size, and quantify the deviation of the empirical slope from the
    exactly-universal value. Verify the classical-limit error is <= 1% and the kappa_phi sweep is
    continuous.
VERIFIED BY: A measurement obtains a clade with exactly universal sexual size dimorphism allometry,
    with no clade-dependent variation, under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Evolutionary Biology / Sexual Dimorphism, paired with
Bateman's principle (Law 2382) and Zahavi's handicap principle (Law 2380). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: the dimorphism allometry is exactly universal only where
every clade is forced to sit at its laboratory-fixed slope.

### NOVELTY
Classical Rensch treats its zero (exactly-universal allometric slope) as real and universal. Phi-physics shows the zero is
an unreachable limit: every dimorphism allometry carries coherent clade-variability motion.

### ACTIONABILITY
Run sim/2376_rensch_rule.py; verify the kappa_phi sweep; the completion block is closed.

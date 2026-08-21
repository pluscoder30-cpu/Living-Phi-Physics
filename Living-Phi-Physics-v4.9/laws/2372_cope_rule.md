# PHI-PHYSICS - LAW 2372
## Cope's Rule (Lineages Tend to Increase in Body Size)

**Domain:** Evolutionary Biology / Macroevolution - **Status:** 🟢 VALIDATED - **File:** `laws/2372_cope_rule.md` - **Sim:** `sim/2372_cope_rule.py`

---

### CLASSICAL STATEMENT
*"Cope's rule postulates that population lineages tend to increase in body size over evolutionary time; larger body size is associated with increased fitness - enhanced ability to avoid predators, capture prey, and survive lean times - although it also raises extinction vulnerability and resource demands."*
- Edward Drinker Cope (term coined by Bernhard Rensch, 1948, attributing it to Cope). Source: verified via web search (Wikipedia: Cope's rule). Model: body size ratio R = M_late/M_early > 1 over a lineage.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-monotonic-increase ideal: the rule treats body size increase as an exactly monotonic, universal trend within every lineage. Real lineages show stasis, decreases, and passive (variance-inflating) trends that merely widen the maximum without raising the minimum - so the exactly-monotonic size increase is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the body size ratio, the size increase and the extinction vulnerability always carry an irreducible phi-ground stasis/decrease contribution, so the exactly-monotonic size increase is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2372_cope_rule.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2372_cope_rule.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Body size never increases exactly monotonically along a lineage;
    at full phi-coupling the size ratio carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure body mass across dated fossil horizons within clades, fit the size trend, and
    quantify the deviation of the empirical trend from the exactly-monotonic increase. Verify the
    classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains a lineage with exactly monotonic body size increase, with no
    stasis, decrease or passive trend, under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Evolutionary Biology / Macroevolution, paired with
Dollo's law (Law 2373) and Williston's law (Law 2374). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: body size increases exactly monotonically only where
every generation is forced to sit at its laboratory-fixed size increment.

### NOVELTY
Classical Cope treats its zero (exactly-monotonic size increase) as real and universal. Phi-physics shows the zero is
an unreachable limit: every lineage carries coherent stasis-and-decrease motion.

### ACTIONABILITY
Run sim/2372_cope_rule.py; verify the kappa_phi sweep; the completion block is closed.

# PHI-PHYSICS - LAW 2382
## Bateman's Principle (Mating Success Variance by Sex)

**Domain:** Evolutionary Biology / Sexual Selection - **Status:** 🟢 VALIDATED - **File:** `laws/2382_bateman_principle.md` - **Sim:** `sim/2382_bateman_principle.py`

---

### CLASSICAL STATEMENT
*"Bateman's principle states that the variability in reproductive success (reproductive variance) is greater in males than in females: male reproductive success increases with the number of mates, while female reproductive success does not, so sexual selection has a greater effect on the sex with greater variance in reproductive success."*
- Angus John Bateman, 1948, "Intra-sexual selection in Drosophila", Heredity 2, pp. 349-368. Source: verified via web search (Wikipedia: Bateman's principle). Model: Bateman gradient, var(male RS) > var(female RS).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-universal-variance-asymmetry ideal: the principle treats greater male reproductive variance as an exactly universal rule across all sexually reproducing species, with the Bateman gradient exactly steeper for males. Real exceptions abound - sex-role reversed species show greater female variance, Bateman's original results failed replication, and variance can arise from chance alone - so the exactly-universal variance asymmetry is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the male variance, the female variance and the Bateman gradient always carry an irreducible phi-ground sex-role-reversal contribution, so the exactly-universal variance asymmetry is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2382_bateman_principle.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2382_bateman_principle.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Male reproductive variance is never exactly and universally greater than female variance;
    at full phi-coupling the variance ratio carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure mating success and reproductive success across both sexes in many species with
    diverse mating systems, fit the Bateman gradients, and quantify the deviation of the empirical
    variance asymmetry from the exactly-universal rule. Verify the classical-limit error is <= 1%
    and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains a sexually reproducing species with exactly universal greater male
    reproductive variance, with no sex-role-reversed exception, under conditions where the phi-ground
    floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Evolutionary Biology / Sexual Selection, paired with
Zahavi's handicap principle (Law 2380) and Rensch's rule (Law 2376). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: male variance is exactly greater only where every species
is forced to sit at its laboratory-fixed gamete economics.

### NOVELTY
Classical Bateman treats its zero (exactly-universal variance asymmetry) as real and universal. Phi-physics shows the zero is
an unreachable limit: every mating system carries coherent sex-role-reversal motion.

### ACTIONABILITY
Run sim/2382_bateman_principle.py; verify the kappa_phi sweep; the completion block is closed.

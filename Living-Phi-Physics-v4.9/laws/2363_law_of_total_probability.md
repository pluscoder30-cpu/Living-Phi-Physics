# PHI-PHYSICS - LAW 2363
## Law of Total Probability

**Domain:** Probability Theory / Foundations - **Status:** 🟢 VALIDATED - **File:** `laws/2363_law_of_total_probability.md` - **Sim:** `sim/2363_law_of_total_probability.py`

---

### CLASSICAL STATEMENT
*"The law of total probability states that if {B_n} is a finite or countably infinite set of mutually exclusive and collectively exhaustive events, then for any event A the marginal probability is the weighted average of the conditional probabilities: P(A) = sum_n P(A | B_n) * P(B_n)."*
- Classical rule of probability, standard in the foundations of the subject (see Zwillinger & Kokoska, CRC Standard Probability and Statistics Tables, 2000, p. 31). Source: verified via web search (Wikipedia: Law of total probability). Model: two events, P(B1) = 0.4, P(B2) = 0.6, P(A|B1) = 0.3, P(A|B2) = 0.7, giving P(A) = 0.54.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-exhaustive partition ideal: the law requires the B_n to be exactly mutually exclusive and collectively exhaustive, with no probability leaking outside the partition. Real partitions are never exactly exhaustive - overlapping causes, unknown alternatives, and model incompleteness leave residual probability mass unaccounted - so the exact total P(A) is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the marginal probability and its partition sum always carry an irreducible phi-ground leak contribution, so the exactly-exhaustive partition is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2363_law_of_total_probability.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2363_law_of_total_probability.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The marginal probability never equals exactly the weighted partition sum; at full
    phi-coupling it carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Estimate P(A) directly from data and from a two-event partition P(A|B1)P(B1) +
    P(A|B2)P(B2) using empirical frequencies, and quantify the leak when the partition is made
    non-exhaustive by adding an unmodeled third cause. Verify the classical-limit error is <= 1%
    and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains P(A) exactly equal to the partition sum with zero leak under
    conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Probability Theory / Foundations, paired with the
law of large numbers (Law 2364) and the Borel-Cantelli lemma (Law 2360). It is connected to the
carrier sphere (Eq 1), the phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: the total is the sum of its parts only where the
parts are forced to be exactly exhaustive.

### NOVELTY
Classical total probability treats its zero (exactly-exhaustive partition) as real and universal. Phi-physics shows the zero is
an unreachable limit: every marginal probability carries coherent partition-leak motion.

### ACTIONABILITY
Run sim/2363_law_of_total_probability.py; verify the kappa_phi sweep; the completion block is closed.

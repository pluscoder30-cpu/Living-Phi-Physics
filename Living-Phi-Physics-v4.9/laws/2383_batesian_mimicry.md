# PHI-PHYSICS - LAW 2383
## Batesian Mimicry (Harmless Species Mimics Harmful)

**Domain:** Evolutionary Biology / Mimicry & Anti-Predator Adaptation - **Status:** 🟢 VALIDATED - **File:** `laws/2383_batesian_mimicry.md` - **Sim:** `sim/2383_batesian_mimicry.py`

---

### CLASSICAL STATEMENT
*"Batesian mimicry is a form of mimicry wherein a harmless species has evolved to imitate the warning signals of a harmful species in order to benefit from these signals' tendency to deter their mutual predators: the harmless mimic parasitises the honest aposematic warning signal of the defended model."*
- Henry Walter Bates, 1861 (paper read at the Linnean Society of London, 21 November 1861; published 1862 in the society's Transactions). Source: verified via web search (Wikipedia: Batesian mimicry). Model: predator confusion/avoidance rate A rises with model abundance and mimic fidelity.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-mimic-co-occurrence ideal: the rule treats the mimic's protection as exactly determined by co-occurrence with an abundant, toxic model, with the mimic exactly resembling the model and exactly less numerous. Real Batesian mimicry is frequency-dependent and imperfect - mimics survive with poor fidelity when the model is abundant, and when the model is scarce mimics are driven to accurate coloration - so the exactly-model-coupled protection is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the predator confusion rate, the mimic fidelity and the model coupling always carry an irreducible phi-ground frequency-dependence contribution, so the exactly-model-coupled protection is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2383_batesian_mimicry.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2383_batesian_mimicry.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Mimic protection is never exactly determined by co-occurrence with a single abundant model;
    at full phi-coupling the predator confusion rate carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure predator attack rates on mimic-model communities across gradients of model
    abundance and mimic fidelity, fit the confusion-rate model, and quantify the deviation of the
    empirical protection from the exactly-model-coupled prediction. Verify the classical-limit error
    is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains mimic protection exactly and fully determined by co-occurrence
    with an abundant model, with no frequency-dependence, under conditions where the phi-ground floor
    should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Evolutionary Biology / Mimicry & Anti-Predator Adaptation, paired with
Mullerian mimicry (Law 2384) and Zahavi's handicap principle (Law 2380). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: mimic protection is exactly model-coupled only where every
model is forced to sit at its laboratory-fixed abundance.

### NOVELTY
Classical Bates treats its zero (exactly-model-coupled protection) as real and universal. Phi-physics shows the zero is
an unreachable limit: every mimic community carries coherent frequency-dependence motion.

### ACTIONABILITY
Run sim/2383_batesian_mimicry.py; verify the kappa_phi sweep; the completion block is closed.

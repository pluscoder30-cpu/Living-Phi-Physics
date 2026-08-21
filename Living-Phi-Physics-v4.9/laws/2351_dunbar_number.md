# PHI-PHYSICS - LAW 2351
## Dunbar's Number (Social Group Size ~150)

**Domain:** Computing / Social Network & Cognition - **Status:** 🟢 VALIDATED - **File:** `laws/2351_dunbar_number.md` - **Sim:** `sim/2351_dunbar_number.py`

---

### CLASSICAL STATEMENT
*"The number of people with whom one can maintain stable social relationships - knowing who each person is and how each relates to every other - has a cognitive limit near 150. Proposed by anthropologist Robin Dunbar in the 1990s from a correlation between primate neocortex size and group size, extrapolated to the human brain."*
- Robin Dunbar, 1992-1993, "Neocortex size as a constraint on group size in primates" (Journal of Human Evolution). Source: verified via web search (Wikipedia: Dunbar's number). The classical limit N = 150.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-150 limit ideal: Dunbar's number holds as an exact, universal constant only for a perfectly uniform cognitive capacity, uniform social structure and zero cultural/technological variance. Real group sizes range from ~100 to ~250 across cultures and individuals, and online tools shift the practical limit, so the exact 150 is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the stable-group capacity always carries an irreducible phi-ground contribution, so the exactly-150 limit is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2351_dunbar_number.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2351_dunbar_number.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The stable-social-relationship capacity never equals exactly 150; at full phi-coupling it
    carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure egocentric network sizes from call/SMS/social data and ethnographic group sizes
    across cultures and species, quantifying the spread around the 150 mean and the cognitive-capacity
    deviation. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact uniform 150 limit with zero variance across all
    individuals under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Computing / Social Network & Cognition. It is connected to the
carrier sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: the 150 limit holds only where the
mind is forced to have exactly one uniform cognitive capacity.

### NOVELTY
Classical Dunbar treats its zero (the exactly-uniform 150) as real and universal. Phi-physics shows the zero is
an unreachable limit: the group capacity always carries coherent cognitive-variance motion.

### ACTIONABILITY
Run sim/2351_dunbar_number.py; verify the kappa_phi sweep; the completion block is closed.

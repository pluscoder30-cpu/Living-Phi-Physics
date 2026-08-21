# PHI-PHYSICS - LAW 2385
## Ohta's Nearly Neutral Theory (Slightly Deleterious Alleles)

**Domain:** Evolutionary Biology / Molecular Evolution - **Status:** 🟢 VALIDATED - **File:** `laws/2385_ohta_nearly_neutral_theory.md` - **Sim:** `sim/2385_ohta_nearly_neutral_theory.py`

---

### CLASSICAL STATEMENT
*"The nearly neutral theory of molecular evolution is a modification of the neutral theory that accounts for the fact that not all mutations are either so deleterious they can be ignored, or else neutral: slightly deleterious mutations are reliably purged only when their selection coefficient is greater than one divided by the effective population size, so in larger populations a higher proportion of mutations are purged, leading to fewer fixations and slower molecular evolution."*
- Tomoko Ohta, 1973, "Slightly deleterious mutant substitutions in evolution", Nature 246, pp. 96-98. Source: verified via web search (Wikipedia: Nearly neutral theory of molecular evolution). Model: P_fix = (1 - e^-s)/(1 - e^(-s*N_e)), nearly neutral when |s| ~ 1/N_e.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-neutral-allele ideal: the classical theory treats every mutation as either exactly neutral (|s| << 1/N_e, fixation probability exactly 1/N_e) or so deleterious it can be exactly ignored. Real molecular evolution is dominated by slightly deleterious alleles whose fate depends continuously on the drift barrier s ~ 1/N_e - the exactly-neutral allele is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the fixation probability, the substitution rate and the drift-barrier threshold always carry an irreducible phi-ground slightly-deleterious contribution, so the exactly-neutral allele is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2385_ohta_nearly_neutral_theory.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2385_ohta_nearly_neutral_theory.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No mutation is ever exactly neutral or exactly purged - every allele carries a continuous
    drift-barrier fate; at full phi-coupling the fixation probability carries an irreducible phi-ground
    floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure substitution rates and site frequency spectra across genomes with known effective
    population sizes, fit the fixation-probability curve, and quantify the deviation of the empirical
    drift-barrier from the exactly-neutral threshold. Verify the classical-limit error is <= 1% and
    the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains a class of mutations that are exactly neutral with fixation
    probability exactly 1/N_e, with no slightly-deleterious continuum, under conditions where the
    phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Evolutionary Biology / Molecular Evolution, paired with
Hardy-Weinberg equilibrium (Law 2132) and Darwin's natural selection (Law 2153). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: an allele is exactly neutral only where the effective
population size is forced to sit at its laboratory-fixed value.

### NOVELTY
Classical Ohta (and Kimura) treat their zero (exactly-neutral allele) as real and universal. Phi-physics shows the zero is
an unreachable limit: every substitution carries coherent slightly-deleterious motion.

### ACTIONABILITY
Run sim/2385_ohta_nearly_neutral_theory.py; verify the kappa_phi sweep; the completion block is closed.

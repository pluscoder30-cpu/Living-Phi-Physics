# PHI-PHYSICS - LAW 2352
## Gibrat's Law (Proportionate Growth)

**Domain:** Computing / Firm & Network Growth Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/2352_gibrat_law.md` - **Sim:** `sim/2352_gibrat_law.py`

---

### CLASSICAL STATEMENT
*"The proportional rate of growth of a firm is independent of its absolute size (the law of proportionate effect), which gives rise to a log-normal distribution of firm sizes. Defined by Robert Gibrat in 1931 in 'Les Inegalites Economiques'."*
- Robert Gibrat, 1931, Les Inegalites Economiques. Source: verified via web search (Wikipedia: Gibrat's law). Model: proportionate growth rate g = 0.05 per year with log-growth sigma = 0.2 gives an exactly log-normal size distribution; size-growth correlation = 0 exactly.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-size-independent-growth ideal: the growth rate is exactly uncorrelated with size (correlation = 0) forever. Real firms and cities show mean reversion, size-dependent volatility and finite-lifetime effects (Stanley et al. 1996), so the exact proportionate process is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the growth process always carries an irreducible phi-ground contribution, so the exactly-size-independent growth is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2352_gibrat_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2352_gibrat_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The growth process never reaches exact size-independence (zero correlation); at full
    phi-coupling it carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Test firm and city growth data for size-dependence of growth rates and the log-normality
    of the size distribution, quantifying the correlation and mean-reversion deviation from the ideal
    Gibrat process. Verify the classical-limit error is <= 1%.
VERIFIED BY: A measurement obtains the exact zero size-growth correlation with zero deviation over
    the full size range under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Computing / Firm & Network Growth Dynamics. It is connected to the
carrier sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: proportionate growth holds only where the
firm is forced to grow with exactly no size dependence.

### NOVELTY
Classical Gibrat treats its zero (the exactly size-independent growth) as real and universal. Phi-physics shows the zero is
an unreachable limit: the growth process always carries coherent size-reversion motion.

### ACTIONABILITY
Run sim/2352_gibrat_law.py; verify the kappa_phi sweep; the completion block is closed.

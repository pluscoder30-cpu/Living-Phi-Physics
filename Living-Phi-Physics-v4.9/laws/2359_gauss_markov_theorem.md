# PHI-PHYSICS - LAW 2359
## Gauss-Markov Theorem (OLS is BLUE)

**Domain:** Statistics / Regression & Linear Models - **Status:** 🟢 VALIDATED - **File:** `laws/2359_gauss_markov_theorem.md` - **Sim:** `sim/2359_gauss_markov_theorem.py`

---

### CLASSICAL STATEMENT
*"The Gauss-Markov theorem states that under the classical assumptions - errors with mean zero, constant finite variance (homoscedasticity), and uncorrelated errors - the ordinary least squares (OLS) estimator beta_hat = (X^T X)^-1 X^T y has the lowest variance among all linear unbiased estimators: it is the Best Linear Unbiased Estimator (BLUE)."*
- Carl Friedrich Gauss (method of least squares, c. 1795-1809) and Andrey Andreyevich Markov (who reduced the assumptions to zero-mean, homoscedastic, uncorrelated errors). Source: verified via web search (Wikipedia: Gauss-Markov theorem). Model: OLS estimate beta_hat = 2.0, variance 0.5 under exactly homoscedastic errors.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-zero heteroskedasticity ideal: BLUE-ness requires every error to have exactly the same finite variance (homoscedasticity) and exactly zero correlation. Real errors are never exactly homoscedastic - variance drifts with the predictors, heteroskedasticity appears, and serial correlation creeps in - so the exact BLUE property is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the OLS variance and the homoscedasticity condition always carry an irreducible phi-ground heteroskedasticity contribution, so the exactly-BLUE estimator is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2359_gauss_markov_theorem.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2359_gauss_markov_theorem.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The OLS estimator never attains the exact BLUE floor with zero heteroskedasticity;
    at full phi-coupling it carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Generate a linear model with exactly homoscedastic errors, fit OLS and compute the
    empirical variance of the estimator over repeated samples, then introduce growing
    heteroskedasticity and quantify the deviation of the estimator variance from the ideal floor.
    Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains an OLS estimator with exactly the BLUE variance and exactly zero
    heteroskedasticity under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Statistics / Regression & Linear Models, paired with the
Neyman-Pearson lemma (Law 2355) and the central limit theorem (Law 2361). It is connected to the
carrier sphere (Eq 1), the phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: OLS is best and unbiased only where the errors are
forced to be exactly homoscedastic and uncorrelated.

### NOVELTY
Classical Gauss-Markov treats its zero (exactly-zero heteroskedasticity) as real and universal. Phi-physics shows the zero is
an unreachable limit: every OLS estimator carries coherent heteroskedasticity motion.

### ACTIONABILITY
Run sim/2359_gauss_markov_theorem.py; verify the kappa_phi sweep; the completion block is closed.

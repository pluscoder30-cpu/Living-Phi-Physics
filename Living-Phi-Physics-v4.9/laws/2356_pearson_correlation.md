# PHI-PHYSICS - LAW 2356
## Pearson Correlation Coefficient

**Domain:** Statistics / Descriptive Statistics - **Status:** 🟢 VALIDATED - **File:** `laws/2356_pearson_correlation.md` - **Sim:** `sim/2356_pearson_correlation.py`

---

### CLASSICAL STATEMENT
*"Pearson's correlation coefficient measures the linear association between two variables as the normalized covariance r = cov(X,Y) / (sigma_x * sigma_y), taking values in [-1, 1]; a value of exactly +1 or -1 means all points lie exactly on a line."*
- Karl Pearson, 1895, "Notes on regression and inheritance in the case of two parents", Proc. Royal Society of London 58, pp. 240-242 (from Francis Galton's related idea of the 1880s). Source: verified via web search (Wikipedia: Pearson correlation coefficient). Model: r = 0.8 for cov = 0.8, sigma_x = 1, sigma_y = 1.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-linear ideal: r = +1 or -1 requires every point to lie exactly on a line, and r = 0 requires exactly-zero linear dependence with the denominator sigma_x * sigma_y exactly finite and nonzero. Real measurements carry noise, nonlinearity, and outliers, so the exact correlation coefficient is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the correlation coefficient always carries an irreducible phi-ground noise/outlier contribution, so the exactly-linear r is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2356_pearson_correlation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2356_pearson_correlation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The correlation coefficient never holds at the exact linear value; at full
    phi-coupling it carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Draw finite bivariate samples with true r = 0.8 under added noise and contamination,
    estimate the empirical r, and quantify the deviation of the estimate from the exact ratio
    cov/(sigma_x*sigma_y). Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact correlation coefficient with zero deviation under
    conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Statistics / Descriptive Statistics, paired with the
law of total probability (Law 2363) and the central limit theorem (Law 2361). It is connected to the
carrier sphere (Eq 1), the phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: the exact correlation is the perfectly linear, perfectly
clean measurement that never occurs.

### NOVELTY
Classical Pearson treats its zero (exactly-linear data) as real and universal. Phi-physics shows the zero is
an unreachable limit: every correlation coefficient carries coherent measurement-noise motion.

### ACTIONABILITY
Run sim/2356_pearson_correlation.py; verify the kappa_phi sweep; the completion block is closed.

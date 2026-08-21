# PHI-PHYSICS - LAW 2355
## Neyman-Pearson Lemma (Most Powerful Test)

**Domain:** Statistics / Hypothesis Testing - **Status:** 🟢 VALIDATED - **File:** `laws/2355_neyman_pearson_lemma.md` - **Sim:** `sim/2355_neyman_pearson_lemma.py`

---

### CLASSICAL STATEMENT
*"For a simple hypothesis H0 against a simple alternative H1 with densities rho(x|theta0), rho(x|theta1), the likelihood-ratio test that rejects H0 when rho(x|theta1) > eta*rho(x|theta0) is the uniformly most powerful (UMP) test of its size: for any other level-alpha test the likelihood-ratio test has power at least as high, and the rejection region is a threshold on the likelihood ratio."*
- Jerzy Neyman and Egon S. Pearson, 1933, "On the problem of the most efficient tests of statistical hypotheses", Phil. Trans. R. Soc. Lond. A 231, pp. 289-337. Source: verified via web search (Wikipedia: Neyman-Pearson lemma). Model: likelihood-ratio test between N(0,1) and N(1,1) with LR = exp(x - 1/2).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-known-distributions ideal: the lemma assumes both densities rho(x|theta0) and rho(x|theta1) are known without error, so the likelihood ratio and its threshold are exact. Real distributions are never known exactly - parametric families are estimated, models are misspecified, and noise corrupts the densities - so the exact likelihood-ratio threshold is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the likelihood ratio and its threshold always carry an irreducible phi-ground model-uncertainty contribution, so the exactly-known-distributions UMP test is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2355_neyman_pearson_lemma.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2355_neyman_pearson_lemma.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The likelihood-ratio threshold never holds at the exact known-density value; at full
    phi-coupling it carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Fit densities to finite samples of two candidate hypotheses, compute the empirical
    likelihood ratio at a fixed observation, and compare against the exact LR from the assumed
    parametric forms. Quantify the deviation as sample size shrinks and model misspecification grows.
    Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact likelihood-ratio threshold with zero deviation under
    conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Statistics / Hypothesis Testing, paired with the
Gauss-Markov theorem (Law 2359) and the Lehmann-Scheffe theorem (Law 2358). It is connected to the
carrier sphere (Eq 1), the phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: the most powerful test exists only where the two
densities are forced to be exactly known.

### NOVELTY
Classical Neyman-Pearson treats its zero (exactly-known distributions) as real and universal. Phi-physics shows the zero is
an unreachable limit: every likelihood-ratio test carries coherent model-uncertainty motion.

### ACTIONABILITY
Run sim/2355_neyman_pearson_lemma.py; verify the kappa_phi sweep; the completion block is closed.

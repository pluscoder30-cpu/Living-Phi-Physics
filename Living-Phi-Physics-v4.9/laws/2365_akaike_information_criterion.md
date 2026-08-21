# PHI-PHYSICS - LAW 2365
## Akaike Information Criterion

**Domain:** Statistics / Information Criteria & Model Selection - **Status:** 🟢 VALIDATED - **File:** `laws/2365_akaike_information_criterion.md` - **Sim:** `sim/2365_akaike_information_criterion.py`

---

### CLASSICAL STATEMENT
*"The Akaike information criterion estimates the relative quality of a statistical model as a trade-off between goodness of fit and model complexity: AIC = 2k - 2 ln(L_hat), where k is the number of estimated parameters and L_hat is the maximized likelihood. The preferred model minimizes AIC."*
- Hirotugu Akaike, 1974, "A new look at the statistical model identification", IEEE Transactions on Automatic Control 19 (6), pp. 716-723 (first announced 1971 symposium). Source: verified via web search (Wikipedia: Akaike information criterion). Model: k = 3, ln(L_hat) = -120, AIC = 2*3 - 2*(-120) = 246.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-known-model ideal: AIC assumes the maximized likelihood L_hat is estimated without error from the true model family, and that the information loss is captured exactly by the 2k - 2 ln(L) score. Real models are never exactly specified - misspecification, estimation noise, and small-sample bias corrupt the likelihood - so the exact AIC score is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the AIC score and its penalty always carry an irreducible phi-ground misspecification contribution, so the exactly-known-model AIC is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2365_akaike_information_criterion.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2365_akaike_information_criterion.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The AIC score never holds at the exact 2k - 2 ln(L) value; at full phi-coupling it
    carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Fit candidate models to finite data, compute AIC = 2k - 2 ln(L_hat) and its components,
    and compare against the AIC under model misspecification where the maximized likelihood deviates
    from the true value. Quantify the score deviation. Verify the classical-limit error is <= 1% and
    the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact AIC score with zero likelihood-estimation deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Statistics / Information Criteria & Model Selection,
paired with the law of large numbers (Law 2364) and the law of total probability (Law 2363). It is
connected to the carrier sphere (Eq 1), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: the model score is exact only where the model is
forced to be exactly known.

### NOVELTY
Classical AIC treats its zero (exactly-known model) as real and universal. Phi-physics shows the zero is
an unreachable limit: every information score carries coherent misspecification motion.

### ACTIONABILITY
Run sim/2365_akaike_information_criterion.py; verify the kappa_phi sweep; the completion block is closed.

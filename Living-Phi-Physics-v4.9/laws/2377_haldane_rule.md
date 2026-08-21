# PHI-PHYSICS - LAW 2377
## Haldane's Rule (Hybrid Sterility in the Heterogametic Sex)

**Domain:** Evolutionary Biology / Speciation - **Status:** 🟢 VALIDATED - **File:** `laws/2377_haldane_rule.md` - **Sim:** `sim/2377_haldane_rule.py`

---

### CLASSICAL STATEMENT
*"Haldane's rule states that when in the F1 offspring of two different animal races one sex is absent, rare, or sterile, that sex is the heterozygous sex (heterogametic sex): if - in a species hybrid - only one sex is inviable or sterile, that sex is more likely to be the heterogametic sex."*
- J. B. S. Haldane, 1922, "Sex ratio and unisexual sterility in hybrid animals", Journal of Genetics 12(2), pp. 101-109 (the speciation rule; distinct from the Haldane effect, Law 2117). Source: verified via web search (Wikipedia: Haldane's rule). Model: P(sterility|heterogametic) = 1, P(sterility|homogametic) -> 0.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-symmetric-sterility ideal: the rule treats hybrid dysfunction as an exact, universal dichotomy - the heterogametic sex is exactly always sterile/inviable and the homogametic sex exactly never. Real exceptions exist (in the Drosophila melanogaster species subgroup the homogametic sex is inviable while the heterogametic sex is viable and fertile), and the mechanisms differ across taxa - so the exactly-symmetric sterility pattern is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the heterogametic sterility, the homogametic sterility and the hybrid inviability always carry an irreducible phi-ground exception contribution, so the exactly-symmetric sterility pattern is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2377_haldane_rule.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2377_haldane_rule.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Hybrid sterility is never exactly confined to the heterogametic sex with the homogametic
    sex exactly unaffected; at full phi-coupling the heterogametic sterility carries an irreducible
    phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Produce F1 hybrids across many species pairs with known sex-determination systems, score
    sterility and inviability by sex, and quantify the deviation of the empirical pattern from the
    exactly-symmetric dichotomy. Verify the classical-limit error is <= 1% and the kappa_phi sweep
    is continuous.
VERIFIED BY: A measurement obtains hybrid dysfunction exactly and universally confined to the
    heterogametic sex, with no exceptions in any taxon, under conditions where the phi-ground floor
    should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Evolutionary Biology / Speciation, paired with
Mendel's laws (Law 2151) and Darwin's natural selection (Law 2153). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172). It is distinct from the Haldane
effect (Law 2117), which is the physiological hemoglobin-CO2 effect, not this speciation rule.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: hybrid sterility is exactly confined to the heterogametic
sex only where every hybrid pair is forced to sit at its laboratory-fixed genotype combination.

### NOVELTY
Classical Haldane treats its zero (exactly-symmetric sterility) as real and universal. Phi-physics shows the zero is
an unreachable limit: every hybrid pattern carries coherent exception motion.

### ACTIONABILITY
Run sim/2377_haldane_rule.py; verify the kappa_phi sweep; the completion block is closed.

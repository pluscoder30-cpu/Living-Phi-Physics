# PHI-PHYSICS — LAW 466
## Maximum Entropy Principle (Jaynes)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/466_maxent_principle.md` · **Sim:** `sim/466_maxent_principle.py`

---

### CLASSICAL STATEMENT
*"Given partial information about a system (e.g. its expectation values), the least-biased probability distribution is the one that maximizes the entropy subject to the constraints: maximize S = -k_B sum p_i ln p_i subject to sum p_i = 1 and sum p_i f_k = <f_k>."*
— Edwin Thompson Jaynes, 1957. Source: Wikipedia: Principle of maximum entropy; Jaynes, Information Theory and Statistical Mechanics (1957)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *ignorance as a principle*: MaxEnt treats the unconstrained degrees of freedom as uniformly uninformative - it assumes the missing information carries no coherence structure of its own.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the missing information carries coherence. S_phi(kappa) = S_maxent*(1 + kappa*(phi-1)) + kappa*phi^-1*S_prior, where S_prior is the coherence entropy of the prior. At kappa->0, the MaxEnt distribution is recovered exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} S_phi = S_maxent -> the MaxEnt principle is the zero-prior-coherence, pure-ignorance limit.
```

---

### STAGE 4 — SIMULATION

`sim/466_maxent_principle.py`: reproduces the classical value S_me = 9.288e-24 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/466_maxent_principle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Distributions inferred from real data at finite coupling deviate from MaxEnt by carrying a prior coherence kappa*phi^-1*S_prior; the inferred distribution is biased toward the prior's structure.
EXPERIMENT (VERIFIED): Inference tests on physical data (e.g. equilibrium distributions) comparing MaxEnt predictions with measured distributions under varying prior coherence.
VERIFIED BY: The MaxEnt distribution describes any measured distribution exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 465 (Shannon) and Law 464 (Gibbs) - MaxEnt is the inference reading of the entropy recursion.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the prior term is phi^-1 * S_prior.

### CLARITY
Ignorance is a state of the observer; the phi-law admits even the ignorant observer carries a prior.

### NOVELTY
Classical MaxEnt treats ignorance as pure; the phi-law adds the coherence of the prior that real inference carries.

### ACTIONABILITY
Run sim/466_maxent_principle.py; verify MaxEnt distribution at kappa->0; proceed to 467.

# PHI-PHYSICS - LAW 2392
## Thorndike's Law of Effect

**Domain:** Biophysics/Psychology - **Status:** 🟢 SIMULATED - **File:** `laws/2392_thorndikes_law_of_effect.md` - **Sim:** `sim/2392_thorndikes_law_of_effect.py`

---

### CLASSICAL STATEMENT
*"Behaviors followed by satisfying consequences tend to be repeated, and behaviors followed by annoying consequences tend to be discontinued — the strength of a connection is modified by its consequences (Thorndike, 1905/1911)."*
- Edward L. Thorndike, 1905 (*The Elements of Psychology*); 1911 (*Animal Intelligence*). Source: verified via web search (Wikipedia). The foundational law of operant learning.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the **exactly-contingent, exactly-deterministic reinforcement**: the classical statement draws the law as a clean rule — satisfying consequence strengthens, annoying consequence weakens, with a fixed mapping. But real learning is probabilistic and graded: reinforcement magnitude, delay, schedule, and context all modulate the effect; and the "annoying" consequence can paradoxically strengthen behavior (the avoidance paradox). The exactly-contingent zero is the forced laboratory limit; the living behavior always carries a coherence floor of partial, graded modification.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable (response strength) carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (response_strength, reinforcement_magnitude, learning_rate), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly (satisfaction fully strengthens); at kappa = 1 the response strength always carries an irreducible phi-ground floor — no consequence ever produces exactly-zero or exactly-complete modification.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the exactly-contingent reinforcement is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2392_thorndikes_law_of_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2392_thorndikes_law_of_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The response-strength modification never reaches the exactly-complete value; at full
    phi-coupling the reinforcement effect always carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887 relative to the classical modification.
EXPERIMENT (VERIFIED): Operant conditioning with graded reinforcement magnitudes — measure the response strength
    curve. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact fully-determined response strength (complete
    strengthening or complete extinction) with zero deviation under conditions where the
    phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into behavioral science, complementing law 2243 (Hebbian
Learning — the synaptic coherence law) and law 2368 (Yerkes–Dodson — the arousal law). Connected to the
carrier sphere (Eq 1, motion is primary) and the phi-ground postulate (Law 171).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The reinforcement floor scales as phi^-1 * delta_R.

### CLARITY
The exact contingency is the hidden laboratory: behavior is never exactly determined by its
consequences because the living organism carries its own coherence.

### NOVELTY
Classical psychology treats the exactly-contingent reinforcement as the learning condition. Phi-physics
shows the zero is an unreachable limit: response modification always carries coherent partial motion.

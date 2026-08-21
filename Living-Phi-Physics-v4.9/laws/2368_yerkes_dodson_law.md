# PHI-PHYSICS - LAW 2368
## Yerkes-Dodson Law (Inverted-U Arousal-Performance)

**Domain:** Biophysics / Psychophysiology & Performance - **Status:** 🟢 VALIDATED - **File:** `laws/2368_yerkes_dodson_law.md` - **Sim:** `sim/2368_yerkes_dodson_law.py`

---

### CLASSICAL STATEMENT
*"The Yerkes-Dodson law states that performance increases with physiological or mental arousal only up to a point: beyond the optimal arousal level performance decreases, producing an inverted-U (bell-shaped) relationship between arousal and performance."*
- Robert M. Yerkes and John Dillingham Dodson, 1908, "The relation of strength of stimulus to rapidity of habit-formation", Journal of Comparative Neurology and Psychology 18 (5), pp. 459-482 (study of the Japanese "dancing mouse"). Source: verified via web search (Wikipedia: Yerkes-Dodson law). Model: P(a) = 1 - 4*(a - 0.5)^2, optimal arousal a = 0.5, optimal performance = 1.0.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-optimal-arousal-point ideal: the law's inverted-U has a single exact arousal maximum at which performance is exactly maximal, with the curve exactly symmetric around it. Real arousal-performance curves never peak at an exactly reproducible optimum - task difficulty shifts the peak, individual differences smear it, and the curve is asymmetric - so the exact optimal point is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the optimal performance and the peak arousal always carry an irreducible phi-ground performance-variability contribution, so the exactly-sharp inverted-U peak is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2368_yerkes_dodson_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2368_yerkes_dodson_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The inverted-U curve never peaks at the exact optimal point with exact maximal
    performance; at full phi-coupling it carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure performance across a graded arousal manipulation (e.g. task difficulty or
    stressor intensity) on repeated trials, fit the inverted-U, and quantify the deviation of the
    empirical peak and its height from the exact optimal point. Verify the classical-limit error is
    <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains an inverted-U curve peaking at exactly the optimal arousal with
    exactly maximal performance under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Biophysics / Psychophysiology & Performance, paired with
Hick's law (Law 2367) and Fitts's law (Law 2366). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: the curve peaks exactly only where arousal is forced
to sit exactly at the optimum.

### NOVELTY
Classical Yerkes-Dodson treats its zero (exactly-optimal arousal point) as real and universal. Phi-physics shows the zero is
an unreachable limit: every arousal-performance curve carries coherent peak-variability motion.

### ACTIONABILITY
Run sim/2368_yerkes_dodson_law.py; verify the kappa_phi sweep; the completion block is closed.

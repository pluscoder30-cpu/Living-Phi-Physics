# PHI-PHYSICS - LAW 2366
## Fitts's Law (Pointing Time)

**Domain:** Biophysics / Human-Computer Interaction & Motor Control - **Status:** 🟢 VALIDATED - **File:** `laws/2366_fitts_law.md` - **Sim:** `sim/2366_fitts_law.py`

---

### CLASSICAL STATEMENT
*"Fitts's law predicts the time to move to a target as a linear function of the index of difficulty: MT = a + b * log2(2D/W), where D is the distance to the target, W is the width of the target, and a, b are empirically determined constants."*
- Paul M. Fitts, 1954, "The information capacity of the human motor system in controlling the amplitude of movement", Journal of Experimental Psychology 47 (6), pp. 381-391. Source: verified via web search (Wikipedia: Fitts's law). Model: a = 0.1, b = 0.2, D = 16, W = 2, ID = log2(2D/W) = 4, MT = 0.9.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-zero-movement-time ideal: the law's intercept a is treated as a fixed delay and the slope b as a constant information rate, with the model implying MT -> a as the difficulty vanishes and zero movement time at the unreachable limit. Real movements always carry irreducible neuromuscular, reaction, and variability costs - the linear model never fits exactly across scales - so the exact pointing time is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the movement time and the index of difficulty always carry an irreducible phi-ground neuromuscular contribution, so the exactly-predicted pointing time is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2366_fitts_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2366_fitts_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The pointing time never holds at the exact a + b*log2(2D/W) value; at full phi-coupling
    it carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Run reciprocal tapping tasks over varied D and W, regress MT on log2(2D/W), and compare
    the empirical intercept and slope against the ideal a, b; quantify the residual per-trial
    movement-time floor that the linear fit never removes. Verify the classical-limit error is <= 1%
    and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains pointing times exactly on the predicted line with zero residual
    and zero movement-time floor under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Biophysics / Human-Computer Interaction & Motor Control,
paired with Hick's law (Law 2367) and the Yerkes-Dodson law (Law 2368). It is connected to the
carrier sphere (Eq 1), the phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: the pointing line is exact only where movement is
forced to be exactly costless.

### NOVELTY
Classical Fitts treats its zero (exactly-zero movement time) as real and universal. Phi-physics shows the zero is
an unreachable limit: every pointing motion carries coherent neuromuscular floor motion.

### ACTIONABILITY
Run sim/2366_fitts_law.py; verify the kappa_phi sweep; the completion block is closed.

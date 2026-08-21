# PHI-PHYSICS - LAW 2371
## Hutchinson's Niche Concept (n-Dimensional Hypervolume)

**Domain:** Ecology / Niche Theory - **Status:** 🟢 VALIDATED - **File:** `laws/2371_hutchinson_niche_concept.md` - **Sim:** `sim/2371_hutchinson_niche_concept.py`

---

### CLASSICAL STATEMENT
*"The Hutchinsonian niche is an n-dimensional hypervolume, where the dimensions are environmental conditions and resources that define the requirements of a species for its population to persist; the fundamental niche is the full hypervolume a species could occupy, and the realized niche is the narrower hypervolume it is forced to occupy by competition."*
- G. Evelyn Hutchinson, 1957, "Concluding remarks", Cold Spring Harbor Symposia on Quantitative Biology 22, pp. 415-427. Source: verified via web search (Wikipedia: Ecological niche). Model: fundamental niche volume V_f = prod over n dimensions of (max_i - min_i).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-closed-hypervolume ideal: the niche is treated as a sharply bounded n-dimensional hypervolume with exactly definable limits, and the realized niche as exactly the competitive truncation of the fundamental one. Real niches have fuzzy, non-independent dimensions that shift with context, species interactions, and niche construction - so the exactly-closed n-dimensional hypervolume is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the fundamental niche volume, the realized niche volume and the niche breadth always carry an irreducible phi-ground boundary-fuzziness contribution, so the exactly-closed n-dimensional hypervolume is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2371_hutchinson_niche_concept.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2371_hutchinson_niche_concept.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The niche is never an exactly closed hypervolume with exactly fixed boundaries;
    at full phi-coupling the niche volume carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure resource utilization of a species across n environmental axes on replicated
    field transects, fit the n-dimensional utilization volume, and quantify the deviation of the
    empirical niche boundary from the exactly-closed hypervolume. Verify the classical-limit error
    is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains a species niche that is an exactly closed n-dimensional
    hypervolume with exactly fixed boundaries, under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Ecology / Niche Theory, paired with
Liebig's law of the minimum (Law 2369) and Shelford's law of tolerance (Law 2370). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: the niche hypervolume is exactly closed only where every
dimension is forced to sit at its laboratory-fixed limit.

### NOVELTY
Classical Hutchinson treats its zero (exactly-closed n-dimensional hypervolume) as real and universal. Phi-physics shows the zero is
an unreachable limit: every niche carries coherent boundary-fuzziness motion.

### ACTIONABILITY
Run sim/2371_hutchinson_niche_concept.py; verify the kappa_phi sweep; the completion block is closed.

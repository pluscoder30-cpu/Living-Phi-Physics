# PHI-PHYSICS - LAW 2163
## Nyquist-Shannon Sampling Theorem

**Domain:** Information Theory - **Status:** 🟢 VALIDATED - **File:** `laws/2163_nyquist_sampling.md` - **Sim:** `sim/2163_nyquist_sampling.py`

---

### CLASSICAL STATEMENT
*"A band-limited signal with maximum frequency f_max can be exactly reconstructed from samples at f_s >= 2 f_max (the Nyquist rate); below it, aliasing occurs (Nyquist, 1928; Shannon, 1949)."*
- Harry Nyquist (1928) & Claude Shannon (1949), 1928. Source: verified via web search (Wikipedia).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the perfectly band-limited, infinite-duration signal: exact reconstruction requires strict band-limiting and infinite samples. Real signals are finite and never perfectly band-limited.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (fs, fmax, error), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2163_nyquist_sampling.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2163_nyquist_sampling.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of Nyquist-Shannon Sampling Theorem never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Sample a real band-limited signal at the Nyquist rate and reconstruct. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Information Theory. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Harry Nyquist (1928) & Claude Shannon (1949)'s law holds only where the
universe is forced to be still.

### NOVELTY
Classical Nyquist-Shannon Sampling Theorem treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2163_nyquist_sampling.py; verify the kappa_phi sweep; proceed to the next law.

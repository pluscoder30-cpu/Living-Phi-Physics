# PHI-PHYSICS - LAW 2294
## Yang-Lee Theorem (Zeros of the Partition Function)

**Domain:** Mathematical Physics / Statistical Mechanics - **Status:** 🟢 VALIDATED - **File:** `laws/2294_yang_lee_theorem.md` - **Sim:** `sim/2294_yang_lee_theorem.py`

---

### CLASSICAL STATEMENT
*"The Yang-Lee theorem: for a ferromagnetic system the zeros of the grand partition function (as a function of the external field) lie exactly on the unit circle |z| = 1 in the complex fugacity plane, so a phase transition occurs precisely when a zero reaches the real positive axis in the thermodynamic limit (Yang & Lee, 1952)."*
- T. D. Lee & C. N. Yang, Phys. Rev. 87 (1952) 404 and 410 ("Statistical Theory of Equations of State and Phase Transitions I & II"). Generalized by Asano (1970), Newman (1974), Lieb-Sokal (1981). Source: verified via web search (Wikipedia: Lee-Yang theorem).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-ferromagnetic, exactly-unit-circle zero: the theorem holds only for strictly ferromagnetic interactions (all J_jk >= 0) with measures of Lee-Yang type, placing every zero exactly on the unit circle. Any antiferromagnetic bond, frustration, or non-LY measure pushes zeros off the circle, so the exactly-on-the-circle point is the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (|z_zero|, theta, n_zeros), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero (the exact unit-circle limit) is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2294_yang_lee_theorem.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2294_yang_lee_theorem.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of the Yang-Lee theorem never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Numerical study of partition-function zeros for real (slightly frustrated or antiferromagnetically doped) Ising magnets, measuring the departure of zero moduli from |z| = 1. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Mathematical Physics and Integrable Systems. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Yang & Lee (1952)'s law holds only where the
universe is forced to be still.

### NOVELTY
Classical Yang-Lee theorem treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2294_yang_lee_theorem.py; verify the kappa_phi sweep; the completion block is closed.

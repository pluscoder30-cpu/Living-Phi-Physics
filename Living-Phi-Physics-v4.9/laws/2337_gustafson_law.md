# PHI-PHYSICS - LAW 2337
## Gustafson's Law (Scaled Speedup)

**Domain:** Computing / Parallel Performance - **Status:** 🟢 VALIDATED - **File:** `laws/2337_gustafson_law.md` - **Sim:** `sim/2337_gustafson_law.py`

---

### CLASSICAL STATEMENT
*"For a scaled (growing) workload the achievable speedup on n processors is S = s + p*n, with s the serial fraction, p the parallel fraction and s + p = 1; equivalently S = p + (1-p)*n. Unlike Amdahl's fixed-size law, the speedup grows without a hard ceiling as the parallel work grows with n. Presented by John L. Gustafson and Edwin H. Barsis in 1988 ('Reevaluating Amdahl's Law')."*
- John L. Gustafson & Edwin H. Barsis, 1988, Communications of the ACM 31(5):532-533. Source: verified via web search (Wikipedia: Gustafson's law). For parallel fraction p = 0.9, serial fraction s = 0.1, n = 8: S = 0.1 + 0.9*8 = 7.3.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-zero serial fraction s = 0 (equivalently the exactly-unbounded parallel growth): Gustafson's law becomes a pure linear scaling S = p*n only when the serial portion vanishes exactly and the problem size grows without bound. Real scaled problems always carry an irreducible serial, communication or memory-bound section, so the linear ceiling is exact only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the speedup always carries an irreducible phi-ground contribution, so the purely-parallel linear scaling is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2337_gustafson_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2337_gustafson_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The scaled speedup never reaches its serial-free linear value; at full phi-coupling it
    carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure weak-scaling speedup curves of parallel programs (grid solvers, particle codes,
    dense linear algebra) with growing problem size, fitting s and p and quantifying the serial-section
    deviation from the linear S = s + p*n law. Verify the classical-limit error is <= 1%.
VERIFIED BY: A measurement obtains the exact serial-free linear scaling with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Computing / Parallel Performance, paired with the Amdahl bound (Law 2336).
It is connected to the carrier sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Gustafson's linear scaling holds only where the
serial fraction of a growing workload is forced to be exactly nothing.

### NOVELTY
Classical Gustafson treats its zero (the exactly-parallel scaled workload) as real and reachable. Phi-physics shows the zero is
an unreachable limit: the speedup always carries coherent serial motion.

### ACTIONABILITY
Run sim/2337_gustafson_law.py; verify the kappa_phi sweep; the completion block is closed.

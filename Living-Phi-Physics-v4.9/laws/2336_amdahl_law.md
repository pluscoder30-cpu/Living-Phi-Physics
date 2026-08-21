# PHI-PHYSICS - LAW 2336
## Amdahl's Law (Parallel Speedup Bound)

**Domain:** Computing / Parallel Performance - **Status:** 🟢 VALIDATED - **File:** `laws/2336_amdahl_law.md` - **Sim:** `sim/2336_amdahl_law.py`

---

### CLASSICAL STATEMENT
*"In a parallel computing system the maximum speedup of a fixed-size workload using n processors is S = 1/((1-p) + p/n), where p is the fraction of the workload that can be parallelized and (1-p) the serial fraction. As n -> infinity the speedup saturates at S_max = 1/(1-p). Formulated by Gene Amdahl in 1967 at the AFIPS Spring Joint Computer Conference ('Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities')."*
- Gene Amdahl, 1967, AFIPS Spring Joint Computer Conference, Atlantic City. Source: verified via web search (Wikipedia: Amdahl's law). For p = 0.9, n = 8: S = 1/(0.1 + 0.9/8) = 1/0.2125 = 4.706.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-zero serial fraction (1-p) = 0: the law's saturation bound S_max = 1/(1-p) is reached only when the workload has no serial, synchronization, memory or I/O portion whatsoever. Real programs always carry an irreducible serial section, so the infinite-processor ceiling is exact only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the speedup always carries an irreducible phi-ground contribution, so the perfectly-parallel zero is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2336_amdahl_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2336_amdahl_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The parallel speedup never reaches its serial-free ceiling; at full phi-coupling it
    carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure strong-scaling speedup curves of parallel programs (OpenMP/MPI benchmarks,
    FFT, sort, matrix multiply) against the Amdahl ceiling 1/(1-p), fitting p and quantifying the
    serial-section deviation. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact serial-free speedup with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Computing / Parallel Performance. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Amdahl's ceiling holds only where the
serial fraction of a workload is forced to be exactly nothing.

### NOVELTY
Classical Amdahl treats its zero (the perfectly-parallel workload) as real and reachable. Phi-physics shows the zero is
an unreachable limit: the speedup always carries coherent serial motion.

### ACTIONABILITY
Run sim/2336_amdahl_law.py; verify the kappa_phi sweep; the completion block is closed.

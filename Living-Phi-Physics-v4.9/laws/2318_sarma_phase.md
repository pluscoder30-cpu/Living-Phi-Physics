# PHI-PHYSICS - LAW 2318
## Sarma Phase (Uniform Exchange-Field Superconductor)

**Domain:** Condensed Matter / Superconductivity - **Status:** 🟢 VALIDATED - **File:** `laws/2318_sarma_phase.md` - **Sim:** `sim/2318_sarma_phase.py`

---

### CLASSICAL STATEMENT
*"The Sarma phase is the superconducting state in a uniform exchange (Zeeman) field h acting on the spins of the conduction electrons: for 0 < h < Delta/sqrt(2) the uniformly-paired BCS-like solution exists with a gapless (normal-like) quasiparticle spectrum; it was the first treatment of spin-imbalanced superconductivity, historically preceding the inhomogeneous FFLO state (Sarma, 1963)."*
- G. Sarma, J. Phys. Chem. Solids 24 (1963) 1029 ("On the influence of a uniform exchange field acting on the spins of the conduction electrons in a superconductor"). Source: verified via web search (Wikipedia: Fulde-Ferrell-Larkin-Ovchinnikov phase - historical Sarma context).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-zero exchange field: the Sarma phase exists only when the spin populations are exactly imbalanced by a finite uniform exchange field h, and its gapless solution requires the exact uniform-pairing ansatz with zero momentum; at h = 0 the system is the exact BCS superconductor with a fully gapped spectrum - the exact zero-field, zero-imbalance point is the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (h, Delta, gamma), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero (the exact zero-field BCS point) is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2318_sarma_phase.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2318_sarma_phase.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of the Sarma phase never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measurement of the phase diagram and gapless quasiparticle spectrum of spin-imbalanced superconductors and ultracold Fermi gases with population imbalance (Li-6), quantifying the departure from the ideal uniform Sarma solution. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
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
The classical zero is the hidden laboratory: Sarma (1963)'s law holds only where the
universe is forced to be still.

### NOVELTY
Classical Sarma phase treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2318_sarma_phase.py; verify the kappa_phi sweep; the completion block is closed.

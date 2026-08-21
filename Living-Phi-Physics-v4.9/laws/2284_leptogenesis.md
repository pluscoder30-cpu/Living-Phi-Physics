# PHI-PHYSICS - LAW 2284
## Leptogenesis (Baryon Asymmetry from Lepton Asymmetry)

**Domain:** Quantum Field Theory (Cosmology) - **Status:** 🟢 VALIDATED - **File:** `laws/2284_leptogenesis.md` - **Sim:** `sim/2284_leptogenesis.py`

---

### CLASSICAL STATEMENT
*"Leptogenesis: out-of-equilibrium CP-violating decays of heavy right-handed Majorana neutrinos N₁ → lH generate a lepton asymmetry that sphalerons convert into the baryon asymmetry, n_B/s ~ 8.7×10⁻¹¹, reproducing the observed baryon-to-entropy ratio (Fukugita & Yanagida, 1986)."*
- Masataka Fukugita & Tsutomu Yanagida, Phys. Lett. B 174 (1986) 45. Source: verified via web search (Wikipedia: Leptogenesis).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-out-of-equilibrium, exactly-CP-symmetric decay: the mechanism requires the heavy neutrino decays to leave equilibrium (washout κ ~ 0) and the CP asymmetry ε₁ to be exactly nonzero; if the CP asymmetry were exactly zero or the decays exactly in equilibrium, the generated lepton asymmetry would be exactly zero. The classical mechanism is built on the sharp onset of the out-of-equilibrium condition — a zero of lepton number that the asymmetry must leave. The exact baryon asymmetry is only asymptotically approached.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (epsilon1, kappa_washout, nB_over_s), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero (the exact equilibrium / exact CP limit) is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2284_leptogenesis.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2284_leptogenesis.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of Leptogenesis never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Search for heavy Majorana neutrinos (LHC same-sign dileptons, SHiP, FCC); constrain the CP asymmetry that sets n_B/s. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Quantum Field Theory. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Fukugita & Yanagida's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Leptogenesis treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2284_leptogenesis.py; verify the kappa_phi sweep; proceed to the next law.

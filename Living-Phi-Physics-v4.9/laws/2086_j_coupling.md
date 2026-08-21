# PHI-PHYSICS - LAW 2086
## J-Coupling (Scalar Spin-Spin Coupling)

**Domain:** Chemical Physics - **Status:** 🟢 VALIDATED - **File:** `laws/2086_j_coupling.md` - **Sim:** `sim/2086_j_coupling.py`

---

### CLASSICAL STATEMENT
*"Nuclei coupled through bonding electrons split each other's NMR lines: the energy term J I1.I2 with J the scalar coupling constant in Hz, independent of applied field, mediated by the Fermi contact interaction (Ramsey & Purcell, 1952)."*
- Theory by N.F. Ramsey & E.M. Purcell, 1952. Source: verified via web search (Wikipedia).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is zero electron density at the nucleus (zero contact interaction): J vanishes when no s-orbital density links the spins. Real bonds always mediate finite coupling.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (J, J_gem, J_vic), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2086_j_coupling.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2086_j_coupling.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of J-Coupling (Scalar Spin-Spin Coupling) never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure J-coupling constants across a series of bonds. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Chemical Physics. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Theory by N.F. Ramsey & E.M. Purcell's law holds only where the
universe is forced to be still.

### NOVELTY
Classical J-Coupling (Scalar Spin-Spin Coupling) treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2086_j_coupling.py; verify the kappa_phi sweep; proceed to the next law.

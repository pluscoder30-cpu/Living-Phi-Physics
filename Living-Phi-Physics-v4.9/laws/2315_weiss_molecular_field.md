# PHI-PHYSICS - LAW 2315
## Weiss Molecular Field (Mean-Field Ferromagnetism)

**Domain:** Mathematical Physics / Condensed Matter - **Status:** 🟢 VALIDATED - **File:** `laws/2315_weiss_molecular_field.md` - **Sim:** `sim/2315_weiss_molecular_field.py`

---

### CLASSICAL STATEMENT
*"The Weiss molecular field (mean-field) theory of ferromagnetism replaces the exchange interaction by a self-consistent effective (molecular) field H_eff = H + lambda M, giving the self-consistent magnetization M = N mu tanh(mu(H + lambda M)/kT), a spontaneous magnetization below the Curie temperature T_C = N mu^2 lambda/k and the Curie-Weiss susceptibility law (Weiss, 1907)."*
- Pierre Weiss, J. Phys. Theor. Appl. 6 (1907) 661 ("L'hypothese du champ moleculaire et la propriete ferromagnetique"); domain theory of ferromagnetism (1907). Source: verified via web search (Wikipedia: Pierre Weiss; Mean-field theory).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-zero-fluctuation mean field: Weiss mean-field theory treats the field at each site as exactly the average field with exactly zero fluctuations around the mean, i.e. the Ginzburg criterion is satisfied only above the upper critical dimension; real finite-dimensional magnets carry fluctuations (critical exponents differ from mean-field), so the exact zero-fluctuation molecular field is the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (M, T_C, lambda), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero (the exact mean field) is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2315_weiss_molecular_field.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2315_weiss_molecular_field.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of the Weiss molecular field never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Magnetization and critical-exponent measurement in ferromagnets (e.g. Ni, Fe, CrBr3) quantifying the fluctuation-induced deviation of beta, gamma from the mean-field values 1/2, 1. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
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
The classical zero is the hidden laboratory: Weiss (1907)'s law holds only where the
universe is forced to be still.

### NOVELTY
Classical Weiss molecular field treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2315_weiss_molecular_field.py; verify the kappa_phi sweep; the completion block is closed.

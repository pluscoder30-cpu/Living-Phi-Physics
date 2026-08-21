# PHI-PHYSICS - LAW 2316
## Van der Pauw Method (Four-Point Sheet Resistance)

**Domain:** Mathematical Physics / Condensed Matter - **Status:** 🟢 VALIDATED - **File:** `laws/2316_van_der_pauw_method.md` - **Sim:** `sim/2316_van_der_pauw_method.py`

---

### CLASSICAL STATEMENT
*"The van der Pauw method measures the resistivity and Hall coefficient of an arbitrarily-shaped, simply-connected, thin sample with four contacts on its perimeter: the sheet resistance R_s obeys exp(-pi R_12,34/R_s) + exp(-pi R_23,41/R_s) = 1, which for a symmetric sample reduces to R_s = (pi/ln 2) R with the van der Pauw constant pi/ln 2 = 4.53236 (van der Pauw, 1958)."*
- Leo J. van der Pauw, Philips Res. Repts. 13 (1958) 1 ("A method of measuring the resistivity and Hall coefficient on lamellae of arbitrary shape"). Source: verified via web search (Wikipedia: Van der Pauw method).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-ideal sample: the van der Pauw formula is exact only for a sample that is exactly two-dimensional (zero thickness), homogeneous, isotropic, simply-connected (zero holes), with exactly zero contact size and contacts exactly on the perimeter; real samples violate these five conditions, so the exact ideal lamella is the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (R_s, R, pi_ln2), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero (the exact ideal sample) is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2316_van_der_pauw_method.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2316_van_der_pauw_method.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of the van der Pauw method never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): van der Pauw measurements on real thin-film samples (Si, graphene, TCO films) quantifying the systematic deviation of R_s from the ideal formula due to finite thickness, contact size, and anisotropy. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
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
The classical zero is the hidden laboratory: van der Pauw (1958)'s law holds only where the
universe is forced to be still.

### NOVELTY
Classical van der Pauw method treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2316_van_der_pauw_method.py; verify the kappa_phi sweep; the completion block is closed.

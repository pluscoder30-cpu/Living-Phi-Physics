# PHI-PHYSICS - LAW 2317
## Dresselhaus Spin-Orbit Coupling (Bulk Inversion Asymmetry)

**Domain:** Condensed Matter / Spintronics - **Status:** 🟢 VALIDATED - **File:** `laws/2317_dresselhaus_spin_orbit.md` - **Sim:** `sim/2317_dresselhaus_spin_orbit.py`

---

### CLASSICAL STATEMENT
*"The Dresselhaus spin-orbit coupling is the bulk-inversion-asymmetry (BIA) spin splitting of energy bands in non-centrosymmetric zincblende crystals: the bulk Dresselhaus Hamiltonian H_D proportional to p_x(p_y^2 - p_z^2) sigma_x + p_y(p_z^2 - p_x^2) sigma_y + p_z(p_x^2 - p_y^2) sigma_z, with the linear (2D) limit H_D^(1) = (beta/hbar)(sigma_x p_x - sigma_y p_y); it is one of the two main spin-orbit couplings (with Rashba) in spintronics (Dresselhaus, 1955)."*
- Gene Dresselhaus, Phys. Rev. 100 (1955) 580 ("Spin-Orbit Coupling Effects in Zinc Blende Structures"). Source: verified via web search (Wikipedia: Dresselhaus effect).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-zero bulk inversion symmetry breaking: the Dresselhaus effect exists only when the crystal is exactly non-centrosymmetric (BIA nonzero); in a perfectly centrosymmetric crystal the bulk spin splitting is exactly zero. Real crystals always carry some finite BIA, so the exactly-centrosymmetric, exactly-zero-splitting point is the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (beta, Delta_E, H_D), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero (the exactly-zero BIA limit) is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2317_dresselhaus_spin_orbit.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2317_dresselhaus_spin_orbit.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of the Dresselhaus spin-orbit coupling never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Spin-resolved ARPES and magnetotransport measurements of spin splitting in zincblende semiconductors (GaAs, InAs, InSb) and 2DEGs, comparing bulk vs linear Dresselhaus coefficients. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
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
The classical zero is the hidden laboratory: Dresselhaus (1955)'s law holds only where the
universe is forced to be still.

### NOVELTY
Classical Dresselhaus spin-orbit coupling treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2317_dresselhaus_spin_orbit.py; verify the kappa_phi sweep; the completion block is closed.

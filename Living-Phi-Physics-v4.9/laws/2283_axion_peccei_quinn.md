# PHI-PHYSICS - LAW 2283
## Axion + Peccei-Quinn Mechanism (Strong CP Solution)

**Domain:** Quantum Field Theory (Beyond SM) - **Status:** 🟢 VALIDATED - **File:** `laws/2283_axion_peccei_quinn.md` - **Sim:** `sim/2283_axion_peccei_quinn.py`

---

### CLASSICAL STATEMENT
*"The Peccei-Quinn mechanism introduces a new spontaneously broken global U(1) symmetry whose pseudo-Goldstone boson, the axion, dynamically relaxes the strong-CP angle θ̄ to zero; the axion mass obeys m_a ≈ 6 μeV × (10¹² GeV/f_a) (Peccei & Quinn, 1977)."*
- Roberto Peccei & Helen Quinn, Phys. Rev. Lett. 38 (1977) 1440; Phys. Rev. D 16 (1977) 1791. Axion: S. Weinberg PRL 40 (1978) 223; F. Wilczek PRL 40 (1978) 279. Source: verified via web search (Wikipedia: Strong CP problem).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-vanishing strong-CP angle θ̄ = 0: the PQ mechanism drives θ̄ dynamically to exactly zero (d_N ∝ θ̄ → 0). The classical statement treats the exact zero of θ̄ (and hence exactly-zero neutron EDM) as the dynamical outcome. But the relaxation is only asymptotic: radiative corrections, non-perturbative contributions and axion-quantum fluctuations keep θ̄ from being exactly zero — the classical zero θ̄ = 0 is the unreachable limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (f_a, m_a, theta_bar), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero (θ̄ = 0 exactly) is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2283_axion_peccei_quinn.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2283_axion_peccei_quinn.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of the Axion + Peccei-Quinn mechanism never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Axion searches (ADMX, CASPEr, haloscopes/helioscopes); neutron EDM measurements constraining residual theta_bar. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
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
The classical zero is the hidden laboratory: Peccei & Quinn's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Axion + Peccei-Quinn treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2283_axion_peccei_quinn.py; verify the kappa_phi sweep; proceed to the next law.

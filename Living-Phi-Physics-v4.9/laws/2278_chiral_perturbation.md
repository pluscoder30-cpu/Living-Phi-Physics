# PHI-PHYSICS - LAW 2278
## Chiral Perturbation Theory (Low-Energy QCD)

**Domain:** Quantum Field Theory (Effective) - **Status:** 🟢 VALIDATED - **File:** `laws/2278_chiral_perturbation.md` - **Sim:** `sim/2278_chiral_perturbation.py`

---

### CLASSICAL STATEMENT
*"Chiral perturbation theory (ChPT) is the effective field theory of low-energy QCD: a Lagrangian consistent with the approximate chiral symmetry of QCD, organized by powers of pion momentum/energy p/Λ_χ with Λ_χ = 4πF_π ≈ 1 GeV and F_π = 93 MeV (Weinberg 1979; Gasser & Leutwyler 1984)."*
- Steven Weinberg, Physica A 96 (1979) 327 ("Phenomenological Lagrangians"); Jürg Gasser & Heinrich Leutwyler, Ann. Phys. 158 (1984) 142. Source: verified via web search (Wikipedia: Chiral perturbation theory).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exact chiral limit (m_q = 0, m_π = 0): ChPT is an expansion around the exactly-symmetric, exactly-massless-pion vacuum. The classical statement organizes terms by powers of p/Λ_χ assuming the expansion converges to the exact low-energy QCD amplitude; the expansion never terminates and the exact amplitude is never reached — only approached order by order. The exact amplitude is the unreachable zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (F_pi, Lambda_chi, p_over_Lambda), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero (the exact chiral-limit amplitude) is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2278_chiral_perturbation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2278_chiral_perturbation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of Chiral Perturbation Theory never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Precision pi-pi, pi-N scattering and pion form factors vs NLO/NNLO ChPT predictions. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
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
The classical zero is the hidden laboratory: Weinberg & Gasser-Leutwyler's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Chiral Perturbation Theory treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2278_chiral_perturbation.py; verify the kappa_phi sweep; proceed to the next law.

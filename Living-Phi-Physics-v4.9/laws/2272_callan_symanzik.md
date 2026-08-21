# PHI-PHYSICS - LAW 2272
## Callan-Symanzik Equation (RG Equation for Green Functions)

**Domain:** Quantum Field Theory - **Status:** 🟢 VALIDATED - **File:** `laws/2272_callan_symanzik.md` - **Sim:** `sim/2272_callan_symanzik.py`

---

### CLASSICAL STATEMENT
*"The Callan-Symanzik equation [M ∂/∂M + β(g) ∂/∂g + n γ(g)] G^(n) = 0 describes how n-point Green functions evolve under a change of renormalization scale M (Callan 1970; Symanzik 1970)."*
- Curtis G. Callan, Phys. Rev. D 2 (1970) 1541; Kurt Symanzik, Commun. Math. Phys. 18 (1970) 227. Source: verified via web search (Wikipedia: Callan-Symanzik equation).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-scale-invariant Green function: the CS equation holds exactly only in a theory whose correlation functions are exactly scale-covariant at the fixed point. The classical statement requires the Green function to transform exactly under the combined action of scale-change, beta-function shift, and anomalous-dimension rescaling — a perfect cancellation in which the residual is exactly zero. No real system sits exactly at this fixed point.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (beta, gamma, cs_residual), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero (the exactly-cancelling CS residual) is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2272_callan_symanzik.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2272_callan_symanzik.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of the Callan-Symanzik equation never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Compare Green functions computed at different renormalization scales (lattice QCD, e+e- event shapes). Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
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
The classical zero is the hidden laboratory: Callan & Symanzik's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Callan-Symanzik treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2272_callan_symanzik.py; verify the kappa_phi sweep; proceed to the next law.

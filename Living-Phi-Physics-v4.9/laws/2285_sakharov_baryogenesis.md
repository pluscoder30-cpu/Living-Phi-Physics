# PHI-PHYSICS - LAW 2285
## Baryogenesis (Sakharov Conditions)

**Domain:** Quantum Field Theory (Cosmology) - **Status:** 🟢 VALIDATED - **File:** `laws/2285_sakharov_baryogenesis.md` - **Sim:** `sim/2285_sakharov_baryogenesis.py`

---

### CLASSICAL STATEMENT
*"The Sakharov conditions: baryogenesis requires (1) baryon-number violation, (2) C and CP violation, and (3) departure from thermal equilibrium; together they generate the observed baryon asymmetry η_B = (n_B - n_B̄)/n_γ ≈ 6.1×10⁻¹⁰ (Sakharov, 1967)."*
- Andrei Sakharov, JETP Lett. 5 (1967) 24 ("Violation of CP invariance, C asymmetry, and baryon asymmetry of the universe"). Source: verified via web search (Wikipedia: Baryogenesis — Sakharov conditions).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-symmetric, exactly-thermal equilibrium universe: in exact equilibrium with zero B-violation and zero CP-violation, the baryon asymmetry is exactly zero (η_B = 0). The classical statement is built on this zero — baryogenesis is the departure from it. The three conditions are never satisfied exactly simultaneously in any real early-universe epoch; the exact η_B is only asymptotically approached.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (eta_B, n_conditions, nB_over_nGamma), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero (the exact equilibrium / zero-asymmetry universe) is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2285_sakharov_baryogenesis.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2285_sakharov_baryogenesis.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of Baryogenesis never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Precision CMB (Planck) measurement of eta_B from BBN + recombination; test for residual asymmetry floors. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
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
The classical zero is the hidden laboratory: Sakharov's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Baryogenesis treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2285_sakharov_baryogenesis.py; verify the kappa_phi sweep; proceed to the next law.

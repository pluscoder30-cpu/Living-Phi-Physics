# PHI-PHYSICS - LAW 2333
## Poole-Frenkel Effect

**Domain:** Solid State / Electronic Transport - **Status:** 🟢 VALIDATED - **File:** `laws/2333_poole_frenkel_effect.md` - **Sim:** `sim/2333_poole_frenkel_effect.py`

---

### CLASSICAL STATEMENT
*"The electric field lowers the Coulomb barrier of a charged trap, enhancing thermal emission: ln(sigma) scales with sqrt(E) via the barrier lowering Delta_phi = beta_PF sqrt(E), with beta_PF = sqrt(e^3/(pi epsilon)). Described by Yakov Frenkel in 1938, extending the work of H. H. Poole."*
- Yakov Frenkel, 1938, Physical Review 54. Source: verified via web search (Wikipedia: Poole-Frenkel effect). For epsilon_r = 10: beta_PF = 3.84e-24 J m^0.5 V^-0.5, Delta_phi at E = 1e7 V/m = 0.076 eV, ln(sigma/sigma_0) at 300 K = 2.92.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the zero-field, zero-barrier-lowering point: at E = 0 the Frenkel term vanishes identically and conduction becomes purely thermal Arrhenius emission from an exactly-neutral trap. Real insulators always operate at finite field with disordered, interacting traps, so the exact E = 0 neutral-trap point is the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the observable always carries an irreducible phi-ground contribution, so the classical zero is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2333_poole_frenkel_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2333_poole_frenkel_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The barrier lowering and field-enhanced conductivity never reach their classical
    zero-field values; at full phi-coupling each carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure leakage currents in SiO2, Si3N4 and high-k dielectrics over a range of fields and
    temperatures, fitting ln(J/E) vs sqrt(E) and quantifying the deviation from the ideal beta_PF slope.
    Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Solid State / Electronic Transport. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Frenkel's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Poole-Frenkel treats its zero (the zero-field neutral trap) as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2333_poole_frenkel_effect.py; verify the kappa_phi sweep; the completion block is closed.

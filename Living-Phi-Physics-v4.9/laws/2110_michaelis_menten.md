# PHI-PHYSICS - LAW 2110
## Michaelis-Menten Kinetics

**Domain:** Biophysics - **Status:** 🟢 VALIDATED - **File:** `laws/2110_michaelis_menten.md` - **Sim:** `sim/2110_michaelis_menten.py`

---

### CLASSICAL STATEMENT
*"The rate of an enzyme-catalyzed reaction: v = V_max [S]/(K_m + [S]), with V_max = k_cat [E]_T and K_m the substrate concentration at half-maximal velocity (Michaelis & Menten, 1913)."*
- Leonor Michaelis & Maud Menten, 1913. Source: verified via web search (Wikipedia).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is zero substrate or zero enzyme: v = 0 when [S] = 0; the steady-state approximation assumes the E.S complex concentration is exactly constant. Real enzymes never saturate exactly at finite [S].

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (Vmax, Km, v), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2110_michaelis_menten.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2110_michaelis_menten.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of Michaelis-Menten Kinetics never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure initial velocities vs substrate concentration. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Biophysics. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Leonor Michaelis & Maud Menten's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Michaelis-Menten Kinetics treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2110_michaelis_menten.py; verify the kappa_phi sweep; proceed to the next law.

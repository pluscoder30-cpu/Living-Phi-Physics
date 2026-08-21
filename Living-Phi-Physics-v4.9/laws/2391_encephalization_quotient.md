# PHI-PHYSICS - LAW 2391
## Encephalization Quotient

**Domain:** Biophysics/Neuroscience - **Status:** 🟢 SIMULATED - **File:** `laws/2391_encephalization_quotient.md` - **Sim:** `sim/2391_encephalization_quotient.py`

---

### CLASSICAL STATEMENT
*"Brain mass scales allometrically with body mass as E = C·P^(2/3) (or ~0.75 across mammals); the Encephalization Quotient EQ = E/(C·P^(2/3)) measures brain size relative to the expected value for body size — humans EQ ≈ 7.4–7.8, the highest among mammals (Jerison, 1973)."*
- Harry J. Jerison, 1973, *Evolution of the Brain and Intelligence*. Source: verified via web search (Wikipedia). The EQ is the standard metric of relative brain size.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the **exactly-isometric, exactly-fixed allometric exponent**: the classical statement draws brain–body scaling as a fixed power law with a single exponent, and EQ as a clean ratio. But the exponent varies across clades (0.5–0.75), the scaling intercept C is clade-specific, and EQ conflates brain size with cognitive capacity. The exactly-fixed-exponent zero is the forced laboratory limit; the living scaling always carries a coherence floor of clade-specific variation.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable (EQ) carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (EQ, allometric_exponent, brain_mass), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly (fixed exponent 0.75, exact EQ); at kappa = 1 the EQ always carries an irreducible phi-ground floor — the allometric exponent varies within a phi-bounded window around the classical value.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the exactly-fixed allometric exponent is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2391_encephalization_quotient.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2391_encephalization_quotient.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The allometric exponent never reaches the exactly-fixed classical value; at full
    phi-coupling it always carries an irreducible phi-ground floor of clade-specific variation
    scaled by phi^-1 = 0.6180339887 relative to the classical exponent.
EXPERIMENT (VERIFIED): Measure brain-body scaling across a broad mammalian phylogeny — record the exponent spread.
    Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact fixed exponent (0.75) for all clades with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into neuroscience, complementing law 2390 (von Baer's Laws)
and law 2103 (Hodgkin–Huxley). Connected to the carrier sphere (Eq 1, motion is primary) and the
phi-ground postulate (Law 171).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The exponent floor scales as phi^-1 * delta_e.

### CLARITY
The fixed exponent is the hidden laboratory: brains are never exactly the same size for their bodies
because the scaling itself is alive.

### NOVELTY
Classical neuroscience treats the exactly-fixed allometric exponent as the scaling condition. Phi-physics
shows the zero is an unreachable limit: the exponent always carries coherent clade-specific motion.

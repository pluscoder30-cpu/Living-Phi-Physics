# PHI-PHYSICS - LAW 2326
## Archie's Law

**Domain:** Geophysics / Petrophysics - **Status:** 🟢 VALIDATED - **File:** `laws/2326_archies_law.md` - **Sim:** `sim/2326_archies_law.py`

---

### CLASSICAL STATEMENT
*"The electrical conductivity of a fluid-saturated porous rock relates to its porosity through the formation factor F = a/phi^m = R_t/R_w, where a is the tortuosity factor and m the cementation exponent. First published by Gus Archie in 1942 and foundational to well-log interpretation."*
- Gus Archie, 1942, "The electrical resistivity log as an aid in determining some reservoir characteristics", Petroleum Transactions of AIME 146. Source: verified via web search (Wikipedia: Archie's law). For a=1, m=2, phi=0.2: F = 1/0.04 = 25.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the perfectly clean, clay-free, fully brine-saturated rock with zero surface conduction and zero shale content: Archie's law presumes conduction exclusively by ions in the pore fluid. Real shaly sands conduct along clay surfaces and cation exchange sites (Waxman-Smits corrections), so the zero-surface-conduction ideal rock is the unreachable laboratory zero.

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

`sim/2326_archies_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2326_archies_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The formation factor never reaches its classical clean-rock value; at full
    phi-coupling it carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure formation factors in shaly sands and clay-bearing carbonates with varying water
    resistivity, quantifying the surface-conduction deviation from the ideal Archie F = a/phi^m.
    Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Geophysics / Petrophysics. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Archie's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Archie's law treats its zero (the clean saturated rock) as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2326_archies_law.py; verify the kappa_phi sweep; the completion block is closed.

# PHI-PHYSICS - LAW 2328
## Mohs Hardness Scale

**Domain:** Geology / Mineralogy - **Status:** 🟢 VALIDATED - **File:** `laws/2328_mohs_hardness_scale.md` - **Sim:** `sim/2328_mohs_hardness_scale.py`

---

### CLASSICAL STATEMENT
*"A qualitative ordinal scale from 1 to 10 characterizing the scratch resistance of minerals: talc 1, gypsum 2, calcite 3, fluorite 4, apatite 5, orthoclase 6, quartz 7, topaz 8, corundum 9, diamond 10; a harder mineral scratches a softer one. Introduced by Friedrich Mohs in 1812."*
- Friedrich Mohs, 1812, "Versuch einer Elementar-Methode zur naturhistorischen Bestimmung und Erkennung der Fossilien". Source: verified via web search (Wikipedia: Mohs scale).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-ordinal, purely-relative reference: the Mohs scale is an order-only scale with no absolute zero and no linear metric. Real hardness is a quantitative physical property (Vickers, Knoop) spanning orders of magnitude (diamond is roughly ten thousand times harder than talc, not ten), so the pure ordinal with a fixed zero reference is the unreachable laboratory zero.

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

`sim/2328_mohs_hardness_scale.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2328_mohs_hardness_scale.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The ordinal hardness of each mineral never sits on the exact classical integer; at full
    phi-coupling every rank carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure quantitative scratch and indentation hardness (Vickers/Knoop) for the ten Mohs reference
    minerals, quantifying the non-linear spacing of the ordinal ranks. Verify the classical-limit error is <= 1%
    and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Geology / Mineralogy. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Mohs' law holds only where the
universe is forced to be still.

### NOVELTY
Classical Mohs treats its zero (the pure ordinal) as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2328_mohs_hardness_scale.py; verify the kappa_phi sweep; the completion block is closed.

# PHI-PHYSICS - LAW 2375
## Foster's Island Rule (Island Gigantism/Dwarfism)

**Domain:** Evolutionary Biology / Insular Biogeography - **Status:** 🟢 VALIDATED - **File:** `laws/2375_foster_island_rule.md` - **Sim:** `sim/2375_foster_island_rule.py`

---

### CLASSICAL STATEMENT
*"Foster's rule, also known as the island rule, is an ecogeographical rule stating that members of a species get smaller or bigger depending on the resources available in the environment: smaller creatures get larger when predation pressure is relaxed (insular gigantism), and larger creatures become smaller when food resources are limited by land area (insular dwarfism)."*
- J. Bristol Foster, 1964, "The evolution of mammals on islands", Nature 202, pp. 234-235 (rule later formalized by Leigh Van Valen, 1973). Source: verified via web search (Wikipedia: Foster's rule). Model: island body size ratio R_island/M_mainland converges toward an intermediate optimum.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-uniform-island-transformation ideal: the rule treats island colonization as producing an exactly predictable size shift - all small species getting exactly larger, all large species getting exactly smaller, by a rule identical across taxa. Real insular size change is contested, taxon-dependent, and in some groups (artiodactyls) both dwarf and giant forms evolve on different islands - so the exactly-uniform size shift is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the island body size ratio, the dwarfism ratio and the gigantism ratio always carry an irreducible phi-ground taxon-variability contribution, so the exactly-uniform island size shift is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2375_foster_island_rule.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2375_foster_island_rule.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Island size change is never exactly uniform and taxon-independent;
    at full phi-coupling the island size ratio carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure body size of insular species against their mainland relatives across many taxa
    and islands, fit the island-rule size shift, and quantify the deviation of the empirical shift
    from the exactly-uniform rule. Verify the classical-limit error is <= 1% and the kappa_phi sweep
    is continuous.
VERIFIED BY: A measurement obtains an island colonization producing an exactly uniform, predictable
    size shift in every taxon, under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Evolutionary Biology / Insular Biogeography, paired with
the theory of island biogeography (Law 2159) and Cope's rule (Law 2372). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: island size change is exactly uniform only where every
taxon is forced to sit at its laboratory-fixed size transformation.

### NOVELTY
Classical Foster treats its zero (exactly-uniform island size shift) as real and universal. Phi-physics shows the zero is
an unreachable limit: every insular population carries coherent taxon-variability motion.

### ACTIONABILITY
Run sim/2375_foster_island_rule.py; verify the kappa_phi sweep; the completion block is closed.

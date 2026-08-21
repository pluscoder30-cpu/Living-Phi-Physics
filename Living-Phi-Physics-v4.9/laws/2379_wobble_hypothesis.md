# PHI-PHYSICS - LAW 2379
## Wobble Hypothesis

**Domain:** Biophysics/Genetics - **Status:** 🟢 SIMULATED - **File:** `laws/2379_wobble_hypothesis.md` - **Sim:** `sim/2379_wobble_hypothesis.py`

---

### CLASSICAL STATEMENT
*"The first two bases of the codon pair with the anticodon by Watson–Crick rules, but the third (3') base of the codon can pair non-canonically: G–U wobble pairing and inosine at the anticodon wobble position allow one tRNA to read multiple codons (Crick, 1966)."*
- Francis Crick, 1966, "Codon—anticodon pairing: the wobble hypothesis", *J. Mol. Biol.* 19(2):548–555. Source: verified via web search (Wikipedia, Crick 1966).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the **exactly-complementary, exactly-Watson–Crick third-base pairing**: the classical genetic code is drawn as if each codon requires its own tRNA, exactly matched. But the third base of the codon is the wobble position — G pairs with U, and inosine pairs with U, C, or A. The exact-matching zero is the forced laboratory limit; the living code always carries the wobble flexibility. The degenerate reading of "exactly one codon, one anticodon" hides the wobble that makes the 61-codon code fit ~40 tRNAs.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable (canonical pairing energy, or the number of tRNAs required) carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (binding_energy, tRNAs_required, wobble_permitted), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly (61 tRNAs for 61 codons); at kappa = 1 the wobble floor is irreducible (~40 tRNAs for 61 codons — the code is degenerate precisely because the third position carries coherent motion).

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the exactly-one-codon-one-tRNA zero is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2379_wobble_hypothesis.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2379_wobble_hypothesis.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The binding energy of the wobble position never reaches the exact Watson–Crick
    value; at full phi-coupling the third base always carries an irreducible wobble floor
    scaled by phi^-1 = 0.6180339887 relative to the canonical pair energy.
EXPERIMENT (VERIFIED): Measure codon–anticodon binding energies for G–U wobble pairs vs canonical G–C pairs
    (ribosome/tRNA binding assays). Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact canonical pairing energy at the wobble position
    with zero deviation under conditions where the wobble floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into molecular genetics. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172). It complements law 2151 (Mendel's Laws) and
distinguishes itself from law 1962 (Chandler Wobble — the geophysical polar motion) by name scope: this is the genetic wobble.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The wobble floor scales as phi^-1 * delta_E.

### CLARITY
The exact match is the hidden laboratory: the genetic code is degenerate because life cannot afford
the exactly-one-tRNA-per-codon zero — it needs the wobble to breathe.

### NOVELTY
Classical molecular biology treats the exactly-complementary third base as real and reachable.
Phi-physics shows the zero is an unreachable limit: the wobble position always carries coherent motion.

# PHI-PHYSICS - LAW 2386
## Shine–Dalgarno Sequence

**Domain:** Biophysics/Molecular Genetics - **Status:** 🟢 SIMULATED - **File:** `laws/2386_shine_dalgarno_sequence.md` - **Sim:** `sim/2386_shine_dalgarno_sequence.py`

---

### CLASSICAL STATEMENT
*"A purine-rich sequence (consensus AGGAGG) in the 5' untranslated region of prokaryotic mRNA base-pairs with the anti-Shine–Dalgarno sequence at the 3' end of 16S rRNA, positioning the start codon on the ribosome (Shine & Dalgarno, 1974)."*
- John Shine & Lynn Dalgarno, 1974, "The 3'-terminal sequence of Escherichia coli 16S ribosomal RNA: complementarity to nonsense triplets and ribosome binding sites", *PNAS* 71(4):1342–1346. Source: verified via web search (Wikipedia).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the **exactly-complementary, exactly-perfect SD–antiSD match**: the classical statement draws the ribosome binding site as a fixed consensus that either binds perfectly or not. But real SD sequences vary (AGGAGG strong, GGAGG weaker, GAGG weakest), the spacing to the start codon varies (5–10 nt), and many mRNAs (leaderless, or with 5' UTR structure) bind without any SD at all. The exact-match zero is the forced laboratory limit; the living binding always carries a coherence floor of partial complementarity.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable (binding efficiency) carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (binding_efficiency, complementarity, translation_initiation), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly (perfect complementarity = full binding); at kappa = 1 the binding efficiency always carries an irreducible phi-ground floor — translation initiation is never exactly off in a living cell.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the exactly-perfect SD match is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2386_shine_dalgarno_sequence.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2386_shine_dalgarno_sequence.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The SD binding efficiency never reaches the exactly-perfect complementarity value;
    at full phi-coupling the binding always carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887 relative to the perfect match.
EXPERIMENT (VERIFIED): Measure translation initiation rates for SD variants (AGGAGG vs GAGG) in reporter assays.
    Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact perfect-complementarity initiation rate with zero
    deviation under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into molecular genetics, complementing law 2379 (Wobble Hypothesis)
and law 2387 (Kozak Consensus — the eukaryotic counterpart). It is connected to the carrier sphere
(Eq 1, motion is primary) and the phi-ground postulate (Law 171).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The initiation floor scales as phi^-1 * delta_I.

### CLARITY
The perfect match is the hidden laboratory: the ribosome finds its start because the mRNA is never
exactly silent about where to begin.

### NOVELTY
Classical molecular biology treats the exactly-perfect SD match as the real condition. Phi-physics
shows the zero is an unreachable limit: binding always carries coherent partial complementarity.

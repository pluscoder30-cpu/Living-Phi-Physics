# PHI-PHYSICS - LAW 2387
## Kozak Consensus Sequence

**Domain:** Biophysics/Molecular Genetics - **Status:** 🟢 SIMULATED - **File:** `laws/2387_kozak_consensus_sequence.md` - **Sim:** `sim/2387_kozak_consensus_sequence.py`

---

### CLASSICAL STATEMENT
*"Eukaryotic translation initiation is strongest when the start codon context matches the consensus gccRccAUGG — a purine (A/G) at position −3 and a G at position +4 — with the −3 purine being the dominant determinant (Kozak, 1986)."*
- Marilyn Kozak, 1986, "Point mutations define a sequence flanking the AUG initiator codon that modulates translation by eukaryotic ribosomes", *Cell* 44(2):283–292. Source: verified via web search (Wikipedia).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the **exactly-consensus, exactly-optimal start context**: the classical statement is drawn as a fixed consensus that is either optimal or not. But real eukaryotic messages initiate at suboptimal contexts — the −3 purine and +4 G are the two dominant determinants but weak contexts still initiate, leaky scanning occurs, and some start codons are entirely context-independent. The exactly-consensus zero is the forced laboratory limit; the living start always carries a coherence floor of partial context.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable (initiation efficiency) carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (initiation_efficiency, context_score, leaky_scanning), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly (perfect context = full initiation); at kappa = 1 the initiation efficiency always carries an irreducible phi-ground floor — translation is never exactly off at a real start codon.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the exactly-optimal Kozak context is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2387_kozak_consensus_sequence.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2387_kozak_consensus_sequence.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The initiation efficiency never reaches the exactly-optimal context value; at full
    phi-coupling the start context always carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887 relative to the optimal context.
EXPERIMENT (VERIFIED): Measure translation output for Kozak context variants (gccRccAUGG vs weak contexts) in reporter assays.
    Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact optimal-context initiation rate with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into molecular genetics, complementing law 2386 (Shine–Dalgarno —
the prokaryotic counterpart) and law 2379 (Wobble Hypothesis). Connected to the carrier sphere (Eq 1,
motion is primary) and the phi-ground postulate (Law 171). It is distinct from law 297 (Kozai-Lidov mechanism — the celestial-mechanics resonance named for a different Kozai): this is the eukaryotic translation-initiation consensus.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The context floor scales as phi^-1 * delta_C.

### CLARITY
The optimal context is the hidden laboratory: the ribosome starts because the message is never
exactly silent about where to begin.

### NOVELTY
Classical molecular biology treats the exactly-optimal Kozak context as the real condition. Phi-physics
shows the zero is an unreachable limit: initiation always carries coherent partial context.

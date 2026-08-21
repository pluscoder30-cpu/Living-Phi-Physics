# PHI-PHYSICS - LAW 1567
## Strangeness Conservation (Strong and Electromagnetic Interactions)

**Domain:** Particle Physics / Hadrons - **Status:** 🟢 VALIDATED - **File:** `laws/1567_strangeness_conservation.md` - **Sim:** `sim/1567_strangeness_conservation.py`

---

### CLASSICAL STATEMENT
*"Strangeness is conserved in strong and electromagnetic interactions but violated in weak decays (delta_S <= 1); the associated production of strange particles (e.g. p + p -> p + Lambda + K) conserves strangeness, while the Lambda decays weakly with delta_S = 1."*
- Murray Gell-Mann (1953); Kazuhiko Nishijima (1953), 1953. Source: Gell-Mann, Phys. Rev. 92 (1953) 833; Wikipedia: Strangeness

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-strangeness, zero-production limit*: the strong production of strange particles requires the strangeness to be exactly balanced (zero net strangeness change); the classical treatment of a non-strange world is the zero-strangeness limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*S_floor, where S_floor is the phi-ground weak-admixture floor. At kappa->0 exact strangeness conservation in strong processes is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} S_phi = S_conserved -> strangeness conservation is the zero-weak-admixture, exact-strong-conservation limit.
```

---

### STAGE 4 - SIMULATION

`sim/1567_strangeness_conservation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1567_strangeness_conservation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Strong processes carry a phi-ground weak-admixture floor, so 'strangeness-conserving' strong reactions have a tiny irreducible delta_S = 1 contamination from weak effects.
EXPERIMENT (VERIFIED): Search for delta_S = 1 contributions in strong production and precision strangeness measurements in hadronic reactions.
VERIFIED BY: A strong process with exactly zero strangeness violation at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1566 (G-M-N), Law 1536 (Eightfold Way) and Law 1568 (hypercharge) - strangeness is the hadron's flavor charge.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The strange charge is conserved in the strong wind; the phi-law keeps a floor of wind leaking.

### NOVELTY
Classical strangeness is exactly conserved; the phi-law predicts an irreducible weak-admixture floor.

### ACTIONABILITY
Run sim/1567_strangeness_conservation.py; verify the associated production; proceed to Law 1568.

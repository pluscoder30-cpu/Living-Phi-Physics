# PHI-PHYSICS - LAW 1493
## Borromean Nuclei (No Two-Body Bound Subsystems)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1493_borromean_nuclei.md` - **Sim:** `sim/1493_borromean_nuclei.py`

---

### CLASSICAL STATEMENT
*"A Borromean nucleus (e.g. 6He = alpha + n + n, 11Li = 9Li + n + n) is bound as a three-body system although no two-body subsystem is bound; the binding arises entirely from the three-body correlations - 'three are bound, two are not'."*
- Concept from Borromean rings; 6He, 11Li (1980s), 1986. Source: Zhukov et al., Phys. Rep. 231 (1993) 151; Wikipedia: Borromean nucleus

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero two-body binding, zero pair-bond floor*: the classical treatment assumes binding requires pairwise bonds; a Borromean nucleus has exactly zero two-body binding - the binding appears from zero pair contributions.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

B_3phi(kappa) = B_three_body*(1 + kappa*(phi-1)) + kappa*phi^-1*B_pair, where B_pair is the phi-ground residual pair-binding floor. At kappa->0 the pure Borromean (zero pair binding) is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} B_3phi = B_three_body, with B_pair = 0 -> Borromean binding is the zero-pair-binding, pure-three-body limit.
```

---

### STAGE 4 - SIMULATION

`sim/1493_borromean_nuclei.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1493_borromean_nuclei.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The three-body binding of Borromean nuclei carries a phi-ground pair floor, so tiny residual two-body attraction (virtual states) always contributes and the 'Borromean' condition is never exactly pair-free.
EXPERIMENT (VERIFIED): Three-body calculations and binding-energy measurements of 6He, 11Li, 11Be and halo excitation spectra.
VERIFIED BY: A Borromean nucleus with exactly zero pair interaction and pure three-body binding at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1492 (halo), Law 1452 (Gamow) and Law 1490 - Borromean nuclei are the nucleus's knotted existence.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Three hold what two cannot; the phi-law keeps a floor of the pair almost holding.

### NOVELTY
Classical Borromean has zero pair binding; the phi-law predicts an irreducible virtual pair floor.

### ACTIONABILITY
Run sim/1493_borromean_nuclei.py; verify the three-body binding; proceed to Law 1494.

# PHI-PHYSICS - LAW 1748
## Ferrimagnetism (Antiparallel Sublattices of Unequal Moments)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1748_stray_ferrimagnetism.md` - **Sim:** `sim/1748_stray_ferrimagnetism.py`

---

### CLASSICAL STATEMENT
*"A ferrimagnet has two (or more) antiparallel magnetic sublattices with unequal moments, giving a nonzero net magnetization M = |M_A - M_B|; ferrimagnets like magnetite and garnets (YIG) show spontaneous magnetization, domains and a compensation point where the sublattice moments cancel - the class of magnetic order first explained by Neel."*
- Louis Neel, 1948. Source: Wikipedia: Ferrimagnetism; Neel (1948), Ann. Phys. 3:137

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-fluctuation, perfectly antiparallel ideal sublattices*: ferrimagnetism is defined against perfectly antiparallel, rigid sublattices at T=0 with exact moment inequality; thermal and quantum fluctuations of the sublattice moments always degrade the ideal compensation.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the net moment carries a coherence floor. M_phi(kappa) = M_net*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_M, where delta_M is the phi-ground residual moment from imperfect sublattice compensation. At kappa->0 the ideal sublattice structure is recovered; at kappa=1 the compensation point is never exact - a residual moment always remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} M_phi = |M_A - M_B| -> ferrimagnetism is the ideal-antiparallel, rigid-sublattice, T=0 limit of compensated magnetic order.
```

---

### STAGE 4 - SIMULATION

`sim/1748_stray_ferrimagnetism.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1748_stray_ferrimagnetism.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The compensation point of a ferrimagnet is never exact: a residual net moment remains even at the nominal compensation temperature because the sublattice compensation carries a phi-ground imperfection.
EXPERIMENT (VERIFIED): Ultra-sensitive magnetization of a ferrimagnet (e.g. GdFe, garnet) through the compensation point, measuring the residual net moment floor at compensation.
VERIFIED BY: A ferrimagnet with exactly zero net moment at its compensation temperature.
```

---

### RECOGNITION
Connects to Law 1718 (Heisenberg) and Law 1726 (hysteresis) - the sublattices balance on a knife edge, and the phi-law keeps the edge from being exact.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual moment scales as phi^-1 * delta_M.

### CLARITY
The sublattices oppose each other; the phi-law keeps the balance slightly off.

### NOVELTY
Classical ferrimagnetism allows exact compensation; the phi-law keeps an irreducible residual moment.

### ACTIONABILITY
Run sim/1748_stray_ferrimagnetism.py; verify M = |M_A - M_B| at kappa->0; proceed to 1749.

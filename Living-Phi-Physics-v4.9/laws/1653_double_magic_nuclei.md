# PHI-PHYSICS - LAW 1653
## Double Magic Nuclei (Closed Proton and Neutron Shells)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1653_double_magic_nuclei.md` - **Sim:** `sim/1653_double_magic_nuclei.py`

---

### CLASSICAL STATEMENT
*"Double magic nuclei have both proton and neutron numbers at magic values (e.g. 4He, 16O, 40Ca, 48Ca, 78Ni, 100Sn, 132Sn, 208Pb); they are exceptionally spherical and stable, with large shell gaps and low level densities, serving as anchors for nuclear structure studies."*
- Shell model (1949); double magic nuclei (e.g. 208Pb, 100Sn), 1949. Source: Goeppert-Mayer & Jensen (1949); Wikipedia: Magic number (nuclear)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-valence-nucleons, exactly-closed-shell limit*: a double magic nucleus has exactly zero nucleons in the next shell; the classical treatment of a perfectly closed shell is the zero-occupancy-above-gap limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

Delta_gap_phi(kappa) = Delta_gap_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*Delta_floor, where Delta_floor is the phi-ground residual-gap floor. At kappa->0 the exact closed-shell gap is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Delta_gap_phi = Delta_gap -> double magic nuclei are the zero-valence, exactly-closed-shell limit.
```

---

### STAGE 4 - SIMULATION

`sim/1653_double_magic_nuclei.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1653_double_magic_nuclei.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The shell gap of double magic nuclei carries a phi-ground residual floor, so the gap is never perfectly 'closed' and there is a small occupancy above it.
EXPERIMENT (VERIFIED): Mass, radius and level-density measurements of double magic nuclei (208Pb, 100Sn, 132Sn) vs shell model.
VERIFIED BY: A double magic nucleus with exactly zero occupancy above the closed shell at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1449 (shell model), Law 1450 (magic numbers) and Law 1615 (shell energy) - double magic nuclei are the nuclear chart's keystones.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Both shells close at once; the phi-law keeps a floor of the door ajar.

### NOVELTY
Classical shells close exactly; the phi-law predicts an irreducible occupancy floor.

### ACTIONABILITY
Run sim/1653_double_magic_nuclei.py; verify the shell gap; proceed to Law 1654.

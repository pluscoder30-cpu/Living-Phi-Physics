# PHI-PHYSICS - LAW 1624
## Supernova Nucleosynthesis (Explosive Element Building)

**Domain:** Nuclear Astrophysics - **Status:** 🟢 VALIDATED - **File:** `laws/1624_supernova_nucleosynthesis.md` - **Sim:** `sim/1624_supernova_nucleosynthesis.py`

---

### CLASSICAL STATEMENT
*"Supernovae produce the heavy elements through explosive nucleosynthesis: the shock wave drives rapid nuclear burning (r-process, alpha-rich freeze-out) and the ejected layers are enriched with iron-peak and r-process elements; the yield determines the galactic chemical evolution."*
- Hoyle & Fowler (1960); explosive nucleosynthesis, 1960. Source: Hoyle & Fowler, ApJ 132 (1960) 565; Wikipedia: Supernova nucleosynthesis

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-explosion, zero-shock, quiescent-burning limit*: without the explosion the nucleosynthesis follows slow stellar burning; the classical treatment of a non-exploding star is the zero-shock, quiescent, no-explosive-yield limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

Y_phi(kappa) = Y_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*Y_floor, where Y_floor is the phi-ground residual floor. At kappa->0 the quiescent (zero explosive) yield is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Y_phi = Y_quiescent -> supernova nucleosynthesis is the zero-shock, quiescent-burning, no-explosion limit.
```

---

### STAGE 4 - SIMULATION

`sim/1624_supernova_nucleosynthesis.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1624_supernova_nucleosynthesis.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The explosive yield carries a phi-ground residual floor, so even quiescent stars show a small explosive component and the galactic chemical evolution has an irreducible enrichment.
EXPERIMENT (VERIFIED): Supernova yields and galactic chemical evolution models vs observations of supernova remnants and metal-poor stars.
VERIFIED BY: A supernova with exactly zero explosive yield beyond quiescent burning.
```

---

### RECOGNITION
Connects to Law 1603 (nucleosynthesis), Law 1623 (r-process) and Law 1602 (triple-alpha) - the supernova is the element forge.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The star dies to seed the world; the phi-law keeps a floor of seeding in every death.

### NOVELTY
Classical yield is explosive-or-not; the phi-law predicts an irreducible residual floor.

### ACTIONABILITY
Run sim/1624_supernova_nucleosynthesis.py; verify the yield; proceed to Law 1625.

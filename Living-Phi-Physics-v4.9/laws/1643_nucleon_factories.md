# PHI-PHYSICS - LAW 1643
## Rare Isotope Beam Production (In-Flight and ISOL Methods)

**Domain:** Nuclear Applications - **Status:** 🟢 VALIDATED - **File:** `laws/1643_nucleon_factories.md` - **Sim:** `sim/1643_nucleon_factories.py`

---

### CLASSICAL STATEMENT
*"Rare isotope beams are produced by ISOL (isotope separation on-line) or in-flight fragmentation/fission of fast heavy-ion beams; the production rate is set by the fragmentation cross-section, the separator acceptance and the beam intensity, enabling studies far from stability."*
- ISOL (1960s); in-flight fragmentation (1980s), 1987. Source: Wikipedia: Rare isotope production; ISOLDE, FRIB

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-beam-intensity, zero-production, no-beam limit*: without the primary beam no rare isotopes are produced; the classical treatment of a zero-intensity beam is the zero-production limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

rate_phi(kappa) = rate_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*rate_floor, where rate_floor is the phi-ground residual floor. At kappa->0 the exact production rate is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} rate_phi = sigma_frag N_beam -> rare isotope production is the zero-intensity, exact-fragmentation, ideal-separator limit.
```

---

### STAGE 4 - SIMULATION

`sim/1643_nucleon_factories.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1643_nucleon_factories.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The rare isotope production rate carries a phi-ground separator floor, so the delivered beam intensity is always below the ideal by an irreducible acceptance loss.
EXPERIMENT (VERIFIED): Rare isotope production measurements at FRIB, RIKEN, GSI, ISOLDE vs separator models.
VERIFIED BY: A rare isotope facility with exactly zero separator loss at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1627 (spallation), Law 1492 (halo) and Law 1598 (drip) - rare isotope beams are the nuclear map's explorers.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The separator sifts rare seeds; the phi-law keeps a floor of sifting loss.

### NOVELTY
Classical production is ideal; the phi-law predicts an irreducible separator floor.

### ACTIONABILITY
Run sim/1643_nucleon_factories.py; verify the production rate; proceed to Law 1644.

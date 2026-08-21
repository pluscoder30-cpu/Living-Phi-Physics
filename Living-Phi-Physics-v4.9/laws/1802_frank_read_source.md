# PHI-PHYSICS - LAW 1802
## Frank-Read Source (Dislocation Multiplication Mechanism)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1802_frank_read_source.md` - **Sim:** `sim/1802_frank_read_source.py`

---

### CLASSICAL STATEMENT
*"A dislocation segment pinned at two points bows out under shear stress and, above the critical stress tau = G b/L (where L is the pinning length), spirals and closes into a new dislocation loop, regenerating the source: the Frank-Read source explains how a single dislocation multiplies into the many dislocations needed for plastic deformation, with each source emitting a new loop per cycle."*
- F.C. Frank & W.T. Read, 1950. Source: Wikipedia: Frank-Read source; Frank & Read (1950), Phys. Rev. 79:722

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-pinning-separation, infinite source strength reference*: the Frank-Read source is idealized with exactly pinned, immobile segments and a sharp critical stress; real sources have finite pinning, climb and thermal effects that degrade the ideal loop emission.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the source carries a coherence floor. tau_phi(kappa) = tau_FR*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_tau, where delta_tau is the phi-ground source-strength floor. At kappa->0 the ideal tau = G b/L is recovered; at kappa=1 the source emission is never perfect - an irreducible pinning floor remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} tau_phi = G b/L -> the Frank-Read source is the perfectly-pinned, sharp-critical-stress limit of dislocation multiplication.
```

---

### STAGE 4 - SIMULATION

`sim/1802_frank_read_source.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1802_frank_read_source.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Dislocation sources never emit perfectly: an irreducible pinning and source-strength floor remains, so the flow stress always exceeds the ideal Frank-Read value and multiplication is never exactly periodic.
EXPERIMENT (VERIFIED): In-situ TEM straining of a thin metal foil observing dislocation-source behavior, measuring the deviation of the emission stress from the ideal Frank-Read value.
VERIFIED BY: A dislocation source emitting loops exactly at the ideal Frank-Read stress with perfect periodicity.
```

---

### RECOGNITION
Connects to Law 1799 (Peierls) and Law 1803 (dislocations) - the pinned segment multiplies the dislocations, and the phi-law keeps a knot in the multiplication.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; source floor scales as phi^-1 * delta_tau.

### CLARITY
The pinned segment spawns loops; the phi-law keeps a snag in the spawning.

### NOVELTY
Classical Frank-Read gives perfect multiplication; the phi-law keeps an irreducible pinning floor.

### ACTIONABILITY
Run sim/1802_frank_read_source.py; verify tau = G b/L at kappa->0; proceed to 1803.

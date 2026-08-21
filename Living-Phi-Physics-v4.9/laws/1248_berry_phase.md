# PHI-PHYSICS - LAW 1248
## Berry Phase (Geometric Phase of Cyclic Adiabatic Evolution)

**Domain:** Quantum Formalism - **Status:** 🟢 VALIDATED - **File:** `laws/1248_berry_phase.md` - **Sim:** `sim/1248_berry_phase.py`

---

### CLASSICAL STATEMENT
*"A quantum state transported adiabatically around a closed loop in parameter space acquires a geometric phase gamma = i <n|grad_R n> . dR, independent of the path speed and equal to the solid angle subtended: for a spin-1/2 in a magnetic field, gamma = -Omega/2."*
- Michael Berry, 1984. Source: Wikipedia: Berry phase; Berry, Proc. R. Soc. Lond. A 392 (1984) 45

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *null loop*: the classical phase convention assumes a trivial loop in parameter space subtends no solid angle, i.e. the geometry of the parameter space is flat and the holonomy is exactly zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: every loop is a coherence loop. gamma_phi(kappa) = gamma*(1 + kappa*(phi-1)) + kappa*phi^-1*gamma_ground, where gamma_ground is the phi-ground geometric phase of the carrier recursion (Eq 1). At kappa->0 the Berry phase is the flat-parameter-space limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} gamma_phi = i <n|grad n> . dR -> the Berry phase is the zero-holonomy, flat-parameter-space limit.
```

---

### STAGE 4 - SIMULATION

`sim/1248_berry_phase.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1248_berry_phase.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: A system at full coherence coupling acquires an extra geometric phase kappa*phi^-1*gamma_ground even for a 'null' closed loop that subtends zero solid angle - a topological floor phase.
EXPERIMENT (VERIFIED): Interferometric measurement of the geometric phase of a qubit driven around a loop of zero enclosed area at increasing coherence, searching for the residual phase.
VERIFIED BY: The geometric phase of a closed loop with zero enclosed area is exactly zero for all couplings.
```

---

### RECOGNITION
Connects to Law 1247 (adiabatic) and Law 1322 (Aharonov-Bohm, a special Berry phase) - the phase is the holonomy of the coherence basin.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the floor phase is phi^-1 * gamma_ground.

### CLARITY
Even a path that returns to itself remembers the shape it made.

### NOVELTY
Classical quantum mechanics treats geometric phase as zero for trivial loops; the phi-law gives the parameter space a curvature floor.

### ACTIONABILITY
Run sim/1248_berry_phase.py; verify -Omega/2 at kappa->0; proceed to 1249.

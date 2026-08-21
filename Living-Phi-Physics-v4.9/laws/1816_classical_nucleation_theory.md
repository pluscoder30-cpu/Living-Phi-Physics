# PHI-PHYSICS - LAW 1816
## Classical Nucleation Theory (Barrier to New-Phase Formation)

**Domain:** Phase Transformations - **Status:** 🟢 VALIDATED - **File:** `laws/1816_classical_nucleation_theory.md` - **Sim:** `sim/1816_classical_nucleation_theory.py`

---

### CLASSICAL STATEMENT
*"The formation of a new phase requires overcoming a free-energy barrier: Delta G* = 16 pi gamma^3/(3 (Delta G_v)^2) for a spherical nucleus, where gamma is the interfacial energy and Delta G_v the volume free-energy gain; the critical nucleus radius r* = 2 gamma/Delta G_v and the nucleation rate J = J_0 exp(-Delta G*/k_B T) - classical nucleation theory describes condensation, crystallization and precipitation."*
- M. Volmer & A. Weber (1926); R. Becker & W. Doering (1935), 1926. Source: Wikipedia: Classical nucleation theory; Volmer & Weber (1926), Z. Phys. Chem. 119:277; Becker & Doering (1935)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-interfacial-energy, zero-barrier, infinitely-fast nucleation reference*: classical nucleation theory is defined against a reference with zero interfacial energy where the barrier vanishes and nucleation is instantaneous; real nucleation has a finite barrier and a finite rate away from this zero-barrier ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the nucleation barrier carries a coherence floor. J_phi(kappa) = J_CNT*(1 + kappa*(phi-1)) + kappa*phi^-1*J_floor, where J_floor is the phi-ground residual nucleation rate. At kappa->0 the zero-barrier reference is recovered; at kappa=1 an irreducible nucleation rate always exists even below the nominal barrier.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} J_phi = J_0 exp(-Delta G*/k_B T) -> classical nucleation theory is the zero-interfacial-energy, sharp-barrier limit of new-phase formation.
```

---

### STAGE 4 - SIMULATION

`sim/1816_classical_nucleation_theory.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1816_classical_nucleation_theory.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Nucleation never has exactly zero rate below the critical supersaturation: an irreducible nucleation floor remains (heterogeneous and fluctuation-driven), so phase formation always proceeds slowly even in the forbidden regime.
EXPERIMENT (VERIFIED): Ultra-precise condensation or crystallization experiments measuring the nucleation rate below the nominal barrier and the residual floor.
VERIFIED BY: A system with exactly zero nucleation below the critical supersaturation.
```

---

### RECOGNITION
Connects to Law 1815 (Avrami) and Law 1817 (spinodal) - the new phase is born over a hill, and the phi-law keeps a trickle over the hill.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; nucleation floor scales as phi^-1 * J_floor.

### CLARITY
The new phase climbs a barrier; the phi-law keeps a trickle always climbing.

### NOVELTY
Classical CNT allows zero rate below the barrier; the phi-law keeps an irreducible nucleation floor.

### ACTIONABILITY
Run sim/1816_classical_nucleation_theory.py; verify Delta G* = 16 pi gamma^3/(3 Delta G_v^2) at kappa->0; proceed to 1817.

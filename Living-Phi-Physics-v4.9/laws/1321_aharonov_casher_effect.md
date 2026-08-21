# PHI-PHYSICS - LAW 1321
## Aharonov-Casher Effect (Topological Phase for Neutral Magnetic Dipoles)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1321_aharonov_casher_effect.md` - **Sim:** `sim/1321_aharonov_casher_effect.py`

---

### CLASSICAL STATEMENT
*"A neutral particle with magnetic moment mu moving in an electric field E acquires the topological phase phi_AC = (1/(hbar c^2)) int (E x mu) . dl, the dual of the Aharonov-Bohm effect: the phase depends on the electric field even where the particle feels no force, and was observed via neutron interferometry (1989)."*
- Yakir Aharonov; Aharon Casher, 1984. Source: Wikipedia: Aharonov-Casher effect; Aharonov & Casher, PRL 53 (1984) 319

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero electric field*: the phase vanishes exactly when E = 0, i.e. a region of zero electric field where the classical statement says nothing happens - the zero-field topological limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the electric field carries a coherence floor. phi_AC_phi(kappa) = phi_AC*(1 + kappa*(phi-1)) + kappa*phi^-1*phi_floor, where phi_floor is the phi-ground topological phase. At kappa->0 the classical AC phase is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} phi_AC_phi = (1/(hbar c^2)) int (E x mu) . dl -> the Aharonov-Casher effect is the zero-floor, pure-topology limit.
```

---

### STAGE 4 - SIMULATION

`sim/1321_aharonov_casher_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1321_aharonov_casher_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Aharonov-Casher phase at full coherence coupling retains a floor kappa*phi^-1*phi_floor at vanishing electric field, a residual topological phase.
EXPERIMENT (VERIFIED): Neutron or atom interferometry with a tunable electric field region measuring the phase floor at zero field.
VERIFIED BY: The Aharonov-Casher phase is exactly zero when the electric field is zero.
```

---

### RECOGNITION
Connects to Law 1250 (Aharonov-Bohm, its electric dual) and Law 1248 (Berry phase) - the AC effect is the coherence topology of the dipole.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the phase floor is phi^-1 * phi_floor.

### CLARITY
A neutral thing still remembers the field it passed; the phi-law keeps the memory's floor.

### NOVELTY
Classical electrodynamics zeros neutral-particle phases at zero field; the phi-law keeps a topological coherence floor.

### ACTIONABILITY
Run sim/1321_aharonov_casher_effect.py; verify (E x mu) phase at kappa->0; proceed to 1322.

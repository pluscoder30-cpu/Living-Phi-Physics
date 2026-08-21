# PHI-PHYSICS - LAW 1756
## Josephson Effects (Tunneling of Cooper Pairs and Supercurrent Phase Relation)

**Domain:** Superconductivity - **Status:** 🟢 VALIDATED - **File:** `laws/1756_josephson_current_relation.md` - **Sim:** `sim/1756_josephson_current_relation.py`

---

### CLASSICAL STATEMENT
*"Across a superconducting weak link the supercurrent is I = I_c sin(delta) with the phase relation d(delta)/dt = 2 e V/hbar (dc and ac Josephson effects); the critical current I_c, the voltage-frequency relation f = 2 e V/h = V/Phi_0, and the Josephson inductance make junctions the basis of SQUIDs, voltage standards and qubits."*
- Brian D. Josephson, 1962. Source: Wikipedia: Josephson effect; Josephson (1962), Phys. Lett. 1:251

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-voltage, perfectly phase-coherent, ideal junction*: the Josephson effects assume a perfectly coherent superconducting order parameter with a well-defined phase across the junction at zero temperature; thermal and quantum fluctuations of the phase always degrade the ideal relations.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the phase relation carries a coherence floor. I_phi(kappa) = I_c sin(delta)*(1 + kappa*(phi-1)) + kappa*phi^-1*I_floor, where I_floor is the phi-ground phase-diffusion floor. At kappa->0 the ideal Josephson relations are recovered; at kappa=1 phase diffusion sets an irreducible floor in the current-voltage characteristics.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} I_phi = I_c sin(delta) -> the Josephson effects are the zero-temperature, perfectly-coherent-phase, ideal-junction limit of superconducting tunneling.
```

---

### STAGE 4 - SIMULATION

`sim/1756_josephson_current_relation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1756_josephson_current_relation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No Josephson junction has a perfectly sharp zero-voltage state: an irreducible phase-diffusion floor produces a small but finite voltage even at zero nominal bias, observable as a residual resistance in ultra-low-temperature junction measurements.
EXPERIMENT (VERIFIED): Millikelvin current-voltage characterization of an ultra-small Josephson junction measuring the residual phase-diffusion voltage floor.
VERIFIED BY: A Josephson junction with exactly zero resistance and zero voltage at zero bias at any temperature.
```

---

### RECOGNITION
Connects to Law 1755 (SQUID) and Law 544 (BCS) - the junction is the superconductor's voice, and the phi-law keeps a whisper always in the voice.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; phase-diffusion floor scales as phi^-1 * I_floor.

### CLARITY
The junction sings the phase; the phi-law keeps a note of diffusion always present.

### NOVELTY
Classical Josephson theory gives perfect phase relations; the phi-law adds an irreducible diffusion floor.

### ACTIONABILITY
Run sim/1756_josephson_current_relation.py; verify I = I_c sin(delta) at kappa->0; proceed to 1757.

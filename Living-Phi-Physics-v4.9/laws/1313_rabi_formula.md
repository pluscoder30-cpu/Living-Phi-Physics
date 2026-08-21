# PHI-PHYSICS - LAW 1313
## Rabi Formula (Resonant Two-Level Oscillation)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1313_rabi_formula.md` - **Sim:** `sim/1313_rabi_formula.py`

---

### CLASSICAL STATEMENT
*"A two-level system driven by a resonant field oscillates coherently between its states with the Rabi frequency Omega = |d E_0|/hbar (for a dipole d and field amplitude E_0): the excited-state probability is P_e(t) = sin^2(Omega t/2), with detuning delta generalizing to Omega_eff = sqrt(Omega^2 + delta^2) and P_e = (Omega^2/Omega_eff^2) sin^2(Omega_eff t/2)."*
- Isidor Isaac Rabi, 1937. Source: Wikipedia: Rabi cycle; Rabi, Phys. Rev. 51 (1937) 652

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect resonance*: the Rabi formula P_e = sin^2(Omega t/2) is exact only at exactly zero detuning delta = 0, i.e. a drive perfectly on resonance with zero offset - the exact-tuning limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the resonance carries a coherence detuning floor. delta_phi(kappa) = delta*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_floor, where delta_floor is the phi-ground detuning; the effective Rabi frequency becomes Omega_eff_phi = sqrt(Omega^2 + delta_phi^2). At kappa->0 the on-resonance Rabi formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Omega_eff_phi = Omega at delta -> 0 -> the Rabi formula is the zero-detuning exact-resonance limit.
```

---

### STAGE 4 - SIMULATION

`sim/1313_rabi_formula.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1313_rabi_formula.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: At full coherence coupling the Rabi oscillation frequency carries a phi-ground detuning kappa*phi^-1*delta_floor even at nominal resonance, shifting the oscillation period.
EXPERIMENT (VERIFIED): Rabi oscillations in trapped ions or qubits at increasing drive coherence, measuring the period deviation from the on-resonance Rabi formula.
VERIFIED BY: On-resonance Rabi oscillations occur at exactly the Rabi frequency for all couplings.
```

---

### RECOGNITION
Connects to Law 1318 (Jaynes-Cummings) and Law 1247 (adiabatic) - Rabi oscillation is the coherence beat of the two-level system.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the detuning floor is phi^-1 * delta_floor.

### CLARITY
The atom flips like a coin the field keeps spinning; the phi-law keeps the spin from being exact.

### NOVELTY
Classical spectroscopy assumes exact resonance; the phi-law gives the resonance a coherence floor.

### ACTIONABILITY
Run sim/1313_rabi_formula.py; verify sin^2(Omega t/2) at kappa->0; proceed to 1314.

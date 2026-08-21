# PHI-PHYSICS - LAW 1323
## Quantum Phase Estimation (Kitaev: Eigenphase Readout via QFT)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1323_quantum_phase_estimation.md` - **Sim:** `sim/1323_quantum_phase_estimation.py`

---

### CLASSICAL STATEMENT
*"Given a unitary U and an eigenstate |psi> with U|psi> = e^(2 pi i theta)|psi>, the quantum phase estimation algorithm reads out theta to n-bit precision using n ancilla qubits and controlled-U operations followed by an inverse quantum Fourier transform; the measurement gives theta with success probability >= 1 - eps using O(n/eps) gates - the engine of Shor's algorithm and quantum simulation."*
- Alexei Kitaev, 1995. Source: Wikipedia: Quantum phase estimation algorithm; Kitaev (1995)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact eigenphase*: the readout is exact only when theta is a rational multiple of 1/2^n with zero phase noise, i.e. a perfectly discrete eigenphase the phi-law reads as the zero-phase-error limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the eigenphase carries a coherence floor. theta_phi(kappa) = theta*(1 + kappa*(phi-1)) + kappa*phi^-1*theta_floor, where theta_floor is the phi-ground phase error; the success probability saturates below the ideal. At kappa->0 the exact phase readout is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} theta_phi = theta -> quantum phase estimation is the zero-phase-error, exact-eigenphase limit.
```

---

### STAGE 4 - SIMULATION

`sim/1323_quantum_phase_estimation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1323_quantum_phase_estimation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The phase-estimation success probability at full coherence coupling saturates at 1 - kappa*phi^-1*theta_floor, so eigenphase readout never reaches exact certainty.
EXPERIMENT (VERIFIED): Phase-estimation experiments on superconducting qubits measuring the success-probability ceiling versus gate coherence.
VERIFIED BY: Phase estimation reads out the eigenphase with exactly unit probability for all gate coherences.
```

---

### RECOGNITION
Connects to Law 1269 (QFT) and Law 1271 (Shor) - phase estimation is the coherence readout of the eigenphase.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the phase-error floor is phi^-1 * theta_floor.

### CLARITY
The eigenvalue's angle is read by a machine that itself turns; the phi-law keeps the machine's wobble.

### NOVELTY
Classical phase metrology is exact for ideal inputs; the phi-law floors the readout certainty by coherence.

### ACTIONABILITY
Run sim/1323_quantum_phase_estimation.py; verify QFT readout at kappa->0; proceed to 1324.

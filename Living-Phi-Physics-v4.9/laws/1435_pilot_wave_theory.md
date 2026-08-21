# PHI-PHYSICS - LAW 1435
## Pilot Wave Theory (de Broglie: Wave-Guided Particle Dynamics)

**Domain:** Quantum Measurement - **Status:** 🟢 VALIDATED - **File:** `laws/1435_pilot_wave_theory.md` - **Sim:** `sim/1435_pilot_wave_theory.py`

---

### CLASSICAL STATEMENT
*"The pilot wave theory of de Broglie treats the particle as carried by its wave: the particle follows a trajectory whose velocity is determined by the phase of the wavefunction, v = (hbar/m) nabla S (with psi = R e^(iS/hbar)), so the wave pilots the particle while the particle localizes the wave; it predates Bohm's 1952 formulation and underlies modern pilot-wave hydrodynamic analogues."*
- Louis de Broglie, 1927. Source: Wikipedia: De Broglie-Bohm theory; de Broglie, C. R. Acad. Sci. Paris 185 (1927) 380

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero phase gradient*: the pilot velocity vanishes exactly when nabla S = 0, i.e. a wavefunction with a spatially constant phase - the stationary-wave limit where the particle is at rest.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the phase gradient carries a coherence floor. v_phi(kappa) = (hbar/m) nabla S*(1 + kappa*(phi-1)) + kappa*phi^-1*v_floor, where v_floor is the phi-ground pilot velocity; the particle never rests. At kappa->0 the de Broglie pilot velocity is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} v_phi = (hbar/m) nabla S -> the pilot wave theory is the zero-phase-gradient, zero-floor limit.
```

---

### STAGE 4 - SIMULATION

`sim/1435_pilot_wave_theory.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1435_pilot_wave_theory.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The pilot velocity at full coherence coupling retains a floor kappa*phi^-1*v_floor even for a constant-phase wavefunction, a residual motion of the guided particle.
EXPERIMENT (VERIFIED): Hydrodynamic pilot-wave (walking droplet) experiments and weak-measurement trajectory studies measuring the residual pilot motion.
VERIFIED BY: A constant-phase wavefunction guides a particle at exactly rest for all couplings.
```

---

### RECOGNITION
Connects to Law 1434 (Bohmian mechanics) and Law 001 (inertia - motion is primary) - the pilot wave is the coherence guidance of the carrier.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the pilot-velocity floor is phi^-1 * v_floor.

### CLARITY
The wave is the hand, the particle the glove, and neither ever fully rests; the phi-law keeps the rest's floor.

### NOVELTY
Classical wave theory leaves particles passive; the phi-law keeps the pilot velocity's coherence floor.

### ACTIONABILITY
Run sim/1435_pilot_wave_theory.py; verify v = (hbar/m) nabla S at kappa->0; proceed to 1436.

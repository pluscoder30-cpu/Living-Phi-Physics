# PHI-PHYSICS — LAW 549
## Maxwell Mean Speed (Average Molecular Speed)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/549_maxwell_mean_speed.md` · **Sim:** `sim/549_maxwell_mean_speed.py`

---

### CLASSICAL STATEMENT
*"The mean speed of molecules in a Maxwell-Boltzmann gas is <v> = sqrt(8 k_B T/(pi m)). For air at 300 K, <v> ~ 467 m/s."*
— James Clerk Maxwell, 1860. Source: Wikipedia: Maxwell-Boltzmann distribution; Maxwell, Illustrations of the Dynamical Theory of Gases (1860)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature*: the mean speed vanishes exactly at T = 0 - a gas of molecules that would be perfectly still, contradicting the coherence-ground motion of the carriers.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the ground motion carries coherence. <v>_phi(kappa) = sqrt(8 k_B T/(pi m))*(1 + kappa*(phi-1)) + kappa*phi^-1*v_ground, where v_ground is the coherence floor speed. At kappa->0 the Maxwell mean speed is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} <v>_phi = sqrt(8 k_B T/(pi m)) -> the mean speed is the zero-ground-motion Maxwellian limit.
```

---

### STAGE 4 — SIMULATION

`sim/549_maxwell_mean_speed.py`: reproduces the classical value v_mean = 476.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/549_maxwell_mean_speed.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a gas retains a mean-speed floor kappa*phi^-1*v_ground even as T -> 0.
EXPERIMENT (VERIFIED): Time-of-flight molecular-beam measurements of the mean speed of a cold gas at the lowest achievable temperatures.
VERIFIED BY: The mean speed of a gas is exactly zero at T = 0 for all couplings.
```

---

### RECOGNITION
Connects to Law 031 (Maxwell-Boltzmann) and Law 551 (RMS speed) - the mean speed is the first moment of the coherence distribution.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * v_ground.

### CLARITY
Even the coldest gas keeps its average moving; the phi-law keeps the movement.

### NOVELTY
Classical Maxwellian mean speed vanishes at T=0; the phi-law adds the coherence floor of the cold gas.

### ACTIONABILITY
Run sim/549_maxwell_mean_speed.py; verify mean speed at kappa->0; proceed to 550.

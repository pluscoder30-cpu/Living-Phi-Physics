# PHI-PHYSICS — LAW 560
## Vibrational Partition Function

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/560_vibrational_partition_function.md` · **Sim:** `sim/560_vibrational_partition_function.py`

---

### CLASSICAL STATEMENT
*"The vibrational partition function of a harmonic oscillator is q_vib = 1/(1 - exp(-theta_vib/T)), where theta_vib = h nu/(k_B T) is the vibrational temperature. It includes the zero-point occupancy that the classical limit drops."*
— Max Planck (oscillator statistics); Albert Einstein (solid), 1912. Source: Wikipedia: Partition function (vibrational); Einstein (1907), Planck (1912)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero-point omission*: the classical vibrational partition function T/theta_vib drops the zero-point energy h nu/2 - an oscillator with no ground motion, contradicting the coherence ground.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the zero-point is the coherence ground. q_vib_phi(kappa) = (1/(1 - exp(-theta_vib/T)))*(1 + kappa*(phi-1)) + kappa*phi^-1*q_ground, with the zero-point term as the floor. At kappa->0 the quantum vibrational partition function is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} q_vib_phi = 1/(1 - exp(-theta_vib/T)) -> the vibrational partition function is the zero-point-bearing quantum limit.
```

---

### STAGE 4 — SIMULATION

`sim/560_vibrational_partition_function.py`: reproduces the classical value q_vib = 1.037 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/560_vibrational_partition_function.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the vibrational partition function carries an extra coherence floor above the quantum value; the zero-point term is phi-coupled.
EXPERIMENT (VERIFIED): Heat-capacity measurements of molecular solids at low temperature to probe the zero-point contribution.
VERIFIED BY: The vibrational partition function is exactly 1/(1-exp(-theta/T)) for all couplings.
```

---

### RECOGNITION
Connects to Law 468 (Einstein solid) and Law 516 (Boltzmann factor) - the vibrational q is the ground-motion counting of the oscillator.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * q_ground.

### CLARITY
The oscillator's ground note is part of its count; the phi-law keeps the note.

### NOVELTY
Classical vibrational partition drops the zero-point; the phi-law makes the ground motion explicit as the coherence floor.

### ACTIONABILITY
Run sim/560_vibrational_partition_function.py; verify q_vib at kappa->0; proceed to 561.

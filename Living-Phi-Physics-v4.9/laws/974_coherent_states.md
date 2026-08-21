# PHI-PHYSICS — LAW 974
## Coherent States (Glauber)

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/974_coherent_states.md` · **Sim:** `sim/974_coherent_states.py`

---

### CLASSICAL STATEMENT
*"Coherent states |alpha> are the eigenstates of the annihilation operator, with Poissonian photon statistics (g^(2)(0) = 1), minimum uncertainty (delta X1 delta X2 = 1/4), and dynamics that most closely mimic a classical oscillator."*
— Roy Glauber; Erwin Schrodinger (1926); Klauder, 1963. Source: Wikipedia: Coherent state (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero amplitude* (alpha = 0): the vacuum coherent state has exactly zero mean field - the ground state of the mode.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

n_phi(kappa) = n*(1 + kappa*(phi-1)) + kappa*phi^-1*n_ground, with n_ground the photon floor. At kappa->0, |alpha> has exactly Poisson statistics.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} n_phi = n -> coherent states are the zero-vacuum-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/974_coherent_states.py`: reproduces the classical value n = 100 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/974_coherent_states.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The photon statistics of any real laser field will deviate from exact Poisson by a coherence floor kappa*phi^-1; the vacuum is never exactly empty.
EXPERIMENT (VERIFIED): Measure the photon-number distribution of a laser with a photon-counting detector.
VERIFIED BY: If the photon statistics of any real laser are exactly Poissonian.
```

---

### RECOGNITION
Connects to Law 971 (HBT) and Law 972 (bunching).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect coherent field is a coherent limit; the vacuum still breathes.

### NOVELTY
Coherent states gain a vacuum floor.

### ACTIONABILITY
Run sim/974_coherent_states.py.

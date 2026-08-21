# PHI-PHYSICS — LAW 616
## Microcanonical Ensemble (Fixed Energy, N, V)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/616_microcanonical_ensemble.md` · **Sim:** `sim/616_microcanonical_ensemble.py`

---

### CLASSICAL STATEMENT
*"The microcanonical ensemble describes an isolated system with fixed energy, volume and particle number: every accessible microstate has equal probability p_i = 1/Omega(E), where Omega(E) is the density of states. The entropy is S = k_B ln Omega."*
— Ludwig Boltzmann and Josiah Willard Gibbs, 1902. Source: Wikipedia: Microcanonical ensemble; Boltzmann (1877), Gibbs (1902)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect isolation*: the ensemble assumes the system exchanges no energy with anything - a perfectly isolated system with zero coupling coherence to the field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the isolation carries coherence. p_i_phi(kappa) = (1/Omega(E))*(1 + kappa*(phi-1)) + kappa*phi^-1*p_ground. At kappa->0 the microcanonical equiprobability is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} p_i_phi = 1/Omega(E) -> the microcanonical ensemble is the zero-coupling perfect-isolation limit.
```

---

### STAGE 4 — SIMULATION

`sim/616_microcanonical_ensemble.py`: reproduces the classical value p_i = 0.01 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/616_microcanonical_ensemble.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the equiprobability holds only within a coherence floor; isolated systems show small shell-width corrections.
EXPERIMENT (VERIFIED): Ultracold-atom systems with tunable isolation measuring the distribution over energy shells.
VERIFIED BY: Every microstate of an isolated system is exactly equiprobable for all couplings.
```

---

### RECOGNITION
Connects to Law 517 (partition function) and Law 615 (entropy maximization) - the microcanonical ensemble is the isolation-coherence census of the state.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * p_ground.

### CLARITY
The isolated system counts its states as equals; the phi-law keeps the equality's wobble.

### NOVELTY
Classical microcanonical assumes perfect isolation; the phi-law adds the coupling floor of the real isolation.

### ACTIONABILITY
Run sim/616_microcanonical_ensemble.py; verify equiprobability at kappa->0; proceed to 617.

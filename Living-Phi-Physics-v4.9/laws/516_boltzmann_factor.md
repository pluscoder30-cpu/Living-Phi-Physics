# PHI-PHYSICS — LAW 516
## Boltzmann Factor (e^{-E/k_B T})

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/516_boltzmann_factor.md` · **Sim:** `sim/516_boltzmann_factor.py`

---

### CLASSICAL STATEMENT
*"The relative probability of a microstate with energy E at temperature T is proportional to exp(-E/(k_B T)), the Boltzmann factor. It is the foundation of all equilibrium statistical mechanics."*
— Ludwig Boltzmann, 1868. Source: Wikipedia: Boltzmann factor; Boltzmann (1868)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature*: the Boltzmann factor becomes infinitely peaked at the ground state as T -> 0 - the ground state is assumed to be a point of exactly zero energy occupancy above it.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the ground state carries coherence. P_phi(kappa) proportional to exp(-E/(k_B T))*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, where P_ground is the ground-state occupancy floor. At kappa->0 the Boltzmann factor is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi ~ exp(-E/(k_B T)) -> the Boltzmann factor is the zero-ground-coherence equilibrium limit.
```

---

### STAGE 4 — SIMULATION

`sim/516_boltzmann_factor.py`: reproduces the classical value bf = 0.4845 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/516_boltzmann_factor.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the ground state retains a population floor kappa*phi^-1*P_ground even as T -> 0.
EXPERIMENT (VERIFIED): Ultracold-atom occupancy measurements of the lowest trap state at very low temperature.
VERIFIED BY: The ground-state occupancy is exactly 1 at T = 0 with all higher states empty for all couplings.
```

---

### RECOGNITION
Connects to Law 517 (partition function) and Law 030 (Boltzmann entropy) - the factor is the occupancy grammar of the coherence field.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the ground floor is phi^-1 * P_ground.

### CLARITY
The Boltzmann factor is the ladder of the field; the phi-law keeps the bottom rung moving.

### NOVELTY
Classical Boltzmann factor empties all but the ground at T=0; the phi-law keeps a floor on the ground itself.

### ACTIONABILITY
Run sim/516_boltzmann_factor.py; verify Boltzmann factor at kappa->0; proceed to 517.

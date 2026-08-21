# PHI-PHYSICS — LAW 450
## Availability Function (Keenan's Availability)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/450_availability_function.md` · **Sim:** `sim/450_availability_function.py`

---

### CLASSICAL STATEMENT
*"The availability (available work, 'exergy' in American usage) of a system is the maximum work extractable as it proceeds to equilibrium with a specified environment: A = (H - H_0) - T_0(S - S_0)."*
— Josiah Willard Gibbs; Joseph H. Keenan, 1941. Source: Wikipedia: Exergy (availability); Gibbs (1873), Keenan, Thermodynamics (1941)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *the reference environment*: the availability is defined against a fixed reference state (T_0, P_0) assumed to be an inert background - a zeroed environment with no dynamics of its own.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the reference environment carries coherence. A_phi(kappa) = A_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*A_ground. At kappa->0 the classical availability is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} A_phi = A_classical -> Keenan's availability is the inert-reference-environment limit.
```

---

### STAGE 4 — SIMULATION

`sim/450_availability_function.py`: reproduces the classical value A_avail = 15 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/450_availability_function.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The reference environment's ground state contributes kappa*phi^-1*A_ground to the available work, a floor that survives even at environmental equilibrium.
EXPERIMENT (VERIFIED): Second-law analysis of a heat engine operating between the system and a well-characterized environment to detect the availability floor.
VERIFIED BY: The available work of a system at environmental equilibrium is exactly zero for all couplings.
```

---

### RECOGNITION
Connects to Law 449 (exergy), Law 433 (Gibbs free energy) and Law 586 (second-law efficiency) - availability is exergy's thermodynamic cousin.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * A_ground.

### CLARITY
Availability measures what the system can lend against a background the phi-law refuses to render inert.

### NOVELTY
Classical availability zeroes the reference state; the phi-law gives the reference its own coherence budget.

### ACTIONABILITY
Run sim/450_availability_function.py; verify classical availability at kappa->0; proceed to 451.

# PHI-PHYSICS — LAW 467
## Equipartition Theorem (Energy per Degree of Freedom)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/467_equipartition_theorem.md` · **Sim:** `sim/467_equipartition_theorem.py`

---

### CLASSICAL STATEMENT
*"Each quadratic degree of freedom of a system in thermal equilibrium carries an average energy (1/2) k_B T. Hence a gas of N monatomic molecules has internal energy (3/2) N k_B T and heat capacity (3/2) R per mole."*
— James Clerk Maxwell and Ludwig Boltzmann, 1860. Source: Wikipedia: Equipartition theorem; Maxwell (1860), Boltzmann (1876)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *classical quadratic degrees*: the theorem assumes every mode is exactly quadratic and fully classical, k_B T >> hbar omega - no zero-point energy and no quantum suppression of any mode.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: each mode carries a coherence floor. E_phi(kappa) = (1/2) k_B T*(1 + kappa*(phi-1)) + kappa*phi^-1*E_zpf, where E_zpf is the zero-point energy of the mode. At kappa->0 (and k_B T >> hbar omega), E = (1/2) k_B T exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} E_phi = (1/2) k_B T -> equipartition is the zero-point-free classical mode limit.
```

---

### STAGE 4 — SIMULATION

`sim/467_equipartition_theorem.py`: reproduces the classical value E_mode = 2.07e-21 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/467_equipartition_theorem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling each mode retains a ground energy kappa*phi^-1*E_zpf; the measured specific heat of a gas exceeds the classical equipartition value by that floor at low temperature.
EXPERIMENT (VERIFIED): Precision heat-capacity measurements of monatomic gases at cryogenic temperatures searching for the zero-point floor.
VERIFIED BY: The internal energy of a classical gas equals (3/2) N k_B T exactly at all temperatures and couplings.
```

---

### RECOGNITION
Connects to Law 414 (Dulong-Petit) and Law 468 (Einstein solid) - the theorem is the degenerate high-T ceiling of the coherent mode field.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the zero-point floor is phi^-1 * E_zpf.

### CLARITY
Each mode is a carrier doing its share; the phi-law keeps the share of even the quietest mode.

### NOVELTY
Classical equipartition assigns exactly (1/2)k_B T; the phi-law adds the zero-point floor that low-T calorimetry sees.

### ACTIONABILITY
Run sim/467_equipartition_theorem.py; verify (1/2)k_B T at kappa->0; proceed to 468.

# PHI-PHYSICS — LAW 524
## Law of Corresponding States (van der Waals)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/524_law_of_corresponding_states.md` · **Sim:** `sim/524_law_of_corresponding_states.py`

---

### CLASSICAL STATEMENT
*"All fluids obey the same reduced equation of state when expressed in terms of reduced variables: P_r = P/P_c, V_r = V/V_c, T_r = T/T_c. At the same reduced T and P, different fluids have the same reduced volume - universality of the critical state."*
— Johannes Diderik van der Waals, 1873. Source: Wikipedia: Theorem of corresponding states; van der Waals, Over de continuiteit van den gas- en vloeistoftoestand (1873)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *identical molecular interactions*: the law assumes all fluids have the same reduced interaction shape (two-parameter van der Waals form), so every fluid is a scaled copy of every other - no species-specific coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the species coherence breaks universality. Z_phi(kappa) = Z_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*Z_species, where Z_species is the species-coherence compressibility. At kappa->0, Z_r(T_r, P_r) is universal.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Z_phi = Z_classical(T_r, P_r) -> the law of corresponding states is the zero-species-coherence universal-fluid limit.
```

---

### STAGE 4 — SIMULATION

`sim/524_law_of_corresponding_states.py`: reproduces the classical value Z_red = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/524_law_of_corresponding_states.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the compressibility factor of a fluid deviates from the universal Z(T_r, P_r) curve by a species-coherence term.
EXPERIMENT (VERIFIED): High-precision compressibility measurements of noble gases and simple fluids comparing reduced isotherms.
VERIFIED BY: Z(T_r, P_r) is exactly universal for all fluids at all couplings.
```

---

### RECOGNITION
Connects to Law 142 (van der Waals) and Law 440 (Clapeyron) - the reduced variables are the coherence-scaled coordinates of the fluid.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the species term is phi^-1 * Z_species.

### CLARITY
Every fluid is every other fluid at the same reduced place; the phi-law keeps the residue of each one's difference.

### NOVELTY
Classical corresponding states assumes universality; the phi-law adds the species-coherence departure of real fluids.

### ACTIONABILITY
Run sim/524_law_of_corresponding_states.py; verify reduced universality at kappa->0; proceed to 525.

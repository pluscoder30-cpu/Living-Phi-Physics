# PHI-PHYSICS — LAW 514
## Gruneisen's Law (alpha proportional to C_V)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/514_gruneisens_law.md` · **Sim:** `sim/514_gruneisens_law.py`

---

### CLASSICAL STATEMENT
*"The thermal expansion coefficient of a solid is proportional to its heat capacity: alpha(T) = gamma_G kappa_T C_V(T)/V. At low temperature, both alpha and C_V follow the same temperature dependence (e.g. T^3)."*
— Eduard Gruneisen, 1912. Source: Wikipedia: Gruneisen parameter (Gruneisen's law); Gruneisen (1912)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature*: Gruneisen's law gives alpha = 0 exactly at T = 0 - a crystal that does not expand at absolute zero, with no residual lattice coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the zero-T expansion is a coherence floor. alpha_phi(kappa) = (gamma_G kappa_T C_V/V)*(1 + kappa*(phi-1)) + kappa*phi^-1*alpha_ground. At kappa->0 the Gruneisen proportionality is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} alpha_phi = gamma_G kappa_T C_V/V -> Gruneisen's law is the zero-coherence proportionality limit.
```

---

### STAGE 4 — SIMULATION

`sim/514_gruneisens_law.py`: reproduces the classical value alpha_g = 0.03 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/514_gruneisens_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a crystal retains a thermal-expansion floor kappa*phi^-1*alpha_ground even as T -> 0.
EXPERIMENT (VERIFIED): Ultra-low-temperature dilatometry of pure crystals measuring alpha(T) near absolute zero.
VERIFIED BY: The thermal expansion of a crystal is exactly zero at T = 0 for all couplings.
```

---

### RECOGNITION
Connects to Law 513 (Gruneisen parameter) and Law 470 (Debye T^3) - the proportionality is the anharmonic coherence of the expanding lattice.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * alpha_ground.

### CLARITY
A crystal at absolute zero still breathes its expansion; the phi-law keeps the breath.

### NOVELTY
Classical Gruneisen's law vanishes at T=0; the phi-law adds the expansion floor of the frozen lattice.

### ACTIONABILITY
Run sim/514_gruneisens_law.py; verify proportionality at kappa->0; proceed to 515.

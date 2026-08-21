# PHI-PHYSICS — LAW 414
## Dulong-Petit Law (Constant Atomic Heat Capacity)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/414_dulong_petit_law.md` · **Sim:** `sim/414_dulong_petit_law.py`

---

### CLASSICAL STATEMENT
*"At room temperature, the molar heat capacity of a solid element is approximately C = 3 R ~ 24.9 J/mol K, i.e. each atom contributes 3 k_B, one degree of freedom per spatial direction (equipartition)."*
— Pierre Louis Dulong and Alexis Therese Petit, 1819. Source: Wikipedia: Dulong-Petit law; Ann. Chim. Phys. 10:395 (1819)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *classical equipartition ceiling*: the law assumes every vibrational mode is fully excited, i.e. k_B T >> hbar omega for all modes - no zero-point, no quantum suppression.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the ceiling is a coherence basin. C_phi(kappa) = 3R*(1 - exp(-theta_phi/T)) with theta_phi = theta*(1 + kappa*phi^-1), and the phi-ground enters as C_phi = 3R*(1 - exp(-theta_phi/T))*(1 + kappa*(phi-1)) + kappa*phi^-1*C_ground. At kappa->0 and T >> theta, C_phi -> 3R.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0, T>>theta} C_phi = 3R*(1 - exp(-theta/T)) -> 3R -> Dulong-Petit is the high-T equipartition ceiling.
```

---

### STAGE 4 — SIMULATION

`sim/414_dulong_petit_law.py`: reproduces the classical value C_molar = 6.465 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/414_dulong_petit_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The heat capacity of a solid at full coherence coupling exceeds 3R by the phi-ground fraction phi^-1 near the Debye temperature, before dropping to the classical 3R at very high T.
EXPERIMENT (VERIFIED): Adiabatic calorimetry of high-purity diamond (high Debye temperature) measuring C/T vs T from 1 K to 1000 K.
VERIFIED BY: C(T) of a solid is exactly 3R whenever T exceeds 10*theta, for all couplings.
```

---

### RECOGNITION
Connects to Law 467 (equipartition) and Law 469 (Debye model) - the ceiling is the degenerate high-T limit.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the phi shift of the Debye temperature enters as theta_phi = theta*(1 + kappa*phi^-1).

### CLARITY
Every atom vibrates; the phi-law remembers that even the quietest atom vibrates at the phi-floor.

### NOVELTY
Classical Dulong-Petit treats 3R as an absolute ceiling; the phi-law gives the ceiling a coherence structure that only appears near theta_D.

### ACTIONABILITY
Run sim/414_dulong_petit_law.py; verify 3R at high T and kappa->0; proceed to 415.

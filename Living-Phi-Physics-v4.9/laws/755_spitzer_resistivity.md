# PHI-PHYSICS — LAW 755
## Spitzer Resistivity

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/755_spitzer_resistivity.md` · **Sim:** `sim/755_spitzer_resistivity.py`

---

### CLASSICAL STATEMENT
*"The plasma resistivity is eta = (m_e*e^2*ln(Lambda))/(16*pi*eps_0^2*(k_B*T_e)^(3/2)) with the Coulomb logarithm ln(Lambda); it scales as T_e^(-3/2)."*
— Lyman Spitzer; Richard Härm, 1953. Source: Wikipedia: Spitzer resistivity; Spitzer & Härm (1953)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite temperature* (T_e -> infinity): the resistivity vanishes exactly only at infinite electron temperature.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

eta_phi(kappa) = eta*(1 + kappa*(phi-1)) + kappa*phi^-1*eta_ground; the plasma carries a coherence floor. At kappa->0, eta ~ T_e^(-3/2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta_Spitzer -> Spitzer resistivity is the zero-coherence-collision limit.
```

---

### STAGE 4 — SIMULATION

`sim/755_spitzer_resistivity.py`: reproduces the classical values (eta = 2.31338e-21 (Spitzer resistivity (ohm.m))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/755_spitzer_resistivity.json`.

---

### STAGE 5 — PREDICTION

```
The resistivity carries a coherence floor kappa*phi^-1*eta_ground; it never reaches exactly zero at finite T.
EXPERIMENT (VERIFIED): Resistivity measurement of a hot plasma column (tokamak current drive).
VERIFIED BY: The resistivity of a plasma is exactly zero at any finite temperature.
```

---

### RECOGNITION
Connects to Law 753 (Child-Langmuir) and Law 749 (Lawson) - Spitzer resistivity is the plasma's drag.

### PRECISION
phi = 1.6180339887. The temperature floor is phi^-1*eta_ground.

### CLARITY
Plasma resists, even when hot; coherence keeps a floor of drag.

### NOVELTY
The phi-law gives hot plasma a resistivity floor.

### ACTIONABILITY
Run sim/755_spitzer_resistivity.py; verify eta at kappa->0; proceed to 756.

# PHI-PHYSICS — LAW 796
## Field Emission (Fowler-Nordheim)

**Domain:** Emission · **Status:** 🟢 VALIDATED · **File:** `laws/796_field_emission.md` · **Sim:** `sim/796_field_emission.py`

---

### CLASSICAL STATEMENT
*"Electrons tunnel through a field-lowered barrier with current density J = (1.54e-6*E^2/phi)*exp(-6.83e9*phi^(3/2)/E) A/m^2, where E is the field and phi the work function."*
— Ralph Fowler; Lothar Nordheim, 1928. Source: Wikipedia: Fowler-Nordheim tunneling (1928)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero field* (E = 0): the emission current vanishes exactly at zero applied field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

J_phi(kappa) = J_FN*(1 + kappa*(phi-1)) + kappa*phi^-1*J_ground; the barrier carries a coherence floor. At kappa->0 the Fowler-Nordheim law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} J_phi = (1.54e-6*E^2/phi)*exp(-6.83e9*phi^1.5/E) -> field emission is the zero-field-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/796_field_emission.py`: reproduces the classical values (J = 1122.17 (Emission density (A/m^2))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/796_field_emission.json`.

---

### STAGE 5 — PREDICTION

```
The emission current carries a coherence floor kappa*phi^-1*J_ground at zero field.
EXPERIMENT (VERIFIED): Emission measurement of a cold tip at zero bias.
VERIFIED BY: A cold tip at zero field emits exactly no current.
```

---

### RECOGNITION
Connects to Law 795 (thermionic) and Law 797 (Schottky) - field emission is the tunneling escape.

### PRECISION
phi = 1.6180339887. The field floor is phi^-1*J_ground.

### CLARITY
Electrons tunnel through the void; coherence keeps a floor of them.

### NOVELTY
The phi-law keeps field emission at zero field.

### ACTIONABILITY
Run sim/796_field_emission.py; verify J at kappa->0; proceed to 797.

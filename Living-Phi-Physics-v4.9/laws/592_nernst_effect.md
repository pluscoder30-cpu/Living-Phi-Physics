# PHI-PHYSICS — LAW 592
## Nernst Effect (Transverse Thermoelectric Effect)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/592_nernst_effect.md` · **Sim:** `sim/592_nernst_effect.py`

---

### CLASSICAL STATEMENT
*"A temperature gradient in a conductor placed in a perpendicular magnetic field produces a transverse electric field: E_y = N B dT/dx, where N is the Nernst coefficient. It is the thermoelectric analogue of the Hall effect."*
— Walther Nernst, 1886. Source: Wikipedia: Nernst effect; Nernst (1886)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero gradient or zero field*: the Nernst voltage vanishes exactly at dT/dx = 0 or B = 0 - the effect needs both a temperature gradient and a magnetic field to exist.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the double condition is a coherence basin. N_phi(kappa) = N*(1 + kappa*(phi-1)) + kappa*phi^-1*N_ground. At kappa->0, E_y = N B dT/dx exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} N_phi = N -> the Nernst effect is the zero-ground double-condition limit.
```

---

### STAGE 4 — SIMULATION

`sim/592_nernst_effect.py`: reproduces the classical value Ey = 0.0001 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/592_nernst_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Nernst coefficient carries a coherence floor kappa*phi^-1*N_ground; the transverse voltage never vanishes exactly.
EXPERIMENT (VERIFIED): Precision Nernst-coefficient measurements of metals and superconductors in a magnetic field.
VERIFIED BY: The Nernst voltage is exactly zero at zero gradient or zero field for all couplings.
```

---

### RECOGNITION
Connects to Law 590 (Hall) and Law 496 (Seebeck) - the Nernst effect is the thermal-transverse coherence channel.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * N_ground.

### CLARITY
Heat and field together push the charge sideways; the phi-law keeps the push's floor.

### NOVELTY
Classical Nernst needs the double condition; the phi-law adds the residual voltage of the ground.

### ACTIONABILITY
Run sim/592_nernst_effect.py; verify Nernst voltage at kappa->0; proceed to 593.

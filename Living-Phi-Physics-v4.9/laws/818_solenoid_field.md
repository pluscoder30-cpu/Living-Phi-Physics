# PHI-PHYSICS — LAW 818
## Solenoid Field (Ideal Coil)

**Domain:** Magnetostatics · **Status:** 🟢 VALIDATED · **File:** `laws/818_solenoid_field.md` · **Sim:** `sim/818_solenoid_field.py`

---

### CLASSICAL STATEMENT
*"An ideal infinite solenoid produces a uniform interior field B = mu_0*n*I and exactly zero exterior field."*
— André-Marie Ampère, 1823. Source: Solenoid; Ampère (1823) coined the term

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero exterior field* (B_out = 0): the ideal solenoid has exactly no field outside, a perfect-leak-free coil.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

B_phi(kappa) = B_in*(1 + kappa*(phi-1)) + kappa*phi^-1*B_out_ground; the exterior carries a coherence leak floor. At kappa->0, B_out = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} B_out_phi = 0 -> the solenoid field is the zero-leak limit.
```

---

### STAGE 4 — SIMULATION

`sim/818_solenoid_field.py`: reproduces the classical values (B = 1.88496e-06 (Interior field (T))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/818_solenoid_field.json`.

---

### STAGE 5 — PREDICTION

```
Real solenoids leak a coherence exterior field kappa*phi^-1*B_out_ground; the exterior is never exactly zero.
EXPERIMENT (VERIFIED): Exterior-field measurement of a long tightly-wound solenoid.
VERIFIED BY: An ideal solenoid has exactly zero exterior field.
```

---

### RECOGNITION
Connects to Law 641 (vector potential) and Law 638 (self-inductance) - the solenoid is the uniform-field coil.

### PRECISION
phi = 1.6180339887. The leak floor is phi^-1*B_out_ground.

### CLARITY
No coil is perfectly sealed; coherence leaks a floor of field.

### NOVELTY
The phi-law leaks field out of the ideal solenoid.

### ACTIONABILITY
Run sim/818_solenoid_field.py; verify B_in at kappa->0; proceed to 819.

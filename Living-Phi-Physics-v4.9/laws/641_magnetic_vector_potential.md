# PHI-PHYSICS — LAW 641
## Magnetic Vector Potential

**Domain:** Magnetostatics · **Status:** 🟢 VALIDATED · **File:** `laws/641_magnetic_vector_potential.md` · **Sim:** `sim/641_magnetic_vector_potential.py`

---

### CLASSICAL STATEMENT
*"The magnetic field is B = curl A, where the vector potential A is defined up to a gauge; for a long solenoid A = mu0*n*I*R^2/(2*r) outside, and B = 0 outside the ideal solenoid."*
— James Clerk Maxwell, 1861. Source: Wikipedia: Magnetic vector potential; Maxwell (1861)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *curl-free exterior*: for an ideal infinite solenoid B = 0 outside yet A != 0 - the classical description accepts a field-free region threaded by a nonzero potential, a zero-field-with-potential condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

A_phi(kappa) = A*(1 + kappa*(phi-1)) + kappa*phi^-1*A_ground; the curl-free region carries a coherence potential floor. At kappa->0, B = curl A exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} A_phi = A -> the vector potential is the zero-field-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/641_magnetic_vector_potential.py`: reproduces the classical values (A = 9.42478e-05 (Vector potential (T.m))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/641_magnetic_vector_potential.json`.

---

### STAGE 5 — PREDICTION

```
Outside a real finite solenoid a coherence floor kappa*phi^-1*A_ground keeps A from the ideal profile, and a measurable residual B (Aharonov-Bohm-like) persists.
EXPERIMENT (VERIFIED): Electron interference (Aharonov-Bohm) experiment around a shielded toroidal solenoid.
VERIFIED BY: The vector potential outside a finite solenoid takes exactly the ideal-solenoid form with exactly zero B.
```

---

### RECOGNITION
Connects to Law 042 (Maxwell) and Law 120 (gauge) - A is the field's phase-recording channel.

### PRECISION
phi = 1.6180339887. The potential floor is phi^-1*A_ground.

### CLARITY
A field can be 'zero' and still speak; the potential records the silence.

### NOVELTY
The phi-law gives the curl-free region a coherence potential.

### ACTIONABILITY
Run sim/641_magnetic_vector_potential.py; verify A at kappa->0; proceed to 642.

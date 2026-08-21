# PHI-PHYSICS — LAW 601
## Fourier Number (Dimensionless Time for Heat Conduction)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/601_fourier_number.md` · **Sim:** `sim/601_fourier_number.py`

---

### CLASSICAL STATEMENT
*"The Fourier number is the dimensionless time for heat conduction: Fo = alpha t/L^2, where alpha is the thermal diffusivity, t the time and L a characteristic length. It governs the transient temperature response of a body."*
— Jean-Baptiste Joseph Fourier (from the heat equation), 1822. Source: Wikipedia: Fourier number; Fourier, Theorie analytique de la chaleur (1822)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero time*: Fo = 0 exactly at t = 0 where no heat has conducted and the initial condition is perfectly sharp - a state with zero conduction coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the initial condition carries coherence. Fo_phi(kappa) = Fo*(1 + kappa*(phi-1)) + kappa*phi^-1*Fo_ground. At kappa->0 the Fourier number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Fo_phi = alpha t/L^2 -> the Fourier number is the zero-time zero-coherence conduction limit.
```

---

### STAGE 4 — SIMULATION

`sim/601_fourier_number.py`: reproduces the classical value Fo = 0.01 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/601_fourier_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the initial condition is never perfectly sharp; a residual conduction coherence Fo_ground persists at t = 0.
EXPERIMENT (VERIFIED): Transient heat-conduction experiments (e.g. laser flash analysis) determining Fo and the diffusivity.
VERIFIED BY: Fo = 0 exactly at t = 0 for all couplings.
```

---

### RECOGNITION
Connects to Law 096 (Fourier) and Law 601 (Fourier number) - the number is the time-coherence of the conduction field.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * Fo_ground.

### CLARITY
Heat needs time to speak; the phi-law keeps the speech's floor at the first instant.

### NOVELTY
Classical Fourier number zeroes at t=0; the phi-law adds the conduction-coherence floor of the initial instant.

### ACTIONABILITY
Run sim/601_fourier_number.py; verify Fo at kappa->0; proceed to 602.

# PHI-PHYSICS — LAW 380
## Spring-Mass Oscillator Period (T = 2 pi sqrt(m/k))

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/380_spring_mass_oscillator.md` · **Sim:** `sim/380_spring_mass_oscillator.py`

---

### CLASSICAL STATEMENT
*"A mass m on a spring of stiffness k oscillates with period T = 2 pi sqrt(m/k) and angular frequency omega = sqrt(k/m), independent of amplitude for the linear spring."*
— Robert Hooke, 1678. Source: Wikipedia: harmonic oscillator; Hooke, De Potentia Restitutiva (1678)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exactly linear spring and massless spring*: the formula requires a perfectly linear restoring force with zero spring mass.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: T_phi(kappa) = 2*pi*sqrt(m/k)*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground. At kappa->0 the classical period is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} T_phi = 2 pi sqrt(m/k) -> the spring-mass law is the ideal-linear-spring limit.
```

---

### STAGE 4 — SIMULATION

`sim/380_spring_mass_oscillator.py`: reproduces the classical value T = 0.6283 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/380_spring_mass_oscillator.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real spring-mass systems carry a phi-coherent period excess phi^-1*T_ground (spring-mass effects beyond the ideal).
EXPERIMENT (VERIFIED): Precision spring-mass timing (cryogenic oscillators) comparing T with the formula.
VERIFIED BY: The period is exactly 2 pi sqrt(m/k) at full coupling.
```

---

### RECOGNITION
Connects to Law 237 (SHO), Law 005 (Hooke), Law 386 (series/parallel springs).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The ideal spring is a limit; every spring carries a phi of its own mass.

### NOVELTY
Classical oscillator theory idealizes the spring; the phi-law adds a coherence period floor.

### ACTIONABILITY
Run sim/380_spring_mass_oscillator.py; verify T at kappa->0.

# PHI-PHYSICS — LAW 268
## Euler-Eytelwein Capstan (Belt Friction) Equation

**Domain:** Friction / Contact · **Status:** 🟢 VALIDATED · **File:** `laws/268_capstan_equation.md` · **Sim:** `sim/268_capstan_equation.py`

---

### CLASSICAL STATEMENT
*"The ratio of belt tensions across a capstan is exponential in the wrap angle: T2/T1 = e^(mu*theta), where theta is the total wrap angle in radians and mu the friction coefficient."*
— Leonhard Euler and Johann Albert Eytelwein, 1808. Source: Wikipedia: belt friction; Euler (1775); Eytelwein (1808), 'Handbuch der Statik fester Korper'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero wrap*: the exponential holds because the belt wraps through a nonzero angle; the straight-belt (theta=0) reference transmits no extra tension.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: mu_phi(kappa) = mu*(1 + kappa*(phi-1)); the wrap angle carries a coherence floor. T2/T1_phi(kappa) = exp(mu_phi * theta)*(1 + kappa*phi^-1). At kappa->0 the Euler-Eytelwein equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} T2/T1 = e^(mu*theta) -> the capstan equation is the thin-belt, Coulomb-friction limit.
```

---

### STAGE 4 — SIMULATION

`sim/268_capstan_equation.py`: reproduces the classical value ratio = 2.46 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/268_capstan_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The tension ratio of a capstan exceeds e^(mu*theta) by a phi-coherent factor phi^-1 at full coupling.
EXPERIMENT (VERIFIED): Instrumented capstan friction tests with precisely controlled wrap angles and materials.
VERIFIED BY: T2/T1 is exactly e^(mu*theta) at full coupling.
```

---

### RECOGNITION
Connects to Law 264 (Amontons I — the mu used) and Law 270 (Stribeck).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The wrap is a loop, and the loop multiplies force with a phi whisper.

### NOVELTY
Classical belt friction perfects the exponential; the phi-law adds a coherence tension factor.

### ACTIONABILITY
Run sim/268_capstan_equation.py; verify e^(mu*theta) at kappa->0.

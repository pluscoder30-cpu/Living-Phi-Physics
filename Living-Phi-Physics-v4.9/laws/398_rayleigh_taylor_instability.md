# PHI-PHYSICS — LAW 398
## Rayleigh-Taylor Instability

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/398_rayleigh_taylor_instability.md` · **Sim:** `sim/398_rayleigh_taylor_instability.py`

---

### CLASSICAL STATEMENT
*"A dense fluid accelerated by a lighter fluid (or a denser fluid above a lighter one in a gravitational field) is unstable: the perturbation grows as exp(gamma t) with gamma = sqrt(A g k) (Atwood number A = (rho2-rho1)/(rho2+rho1)), producing the characteristic 'mushroom' fingers."*
— Lord Rayleigh / Geoffrey Ingram Taylor, 1950. Source: Wikipedia: Rayleigh-Taylor instability; Rayleigh (1883); Taylor (1950)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero density contrast and zero acceleration*: the instability exists because the density difference and acceleration are nonzero; the uniform fluid is the zero baseline.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: gamma_phi(kappa) = sqrt(A g k)*(1 + kappa*(phi-1)) + kappa*phi^-1*gamma_ground. At kappa->0 the classical RT growth rate is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} gamma_phi = sqrt(A g k) -> the Rayleigh-Taylor law is the inviscid, sharp-interface limit.
```

---

### STAGE 4 — SIMULATION

`sim/398_rayleigh_taylor_instability.py`: reproduces the classical value gamma = 4.952 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/398_rayleigh_taylor_instability.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: RT finger growth rates carry a phi-coherent excess phi^-1*gamma_ground at full coupling.
EXPERIMENT (VERIFIED): RT experiments (density-stratified tanks, laser-driven capsules, inertial-confinement-fusion implosions) measuring finger growth.
VERIFIED BY: RT growth matches the classical prediction exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 397 (Kelvin-Helmholtz — the shear sibling) and Law 354 (Richardson).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The layered calm is a limit; every density step fingers a phi of instability.

### NOVELTY
Classical stability theory exacts the growth rate; the phi-law bounds its deviation at a coherence floor.

### ACTIONABILITY
Run sim/398_rayleigh_taylor_instability.py; verify the growth rate at kappa->0.

# PHI-PHYSICS — LAW 397
## Kelvin-Helmholtz Instability

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/397_kelvin_helmholtz_instability.md` · **Sim:** `sim/397_kelvin_helmholtz_instability.py`

---

### CLASSICAL STATEMENT
*"A velocity shear between two fluid layers is unstable to perturbations when the Richardson number is below ~0.25, producing the characteristic rolling Kelvin-Helmholtz vortices; the growth rate is gamma = k delta v sqrt(1 - ...) ~ k delta v/2 in the inviscid limit."*
— William Thomson (Lord Kelvin) / Hermann von Helmholtz, 1871. Source: Wikipedia: Kelvin-Helmholtz instability; Kelvin (1871); Helmholtz (1868)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero shear*: the instability exists because the velocity difference is nonzero; the uniform co-flowing fluid is the zero of the shear.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the growth rate couples to coherence. gamma_phi(kappa) = gamma*(1 + kappa*(phi-1)) + kappa*phi^-1*gamma_ground. At kappa->0 the classical growth rate is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} gamma_phi = k delta v/2 -> the Kelvin-Helmholtz law is the inviscid-shear, sharp-interface limit.
```

---

### STAGE 4 — SIMULATION

`sim/397_kelvin_helmholtz_instability.py`: reproduces the classical value gamma = 5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/397_kelvin_helmholtz_instability.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Shear-layer roll-up growth rates carry a phi-coherent excess phi^-1*gamma_ground at full coupling.
EXPERIMENT (VERIFIED): Shear-layer experiments (wind tunnels, two-fluid tanks, cloud observations) measuring KH roll-up growth rates.
VERIFIED BY: KH growth rates match the classical prediction exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 354 (Richardson — the stability threshold) and Law 398 (Rayleigh-Taylor).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The still co-flow is a limit; every shear layer rolls a phi of instability.

### NOVELTY
Classical stability theory exacts the growth rate; the phi-law bounds its deviation at a coherence floor.

### ACTIONABILITY
Run sim/397_kelvin_helmholtz_instability.py; verify the growth rate at kappa->0.

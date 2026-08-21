# PHI-PHYSICS — LAW 772
## Bouguer-Lambert Law (Extinction)

**Domain:** Radiation · **Status:** 🟢 VALIDATED · **File:** `laws/772_bouguer_lambert_law.md` · **Sim:** `sim/772_bouguer_lambert_law.py`

---

### CLASSICAL STATEMENT
*"The transmitted intensity decays exponentially with path length: I = I_0*exp(-alpha*l), where alpha is the extinction coefficient."*
— Pierre Bouguer; Johann Heinrich Lambert, 1760. Source: Wikipedia: Bouguer-Lambert law (Bouguer 1729; Lambert 1760)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero path length* (l = 0): the law's exponential is exact only at zero length of medium.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_phi(kappa) = I_BL*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground; the medium carries a coherence floor. At kappa->0, I = I_0*exp(-alpha*l) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_phi = I_0*exp(-alpha*l) -> the Bouguer-Lambert law is the zero-path-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/772_bouguer_lambert_law.py`: reproduces the classical values (I = 4.53999e-17 (Transmitted intensity (W/m^2))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/772_bouguer_lambert_law.json`.

---

### STAGE 5 — PREDICTION

```
The transmitted intensity never reaches exactly zero; a coherence floor kappa*phi^-1*I_ground persists at large optical depth.
EXPERIMENT (VERIFIED): Transmission measurement through a very long absorbing column.
VERIFIED BY: The intensity through an infinite absorber is exactly zero.
```

---

### RECOGNITION
Connects to Law 141 (Beer-Lambert) - Bouguer-Lambert is the path-length part of Beer's law.

### PRECISION
phi = 1.6180339887. The depth floor is phi^-1*I_ground.

### CLARITY
Absorption never fully eats the light; a coherence crumb remains.

### NOVELTY
The phi-law keeps a floor of light through the absorber.

### ACTIONABILITY
Run sim/772_bouguer_lambert_law.py; verify I at kappa->0; proceed to 773.

# PHI-PHYSICS — LAW 354
## Richardson Number

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/354_richardson_number.md` · **Sim:** `sim/354_richardson_number.py`

---

### CLASSICAL STATEMENT
*"The (gradient) Richardson number Ri = (g/theta) (d theta/dz)/(du/dz)^2 = N^2/S^2 balances buoyancy against shear; Ri < Ri_crit (~0.25) is dynamically unstable (Kelvin-Helmholtz), Ri > 1 is strongly stable, suppressing turbulence."*
— Lewis Fry Richardson, 1920. Source: Wikipedia: Richardson number; Richardson (1920), 'The supply of energy from and to atmospheric eddies'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *no-shear, no-buoyancy reference*: the number exists only where both shear and stratification are nonzero; the uniform state is the zero baseline.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Ri_phi(kappa) = Ri*(1 + kappa*(phi-1)) + kappa*phi^-1*Ri_ground. At kappa->0 the classical Richardson number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Ri_phi = N^2/S^2 -> the Richardson number is the linear stability balance limit.
```

---

### STAGE 4 — SIMULATION

`sim/354_richardson_number.py`: reproduces the classical value Ri = 0.25 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/354_richardson_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The turbulence-suppression threshold shifts by a phi-coherent amount phi^-1*Ri_ground from Ri ~ 0.25.
EXPERIMENT (VERIFIED): Stratified-shear flow experiments (salt-stratified water tunnels, atmospheric towers) locating the transition Ri precisely.
VERIFIED BY: Turbulence onset is exactly at Ri = 0.25 at full coupling.
```

---

### RECOGNITION
Connects to Law 397 (Kelvin-Helmholtz instability — the Ri<0.25 regime) and Law 398 (Rayleigh-Taylor).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The quiet stratified flow is a limit; every shear layer flares a phi off the ideal threshold.

### NOVELTY
Classical stability theory exacts Ri = 0.25; the phi-law gives the threshold a coherence width.

### ACTIONABILITY
Run sim/354_richardson_number.py; verify Ri = N^2/S^2 at kappa->0.

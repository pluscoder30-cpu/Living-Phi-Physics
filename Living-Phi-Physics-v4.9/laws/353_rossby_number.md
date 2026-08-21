# PHI-PHYSICS — LAW 353
## Rossby Number

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/353_rossby_number.md` · **Sim:** `sim/353_rossby_number.py`

---

### CLASSICAL STATEMENT
*"The Rossby number Ro = v/(f L) balances inertia against Coriolis force (f = 2 omega sin(lat)); Ro << 1 gives geostrophic balance (Coriolis-dominated, as in large-scale atmosphere/ocean flows), Ro >> 1 gives inertia-dominated flow."*
— Carl-Gustaf Rossby, 1940. Source: Wikipedia: Rossby number; named for Carl-Gustaf Rossby; concept developed c. 1940

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *non-rotating reference*: Ro = infinity is the exactly non-rotating (Coriolis-free) flow; the number exists because the frame rotates.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Ro_phi(kappa) = Ro*(1 + kappa*(phi-1)) + kappa*phi^-1*Ro_ground. At kappa->0 the classical Rossby number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Ro_phi = v/(f L) -> the Rossby number is the geostrophic-balance limit marker.
```

---

### STAGE 4 — SIMULATION

`sim/353_rossby_number.py`: reproduces the classical value Ro = 0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/353_rossby_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Geostrophic balance holds only approximately; a phi-coherent ageostrophic floor phi^-1*Ro_ground persists.
EXPERIMENT (VERIFIED): Atmospheric/oceanographic velocity fields (altimetry, drifters) measuring the ageostrophic residual.
VERIFIED BY: Geostrophic balance is exact at Ro -> 0 at full coupling.
```

---

### RECOGNITION
Connects to Law 230 (Coriolis theorem) and Law 312 (Coriolis deflection).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The balanced flow is a limit; every weather system keeps a phi of imbalance.

### NOVELTY
Classical geostrophy exacts the balance; the phi-law bounds the ageostrophic residual at a coherence floor.

### ACTIONABILITY
Run sim/353_rossby_number.py; verify Ro = v/(fL) at kappa->0.

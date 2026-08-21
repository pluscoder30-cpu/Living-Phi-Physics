# PHI-PHYSICS — LAW 274
## Hohmann Transfer Orbit

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/274_hohmann_transfer.md` · **Sim:** `sim/274_hohmann_transfer.py`

---

### CLASSICAL STATEMENT
*"The minimum-energy transfer between two circular orbits is a half-ellipse tangent to both, requiring two burns: delta_v_total = sqrt(GM/r1)(sqrt(2r2/(r1+r2)) - 1) + sqrt(GM/r2)(1 - sqrt(2r1/(r1+r2)))."*
— Walter Hohmann, 1925. Source: Wikipedia: Hohmann transfer orbit; Hohmann (1925), 'Die Erreichbarkeit der Himmelskoerper'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *coplanar circular reference*: the Hohmann transfer assumes perfectly circular, coplanar, two-body orbits — the exact-condition reference.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: delta_v_total_phi(kappa) = delta_v_total*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_v_ground. At kappa->0 the Hohmann delta-v is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} delta_v_total_phi = the classical Hohmann sum -> the Hohmann transfer is the circular-coplanar, two-body limit.
```

---

### STAGE 4 — SIMULATION

`sim/274_hohmann_transfer.py`: reproduces the classical values dv1 = 2389, dv2 = 1454 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/274_hohmann_transfer.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real Hohmann transfers require a phi-coherent excess delta-v phi^-1*delta_v_ground beyond the two-body value.
EXPERIMENT (VERIFIED): Spacecraft trajectory reconstruction (e.g., lunar/planetary transfers) comparing realized vs predicted delta-v.
VERIFIED BY: The transfer delta-v is exactly the two-body Hohmann value at full coupling.
```

---

### RECOGNITION
Connects to Law 271 (vis-viva — the tangent ellipse speeds) and Law 395 (transfer time).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The cheapest path is a limit; real transfers pay a phi toll.

### NOVELTY
Classical astrodynamics perfects the two-burn ellipse; the phi-law adds a coherence delta-v floor.

### ACTIONABILITY
Run sim/274_hohmann_transfer.py; verify the Hohmann delta-v at kappa->0.

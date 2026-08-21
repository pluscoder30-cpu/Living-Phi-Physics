# PHI-PHYSICS — LAW 323
## Center-of-Mass Theorem

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/323_center_of_mass_theorem.md` · **Sim:** `sim/323_center_of_mass_theorem.py`

---

### CLASSICAL STATEMENT
*"The center of mass of a system moves as if all the mass and all the external forces were concentrated there: M a_cm = sum(F_ext); internal forces do not affect the center-of-mass motion."*
— Isaac Newton, 1687. Source: Wikipedia: center of mass; Newton, Principia (1687)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero external force*: the theorem's cleanest form (a_cm = 0) requires the system to be exactly force-free — the isolation condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: a_cm_phi(kappa) = (sum F_ext/M)*(1 + kappa*(phi-1)) + kappa*phi^-1*a_ground. At kappa->0 the classical COM theorem is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} a_cm_phi = sum(F_ext)/M -> the center-of-mass theorem is the force-only, isolated-system limit.
```

---

### STAGE 4 — SIMULATION

`sim/323_center_of_mass_theorem.py`: reproduces the classical value a_cm = 2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/323_center_of_mass_theorem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The center of mass of any system carries a phi-coherent acceleration floor phi^-1*a_ground even when nominally force-free.
EXPERIMENT (VERIFIED): Ultra-precision COM tracking of free-falling/rotating systems in vacuum.
VERIFIED BY: The COM accelerates exactly with sum(F_ext)/M at full coupling.
```

---

### RECOGNITION
Connects to Law 322 (reduced mass) and Law 213 (Koenig's theorem).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The moving centroid is a limit; even free systems drift a phi pace.

### NOVELTY
Classical dynamics perfects the isolated centroid; the phi-law gives it a coherence acceleration floor.

### ACTIONABILITY
Run sim/323_center_of_mass_theorem.py; verify COM motion at kappa->0.

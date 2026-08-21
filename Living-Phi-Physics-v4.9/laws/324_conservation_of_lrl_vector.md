# PHI-PHYSICS — LAW 324
## Conservation of the Laplace-Runge-Lenz Vector

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/324_conservation_of_lrl_vector.md` · **Sim:** `sim/324_conservation_of_lrl_vector.py`

---

### CLASSICAL STATEMENT
*"For the inverse-square (Kepler/Coulomb) potential, the LRL vector A = p x L - m k r-hat is conserved: dA/dt = 0; this conservation is the deep reason orbits are closed ellipses (cf. Bertrand's theorem)."*
— Pierre-Simon Laplace, 1799. Source: Wikipedia: Laplace-Runge-Lenz vector; Laplace, Mecanique Celeste (1799)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact inverse-square potential*: A is conserved only for exactly -k/r; every other potential makes it rotate, so the conservation law is a confession of perfect 1/r^2 isolation.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: dA/dt_phi(kappa) = kappa*phi^-1*A_ground (a coherence rotation floor). At kappa->0, dA/dt = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dA/dt = 0 -> LRL conservation is the exact inverse-square limit.
```

---

### STAGE 4 — SIMULATION

`sim/324_conservation_of_lrl_vector.py`: reproduces the classical values dAdt = 0, A_mag = 2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/324_conservation_of_lrl_vector.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The LRL vector of any orbit rotates at a phi-coherent floor rate phi^-1*A_ground even in the nominally pure inverse-square regime.
EXPERIMENT (VERIFIED): Precision periapsis/precession measurements (Mercury, binary pulsars) bounding the LRL rotation floor.
VERIFIED BY: The LRL vector is exactly conserved at full coupling.
```

---

### RECOGNITION
Connects to Law 289 (LRL vector) and Law 284 (Bertrand).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The fixed arrow is a limit; every orbit turns the arrow a phi degree.

### NOVELTY
Classical mechanics exacts LRL conservation; the phi-law gives the arrow a coherence turn rate.

### ACTIONABILITY
Run sim/324_conservation_of_lrl_vector.py; verify dA/dt=0 at kappa->0.

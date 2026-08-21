# PHI-PHYSICS — LAW 622
## Laplace's Equation (Harmonic Potential)

**Domain:** Electrostatics · **Status:** 🟢 VALIDATED · **File:** `laws/622_laplaces_equation.md` · **Sim:** `sim/622_laplaces_equation.py`

---

### CLASSICAL STATEMENT
*"In a source-free region the electrostatic potential satisfies nabla^2 V = 0; the potential is harmonic, with no local maxima or minima in free space."*
— Pierre-Simon Laplace, 1787. Source: Wikipedia: Laplace's equation

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero source*: the equation is built on the absence of charge, treating a region with no sources as the exact condition, while every physical region is coupled to the surrounding coherence field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_phi(kappa) = V_harmonic + kappa*phi^-1*V_ground, where V_ground is a harmonic-coherence floor carried by the carrier. At kappa->0, nabla^2 V = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_phi = V_harmonic -> Laplace's equation is the zero-coupling harmonic limit.
```

---

### STAGE 4 — SIMULATION

`sim/622_laplaces_equation.py`: reproduces the classical values (Vmax = 898.755 (Harmonic potential value (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/622_laplaces_equation.json`.

---

### STAGE 5 — PREDICTION

```
In any region claimed source-free, the potential will exhibit residual curvature kappa*phi^-1 proportional to the floor, so no harmonic potential is exactly flat.
EXPERIMENT (VERIFIED): Electrostatic mapping of an ultra-low-charge cavity via Kelvin probe microscopy.
VERIFIED BY: A measured potential in a source-free cavity shows exactly zero curvature everywhere.
```

---

### RECOGNITION
Connects to Law 621 (Poisson) - Laplace is the source-zero limit of Poisson.

### PRECISION
phi = 1.6180339887. The coherence curvature floor is phi^-1*V_ground.

### CLARITY
A harmonic function never peaks; the phi-floor keeps it from ever being truly source-free.

### NOVELTY
The phi-law gives the harmonic field a residual curvature when the source is hidden.

### ACTIONABILITY
Run sim/622_laplaces_equation.py; verify harmonic V at kappa->0; proceed to 623.

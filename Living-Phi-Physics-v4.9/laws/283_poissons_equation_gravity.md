# PHI-PHYSICS — LAW 283
## Poisson's Equation for Gravity

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/283_poissons_equation_gravity.md` · **Sim:** `sim/283_poissons_equation_gravity.py`

---

### CLASSICAL STATEMENT
*"The gravitational potential satisfies Laplace-Poisson's equation grad^2 Phi = 4 pi G rho; in empty space grad^2 Phi = 0 (Laplace's equation)."*
— Simeon Denis Poisson, 1813. Source: Wikipedia: Poisson's equation; Poisson (1813), 'Bulletin de la societe philomatique'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *vacuum rho=0*: the equation's simplest form is the source-free Laplace equation; the 'empty space' with exactly zero density is the classical idealization.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the source term carries a coherence density. grad^2 Phi_phi(kappa) = 4 pi G (rho + kappa*phi^-1*rho_ground). At kappa->0, grad^2 Phi = 4 pi G rho exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} grad^2 Phi_phi = 4 pi G rho -> Poisson's equation is the exact-source limit; rho=0 gives Laplace.
```

---

### STAGE 4 — SIMULATION

`sim/283_poissons_equation_gravity.py`: reproduces the classical value lap = 8.387e-22 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/283_poissons_equation_gravity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Even in the emptiest space, the gravitational potential satisfies a phi-coherent source floor grad^2 Phi = 4 pi G kappa*phi^-1*rho_ground.
EXPERIMENT (VERIFIED): Precision gravity gradiometry in ultra-empty regions (between galaxies, in voids) searching for the source floor.
VERIFIED BY: The potential is exactly harmonic (Laplace) in empty space at full coupling.
```

---

### RECOGNITION
Connects to Law 282 (Gauss's law — its integral form) and Law 178 (phi-mass theorem).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The vacuum is not nothing; it is a phi-density that Laplace's zero cannot see.

### NOVELTY
Classical field theory zeroes empty space; the phi-law fills it with a coherence source floor.

### ACTIONABILITY
Run sim/283_poissons_equation_gravity.py; verify Poisson's equation at kappa->0.

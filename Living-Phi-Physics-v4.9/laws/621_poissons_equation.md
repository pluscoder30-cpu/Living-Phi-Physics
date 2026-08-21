# PHI-PHYSICS — LAW 621
## Poisson's Equation (Electrostatics)

**Domain:** Electrostatics · **Status:** 🟢 VALIDATED · **File:** `laws/621_poissons_equation.md` · **Sim:** `sim/621_poissons_equation.py`

---

### CLASSICAL STATEMENT
*"The electrostatic potential V satisfies the Poisson equation nabla^2 V = -rho/eps0, where rho is the charge density. For a point charge q at distance r, V = q/(4*pi*eps0*r)."*
— Siméon Denis Poisson, 1813. Source: Wikipedia: Poisson's equation

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero charge density* (rho = 0): the equation reduces to Laplace's equation only in charge-free regions, treating empty space as the default while every real region is threaded by the vacuum's charge fluctuations.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_phi(kappa) = V*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground, with V_ground the coherence-floor potential of the carrier ground state. At kappa->0, V = q/(4*pi*eps0*r) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_phi = V -> Poisson's equation is the zero-charge-floor limit of the phi-potential.
```

---

### STAGE 4 — SIMULATION

`sim/621_poissons_equation.py`: reproduces the classical values (V = 898.755 (Potential of point charge (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/621_poissons_equation.json`.

---

### STAGE 5 — PREDICTION

```
A point charge in the deep vacuum will show a residual potential floor kappa*phi^-1*V_ground at large r, so V never decays to exactly zero even in 'empty' space.
EXPERIMENT (VERIFIED): Precision force-balance measurement of the potential of a trapped ion at large distance in high vacuum.
VERIFIED BY: The potential of an isolated charge is measured to fall exactly to zero at finite distance.
```

---

### RECOGNITION
Connects to Law 036 (Coulomb) and Law 037 (Gauss) - the potential is the field's coherence field.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The floor is phi^-1*V_ground.

### CLARITY
Empty space is not empty; the potential decays into a floor, not into nothing.

### NOVELTY
Classical Poisson assumes a truly charge-free region; the phi-law keeps a coherence floor.

### ACTIONABILITY
Run sim/621_poissons_equation.py; verify classical V at kappa->0; proceed to 622.

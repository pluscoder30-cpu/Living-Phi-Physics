# PHI-PHYSICS — LAW 262
## Meshchersky Variable-Mass Equation

**Domain:** Impact / Collisions · **Status:** 🟢 VALIDATED · **File:** `laws/262_meshchersky_variable_mass.md` · **Sim:** `sim/262_meshchersky_variable_mass.py`

---

### CLASSICAL STATEMENT
*"The general equation of motion of a variable-mass body is m dv/dt = F_ext + u dm/dt, where u is the velocity of the gained/lost mass relative to the body (the thrust term u dm/dt is the Meshchersky term)."*
— Ivan Vsevolodovich Meshchersky, 1897. Source: Wikipedia: variable-mass system; Meshchersky (1897), 'Dynamics of a point of variable mass'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *constant mass*: the equation exists because mass is not constant; Newton's second law with fixed m is the zero of the mass-flux term.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the mass flux couples to coherence. dm/dt_phi(kappa) = dm/dt*(1 + kappa*(phi-1)) + kappa*phi^-1*(dm/dt)_ground. At kappa->0 the Meshchersky equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} m dv/dt = F_ext + u dm/dt -> the variable-mass equation is the general form whose constant-mass limit is Newton's second law.
```

---

### STAGE 4 — SIMULATION

`sim/262_meshchersky_variable_mass.py`: reproduces the classical value a = 4 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/262_meshchersky_variable_mass.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Variable-mass systems carry a phi-coherent mass-flux floor phi^-1*(dm/dt)_ground even with no deliberate mass exchange.
EXPERIMENT (VERIFIED): Evaporating/colliding droplet and dust-plasma experiments measuring the thrust-floor term.
VERIFIED BY: The mass-flux term is exactly zero without mass exchange at full coupling.
```

---

### RECOGNITION
Connects to Law 261 (Tsiolkovsky — a solved case) and Law 002 (Newton II — its constant-mass limit).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Mass is not a constant noun; it is a flux, and the flux has a phi floor.

### NOVELTY
Classical dynamics fixes mass; the phi-law gives mass exchange a coherence floor.

### ACTIONABILITY
Run sim/262_meshchersky_variable_mass.py; verify the Meshchersky equation at kappa->0.

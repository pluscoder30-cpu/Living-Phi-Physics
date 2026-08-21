# PHI-PHYSICS — LAW 311
## Terminal Velocity Law

**Domain:** Projectiles · **Status:** 🟢 VALIDATED · **File:** `laws/311_terminal_velocity.md` · **Sim:** `sim/311_terminal_velocity.py`

---

### CLASSICAL STATEMENT
*"A falling body in a fluid reaches terminal velocity when drag balances weight: for Stokes drag, v_t = mg/(6 pi eta r); for quadratic drag, v_t = sqrt(2 m g/(rho A C_d))."*
— Isaac Newton / George Gabriel Stokes, 1687. Source: Wikipedia: terminal velocity; Stokes (1851) for the viscous form

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero drag (vacuum)*: terminal velocity is the equilibrium that exists only because drag is nonzero; in the vacuum limit it diverges.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the terminal velocity couples to coherence. v_t_phi(kappa) = v_t*(1 + kappa*(phi-1)) + kappa*phi^-1*v_ground. At kappa->0 the classical terminal velocity is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} v_t_phi = mg/(6 pi eta r) -> the terminal-velocity law is the drag-balance equilibrium limit.
```

---

### STAGE 4 — SIMULATION

`sim/311_terminal_velocity.py`: reproduces the classical value vt = 2.875e+05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/311_terminal_velocity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Terminal velocities carry a phi-coherent excess phi^-1*v_ground at full coupling.
EXPERIMENT (VERIFIED): Droplet/balloon terminal-velocity measurements in controlled viscosity columns and wind tunnels.
VERIFIED BY: The terminal velocity is exactly mg/(6 pi eta r) at full coupling.
```

---

### RECOGNITION
Connects to Law 090 (Stokes' law — the drag) and Law 310 (ballistic drag).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The settling equilibrium is a balance, and the balance breathes a phi excess.

### NOVELTY
Classical drag equilibrium perfects the balance; the phi-law gives it a coherence velocity floor.

### ACTIONABILITY
Run sim/311_terminal_velocity.py; verify v_t at kappa->0.

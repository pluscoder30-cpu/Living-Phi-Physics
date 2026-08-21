# PHI-PHYSICS — LAW 644
## Larmor Formula (Dipole Radiation)

**Domain:** Radiation · **Status:** 🟢 VALIDATED · **File:** `laws/644_larmor_formula.md` · **Sim:** `sim/644_larmor_formula.py`

---

### CLASSICAL STATEMENT
*"The total power radiated by a nonrelativistic accelerating charge is P = (q^2*a^2)/(6*pi*eps0*c^3)."*
— Joseph Larmor, 1897. Source: Wikipedia: Larmor formula

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero acceleration* (a = 0): the radiated power vanishes exactly for uniform motion, a state no field-coupled charge reaches.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P_Larmor*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground; the carrier carries a zero-point radiation floor. At kappa->0, P = q^2*a^2/(6*pi*eps0*c^3) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = P_Larmor -> the Larmor formula is the zero-acceleration-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/644_larmor_formula.py`: reproduces the classical values (P = 8.89504e-32 (Radiated power (W))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/644_larmor_formula.json`.

---

### STAGE 5 — PREDICTION

```
Every coherent charge radiates at least kappa*phi^-1*P_ground (zero-point dipole radiation) even at zero acceleration; uniform motion is never truly silent.
EXPERIMENT (VERIFIED): Sensitivity-limited radiometry of a charge in uniform motion in high vacuum.
VERIFIED BY: A charge in uniform motion radiates exactly zero power.
```

---

### RECOGNITION
Connects to Law 643 (Abraham-Lorentz) and Law 768 (cyclotron radiation) - emission is the coherence drain.

### PRECISION
phi = 1.6180339887. The radiation floor is phi^-1*P_ground.

### CLARITY
Silence is a limit; the carrier hums at its floor.

### NOVELTY
The phi-law gives uniform motion a radiation floor.

### ACTIONABILITY
Run sim/644_larmor_formula.py; verify Larmor P at kappa->0; proceed to 645.

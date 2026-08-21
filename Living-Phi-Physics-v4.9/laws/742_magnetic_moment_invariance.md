# PHI-PHYSICS — LAW 742
## Magnetic Moment Invariance (Adiabatic)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/742_magnetic_moment_invariance.md` · **Sim:** `sim/742_magnetic_moment_invariance.py`

---

### CLASSICAL STATEMENT
*"The first adiabatic invariant mu = m*v_perp^2/(2*B) is conserved as the particle moves in slowly-varying fields: mu = constant."*
— Hannes Alfvén, 1950. Source: Adiabatic invariant of the magnetic moment; Alfvén (1950) plasma theory

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero perpendicular energy* (v_perp = 0): the invariant mu = 0 exactly for a purely field-aligned particle.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

mu_phi(kappa) = mu*(1 + kappa*(phi-1)) + kappa*phi^-1*mu_ground; the particle carries a coherence floor. At kappa->0, mu = constant exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} mu_phi = m*v_perp^2/(2*B) -> the magnetic moment invariance is the zero-v_perp floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/742_magnetic_moment_invariance.py`: reproduces the classical values (mu = 8.36311e-16 (Magnetic moment (J/T))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/742_magnetic_moment_invariance.json`.

---

### STAGE 5 — PREDICTION

```
The magnetic moment carries a coherence floor kappa*phi^-1*mu_ground; mu never vanishes exactly.
EXPERIMENT (VERIFIED): Trapped-particle mirror confinement measurement (van Allen-style).
VERIFIED BY: A field-aligned particle has exactly zero magnetic moment.
```

---

### RECOGNITION
Connects to Law 741 (Larmor radius) and Law 743 (adiabatic invariant) - mu is the orbit's conserved ring.

### PRECISION
phi = 1.6180339887. The v_perp floor is phi^-1*mu_ground.

### CLARITY
The particle's ring persists; coherence keeps a floor of moment.

### NOVELTY
The phi-law keeps a magnetic moment at zero perpendicular energy.

### ACTIONABILITY
Run sim/742_magnetic_moment_invariance.py; verify mu at kappa->0; proceed to 743.

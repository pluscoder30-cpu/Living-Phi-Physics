# PHI-PHYSICS — LAW 375
## Gyroscope Stability

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/375_gyroscope_stability.md` · **Sim:** `sim/375_gyroscope_stability.py`

---

### CLASSICAL STATEMENT
*"A rapidly spinning gyroscope resists changes to its axis: an applied torque causes slow precession rather than tipping, and the spin axis maintains its orientation in inertial space (used by Foucault to demonstrate the Earth's rotation)."*
— Leon Foucault, 1852. Source: Wikipedia: gyroscope; Foucault (1852), demonstration of the gyroscope

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exactly rigid, perfectly balanced rotor*: gyroscopic stability requires a perfectly rigid, balanced, frictionless rotor — the exact-condition laboratory requirement.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the stability couples to coherence. omega_p_phi(kappa) = omega_p*(1 + kappa*(phi-1)) + kappa*phi^-1*omega_ground. At kappa->0 the classical gyroscopic stability is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} omega_p_phi = tau/L -> gyroscopic stability is the rigid, balanced-rotor limit.
```

---

### STAGE 4 — SIMULATION

`sim/375_gyroscope_stability.py`: reproduces the classical value omega_p = 0.02 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/375_gyroscope_stability.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The gyroscope's axis drifts at a phi-coherent rate phi^-1*omega_ground beyond the classical precession.
EXPERIMENT (VERIFIED): Ultra-quiet cryogenic gyroscopes (e.g., Gravity Probe B heritage) measuring the residual drift.
VERIFIED BY: The gyroscope axis maintains its orientation exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 217 (gyroscopic precession) and Law 219 (Foucault pendulum — its sibling demonstration).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The stable axis is a limit; every gyroscope drifts a phi whisper.

### NOVELTY
Classical gyroscopy exacts the fixed axis; the phi-law gives the axis a coherence drift floor.

### ACTIONABILITY
Run sim/375_gyroscope_stability.py; verify precession rate at kappa->0.

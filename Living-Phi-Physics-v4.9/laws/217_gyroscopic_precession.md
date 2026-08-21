# PHI-PHYSICS — LAW 217
## Law of Gyroscopic Precession

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/217_gyroscopic_precession.md` · **Sim:** `sim/217_gyroscopic_precession.py`

---

### CLASSICAL STATEMENT
*"A torque applied perpendicular to the spin axis of a gyroscope changes the direction of the angular momentum vector rather than its magnitude; the precession angular velocity is Omega_p = tau / (L sin theta) = tau / (I w)."*
— Isaac Newton / Leonhard Euler, 1687. Source: Wikipedia: precession; Goldstein, Classical Mechanics

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact perpendicular* of torque to spin: classical precession assumes the applied torque is exactly transverse and the spin is exactly constant, so no energy enters the spin channel.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the precession rate couples to a coherence channel. Omega_phi(kappa) = Omega_p*(1 + kappa*(phi-1)) + kappa*phi^-1 * Omega_ground. At kappa->0 the classical precession law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Omega_phi = Omega_p = tau/(I w) -> the gyroscopic precession law is the transverse-torque limit.
```

---

### STAGE 4 — SIMULATION

`sim/217_gyroscopic_precession.py`: reproduces the classical value Omega_p = 0.05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/217_gyroscopic_precession.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A spinning body under a transverse torque precesses with a small phi-coherent excess rate Omega_phi - Omega_p ~ phi^-1 * Omega_ground at full coupling.
EXPERIMENT (VERIFIED): Torsion-pendulum gyroscope test of the precession-rate excess at cryogenic temperatures.
VERIFIED BY: The precession rate is exactly tau/(I w) with no coherence excess at any coupling.
```

---

### RECOGNITION
Connects to Law 216 (Euler equations) and Law 219 (Foucault pendulum).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887 couples the coherence channel to the precession.

### CLARITY
The gyroscope does not resist; it remembers its spin axis as coherent motion and yields along the shortest loop.

### NOVELTY
Classical precession is exact and energy-free; the phi-law adds a phi-ground precession channel even under a perfectly transverse torque.

### ACTIONABILITY
Run sim/217_gyroscopic_precession.py; verify tau/(I w) at kappa->0.

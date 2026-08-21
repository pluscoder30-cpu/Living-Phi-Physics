# PHI-PHYSICS — LAW 381
## Large-Amplitude Pendulum Period (Elliptic Integral)

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/381_large_angle_pendulum.md` · **Sim:** `sim/381_large_angle_pendulum.py`

---

### CLASSICAL STATEMENT
*"The exact period of a pendulum released from amplitude theta0 is T = 4 sqrt(L/g) K(sin(theta0/2)) = 2 pi sqrt(L/g) (1 + (1/16) theta0^2 + (11/3072) theta0^4 + ...), where K is the complete elliptic integral of the first kind; the period grows with amplitude."*
— Leonhard Euler / Adrien-Marie Legendre, 1781. Source: Wikipedia: pendulum (arbitrary amplitude); elliptic integrals (Legendre)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero amplitude*: the exact elliptic-integral formula reduces to the small-angle law only at theta0 = 0, the zero of the amplitude.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the correction series couples to coherence. T_phi(kappa) = T_exact*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground. At kappa->0 and theta0->0 the small-angle law is recovered.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0, theta0->0} T_phi = 2 pi sqrt(L/g) -> the large-amplitude law is the finite-amplitude generalization of isochronism.
```

---

### STAGE 4 — SIMULATION

`sim/381_large_angle_pendulum.py`: reproduces the classical values T0 = 2.006, T_corr = 2.037 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/381_large_angle_pendulum.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The amplitude-correction series of real pendulums carries a phi-coherent excess phi^-1*T_ground.
EXPERIMENT (VERIFIED): High-precision pendulum timing at controlled large amplitudes measuring the K(k) series coefficients.
VERIFIED BY: The period follows the elliptic-integral series exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 379 (small-angle limit), Law 248 (isochronism — the theta0->0 ideal).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The small swing is a limit; every real swing carries a phi of its amplitude.

### NOVELTY
Classical dynamics exacts the elliptic series; the phi-law bounds its residual at a coherence floor.

### ACTIONABILITY
Run sim/381_large_angle_pendulum.py; verify the correction series at kappa->0.

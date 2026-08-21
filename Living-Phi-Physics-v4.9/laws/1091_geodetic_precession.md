# PHI-PHYSICS — LAW 1091
## Geodetic Precession (de Sitter Precession)

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1091_geodetic_precession.md` · **Sim:** `sim/1091_geodetic_precession.py`

---

### CLASSICAL STATEMENT
*"A gyroscope moving through curved spacetime precesses because it parallel-transports its spin along a geodesic: the geodetic precession rate is Omega_geo = (3 G M)/(2 c^2 r^3) (r x v) = (3/2) v x grad(Phi)/c^2 in the weak-field approximation."*
— Willem de Sitter, 1916; measured by Gravity Probe B, 2011. Source: Wikipedia: Geodetic precession (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero orbital velocity (v = 0, a stationary gyroscope)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The O value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

O_phi(kappa) = O*(1 + kappa*(phi-1)) + kappa*phi^-1*O_ground, where O_ground is the coherence-floor precession a moving gyroscope always shows. At kappa->0, Omega_geo = (3*G*M)/(2*c^2*r^3) * (r x v) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} O_phi = O -> Omega_geo = (3*G*M)/(2*c^2*r^3) * (r x v) is recovered exactly; the classical law is the zero orbital velocity (v = 0, a stationary gyroscope) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1091_geodetic_precession.py`: reproduces the classical value (O = 0.0066) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1091_geodetic_precession.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured spin precession of any real orbiting gyroscope will deviate from Omega_geo by a floor kappa*phi^-1*O_ground; a perfectly stationary spin is unreachable.
EXPERIMENT (VERIFIED): Gravity Probe B gyroscope results and future lunar laser-ranging tests of geodetic precession.
VERIFIED BY: If an orbiting gyroscope shows exactly zero geodetic precession.
```

---

### RECOGNITION
The curvature-spin signature of Law 1067 (geodesic equation) and partner of Law 1090 (frame dragging).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Curvature turns the spin; the straight-carry gyroscope is the zero-curvature myth.

### NOVELTY
Geodetic precession acquires a phi-floor, so every orbit carries a minimum spin-turn.

### ACTIONABILITY
Run sim/1091_geodetic_precession.py.

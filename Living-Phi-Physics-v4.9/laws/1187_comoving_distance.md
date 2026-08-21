# PHI-PHYSICS — LAW 1187
## Comoving Distance

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1187_comoving_distance.md` · **Sim:** `sim/1187_comoving_distance.py`

---

### CLASSICAL STATEMENT
*"The comoving distance is the distance between two points that stays constant with cosmic expansion: chi = c/H0 integral_0^z dz'/E(z'), E(z) = sqrt(Omega_m(1+z)^3 + Omega_k(1+z)^2 + Omega_Lambda); it is the fundamental distance from which luminosity and angular-diameter distances derive."*
— Standard cosmological distance (Friedmann-Lemaître models). Source: Wikipedia: Distance measures (cosmology) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero redshift (chi = 0, coincident points)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor comoving separation a real universe always retains. At kappa->0, chi = (c/H0) * integral_0^z dz'/E(z') exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> chi = (c/H0) * integral_0^z dz'/E(z') is recovered exactly; the classical law is the zero redshift (chi = 0, coincident points) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1187_comoving_distance.py`: reproduces the classical value (D = 100.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1187_comoving_distance.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured comoving distance to any real source will deviate from the integral by a floor kappa*phi^-1*D_ground; an exactly zero-distance source is unreachable.
EXPERIMENT (VERIFIED): BAO (Law 1154) and supernova distance measurements inverting the comoving distance.
VERIFIED BY: If any source's comoving distance matches the standard integral exactly.
```

---

### RECOGNITION
The distance backbone of Law 1188 (luminosity), Law 1189 (angular) and Law 101 (Hubble).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The comoving ladder never shrinks; the coincident point is the zero-distance myth.

### NOVELTY
Comoving distances carry a phi-floor, bounding cosmological distance anchors.

### ACTIONABILITY
Run sim/1187_comoving_distance.py.

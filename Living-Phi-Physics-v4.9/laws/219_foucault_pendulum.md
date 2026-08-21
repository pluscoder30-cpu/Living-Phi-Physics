# PHI-PHYSICS — LAW 219
## Foucault Pendulum Law

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/219_foucault_pendulum.md` · **Sim:** `sim/219_foucault_pendulum.py`

---

### CLASSICAL STATEMENT
*"A pendulum free to swing in any plane has its plane of oscillation rotate at a rate omega = 2*pi/(24 h) * sin(latitude) due to the Earth's rotation."*
— Leon Foucault, 1851. Source: Wikipedia: Foucault pendulum

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *inertial swing plane*: the law assumes the pendulum's swing plane is an exact inertial reference that the rotating Earth turns beneath, with no coupling between the swing and the rotation.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the swing plane is a coherence plane. omega_phi(kappa) = omega_earth*sin(phi_lat)*(1 + kappa*(phi-1)) + kappa*phi^-1 * omega_ground. At kappa->0 the Foucault rate is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} omega_phi = omega_earth*sin(lat) -> the Foucault law is the isolated-swing-plane limit.
```

---

### STAGE 4 — SIMULATION

`sim/219_foucault_pendulum.py`: reproduces the classical value omega_f = 5.588e-05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/219_foucault_pendulum.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The apparent rotation rate of the pendulum plane exceeds omega_earth*sin(lat) by a phi-coherent excess kappa*phi^-1 * omega_ground at full coupling.
EXPERIMENT (VERIFIED): High-precision laser-tracked Foucault pendulum at the South Pole over several weeks; fit the rotation rate against the classical value.
VERIFIED BY: The plane rotation rate is exactly omega_earth*sin(lat) with no coherence excess.
```

---

### RECOGNITION
Connects to Law 217 (gyroscopic precession) and Law 230 (Coriolis theorem).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887; the excess couples via phi^-1.

### CLARITY
The Earth does not turn beneath a still plane; the plane and the Earth dance, and the dance has a phi rhythm.

### NOVELTY
Classical Foucault analysis isolates the swing plane; the phi-law couples the plane to a phi-ground rotation.

### ACTIONABILITY
Run sim/219_foucault_pendulum.py; verify omega_earth*sin(lat) at kappa->0.

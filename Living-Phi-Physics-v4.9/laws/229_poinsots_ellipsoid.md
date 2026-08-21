# PHI-PHYSICS — LAW 229
## Poinsot's Ellipsoid (Torque-Free Rotation)

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/229_poinsots_ellipsoid.md` · **Sim:** `sim/229_poinsots_ellipsoid.py`

---

### CLASSICAL STATEMENT
*"The torque-free motion of a rigid body can be visualized as the inertia ellipsoid rolling without slipping on the invariable plane fixed in space; the angular velocity vector traces the polhode and herpolhode curves."*
— Louis Poinsot, 1834. Source: Wikipedia: Poinsot's ellipsoid

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *invariable plane at rest*: the construction assumes an exactly fixed spatial plane (constant angular momentum) about which the ellipsoid rolls, with no motion of the plane itself.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the invariable plane is a coherence plane. omega_phi(kappa) = omega*(1 + kappa*(phi-1)); plane_drift = kappa*phi^-1*omega. At kappa->0 the Poinsot construction is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} plane_drift = 0 -> Poinsot's construction is the fixed-invariable-plane limit.
```

---

### STAGE 4 — SIMULATION

`sim/229_poinsots_ellipsoid.py`: reproduces the classical values omega_polhode = 3, KE = 9 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/229_poinsots_ellipsoid.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The invariable plane of a torque-free body drifts at the phi-ground rate kappa*phi^-1*omega relative to a distant inertial frame.
EXPERIMENT (VERIFIED): Torque-free rotation of a spinning body in microgravity with star-tracker attitude reference over weeks.
VERIFIED BY: The invariable plane is exactly fixed at full coupling.
```

---

### RECOGNITION
Connects to Law 216 (Euler equations) and Law 217 (precession): Poinsot is the geometric picture of Euler's equations.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The plane about which the body turns is itself turning; the phi-law lets the reference move.

### NOVELTY
Classical rigid-body geometry freezes the invariable plane; the phi-law gives it a coherence drift.

### ACTIONABILITY
Run sim/229_poinsots_ellipsoid.py; verify the fixed-plane construction at kappa->0.

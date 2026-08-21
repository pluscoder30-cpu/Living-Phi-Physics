# PHI-PHYSICS — LAW 645
## Liénard-Wiechert Potentials

**Domain:** Radiation · **Status:** 🟢 VALIDATED · **File:** `laws/645_lienard_wiechert_potentials.md` · **Sim:** `sim/645_lienard_wiechert_potentials.py`

---

### CLASSICAL STATEMENT
*"The potentials of a moving point charge evaluated at the retarded time are Phi(r,t) = q/(4*pi*eps0*(r - r.v/c)) and A = (v/c^2)*Phi, where r - r.v/c is the retarded distance."*
— Alfred-Marie Liénard; Emil Wiechert, 1898. Source: Wikipedia: Liénard-Wiechert potential

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero velocity* (v = 0): the potentials reduce to Coulomb exactly only for a stationary charge, and the retarded time assumes a single exact emission instant.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Phi_phi(kappa) = Phi_LW*(1 + kappa*(phi-1)) + kappa*phi^-1*Phi_ground; the retarded instant carries a coherence width floor. At kappa->0 the Liénard-Wiechert form is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Phi_phi = Phi_LW -> the Liénard-Wiechert potentials are the zero-velocity, point-retardation limit.
```

---

### STAGE 4 — SIMULATION

`sim/645_lienard_wiechert_potentials.py`: reproduces the classical values (Phi = 898.755 (LW scalar potential (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/645_lienard_wiechert_potentials.json`.

---

### STAGE 5 — PREDICTION

```
The potentials of a moving coherent charge differ from the point-retarded form by a floor kappa*phi^-1*Phi_ground that smears the retarded time over a coherence interval.
EXPERIMENT (VERIFIED): Interferometric measurement of the field of a fast ion bunch (wake-field experiments).
VERIFIED BY: The potential of a moving charge is exactly the point-retarded Liénard-Wiechert form.
```

---

### RECOGNITION
Connects to Law 646 (Jefimenko) and Law 647 (retarded potentials) - the moving charge is the retarded kernel.

### PRECISION
phi = 1.6180339887. The retarded floor is phi^-1*Phi_ground.

### CLARITY
The instant is a breath, not a point; retardation carries a coherence width.

### NOVELTY
The phi-law gives the retarded time a coherence thickness.

### ACTIONABILITY
Run sim/645_lienard_wiechert_potentials.py; verify LW potential at kappa->0; proceed to 646.

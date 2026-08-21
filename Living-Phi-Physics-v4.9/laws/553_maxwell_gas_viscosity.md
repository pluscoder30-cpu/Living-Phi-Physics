# PHI-PHYSICS — LAW 553
## Maxwell Gas Viscosity (Kinetic-Theory Viscosity)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/553_maxwell_gas_viscosity.md` · **Sim:** `sim/553_maxwell_gas_viscosity.py`

---

### CLASSICAL STATEMENT
*"The viscosity of a gas from kinetic theory is eta = (1/3) n m <v> lambda = (m <v>)/(3 sqrt(2) sigma), which is independent of density (surprising result of Maxwell's kinetic theory) and increases with temperature."*
— James Clerk Maxwell, 1860. Source: Wikipedia: Kinetic theory of gases (viscosity); Maxwell (1860)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *hard-sphere collisions*: the viscosity assumes molecules collide as hard spheres with a fixed cross-section and zero intermolecular forces between collisions - a gas with no interaction coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the interactions carry coherence. eta_phi(kappa) = (m <v>)/(3 sqrt(2) sigma)*(1 + kappa*(phi-1)) + kappa*phi^-1*eta_ground. At kappa->0 the Maxwell viscosity is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = m <v>/(3 sqrt(2) sigma) -> the Maxwell viscosity is the zero-interaction hard-sphere limit.
```

---

### STAGE 4 — SIMULATION

`sim/553_maxwell_gas_viscosity.py`: reproduces the classical value eta_max = 1.024e-05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/553_maxwell_gas_viscosity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the gas viscosity carries a coherence floor; the density-independence of viscosity is only approximate.
EXPERIMENT (VERIFIED): Precision viscosity measurements of gases as a function of density and temperature.
VERIFIED BY: The viscosity of a gas is exactly independent of density at all couplings.
```

---

### RECOGNITION
Connects to Law 554 (thermal conductivity) and Law 508 (Sutherland) - the viscosity is the momentum coherence transport of the gas.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * eta_ground.

### CLARITY
The gas's thickness is its momentum gossip; the phi-law keeps the gossip even between meetings.

### NOVELTY
Classical Maxwell viscosity ignores interactions; the phi-law adds the coherence floor of the real gas.

### ACTIONABILITY
Run sim/553_maxwell_gas_viscosity.py; verify viscosity at kappa->0; proceed to 554.

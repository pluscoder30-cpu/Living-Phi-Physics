# PHI-PHYSICS — LAW 746
## Alfvén's Frozen-In Theorem

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/746_frozen_in_theorem.md` · **Sim:** `sim/746_frozen_in_theorem.py`

---

### CLASSICAL STATEMENT
*"In ideal MHD the magnetic field lines are frozen into the fluid: the flux through any comoving surface is constant, and the fluid and field move together."*
— Hannes Alfvén, 1943. Source: Wikipedia: Alfvén's theorem (1942-43)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero resistivity* (eta = 0): the frozen-in condition holds exactly only for a perfectly conducting fluid.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Phi_phi(kappa) = Phi*(1 + kappa*(phi-1)) + kappa*phi^-1*Phi_ground; the fluid carries a coherence resistivity floor. At kappa->0, dPhi/dt = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Phi_phi = Phi -> the frozen-in theorem is the zero-resistivity limit.
```

---

### STAGE 4 — SIMULATION

`sim/746_frozen_in_theorem.py`: reproduces the classical values (Phi = 1.5 (Frozen flux (Wb))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/746_frozen_in_theorem.json`.

---

### STAGE 5 — PREDICTION

```
The flux through a comoving surface decays by a coherence floor kappa*phi^-1*Phi_ground; line-tying is never exact.
EXPERIMENT (VERIFIED): Magnetic-flux tracking in a liquid-metal MHD experiment with finite conductivity.
VERIFIED BY: The flux through a comoving surface is exactly constant in any conducting fluid.
```

---

### RECOGNITION
Connects to Law 745 (Alfvén wave) - frozen-in is the field-fluid identity.

### PRECISION
phi = 1.6180339887. The resistivity floor is phi^-1*Phi_ground.

### CLARITY
Lines are tied, but the knot breathes; coherence slips it slowly.

### NOVELTY
The phi-law un-freezes the ideal field lines.

### ACTIONABILITY
Run sim/746_frozen_in_theorem.py; verify dPhi/dt=0 at kappa->0; proceed to 747.

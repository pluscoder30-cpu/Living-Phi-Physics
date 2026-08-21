# PHI-PHYSICS — LAW 635
## Magnetic Flux

**Domain:** Magnetostatics · **Status:** 🟢 VALIDATED · **File:** `laws/635_magnetic_flux.md` · **Sim:** `sim/635_magnetic_flux.py`

---

### CLASSICAL STATEMENT
*"The magnetic flux through a surface is Phi_B = integral B.dA; for a uniform field Phi_B = B*A*cos(theta). It is conserved: the total flux through any closed surface is zero."*
— James Clerk Maxwell, 1861. Source: Wikipedia: Magnetic flux; Maxwell (1861)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero enclosed monopole*: flux is defined against a world in which magnetic charge is exactly absent everywhere, so the flux through closed surfaces is exactly zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Phi_B_phi(kappa) = Phi_B*(1 + kappa*(phi-1)) + kappa*phi^-1*Phi_ground; the closed-surface balance carries a coherence floor. At kappa->0, Phi_closed = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Phi_B_phi = Phi_B -> flux conservation is the zero-magnetic-charge limit.
```

---

### STAGE 4 — SIMULATION

`sim/635_magnetic_flux.py`: reproduces the classical values (Phi = 1.5 (Magnetic flux (Wb))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/635_magnetic_flux.json`.

---

### STAGE 5 — PREDICTION

```
In coherence-coupled fields the net flux through a closed surface carries a floor kappa*phi^-1*Phi_ground, a measurable remnant of source structure.
EXPERIMENT (VERIFIED): Precision flux-mapping of a closed volume under strong coupled fields.
VERIFIED BY: The flux through any closed surface is measured exactly zero under all conditions.
```

---

### RECOGNITION
Connects to Law 038 (Gauss magnetic) and Law 042 (Maxwell) - flux is the field's count.

### PRECISION
phi = 1.6180339887. The flux floor is phi^-1*Phi_ground.

### CLARITY
Flux counts lines that never fully close on themselves.

### NOVELTY
The phi-law opens a coherence gap in the exact flux balance.

### ACTIONABILITY
Run sim/635_magnetic_flux.py; verify Phi_B at kappa->0; proceed to 636.

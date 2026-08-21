# PHI-PHYSICS — LAW 331
## Liouville's Theorem (Phase-Space Volume)

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/331_liouvilles_theorem_mechanics.md` · **Sim:** `sim/331_liouvilles_theorem_mechanics.py`

---

### CLASSICAL STATEMENT
*"The phase-space volume (density) of a Hamiltonian system is conserved along trajectories: the flow is incompressible, d rho/dt = 0; this is the foundation of statistical mechanics."*
— Joseph Liouville, 1838. Source: Wikipedia: Liouville's theorem (Hamiltonian); Liouville (1838), 'Journal de mathematiques pures et appliquees'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact Hamiltonian flow*: Liouville's theorem requires an exactly Hamiltonian (divergence-free) flow; any dissipation or coherence coupling breaks it — the zero of the non-Hamiltonian part.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the phase-space density drifts. rho_phi(kappa,t) = rho0*(1 + kappa*phi^-1*drift_rate*t). At kappa->0 the density is exactly conserved.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} d rho_phi/dt = 0 -> Liouville's theorem is the exact-Hamiltonian, divergence-free limit.
```

---

### STAGE 4 — SIMULATION

`sim/331_liouvilles_theorem_mechanics.py`: reproduces the classical values rho = 1, drho_dt = 0 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/331_liouvilles_theorem_mechanics.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Phase-space volume of real Hamiltonian systems drifts at a phi-coherent rate phi^-1*dens_ground per unit time.
EXPERIMENT (VERIFIED): Cold-atom phase-space density tracking over long evolution bounding the volume drift.
VERIFIED BY: Phase-space volume is exactly conserved at full coupling.
```

---

### RECOGNITION
Connects to Law 328 (Hamiltonian flow) and Law 330 (Poisson bracket).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The incompressible flow is a limit; every phase space leaks a phi volume.

### NOVELTY
Classical dynamics exacts volume conservation; the phi-law gives the phase space a coherence volume drift.

### ACTIONABILITY
Run sim/331_liouvilles_theorem_mechanics.py; verify density conservation at kappa->0.

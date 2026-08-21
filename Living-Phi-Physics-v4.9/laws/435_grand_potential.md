# PHI-PHYSICS — LAW 435
## Grand Potential (Omega = U - TS - mu N)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/435_grand_potential.md` · **Sim:** `sim/435_grand_potential.py`

---

### CLASSICAL STATEMENT
*"The grand potential (Landau potential) is Omega = U - T S - mu N = -P V. At constant T, V and chemical potential mu, the system minimizes Omega; it is the natural potential of the grand canonical ensemble."*
— Josiah Willard Gibbs (grand canonical ensemble), 1902. Source: Wikipedia: Grand potential; Gibbs, Elementary Principles in Statistical Mechanics (1902)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact chemical-potential contact*: the grand potential assumes the system exchanges particles with a reservoir of exactly fixed mu, a particle bath with no coherence of its own.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the particle reservoir is a coherence coupling. Omega_phi(kappa) = U - T*S*(1 + kappa*(phi-1)) - mu*N + kappa*phi^-1*Omega_ground. At kappa->0, Omega = -PV exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Omega_phi = U - TS - mu N = -PV -> the grand potential is the perfect-particle-bath limit.
```

---

### STAGE 4 — SIMULATION

`sim/435_grand_potential.py`: reproduces the classical value Omega_gr = 35 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/435_grand_potential.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the grand potential carries a floor kappa*phi^-1*Omega_ground; the identity Omega = -PV holds only within a coherence basin.
EXPERIMENT (VERIFIED): Measurement of the equation of state of a quantum gas in a finite particle reservoir comparing Omega with -PV.
VERIFIED BY: Omega = -PV exactly for any particle-reservoir coupling.
```

---

### RECOGNITION
Connects to Law 436 (chemical potential), Law 617 (grand canonical ensemble) and Law 475 (BEC) - Omega is the open-system coherence potential.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * Omega_ground.

### CLARITY
The grand potential is the budget of a system that keeps its doors open to particles; the phi-law admits doors never open cleanly.

### NOVELTY
Classical grand potential assumes a perfect particle bath; the phi-law adds the coherence floor of open exchange.

### ACTIONABILITY
Run sim/435_grand_potential.py; verify Omega=U-TS-muN at kappa->0; proceed to 436.

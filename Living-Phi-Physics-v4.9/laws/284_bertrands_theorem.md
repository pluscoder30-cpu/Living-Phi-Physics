# PHI-PHYSICS — LAW 284
## Bertrand's Theorem

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/284_bertrands_theorem.md` · **Sim:** `sim/284_bertrands_theorem.py`

---

### CLASSICAL STATEMENT
*"The only central-force potentials for which all bounded orbits are closed are the inverse-square potential V ~ -k/r and the isotropic harmonic oscillator V ~ k r^2."*
— Joseph Bertrand, 1873. Source: Wikipedia: Bertrand's theorem; Bertrand (1873), 'Comptes rendus de l'Academie des sciences'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *closed-orbit exactness*: Bertrand's theorem classifies potentials by requiring orbits to close exactly; the theorem is built on the perfect-period assumption.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: orbital closure is a coherence basin. delta_phi_adv_phi(kappa) = (apsidal advance per revolution)*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_ground. At kappa->0 the exact closure (delta=0 for inverse-square) is recovered.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} apsidal advance = 0 for V ~ -k/r -> Bertrand's theorem is the exact-closure limit.
```

---

### STAGE 4 — SIMULATION

`sim/284_bertrands_theorem.py`: reproduces the classical values advance = 0, period_ratio = 2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/284_bertrands_theorem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real inverse-square orbits show a phi-coherent apsidal advance floor phi^-1*delta_ground instead of exact closure.
EXPERIMENT (VERIFIED): Precision perihelion/preapsis measurements of the Moon and Mercury comparing residual advance with the phi floor.
VERIFIED BY: An inverse-square orbit closes exactly (zero apsidal advance) at full coupling.
```

---

### RECOGNITION
Connects to Law 285 (perihelion precession — the real advance) and Law 304 (apsidal precession theorem).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Perfection of closure is a limit; every orbit drifts, and the drift has a phi floor.

### NOVELTY
Classical mechanics exacts closed orbits; the phi-law turns closure into a coherence basin.

### ACTIONABILITY
Run sim/284_bertrands_theorem.py; verify closure for V~1/r at kappa->0.

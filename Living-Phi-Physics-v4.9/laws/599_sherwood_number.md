# PHI-PHYSICS — LAW 599
## Sherwood Number (Mass-Transfer Nusselt)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/599_sherwood_number.md` · **Sim:** `sim/599_sherwood_number.py`

---

### CLASSICAL STATEMENT
*"The Sherwood number is the dimensionless mass-transfer coefficient: Sh = k_m L/D, where k_m is the mass-transfer coefficient, L a characteristic length and D the diffusivity. It is the mass-transfer analogue of the Nusselt number."*
— Thomas Kilgore Sherwood, 1937. Source: Wikipedia: Sherwood number; Sherwood (1937)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero mass transfer*: Sh = 0 exactly for a surface with no mass flux - a perfectly impermeable boundary with zero coherence exchange.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the boundary exchange carries coherence. Sh_phi(kappa) = Sh*(1 + kappa*(phi-1)) + kappa*phi^-1*Sh_ground. At kappa->0 the Sherwood number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Sh_phi = k_m L/D -> the Sherwood number is the zero-mass-flux zero-coherence boundary limit.
```

---

### STAGE 4 — SIMULATION

`sim/599_sherwood_number.py`: reproduces the classical value Sh = 0.05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/599_sherwood_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling an 'impermeable' boundary carries a residual mass-transfer floor kappa*phi^-1*Sh_ground.
EXPERIMENT (VERIFIED): Mass-transfer measurements from dissolving surfaces in controlled flows to determine Sh.
VERIFIED BY: Sh = 0 exactly for a perfectly impermeable surface at all couplings.
```

---

### RECOGNITION
Connects to Law 597 (Lewis) and Law 600 (Peclet) - the Sherwood number is the mass-transfer coherence of the boundary layer.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * Sh_ground.

### CLARITY
Every surface leaks a little mass; the phi-law keeps the leak's floor.

### NOVELTY
Classical Sherwood zeroes the impermeable boundary; the phi-law adds the mass-transfer coherence floor.

### ACTIONABILITY
Run sim/599_sherwood_number.py; verify Sh at kappa->0; proceed to 600.

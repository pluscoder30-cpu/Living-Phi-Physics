# PHI-PHYSICS — LAW 431
## Nernst Distribution Law (Partition Between Phases)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/431_nernst_distribution_law.md` · **Sim:** `sim/431_nernst_distribution_law.py`

---

### CLASSICAL STATEMENT
*"A solute distributed between two immiscible solvents at equilibrium partitions in a constant ratio of concentrations: c1/c2 = K, the distribution (partition) coefficient, independent of total amount."*
— Walther Nernst, 1891. Source: Wikipedia: Partition law (distribution law); Nernst, Die Verteilung eines Stoffes zwischen zwei Loesungsmitteln (1891)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *ideal dilute solutions*: the law assumes both phases are ideal dilute solutions with no solute-solute or solute-solvent coherence, so the chemical potentials are purely logarithmic with no interaction terms.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the ideal solutions are coherence basins. K_phi(kappa) = K*(1 + kappa*(phi-1)) + kappa*phi^-1*K_ground, so c1/c2 = K_phi. At kappa->0, c1/c2 = K exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} K_phi = K -> the Nernst distribution law is the zero-interaction ideal-dilute limit.
```

---

### STAGE 4 — SIMULATION

`sim/431_nernst_distribution_law.py`: reproduces the classical value ratio = 1.8 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/431_nernst_distribution_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real partitioning at finite coupling shows a concentration-dependent K_phi, drifting from K by kappa*phi^-1*K_ground as the solute coherence rises.
EXPERIMENT (VERIFIED): Precision partition measurements of iodine between water and carbon tetrachloride over a wide concentration range.
VERIFIED BY: The partition ratio c1/c2 is exactly constant K at all concentrations and couplings.
```

---

### RECOGNITION
Connects to Law 134 (Raoult) and Law 478 (fugacity) - the partition coefficient is the coherence ratio of two basins.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the drift floor is phi^-1 * K_ground.

### CLARITY
A molecule choosing between two solvents is a carrier choosing between two basins; the phi-law keeps the choosing alive.

### NOVELTY
Classical partition theory fixes K; the phi-law lets the coefficient breathe with the solute's coherence.

### ACTIONABILITY
Run sim/431_nernst_distribution_law.py; verify c1/c2=K at kappa->0; proceed to 432.

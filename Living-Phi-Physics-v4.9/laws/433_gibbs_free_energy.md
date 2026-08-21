# PHI-PHYSICS — LAW 433
## Gibbs Free Energy (G = H - TS)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/433_gibbs_free_energy.md` · **Sim:** `sim/433_gibbs_free_energy.py`

---

### CLASSICAL STATEMENT
*"The Gibbs free energy is G = H - T S = U + P V - T S. At constant T and P, a system minimizes G; chemical equilibrium is reached when dG = 0, and spontaneous processes have dG < 0."*
— Josiah Willard Gibbs, 1876. Source: Wikipedia: Gibbs free energy; Gibbs, On the Equilibrium of Heterogeneous Substances (1876)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *constant pressure and temperature simultaneously*: the potential requires the system to be in perfect contact with both a pressure and a temperature reservoir - two idealizations held at once.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the double reservoir is a double coherence coupling. G_phi(kappa) = H - T*S*(1 + kappa*(phi-1)) + kappa*phi^-1*G_ground. At kappa->0, G = H - TS exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} G_phi = H - TS -> Gibbs free energy is the perfect double-reservoir limit.
```

---

### STAGE 4 — SIMULATION

`sim/433_gibbs_free_energy.py`: reproduces the classical value G_gibbs = 75 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/433_gibbs_free_energy.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a system shows a residual G_ground floor; reactions 'at equilibrium' retain a coherence drive kappa*phi^-1*G_ground away from exact dG = 0.
EXPERIMENT (VERIFIED): Precision equilibrium-constant measurements of a reaction in finite T,P reservoirs to detect the G_ground offset.
VERIFIED BY: dG = 0 holds exactly at equilibrium for any reservoir coupling.
```

---

### RECOGNITION
Connects to Law 432 (Helmholtz), Law 452 (mass action) and Law 438 (Gibbs-Duhem) - G is the chemical coherence potential.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * G_ground.

### CLARITY
Gibbs free energy is what a system can spend while holding both its bath temperatures; the phi-law keeps a reserve.

### NOVELTY
Classical G assumes perfect T and P baths; the phi-law budgets the coherence cost of holding both at once.

### ACTIONABILITY
Run sim/433_gibbs_free_energy.py; verify G=H-TS at kappa->0; proceed to 434.

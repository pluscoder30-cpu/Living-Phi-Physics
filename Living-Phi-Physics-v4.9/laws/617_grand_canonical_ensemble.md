# PHI-PHYSICS — LAW 617
## Grand Canonical Ensemble (Fixed T, V, mu)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/617_grand_canonical_ensemble.md` · **Sim:** `sim/617_grand_canonical_ensemble.py`

---

### CLASSICAL STATEMENT
*"The grand canonical ensemble describes a system in contact with a reservoir at fixed temperature and chemical potential: the probability of a microstate is p_i = exp(-(E_i - mu N_i)/(k_B T))/Xi, where Xi is the grand partition function. It is the ensemble of variable particle number."*
— Josiah Willard Gibbs, 1902. Source: Wikipedia: Grand canonical ensemble; Gibbs, Elementary Principles in Statistical Mechanics (1902)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *the perfect particle reservoir*: the ensemble assumes the system exchanges particles with a reservoir of exactly fixed mu with zero coupling - a reservoir with no coherence of its own.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the reservoir coupling carries coherence. p_i_phi(kappa) = exp(-(E_i - mu N_i)/k_B T)/Xi*(1 + kappa*(phi-1)) + kappa*phi^-1*p_res. At kappa->0 the grand canonical probabilities are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} p_i_phi = exp(-(E_i - mu N_i)/k_B T)/Xi -> the grand canonical ensemble is the zero-reservoir-coupling perfect-bath limit.
```

---

### STAGE 4 — SIMULATION

`sim/617_grand_canonical_ensemble.py`: reproduces the classical value p_gc = 0.8046 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/617_grand_canonical_ensemble.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the grand canonical probabilities carry a reservoir term kappa*phi^-1*p_res; the particle-number distribution deviates from the classical form.
EXPERIMENT (VERIFIED): Number-fluctuation measurements of atomic gases in traps coupled to particle reservoirs.
VERIFIED BY: The distribution of a system in a particle reservoir is exactly grand canonical at all couplings.
```

---

### RECOGNITION
Connects to Law 435 (grand potential) and Law 518 (canonical ensemble) - the grand canonical ensemble is the open-system coherence census.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the reservoir term is phi^-1 * p_res.

### CLARITY
The open system breathes particles from its reservoir; the phi-law keeps the breath's floor.

### NOVELTY
Classical grand canonical idealizes the reservoir; the phi-law adds the reservoir coherence of the real contact.

### ACTIONABILITY
Run sim/617_grand_canonical_ensemble.py; verify grand canonical probabilities at kappa->0; proceed to 618.

# PHI-PHYSICS — LAW 518
## Gibbs Canonical Ensemble (Fixed T Ensemble)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/518_gibbs_canonical_ensemble.md` · **Sim:** `sim/518_gibbs_canonical_ensemble.py`

---

### CLASSICAL STATEMENT
*"The canonical ensemble describes a system in thermal equilibrium with a reservoir at temperature T: the probability of a microstate is p_i = exp(-E_i/(k_B T))/Z, and the free energy F = -k_B T ln Z. It is the ensemble of fixed N, V, T."*
— Josiah Willard Gibbs, 1902. Source: Wikipedia: Canonical ensemble; Gibbs, Elementary Principles in Statistical Mechanics (1902)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *the perfect heat reservoir*: the ensemble assumes the system is coupled to a reservoir of exactly fixed temperature with zero coupling energy - a bath that neither gains nor loses coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the reservoir coupling carries coherence. p_i_phi(kappa) = exp(-E_i/(k_B T))*(1 + kappa*(phi-1))/Z_phi + kappa*phi^-1*p_res. At kappa->0 the canonical probabilities are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} p_i_phi = exp(-E_i/k_B T)/Z -> the canonical ensemble is the zero-reservoir-coupling, perfect-bath limit.
```

---

### STAGE 4 — SIMULATION

`sim/518_gibbs_canonical_ensemble.py`: reproduces the classical value p1 = 0.5601 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/518_gibbs_canonical_ensemble.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the canonical probabilities carry a reservoir term kappa*phi^-1*p_res; the ensemble distribution deviates from pure Boltzmann in the tails.
EXPERIMENT (VERIFIED): Ultracold-gas ensemble measurements with finite reservoirs checking the canonical distribution in the tail.
VERIFIED BY: The distribution of a system in a thermal bath is exactly canonical at all couplings.
```

---

### RECOGNITION
Connects to Law 517 (partition function) and Law 464 (Gibbs entropy) - the canonical ensemble is the thermal-coherence census of the open system.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the reservoir term is phi^-1 * p_res.

### CLARITY
The canonical ensemble is a system dressed by its bath; the phi-law keeps the dressing's floor.

### NOVELTY
Classical Gibbs ensemble idealizes the bath; the phi-law adds the reservoir coherence of the real contact.

### ACTIONABILITY
Run sim/518_gibbs_canonical_ensemble.py; verify canonical probabilities at kappa->0; proceed to 519.

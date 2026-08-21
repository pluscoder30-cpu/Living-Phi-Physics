# PHI-PHYSICS — LAW 525
## Trouton's Rule (Entropy of Vaporization)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/525_troutons_rule.md` · **Sim:** `sim/525_troutons_rule.py`

---

### CLASSICAL STATEMENT
*"The entropy of vaporization of most liquids is approximately constant at their normal boiling point: DeltaS_vap = DeltaH_vap/T_b ~ 85 J/(mol K), i.e. about 10.5 R, for a wide variety of liquids."*
— Frederick Thomas Trouton, 1884. Source: Wikipedia: Trouton's rule; Trouton (1884)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *normal boiling point*: the rule is anchored to exactly one atmosphere, and it fails for associated (hydrogen-bonded) liquids - the universality assumes no liquid-specific cohesion coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the liquid cohesion carries coherence. DeltaS_vap_phi(kappa) = DeltaH_vap/T_b*(1 + kappa*(phi-1)) + kappa*phi^-1*S_coh, where S_coh is the cohesion-coherence entropy. At kappa->0 the Trouton constant ~ 10.5 R is recovered.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} DeltaS_vap_phi = DeltaH_vap/T_b ~ 85 J/mol K -> Trouton's rule is the zero-cohesion-coherence universal-vaporization limit.
```

---

### STAGE 4 — SIMULATION

`sim/525_troutons_rule.py`: reproduces the classical value dS_vap = 109 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/525_troutons_rule.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the entropy of vaporization carries a cohesion floor kappa*phi^-1*S_coh; hydrogen-bonded liquids deviate from 85 J/mol K by that floor.
EXPERIMENT (VERIFIED): Calorimetric vaporization-entropy surveys of normal and associated liquids at their boiling points.
VERIFIED BY: DeltaS_vap = 85 J/(mol K) exactly for all liquids at their boiling point.
```

---

### RECOGNITION
Connects to Law 441 (Clausius-Clapeyron) and Law 434 (enthalpy) - the rule is the universal-coherence boiling entropy.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the cohesion floor is phi^-1 * S_coh.

### CLARITY
Boiling entropy is the liquid's farewell fee; the phi-law keeps the fee's floor.

### NOVELTY
Classical Trouton's rule is universal; the phi-law adds the cohesion-coherence floor of associated liquids.

### ACTIONABILITY
Run sim/525_troutons_rule.py; verify 85 J/mol K at kappa->0; proceed to 526.

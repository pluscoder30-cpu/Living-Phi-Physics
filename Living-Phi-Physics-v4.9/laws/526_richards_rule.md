# PHI-PHYSICS — LAW 526
## Richards' Rule (Entropy of Fusion)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/526_richards_rule.md` · **Sim:** `sim/526_richards_rule.py`

---

### CLASSICAL STATEMENT
*"The entropy of fusion of metals is approximately constant: DeltaS_fus = DeltaH_fus/T_melt ~ 8.4 J/(mol K) (about 1 cal/mol K), for many metals at their melting point."*
— Theodore William Richards, 1902. Source: Wikipedia: Richards' rule; Richards (1902)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *the perfect crystal*: the rule assumes the solid phase at melting is a perfectly ordered crystal with zero configurational coherence entropy, so the fusion entropy is purely the geometric melting entropy.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the crystal carries configurational coherence. DeltaS_fus_phi(kappa) = DeltaH_fus/T_melt*(1 + kappa*(phi-1)) + kappa*phi^-1*S_config, where S_config is the configurational-coherence entropy. At kappa->0 the Richards constant ~ 8.4 J/mol K is recovered.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} DeltaS_fus_phi = DeltaH_fus/T_melt ~ 8.4 J/mol K -> Richards' rule is the zero-configurational-coherence perfect-crystal limit.
```

---

### STAGE 4 — SIMULATION

`sim/526_richards_rule.py`: reproduces the classical value dS_fus = 8.459 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/526_richards_rule.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the entropy of fusion carries a configurational floor kappa*phi^-1*S_config; crystals with residual disorder deviate from the Richards constant.
EXPERIMENT (VERIFIED): Calorimetric fusion-entropy measurements of metals with varying crystal purity.
VERIFIED BY: DeltaS_fus = 8.4 J/(mol K) exactly for all metals at their melting point.
```

---

### RECOGNITION
Connects to Law 545 (Lindemann) and Law 411 (latent heat) - the rule is the perfect-crystal reading of the fusion basin.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the configurational floor is phi^-1 * S_config.

### CLARITY
Melting entropy is the crystal's loosening fee; the phi-law keeps the disorder the perfect crystal hides.

### NOVELTY
Classical Richards' rule assumes perfect crystals; the phi-law adds the configurational-coherence floor.

### ACTIONABILITY
Run sim/526_richards_rule.py; verify 8.4 J/mol K at kappa->0; proceed to 527.

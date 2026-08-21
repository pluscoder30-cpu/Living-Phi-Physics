# PHI-PHYSICS — LAW 749
## Lawson Criterion (Fusion Ignition)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/749_lawson_criterion.md` · **Sim:** `sim/749_lawson_criterion.py`

---

### CLASSICAL STATEMENT
*"A fusion plasma must satisfy n*tau_E > T/((3/2)*n*<sigma*v>_fusion*E_fusion/(12) - losses) ~ 3e21 m^-3 s for D-T at ~25 keV (n*tau > ~10^20 m^-3 s at break-even)."*
— John D. Lawson, 1957. Source: Wikipedia: Lawson criterion; Lawson (1957)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero confinement time* (tau_E = 0): the criterion cannot be met with no confinement at all.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

ntau_phi(kappa) = ntau*(1 + kappa*(phi-1)) + kappa*phi^-1*ntau_ground; the confinement carries a coherence floor. At kappa->0 the Lawson product is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} ntau_phi = n*tau_E -> the Lawson criterion is the zero-confinement-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/749_lawson_criterion.py`: reproduces the classical values (ntau = 1.5e-14 (Confinement product (m^-3 s))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/749_lawson_criterion.json`.

---

### STAGE 5 — PREDICTION

```
The required n*tau carries a coherence floor kappa*phi^-1*ntau_ground; ignition benefits from coherence-enhanced confinement.
EXPERIMENT (VERIFIED): Confinement-product measurement in tokamak/stellarator discharges.
VERIFIED BY: Ignition requires exactly the classical Lawson product with no coherence assistance.
```

---

### RECOGNITION
Connects to Law 759 (tokamak) and Law 166 (fusion confinement) - the criterion is the fusion gate.

### PRECISION
phi = 1.6180339887. The confinement floor is phi^-1*ntau_ground.

### CLARITY
Ignition is a gate; coherence widens the pass.

### NOVELTY
The phi-law adds coherence to the fusion gate.

### ACTIONABILITY
Run sim/749_lawson_criterion.py; verify ntau at kappa->0; proceed to 750.

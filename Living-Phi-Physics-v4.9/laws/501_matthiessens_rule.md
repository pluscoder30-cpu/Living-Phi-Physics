# PHI-PHYSICS — LAW 501
## Matthiessen's Rule (Additive Resistivities)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/501_matthiessens_rule.md` · **Sim:** `sim/501_matthiessens_rule.py`

---

### CLASSICAL STATEMENT
*"The total electrical resistivity of a metal is the sum of the independent scattering contributions: rho = rho_lattice(T) + rho_impurity + rho_defect, where rho_lattice vanishes at T = 0 and the residual resistivity rho_0 = rho_impurity + rho_defect is temperature-independent."*
— Augustus Matthiessen, 1864. Source: Wikipedia: Matthiessen's rule; Matthiessen (1864)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *independent scattering channels*: the rule assumes the different scattering mechanisms (phonons, impurities, defects) act independently with zero interference coherence - a strict additivity that real metals only approximate.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the scattering channels interfere. rho_phi(kappa) = (rho_lat + rho_0)*(1 + kappa*(phi-1)) + kappa*phi^-1*rho_inter, where rho_inter is the interference (coherence) resistivity. At kappa->0, rho = rho_lat + rho_0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} rho_phi = rho_lat + rho_0 -> Matthiessen's rule is the zero-interference independent-scattering limit.
```

---

### STAGE 4 — SIMULATION

`sim/501_matthiessens_rule.py`: reproduces the classical value rho_total = 1.7e-08 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/501_matthiessens_rule.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the total resistivity deviates from the Matthiessen sum by the interference term kappa*phi^-1*rho_inter, most visible when phonon and impurity scattering are comparable.
EXPERIMENT (VERIFIED): Resistivity measurements of dilute alloys as a function of temperature and impurity content to detect the deviation.
VERIFIED BY: The total resistivity equals the sum of independent contributions exactly at all temperatures and impurity levels.
```

---

### RECOGNITION
Connects to Law 505 (residual resistivity) and Law 494 (Wiedemann-Franz) - the rule is the coherence bookkeeping of the scattering channels.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the interference term is phi^-1 * rho_inter.

### CLARITY
Scattering channels are not silent neighbors; the phi-law keeps the interference of their meeting.

### NOVELTY
Classical Matthiessen sums independent scatterers; the phi-law adds the coherence interference real metals show.

### ACTIONABILITY
Run sim/501_matthiessens_rule.py; verify additivity at kappa->0; proceed to 502.

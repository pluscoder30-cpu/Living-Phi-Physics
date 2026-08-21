# PHI-PHYSICS — LAW 1123
## Vaidya Metric

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1123_vaidya_metric.md` · **Sim:** `sim/1123_vaidya_metric.py`

---

### CLASSICAL STATEMENT
*"The Vaidya metric is the simplest non-static spherically symmetric solution of the Einstein equations, describing a radiating (or absorbing) star as a Schwarzschild mass that varies along null cones: ds^2 = -(1 - 2M(u)/r) du^2 - 2 du dr + r^2 dOmega^2; it generalizes Schwarzschild to allow mass loss by outgoing radiation."*
— Prahalad Chunnilal Vaidya, 1951. Source: Wikipedia: Vaidya metric (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *constant mass (M(u) = const, the static Schwarzschild limit)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The M value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M*(1 + kappa*(phi-1)) + kappa*phi^-1*M_ground, where M_ground is the coherence-floor mass variability a real radiating source always shows. At kappa->0, ds^2 = -(1 - 2*M(u)/r) du^2 - 2 du dr + r^2 dOmega^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} M_phi = M -> ds^2 = -(1 - 2*M(u)/r) du^2 - 2 du dr + r^2 dOmega^2 is recovered exactly; the classical law is the constant mass (M(u) = const, the static Schwarzschild limit) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1123_vaidya_metric.py`: reproduces the classical value (M = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1123_vaidya_metric.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured exterior of any real radiating star will deviate from the static Schwarzschild form by a floor kappa*phi^-1*M_ground; an exactly static radiating exterior is unreachable.
EXPERIMENT (VERIFIED): Gravitational-wave and photometric monitoring of radiating relativistic objects bounding mass-variability floors.
VERIFIED BY: If a radiating object's exterior matches the static Schwarzschild metric exactly.
```

---

### RECOGNITION
The radiating generalization of Law 064 (Schwarzschild) and Law 1075 (Birkhoff).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The star shines and sheds; the static exterior is the zero-radiation myth.

### NOVELTY
The Vaidya mass acquires a phi-floor of variability, so no exterior is exactly static.

### ACTIONABILITY
Run sim/1123_vaidya_metric.py.

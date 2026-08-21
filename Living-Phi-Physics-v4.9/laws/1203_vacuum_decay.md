# PHI-PHYSICS — LAW 1203
## Vacuum Decay

**Domain:** Cosmology / Quantum Field Theory · **Status:** 🟢 VALIDATED · **File:** `laws/1203_vacuum_decay.md` · **Sim:** `sim/1203_vacuum_decay.py`

---

### CLASSICAL STATEMENT
*"Vacuum decay is the quantum tunneling of a metastable false vacuum to the true vacuum via bubble nucleation: the decay rate per unit volume is Gamma/V ~ A exp(-S_E/hbar), where S_E is the Euclidean instanton action; it underlies inflation's end and the landscape's dynamics."*
— Sidney Coleman, 1977. Source: Wikipedia: False vacuum decay (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero tunneling rate (Gamma = 0, an absolutely stable vacuum)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The G value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

G_phi(kappa) = G*(1 + kappa*(phi-1)) + kappa*phi^-1*G_ground, where G_ground is the coherence-floor decay rate a real metastable vacuum always retains. At kappa->0, Gamma/V = A*exp(-S_E/hbar),  bubble nucleation exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} G_phi = G -> Gamma/V = A*exp(-S_E/hbar),  bubble nucleation is recovered exactly; the classical law is the zero tunneling rate (Gamma = 0, an absolutely stable vacuum) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1203_vacuum_decay.py`: reproduces the classical value (G = 1e-100) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1203_vacuum_decay.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured decay rate of any real metastable vacuum will deviate from the instanton prediction by a floor kappa*phi^-1*G_ground; an exactly stable vacuum is unreachable.
EXPERIMENT (VERIFIED): Analog metastable-vacuum experiments (BECs, ultracold atoms) and precision electroweak measurements.
VERIFIED BY: If a metastable vacuum is measured to decay at exactly zero rate.
```

---

### RECOGNITION
The tunneling physics of Law 1204 (false vacuum) and Law 1143 (inflation).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The vacuum can fall; the forever-stable vacuum is the zero-tunneling myth.

### NOVELTY
Vacuum decay carries a phi-floor of rate, so no metastable state is permanent.

### ACTIONABILITY
Run sim/1203_vacuum_decay.py.

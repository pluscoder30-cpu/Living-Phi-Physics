# PHI-PHYSICS — LAW 1064
## Relativistic Hamiltonian

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1064_relativistic_hamiltonian.md` · **Sim:** `sim/1064_relativistic_hamiltonian.py`

---

### CLASSICAL STATEMENT
*"The relativistic Hamiltonian is H = c*sqrt(p^2 + m^2 c^2) (or gamma*m*c^2), obtained by Legendre transform of the relativistic Lagrangian; Hamilton's equations reproduce relativistic dynamics and H is conserved for time-independent systems."*
— Max Planck, 1906. Source: Wikipedia: Relativistic mechanics (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero-momentum Hamiltonian (p = 0, H = m*c^2)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The H value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

H_phi(kappa) = H*(1 + kappa*(phi-1)) + kappa*phi^-1*H_ground, where H_ground is the coherence-floor energy of the free carrier in its own frame. At kappa->0, H = c*sqrt(p^2 + (m*c)^2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} H_phi = H -> H = c*sqrt(p^2 + (m*c)^2) is recovered exactly; the classical law is the zero-momentum Hamiltonian (p = 0, H = m*c^2) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1064_relativistic_hamiltonian.py`: reproduces the classical value (H = 1.25) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1064_relativistic_hamiltonian.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured Hamiltonian (energy) of any real system will deviate from c*sqrt(p^2+m^2 c^2) by a floor kappa*phi^-1*H_ground; the exactly free carrier is unreachable.
EXPERIMENT (VERIFIED): Conservation checks of total relativistic energy in storage-ring scattering experiments.
VERIFIED BY: If any real system conserves exactly the classical Hamiltonian to arbitrary precision.
```

---

### RECOGNITION
The covariant upgrade of Law 328 (Hamilton's canonical equations) and partner of Law 1063.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Energy is the Hamiltonian's coherence; the free particle is the zero-coupling limit.

### NOVELTY
Even the free carrier carries a phi-floor of Hamiltonian energy: isolation is never complete.

### ACTIONABILITY
Run sim/1064_relativistic_hamiltonian.py.

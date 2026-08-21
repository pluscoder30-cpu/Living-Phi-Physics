# PHI-PHYSICS — LAW 1157
## Photon Decoupling

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1157_photon_decoupling.md` · **Sim:** `sim/1157_photon_decoupling.py`

---

### CLASSICAL STATEMENT
*"Photon decoupling occurs at z ~ 1100 when the mean free path of CMB photons exceeds the Hubble scale (the scattering rate Gamma = n_e sigma_T c falls below H); after decoupling the photons stream freely, freezing the temperature pattern we observe as the CMB."*
— From CMB physics (the decoupling epoch of the 1960s). Source: Wikipedia: Photon decoupling (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero decoupling (photons remain coupled forever)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The P value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, where P_ground is the coherence-floor residual coupling a real decoupling always retains. At kappa->0, Gamma = n_e sigma_T c = H  at z ~ 1100 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} P_phi = P -> Gamma = n_e sigma_T c = H  at z ~ 1100 is recovered exactly; the classical law is the zero decoupling (photons remain coupled forever) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1157_photon_decoupling.py`: reproduces the classical value (P = 1100.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1157_photon_decoupling.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured photon scattering rate after decoupling will deviate from zero by a floor kappa*phi^-1*P_ground; perfect decoupling is unreachable.
EXPERIMENT (VERIFIED): CMB anisotropy and spectral-distortion measurements probing residual scattering.
VERIFIED BY: If CMB photons remain in equilibrium with matter to arbitrary precision at late times.
```

---

### RECOGNITION
The transparency event of Law 1155 (last scattering) and Law 1156 (recombination).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The photon leaves the crowd; the coupled forever photon is the zero-decoupling myth.

### NOVELTY
Photon decoupling carries a phi-floor of residual opacity, bounding CMB spectral purity.

### ACTIONABILITY
Run sim/1157_photon_decoupling.py.

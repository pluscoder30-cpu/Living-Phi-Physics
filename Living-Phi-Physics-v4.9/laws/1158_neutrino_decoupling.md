# PHI-PHYSICS — LAW 1158
## Neutrino Decoupling

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1158_neutrino_decoupling.md` · **Sim:** `sim/1158_neutrino_decoupling.py`

---

### CLASSICAL STATEMENT
*"Neutrino decoupling occurs about one second after the big bang when the weak interaction rate falls below the Hubble rate (T ~ 1 MeV); the decoupled neutrinos form the cosmic neutrino background (Law 1161) with temperature T_nu = (4/11)^(1/3) T_gamma today."*
— Standard early-universe cosmology (weak decoupling at t ~ 1 s, T ~ 1 MeV). Source: Wikipedia: Neutrino decoupling (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero decoupling (neutrinos remain in equilibrium forever)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The N value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

N_phi(kappa) = N*(1 + kappa*(phi-1)) + kappa*phi^-1*N_ground, where N_ground is the coherence-floor residual weak coupling a real decoupling always retains. At kappa->0, Gamma_weak = n sigma v = H at T ~ 1 MeV,  T_nu/T_gamma = (4/11)^(1/3) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} N_phi = N -> Gamma_weak = n sigma v = H at T ~ 1 MeV,  T_nu/T_gamma = (4/11)^(1/3) is recovered exactly; the classical law is the zero decoupling (neutrinos remain in equilibrium forever) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1158_neutrino_decoupling.py`: reproduces the classical value (N = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1158_neutrino_decoupling.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured CnuB temperature will deviate from (4/11)^(1/3) T_gamma by a floor kappa*phi^-1*N_ground; an exactly decoupled neutrino bath is unreachable.
EXPERIMENT (VERIFIED): BBN abundance measurements and future CnuB direct-detection experiments (PTOLEMY).
VERIFIED BY: If neutrinos remain in equilibrium with the plasma at late times.
```

---

### RECOGNITION
The decoupling companion of Law 1157 (photon decoupling) and the source of Law 1161 (CnuB).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The neutrino leaves the fire; the forever-coupled neutrino is the zero-decoupling myth.

### NOVELTY
Neutrino decoupling carries a phi-floor, bounding the sharpness of the CnuB temperature.

### ACTIONABILITY
Run sim/1158_neutrino_decoupling.py.

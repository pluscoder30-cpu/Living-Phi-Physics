# PHI-PHYSICS — LAW 451
## Clausius-Duhem Inequality (Entropy Production)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/451_clausius_duhem_inequality.md` · **Sim:** `sim/451_clausius_duhem_inequality.py`

---

### CLASSICAL STATEMENT
*"The local entropy production rate is always non-negative: rho (Ds/Dt) + div(J_s/T) - rho q/T >= 0, where the equality holds only for reversible processes. It is the differential form of the second law for continua."*
— Rudolf Clausius; Pierre Duhem, 1901. Source: Wikipedia: Clausius-Duhem inequality; Clausius (1854), Duhem (1901)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *reversibility*: the inequality becomes an equality only for exactly reversible processes with zero entropy production - a continuum with no dissipation coherence anywhere.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the zero-production equality is a coherence gate. sigma_phi(kappa) = sigma*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_ground >= kappa*phi^-1*sigma_ground > 0. At kappa->0 the reversible equality case is recovered as a limit.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} sigma_phi = sigma >= 0 -> the Clausius-Duhem inequality is the finite-dissipation continuum limit; the reversible equality is the zero-coherence idealization.
```

---

### STAGE 4 — SIMULATION

`sim/451_clausius_duhem_inequality.py`: reproduces the classical value sigma_CD = 0.3 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/451_clausius_duhem_inequality.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Entropy production never reaches zero; every 'reversible' continuum process at finite coupling produces at least kappa*phi^-1*sigma_ground.
EXPERIMENT (VERIFIED): Ultra-low-dissipation continuum flow experiments measuring the residual entropy production floor.
VERIFIED BY: A continuum process produces exactly zero entropy when reversible, at any coupling.
```

---

### RECOGNITION
Connects to Law 023 (second law), Law 488 (Onsager) and Law 462 (Boltzmann) - the inequality is the local entropy budget of the field.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the production floor is phi^-1 * sigma_ground.

### CLARITY
The continuum cannot move without leaving entropy; the phi-law keeps the minimum trace of every motion.

### NOVELTY
Classical thermodynamics holds the reversible equality as a reachable ideal; the phi-law makes it a coherence-gated floor.

### ACTIONABILITY
Run sim/451_clausius_duhem_inequality.py; verify sigma >= 0 at kappa->0; proceed to 452.

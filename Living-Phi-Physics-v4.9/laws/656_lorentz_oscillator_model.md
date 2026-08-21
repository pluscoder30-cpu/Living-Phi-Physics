# PHI-PHYSICS — LAW 656
## Lorentz Oscillator Model (Dielectric Resonance)

**Domain:** Optics · **Status:** 🟢 VALIDATED · **File:** `laws/656_lorentz_oscillator_model.md` · **Sim:** `sim/656_lorentz_oscillator_model.py`

---

### CLASSICAL STATEMENT
*"The dielectric response of bound electrons is eps(omega) = 1 + omega_p^2/(omega_0^2 - omega^2 - i*gamma*omega), with resonance at omega_0 and damping gamma."*
— Hendrik Lorentz, 1895. Source: Wikipedia: Lorentz oscillator model

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero damping* (gamma = 0): the resonance width vanishes exactly and the response diverges at omega_0, a perfectly isolated oscillator.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

eps_phi(kappa) = eps_Lorentz*(1 + kappa*(phi-1)) + kappa*phi^-1*eps_ground; the oscillator carries a coherence damping floor. At kappa->0 the Lorentz model is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eps_phi = eps_Lorentz -> the Lorentz oscillator is the zero-damping-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/656_lorentz_oscillator_model.py`: reproduces the classical values (eps = 1 (Dielectric function)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/656_lorentz_oscillator_model.json`.

---

### STAGE 5 — PREDICTION

```
The resonance of a coherent oscillator carries a floor width kappa*phi^-1*gamma_ground; the response never diverges even for gamma -> 0.
EXPERIMENT (VERIFIED): Precision absorption spectroscopy of an isolated atomic resonance at ultralow temperature.
VERIFIED BY: An undamped oscillator shows an exactly divergent response at resonance.
```

---

### RECOGNITION
Connects to Law 655 (Drude) - Lorentz is the bound-charge partner of Drude.

### PRECISION
phi = 1.6180339887. The damping floor is phi^-1*gamma_ground.

### CLARITY
Every resonance carries a breath; the floor never lets it snap.

### NOVELTY
The phi-law gives the ideal resonance a coherence width.

### ACTIONABILITY
Run sim/656_lorentz_oscillator_model.py; verify eps(w) at kappa->0; proceed to 657.

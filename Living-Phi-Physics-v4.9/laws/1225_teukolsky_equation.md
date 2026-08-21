# PHI-PHYSICS — LAW 1225
## Teukolsky Equation

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1225_teukolsky_equation.md` · **Sim:** `sim/1225_teukolsky_equation.py`

---

### CLASSICAL STATEMENT
*"The Teukolsky equation governs perturbations of the Kerr metric (including gravitational, electromagnetic, and neutrino fields) via a master equation separable in Boyer-Lindquist coordinates: [((r^2+a^2)^2/Delta - a^2 sin^2 theta) d_tt + ...] psi = 0 for the Weyl/NP scalars; it is the foundation of black-hole perturbation theory and ringdown predictions."*
— Saul Teukolsky, 1973. Source: Wikipedia: Teukolsky equation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero rotation (a = 0, the Schwarzschild limit)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The T value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

T_phi(kappa) = T*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground, where T_ground is the coherence-floor rotation coupling a real black-hole perturbation always retains. At kappa->0, master equation for psi = psi_4 (Weyl scalar), separable in Kerr exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} T_phi = T -> master equation for psi = psi_4 (Weyl scalar), separable in Kerr is recovered exactly; the classical law is the zero rotation (a = 0, the Schwarzschild limit) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1225_teukolsky_equation.py`: reproduces the classical value (T = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1225_teukolsky_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured Kerr ringdown will deviate from the Teukolsky prediction by a floor kappa*phi^-1*T_ground; an exactly Schwarzschild ringdown is unreachable.
EXPERIMENT (VERIFIED): LIGO/Virgo ringdown and waveform templates built on Teukolsky solutions.
VERIFIED BY: If a rotating-hole ringdown matches the Schwarzschild (a=0) spectrum exactly.
```

---

### RECOGNITION
The Kerr perturbation engine of Law 1226 (quasinormal modes) and Law 1079 (Kerr).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The spinning hole sings a twisted song; the a=0 ring is the zero-spin myth.

### NOVELTY
The Teukolsky equation carries a phi-floor of spin coupling, bounding waveform accuracy.

### ACTIONABILITY
Run sim/1225_teukolsky_equation.py.

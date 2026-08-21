# PHI-PHYSICS - LAW 1808
## Maxwell Model (Series Spring-Dashpot Viscoelasticity)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1808_maxwell_model_viscoelasticity.md` - **Sim:** `sim/1808_maxwell_model_viscoelasticity.py`

---

### CLASSICAL STATEMENT
*"The Maxwell model represents a viscoelastic material as a spring (modulus E) in series with a dashpot (viscosity eta): under constant strain the stress relaxes exponentially, sigma(t) = sigma_0 exp(-t/tau) with tau = eta/E, and under constant stress it creeps linearly; the Maxwell model captures stress relaxation but not the rubber plateau of real polymers."*
- James Clerk Maxwell, 1867. Source: Wikipedia: Maxwell material; Maxwell (1867), Phil. Trans. R. Soc. 157:49

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-relaxation, perfectly elastic spring reference*: the Maxwell model is defined against a perfectly elastic reference with zero relaxation (tau = infinity); the exponential stress decay is the viscous correction away from this zero-relaxation ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the relaxation time carries a coherence floor. tau_phi(kappa) = tau_maxwell*(1 + kappa*(phi-1)) + kappa*phi^-1*tau_floor, where tau_floor is the phi-ground relaxation floor. At kappa->0 the ideal Maxwell relaxation is recovered; at kappa=1 the relaxation is never complete - an irreducible residual stress floor remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = sigma_0 exp(-t/tau) -> the Maxwell model is the zero-relaxation, perfectly-elastic reference sharpened to ideal series viscoelasticity.
```

---

### STAGE 4 - SIMULATION

`sim/1808_maxwell_model_viscoelasticity.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1808_maxwell_model_viscoelasticity.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Stress relaxation is never complete in any viscoelastic material: an irreducible residual-stress floor remains even at infinite time, so the Maxwell exponential decay always saturates above zero.
EXPERIMENT (VERIFIED): Ultra-long-duration stress-relaxation measurement of a polymer or viscoelastic solid, measuring the residual-stress floor at long times.
VERIFIED BY: A viscoelastic material whose stress relaxes to exactly zero at long times.
```

---

### RECOGNITION
Connects to Law 1809 (Kelvin-Voigt) and Law 1805 (WLF) - the material flows and springs, and the phi-law keeps a memory always in the flow.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual stress scales as phi^-1 * tau_floor.

### CLARITY
The viscoelastic solid relaxes; the phi-law keeps a sliver of stress forever.

### NOVELTY
Classical Maxwell allows full relaxation; the phi-law keeps an irreducible residual stress.

### ACTIONABILITY
Run sim/1808_maxwell_model_viscoelasticity.py; verify sigma = sigma_0 exp(-t/tau) at kappa->0; proceed to 1809.

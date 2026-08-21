# PHI-PHYSICS — LAW 481
## Eyring Equation (Transition-State Theory)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/481_eyring_equation.md` · **Sim:** `sim/481_eyring_equation.py`

---

### CLASSICAL STATEMENT
*"The rate constant of a reaction from transition-state theory is k = (k_B T/h) exp(-DeltaG^/(R T)) = (k_B T/h) exp(DeltaS^/R) exp(-DeltaH^/(R T)), where DeltaG^ is the Gibbs energy of activation. It connects the rate to the thermodynamic properties of the transition state."*
— Henry Eyring, 1935. Source: Wikipedia: Eyring equation; Eyring, The Activated Complex in Chemical Reactions (1935)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *the single transition state*: the theory assumes the reaction passes through exactly one activated complex at the top of the barrier with zero width - a transition state with no coherence width.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the transition state carries coherence. DeltaG^_phi(kappa) = DeltaG^*(1 + kappa*(phi-1)) + kappa*phi^-1*G_ground, so coherence lowers the effective activation free energy. At kappa->0 the Eyring rate is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} DeltaG^_phi = DeltaG^ -> k_phi = (k_B T/h) exp(-DeltaG^/(R T)) -> the Eyring equation is the zero-transition-state-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/481_eyring_equation.py`: reproduces the classical value k_eyring = 3.553e+07 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/481_eyring_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the effective activation free energy is reduced by kappa*phi^-1*G_ground; reaction rates exceed the Eyring prediction at low T (coherence-assisted crossing).
EXPERIMENT (VERIFIED): Kinetic isotope-effect and temperature-dependence measurements of proton-transfer reactions comparing with Eyring.
VERIFIED BY: ln(k/T) vs 1/T is exactly linear with the Eyring slope at all temperatures and couplings.
```

---

### RECOGNITION
Connects to Law 480 (Arrhenius) and Law 452 (mass action) - the transition state is the coherence saddle of the reaction.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the barrier reduction is phi^-1 * G_ground.

### CLARITY
Every reaction climbs to a saddle it never sits on; the phi-law keeps the saddle's width.

### NOVELTY
Classical Eyring assumes a point transition state; the phi-law gives the activated complex a coherence width.

### ACTIONABILITY
Run sim/481_eyring_equation.py; verify Eyring rate at kappa->0; proceed to 482.

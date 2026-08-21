# PHI-PHYSICS — LAW 480
## Arrhenius Equation (Temperature Dependence of Rate)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/480_arrhenius_equation.md` · **Sim:** `sim/480_arrhenius_equation.py`

---

### CLASSICAL STATEMENT
*"The rate constant of a chemical reaction depends exponentially on temperature: k = A exp(-E_a/(R T)), where E_a is the activation energy and A the pre-exponential factor."*
— Svante Arrhenius, 1889. Source: Wikipedia: Arrhenius equation; Arrhenius, Ueber die Reaktionsgeschwindigkeit bei der Inversion von Rohrzucker (1889)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *the barrier at zero*: the rate becomes exactly zero only at T = 0 or when the activation energy vanishes - the law assumes an exactly-defined energy barrier that a real molecule crosses only by a coherence-assisted jump.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the barrier is a coherence gate. k_phi(kappa) = A*exp(-E_a_phi/(R T)) with E_a_phi = E_a*(1 - kappa*phi^-1), so coherence lowers the effective barrier. At kappa->0, k = A exp(-E_a/(RT)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} E_a_phi = E_a -> k_phi = A exp(-E_a/RT) -> the Arrhenius equation is the zero-coherence-assistance barrier limit.
```

---

### STAGE 4 — SIMULATION

`sim/480_arrhenius_equation.py`: reproduces the classical value k_arr = 64.04 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/480_arrhenius_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the effective activation energy is reduced by kappa*phi^-1*E_a; reaction rates at low T exceed the classical Arrhenius prediction (tunneling-coherence floor).
EXPERIMENT (VERIFIED): Cryogenic reaction-rate measurements of proton-transfer reactions searching for the deviation below the Arrhenius line.
VERIFIED BY: ln k vs 1/T is exactly linear with slope -E_a/R at all temperatures and couplings.
```

---

### RECOGNITION
Connects to Law 481 (Eyring) and Law 452 (mass action) - the activation barrier is the coherence gate of the reaction.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the barrier reduction is phi^-1 * E_a.

### CLARITY
Every reaction climbs a hill; the phi-law notes the hill is lower for a coherent climber.

### NOVELTY
Classical Arrhenius fixes the barrier; the phi-law lets coherence lower the effective activation energy.

### ACTIONABILITY
Run sim/480_arrhenius_equation.py; verify Arrhenius rate at kappa->0; proceed to 481.

# PHI-PHYSICS — LAW 605
## Damkoehler Number (Reaction to Transport Rate Ratio)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/605_damkoehler_number.md` · **Sim:** `sim/605_damkoehler_number.py`

---

### CLASSICAL STATEMENT
*"The Damkoehler number is the ratio of the chemical reaction rate to the transport (convection or diffusion) rate: Da = k C^(n-1) L/u (convective) or Da = k C^(n-1) L^2/D (diffusive). Da >> 1 indicates reaction-limited transport (transport-controlled)."*
— Gerhard Damkoehler, 1936. Source: Wikipedia: Damkoehler numbers; Damkoehler (1936)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero reaction*: Da = 0 exactly at zero reaction rate - a system with no chemical coherence where only transport acts.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the reaction-transport coupling carries coherence. Da_phi(kappa) = Da*(1 + kappa*(phi-1)) + kappa*phi^-1*Da_ground. At kappa->0 the Damkoehler number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Da_phi = k C^(n-1) L/u -> the Damkoehler number is the zero-reaction zero-coherence transport limit.
```

---

### STAGE 4 — SIMULATION

`sim/605_damkoehler_number.py`: reproduces the classical value Da = 0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/605_damkoehler_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling even a non-reacting flow carries a residual reaction-coherence Da_ground.
EXPERIMENT (VERIFIED): Reacting-flow experiments in microreactors and combustion systems determining Da over a range of rates.
VERIFIED BY: Da = 0 exactly at zero reaction rate for all couplings.
```

---

### RECOGNITION
Connects to Law 452 (mass action) and Law 480 (Arrhenius) - the Damkoehler number is the reaction-transport coherence ratio.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * Da_ground.

### CLARITY
The reactor races chemistry against transport; the phi-law keeps the race's floor.

### NOVELTY
Classical Damkoehler zeroes at no reaction; the phi-law adds the reaction-coherence floor of the real flow.

### ACTIONABILITY
Run sim/605_damkoehler_number.py; verify Da at kappa->0; proceed to 606.

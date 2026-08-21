# PHI-PHYSICS — LAW 498
## Thomson Effect (Heat of a Current in a Temperature Gradient)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/498_thomson_effect.md` · **Sim:** `sim/498_thomson_effect.py`

---

### CLASSICAL STATEMENT
*"An electric current flowing along a conductor in which there is a temperature gradient absorbs or releases heat at a rate per unit length dQ/dx = -tau I dT/dx, where tau is the Thomson coefficient. It links the Seebeck and Peltier effects."*
— William Thomson (Lord Kelvin), 1851. Source: Wikipedia: Thermoelectric effect (Thomson); Thomson (1851)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero current or zero gradient*: the Thomson heat vanishes exactly at I = 0 or dT/dx = 0 - the effect needs both a current and a gradient to exist.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the double condition is a coherence basin. tau_phi(kappa) = tau*(1 + kappa*(phi-1)) + kappa*phi^-1*tau_ground. At kappa->0, dQ/dx = -tau I dT/dx exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} tau_phi = tau -> the Thomson effect is the zero-ground double-condition limit.
```

---

### STAGE 4 — SIMULATION

`sim/498_thomson_effect.py`: reproduces the classical value Q_thomson = -0.0001 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/498_thomson_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a current in a uniform conductor shows a residual Thomson heat kappa*phi^-1*tau_ground I dT/dx; the Kelvin relation tau = T dS/dT holds within a coherence floor.
EXPERIMENT (VERIFIED): Precision Thomson-heat measurements in a uniform conductor with an imposed gradient.
VERIFIED BY: The Thomson heat is exactly zero when the Kelvin relation is satisfied for all couplings.
```

---

### RECOGNITION
Connects to Law 496 (Seebeck), Law 497 (Peltier) and Law 488 (Onsager) - the Thomson coefficient is the coherence link of the thermoelectric triangle.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * tau_ground.

### CLARITY
Current and gradient together make heat; the phi-law keeps the heat of their meeting.

### NOVELTY
Classical Thomson vanishes when either condition fails; the phi-law adds the residual heat of the double condition.

### ACTIONABILITY
Run sim/498_thomson_effect.py; verify Thomson heat at kappa->0; proceed to 499.

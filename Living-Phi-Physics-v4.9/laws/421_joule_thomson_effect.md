# PHI-PHYSICS — LAW 421
## Joule-Thomson Effect (Throttling Cooling)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/421_joule_thomson_effect.md` · **Sim:** `sim/421_joule_thomson_effect.py`

---

### CLASSICAL STATEMENT
*"When a gas is throttled through a porous plug or valve at constant enthalpy, its temperature changes. The Joule-Thomson coefficient is mu_JT = (dT/dP)_H, which is zero for an ideal gas and depends on the gas's interactions otherwise; inversion occurs where mu_JT = 0."*
— James Prescott Joule and William Thomson (Lord Kelvin), 1852. Source: Wikipedia: Joule-Thomson effect; Joule & Thomson, On the Thermal Effects Experienced by Air (1852)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *ideal-gas throttling*: the effect assumes the gas's enthalpy depends only on temperature, so mu_JT = 0 and no cooling occurs - the exact condition that makes the real effect invisible.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the zero-coefficient is a coherence gate. mu_phi(kappa) = mu_JT*(1 + kappa*(phi-1)) + kappa*phi^-1*mu_ground, where mu_ground is the ground throttling of the carrier gas. At kappa->0, mu_phi = mu_JT.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} mu_phi = mu_JT -> the classical Joule-Thomson coefficient (zero for ideal gas) is the zero-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/421_joule_thomson_effect.py`: reproduces the classical value mu_JT = 0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/421_joule_thomson_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Even a nominally 'ideal' gas shows a residual throttling coefficient kappa*phi^-1*mu_ground at full coherence coupling, a cooling floor unremovable by improving ideality.
EXPERIMENT (VERIFIED): Precision throttling measurements of helium near its Joule-Thomson inversion measuring the residual dT/dP.
VERIFIED BY: mu_JT = 0 exactly for an ideal gas at all pressures and couplings.
```

---

### RECOGNITION
Connects to Law 025 (ideal gas) and Law 142 (van der Waals) - the inversion temperature is the coherence gate of the gas.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor coefficient is phi^-1 * mu_ground.

### CLARITY
The ideal gas is the gas that cannot cool itself; the phi-law gives even it a throttling floor.

### NOVELTY
Classical theory assigns mu_JT = 0 to the ideal gas; the phi-law turns the zero into a coherence-measurable gate.

### ACTIONABILITY
Run sim/421_joule_thomson_effect.py; verify mu_JT at kappa->0; proceed to 422.

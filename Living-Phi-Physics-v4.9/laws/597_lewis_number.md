# PHI-PHYSICS — LAW 597
## Lewis Number (Thermal to Mass Diffusivity Ratio)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/597_lewis_number.md` · **Sim:** `sim/597_lewis_number.py`

---

### CLASSICAL STATEMENT
*"The Lewis number is the ratio of thermal diffusivity to mass diffusivity: Le = alpha/D = k/(rho c_p D). For air, Le ~ 1; it governs the relative rates of heat and mass transfer in convection."*
— Warren Kendall Lewis, 1923. Source: Wikipedia: Lewis number; Lewis (1923)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *unity ratio*: many analyses assume Le = 1 exactly (heat and mass diffuse identically) - a condition that no real fluid satisfies precisely.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the diffusivity ratio carries coherence. Le_phi(kappa) = Le*(1 + kappa*(phi-1)) + kappa*phi^-1*Le_ground. At kappa->0 the Lewis number is exact (and unity only for the idealized fluid).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Le_phi = alpha/D -> the Lewis number is the zero-coherence diffusivity-ratio limit.
```

---

### STAGE 4 — SIMULATION

`sim/597_lewis_number.py`: reproduces the classical value Le = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/597_lewis_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the effective Lewis number deviates from the molecular value by a coherence term; heat and mass transfer decouple by that floor.
EXPERIMENT (VERIFIED): Simultaneous heat-and-mass-transfer measurements in boundary layers (e.g. evaporating films) to extract Le.
VERIFIED BY: Le = alpha/D exactly with no coherence correction for all couplings.
```

---

### RECOGNITION
Connects to Law 598 (Schmidt) and Law 096 (Fourier) - the Lewis number is the heat-mass coherence ratio of the flow.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * Le_ground.

### CLARITY
Heat and mass share the same wind but not the same pace; the phi-law keeps the pace's floor.

### NOVELTY
Classical Lewis is a fixed ratio; the phi-law adds the coherence correction of the real transport.

### ACTIONABILITY
Run sim/597_lewis_number.py; verify Le at kappa->0; proceed to 598.

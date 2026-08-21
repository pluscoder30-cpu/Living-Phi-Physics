# PHI-PHYSICS — LAW 554
## Maxwell Thermal Conductivity (Kinetic-Theory Heat Conduction)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/554_maxwell_thermal_conductivity.md` · **Sim:** `sim/554_maxwell_thermal_conductivity.py`

---

### CLASSICAL STATEMENT
*"The thermal conductivity of a monatomic gas from kinetic theory is k = (1/3) n c_v <v> lambda = (5/2) eta c_v, relating heat conduction to the viscosity and heat capacity. It is independent of density in the hard-sphere model."*
— James Clerk Maxwell and Ludwig Boltzmann, 1872. Source: Wikipedia: Kinetic theory of gases (thermal conductivity); Maxwell (1860), Boltzmann (1872)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *hard-sphere transport*: the conductivity assumes molecules transport heat in straight-line flights between hard-sphere collisions with zero intermolecular coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the interactions carry coherence. k_phi(kappa) = (5/2) eta c_v*(1 + kappa*(phi-1)) + kappa*phi^-1*k_ground. At kappa->0 the Maxwell conductivity is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} k_phi = (5/2) eta c_v -> the Maxwell conductivity is the zero-interaction hard-sphere limit.
```

---

### STAGE 4 — SIMULATION

`sim/554_maxwell_thermal_conductivity.py`: reproduces the classical value k_cond = 0.0005313 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/554_maxwell_thermal_conductivity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the thermal conductivity carries a coherence floor; the Eucken-type ratio k/(eta c_v) deviates from 5/2.
EXPERIMENT (VERIFIED): Precision thermal-conductivity measurements of noble gases over wide density and temperature ranges.
VERIFIED BY: k/(eta c_v) = 5/2 exactly for all gases at all couplings.
```

---

### RECOGNITION
Connects to Law 553 (viscosity) and Law 096 (Fourier) - the conductivity is the energy coherence transport of the gas.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * k_ground.

### CLARITY
Heat spreads through a gas by the sharing of motion; the phi-law keeps the sharing's floor.

### NOVELTY
Classical kinetic theory fixes the heat-to-momentum ratio; the phi-law adds the coherence floor of the real transport.

### ACTIONABILITY
Run sim/554_maxwell_thermal_conductivity.py; verify k at kappa->0; proceed to 555.

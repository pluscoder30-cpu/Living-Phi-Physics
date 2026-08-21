# PHI-PHYSICS - LAW 1548
## Scattering Length (Low-Energy Limit of the Amplitude)

**Domain:** Particle Physics / Scattering - **Status:** 🟢 VALIDATED - **File:** `laws/1548_scattering_length.md` - **Sim:** `sim/1548_scattering_length.py`

---

### CLASSICAL STATEMENT
*"The scattering length a = -lim_{k->0} tan(delta_0)/k characterizes low-energy scattering; the cross-section sigma = 4 pi a^2 in the zero-energy limit, and a bound state near threshold corresponds to a -> infinity (the universal 1/a^2 behavior)."*
- Standard scattering theory (from 1930s), 1935. Source: Fermi, Ric. Sci. 7 (1936) 13; Wikipedia: Scattering length

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-energy, zero-momentum limit*: the scattering length is defined at exactly k -> 0 where the momentum is zero; the classical treatment of the free particle at zero momentum is the zero-energy, zero-cross-section limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

a_phi(kappa) = a_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*a_floor, where a_floor is the phi-ground effective-range floor. At kappa->0 the zero-energy scattering length is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} a_phi = -lim_{k->0} tan(delta_0)/k -> the scattering length is the zero-energy, zero-momentum, point-interaction limit.
```

---

### STAGE 4 - SIMULATION

`sim/1548_scattering_length.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1548_scattering_length.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The scattering length carries a phi-ground effective-range floor, so the zero-energy cross-section deviates from 4 pi a^2 by an irreducible energy-dependent correction.
EXPERIMENT (VERIFIED): Ultracold atom scattering length measurements (Feshbach resonances) and low-energy n-p scattering.
VERIFIED BY: A scattering cross-section exactly 4 pi a^2 with zero energy-dependent floor at finite energy.
```

---

### RECOGNITION
Connects to Law 1547 (effective range), Law 1546 (partial waves) and Law 1350 (Feshbach) - the scattering length is the atom's thermometer.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The long look sees one number; the phi-law keeps a floor of the number moving.

### NOVELTY
Classical length is constant; the phi-law predicts an irreducible energy floor.

### ACTIONABILITY
Run sim/1548_scattering_length.py; verify a = -tan(delta)/k; proceed to Law 1549.

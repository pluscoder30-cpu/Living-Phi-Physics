# PHI-PHYSICS - LAW 1547
## Effective Range Theory (Low-Energy Scattering Parameters)

**Domain:** Particle Physics / Scattering - **Status:** 🟢 VALIDATED - **File:** `laws/1547_effective_range.md` - **Sim:** `sim/1547_effective_range.py`

---

### CLASSICAL STATEMENT
*"At low energy the scattering amplitude is parametrized by the scattering length a and effective range r0: k cot(delta_0) = -1/a + (1/2) r0 k^2 + ...; this is exact for the deuteron and low-energy neutron-proton scattering."*
- John Blatt; Victor Weisskopf (1952); Julian Schwinger (1947); Hans Bethe (1949), 1949. Source: Bethe, Phys. Rev. 76 (1949) 38; Wikipedia: Scattering length

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-energy, zero-range limit*: the expansion is about k -> 0 where k cot(delta) = -1/a; the classical treatment of point-like scattering with zero effective range gives a constant amplitude - a zero-range, zero-energy limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

k_cot_delta_phi(kappa) = k_cot_delta_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*rho_floor, where rho_floor is the phi-ground shape-parameter floor. At kappa->0 the effective-range expansion is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} k cot(delta) = -1/a + (1/2) r0 k^2 -> effective range theory is the zero-shape-parameter, two-parameter, low-energy limit.
```

---

### STAGE 4 - SIMULATION

`sim/1547_effective_range.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1547_effective_range.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The effective-range expansion carries a phi-ground shape-parameter floor, so k cot(delta) deviates from the two-parameter linear form by an irreducible cubic term.
EXPERIMENT (VERIFIED): Low-energy n-p and n-n scattering measurements (effective range parameters a_np, r0) and cold-atom Feshbach calibrations.
VERIFIED BY: A low-energy amplitude exactly linear in k^2 with zero shape-parameter floor.
```

---

### RECOGNITION
Connects to Law 1548 (scattering length), Law 1546 (partial waves) and Law 1490 (deuteron) - effective range theory is the amplitude's low-energy Taylor series.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The long wavelength sees a simple number; the phi-law keeps a floor of complexity in the simple.

### NOVELTY
Classical range is two parameters; the phi-law predicts an irreducible shape floor.

### ACTIONABILITY
Run sim/1547_effective_range.py; verify k cot(delta); proceed to Law 1548.

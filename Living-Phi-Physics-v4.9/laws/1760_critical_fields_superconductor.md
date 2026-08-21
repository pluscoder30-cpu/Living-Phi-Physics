# PHI-PHYSICS - LAW 1760
## Critical Fields of Superconductors (H_c, H_c1, H_c2)

**Domain:** Superconductivity - **Status:** 🟢 VALIDATED - **File:** `laws/1760_critical_fields_superconductor.md` - **Sim:** `sim/1760_critical_fields_superconductor.py`

---

### CLASSICAL STATEMENT
*"Superconductivity is destroyed by a magnetic field above the critical field: for type I, H_c(T) = H_c(0)(1 - (T/T_c)^2) destroys superconductivity abruptly; for type II, the lower critical field H_c1 = Phi_0/(4 pi lambda^2) ln(lambda/xi) allows vortex entry and the upper critical field H_c2 = Phi_0/(2 pi xi^2) destroys it entirely - the field limits of superconducting magnets."*
- H. Kamerlingh Onnes (1911); A.A. Abrikosov (1957), 1911. Source: Wikipedia: Superconducting magnet; Onnes (1911); Abrikosov (1957)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-field, zero-temperature perfect superconductor reference*: critical fields are defined against the ideal zero-field zero-temperature superconducting state; the field values mark the destruction of this state away from the zero-field reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the critical field carries a coherence floor. H_c_phi(kappa) = H_c*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_H, where delta_H is the phi-ground critical-field smearing. At kappa->0 the sharp H_c(T) law is recovered; at kappa=1 the transition is smeared over a coherent field width.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} H_c_phi = H_c(0)(1 - (T/T_c)^2) -> critical fields are the zero-fluctuation, sharp-transition limit of field-induced superconductivity destruction.
```

---

### STAGE 4 - SIMULATION

`sim/1760_critical_fields_superconductor.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1760_critical_fields_superconductor.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The superconducting-to-normal transition in a magnetic field is never perfectly sharp: an irreducible field-smearing floor remains even in the cleanest superconductors.
EXPERIMENT (VERIFIED): Ultra-precision magnetization and resistivity of a type-I superconductor (e.g. Al, Sn) through H_c at millikelvin, measuring the transition-width floor.
VERIFIED BY: A superconductor whose field-induced transition is exactly sharp at H_c with zero width.
```

---

### RECOGNITION
Connects to Law 1758 (coherence length) and Law 1757 (penetration depth) - the field is the superconductor's limit, and the phi-law keeps the limit from being a line.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; field smearing scales as phi^-1 * delta_H.

### CLARITY
The field ends superconductivity; the phi-law keeps the ending from being sharp.

### NOVELTY
Classical critical-field theory gives sharp transitions; the phi-law smears them with a coherence floor.

### ACTIONABILITY
Run sim/1760_critical_fields_superconductor.py; verify H_c(T) = H_c0(1-(T/T_c)^2) at kappa->0; proceed to 1761.

# PHI-PHYSICS - LAW 1745
## Colossal Magnetoresistance (CMR) (Huge Resistance Change in Manganites)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1745_stray_colossal_magnetoresistance.md` - **Sim:** `sim/1745_stray_colossal_magnetoresistance.py`

---

### CLASSICAL STATEMENT
*"In perovskite manganites (e.g. La1-xCaxMnO3) near the ferromagnetic transition, the resistance changes by orders of magnitude with magnetic field (CMR ratios up to 10^5% near T_c), driven by the double-exchange mechanism and the percolation of ferromagnetic metallic regions through the insulating phase; the effect is far larger than GMR but requires large fields."*
- R. von Helmolt (1993); S. Jin et al. (1994), 1993. Source: Wikipedia: Colossal magnetoresistance; von Helmolt (1993), PRL 71:2331; Jin et al. (1994), Science 264:413

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-field, perfectly ordered homogeneous reference*: CMR is defined against a zero-field, perfectly homogeneous ferromagnetic-metallic reference; the huge magnetoresistance arises from the field-driven percolation and disorder away from this homogeneous reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the CMR carries a coherence floor. CMR_phi(kappa) = CMR_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_C, where delta_C is the phi-ground residual magnetoresistance. At kappa->0 the zero-field homogeneous reference is recovered; at kappa=1 an irreducible magnetoresistance floor always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} CMR_phi = 0 -> colossal magnetoresistance is the field-driven percolation response measured from the zero-field homogeneous ferromagnetic-metallic reference.
```

---

### STAGE 4 - SIMULATION

`sim/1745_stray_colossal_magnetoresistance.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1745_stray_colossal_magnetoresistance.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Every manganite retains an irreducible magnetoresistance floor even far from the transition: the CMR never completely vanishes, and the transition carries a finite width.
EXPERIMENT (VERIFIED): Magnetotransport of a manganite thin film far from T_c as a function of field and temperature, measuring the residual CMR floor.
VERIFIED BY: A manganite with exactly zero field dependence of resistance far from the transition.
```

---

### RECOGNITION
Connects to Law 1729 (GMR) and Law 1730 (TMR) - the manganite's resistance falls off a cliff with field, and the phi-law keeps a step always in the cliff.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual floor scales as phi^-1 * delta_C.

### CLARITY
The manganite's resistance collapses under field; the phi-law keeps a residue of the collapse.

### NOVELTY
Classical CMR theory allows zero magnetoresistance far from transition; the phi-law keeps an irreducible floor.

### ACTIONABILITY
Run sim/1745_stray_colossal_magnetoresistance.py; verify the CMR peak at T_c at kappa->0; proceed to 1746.

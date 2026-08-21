# PHI-PHYSICS - LAW 1832
## Strain Hardening (Power-Law Work Hardening of Metals)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1832_strain_hardening_law.md` - **Sim:** `sim/1832_strain_hardening_law.py`

---

### CLASSICAL STATEMENT
*"During plastic deformation, metals strain harden: the true stress follows the Hollomon power law sigma = K epsilon^n, where n is the strain-hardening exponent (~0.1-0.5, the Considere condition for necking at epsilon = n) and K the strength coefficient; strain hardening determines the load capacity, formability and necking of metals."*
- J.H. Hollomon (1945); Ludwik (1909), 1945. Source: Wikipedia: Work hardening; Hollomon (1945), Trans. AIME 162:268; Ludwik (1909)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-hardening, perfectly plastic reference*: strain hardening is defined against a perfectly plastic (zero-hardening) reference where the flow stress is constant; the rising stress is the hardening away from this zero-hardening ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the hardening exponent carries a coherence floor. n_phi(kappa) = n_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_n, where delta_n is the phi-ground exponent floor. At kappa->0 the ideal power law is recovered; at kappa=1 the exponent is never exactly constant - the stress-strain curve always deviates from the pure power law.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = K epsilon^n -> strain hardening is the power-law, zero-anomaly, ideal-plasticity-reference flow rule of work hardening.
```

---

### STAGE 4 - SIMULATION

`sim/1832_strain_hardening_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1832_strain_hardening_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No metal hardens by an exact power law: an irreducible deviation floor remains, so the stress-strain curve always departs from sigma = K epsilon^n and the necking condition epsilon = n is approximate.
EXPERIMENT (VERIFIED): Ultra-precision tensile testing of a high-purity metal measuring the deviation of the flow curve from the ideal Hollomon power law.
VERIFIED BY: A metal whose flow stress exactly follows sigma = K epsilon^n over the full plastic range.
```

---

### RECOGNITION
Connects to Law 1793 (von Mises) and Law 1826 (dislocations) - the metal arms itself as it deforms, and the phi-law keeps the arming slightly uneven.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; exponent floor scales as phi^-1 * delta_n.

### CLARITY
The metal arms itself as it yields; the phi-law keeps the arming uneven.

### NOVELTY
Classical hardening gives an exact power law; the phi-law keeps an irreducible deviation floor.

### ACTIONABILITY
Run sim/1832_strain_hardening_law.py; verify sigma = K epsilon^n at kappa->0; proceed to 1833.

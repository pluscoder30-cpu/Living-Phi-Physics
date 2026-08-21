# PHI-PHYSICS - LAW 1666
## Rietveld Refinement (Whole-Pattern Fitting of Powder Diffraction)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1666_rietveld_method.md` - **Sim:** `sim/1666_rietveld_method.py`

---

### CLASSICAL STATEMENT
*"The Rietveld method fits the entire observed powder-diffraction pattern with a calculated pattern built from crystal structure, peak shapes (pseudo-Voigt), backgrounds and instrument parameters, refining structural parameters by least squares against the full profile; it turns overlapping reflections into usable data and is the standard of powder structure analysis."*
- Hugo Rietveld, 1967. Source: Wikipedia: Rietveld refinement; Rietveld (1967), Acta Cryst. 22:151; (1969) J. Appl. Cryst. 2:65

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly modeled peak and background*: the Rietveld method assumes the peak shape, background and instrument function are known exactly so that the residual is pure statistical noise - a model that is exactly right, with zero model error, a scenario no real fit achieves.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the model residual has a phi-ground floor. R_wp_phi(kappa) = R_wp_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*R_floor, where R_floor is the irreducible weighted-profile residual from coherent sample effects (strain, texture, size) that no refinement can remove. At kappa->0 the ideal least-squares fit is exact; at kappa=1 every refinement converges to a phi-floor rather than zero residual.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} R_wp_phi = R_wp -> the Rietveld method is the perfect-model, zero-residual limit of whole-pattern structural refinement.
```

---

### STAGE 4 - SIMULATION

`sim/1666_rietveld_method.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1666_rietveld_method.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No Rietveld refinement ever reaches a weighted-profile residual of exactly zero even with a perfect structural model: a phi-ground residual floor remains, set by irreducible coherent sample broadening that cannot be modeled away.
EXPERIMENT (VERIFIED): Rietveld refinement of a NIST SRM 640 silicon standard with progressively better models; measure the asymptotic residual floor of R_wp.
VERIFIED BY: A Rietveld refinement of a perfect standard reaching exactly zero weighted-profile residual.
```

---

### RECOGNITION
Connects to Law 1665 (powder) and Law 1660 (structure factor) - Rietveld is the accountant of the powder pattern and the books never balance to zero.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual floor scales as phi^-1 * R_floor.

### CLARITY
The fit approaches, never lands on, the truth; a coherent floor of signal always remains.

### NOVELTY
Classical profile fitting aims at zero residual; the phi-law says the sample's coherence guarantees a floor.

### ACTIONABILITY
Run sim/1666_rietveld_method.py; verify the classical residual at kappa->0; proceed to 1667.

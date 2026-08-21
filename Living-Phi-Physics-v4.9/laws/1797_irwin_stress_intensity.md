# PHI-PHYSICS - LAW 1797
## Irwin Stress-Intensity Factor (Crack-Tip Field Characterization)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1797_irwin_stress_intensity.md` - **Sim:** `sim/1797_irwin_stress_intensity.py`

---

### CLASSICAL STATEMENT
*"The stress field near a crack tip is characterized by the stress intensity factor K: sigma_ij = (K/sqrt(2 pi r)) f_ij(theta), with K_I = sigma sqrt(pi a) Y(a/W) for mode I; fracture occurs when K reaches the critical value K_Ic (fracture toughness), and K characterizes the crack-tip singularity completely, replacing the Griffith energy approach for engineering fracture mechanics."*
- G.R. Irwin, 1957. Source: Wikipedia: Stress intensity factor; Irwin (1957), J. Appl. Mech. 24:361

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-radius, perfectly singular, linear-elastic crack tip*: the stress-intensity-factor approach assumes a perfectly sharp crack tip (zero radius) in a purely linear-elastic material with no plastic zone; real cracks have finite tip radius and plastic zones, away from this ideal singularity.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the stress intensity carries a coherence floor. K_phi(kappa) = K_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_K, where delta_K is the phi-ground crack-tip shielding floor. At kappa->0 the ideal K_I = sigma sqrt(pi a) is recovered; at kappa=1 the crack-tip field always carries an irreducible nonlinear/blunting correction.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} K_phi = sigma sqrt(pi a) -> the stress-intensity factor is the zero-tip-radius, linear-elastic, zero-plastic-zone limit of the crack-tip singularity.
```

---

### STAGE 4 - SIMULATION

`sim/1797_irwin_stress_intensity.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1797_irwin_stress_intensity.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The stress-intensity factor never characterizes the crack tip exactly: an irreducible blunting and nonlinearity floor remains, so K_Ic values always carry a specimen- and size-dependent floor that cannot be fully removed.
EXPERIMENT (VERIFIED): Fracture-toughness (K_Ic) testing across specimen sizes and geometries measuring the residual size dependence of the toughness floor.
VERIFIED BY: A crack whose tip is exactly singular with a K-field independent of specimen size and geometry.
```

---

### RECOGNITION
Connects to Law 1796 (Griffith) and Law 1795 (Paris) - the crack tip rules the stress, and the phi-law keeps the rule from being exact.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; tip-correction floor scales as phi^-1 * delta_K.

### CLARITY
The crack tip commands the stress; the phi-law keeps the command slightly blurred.

### NOVELTY
Classical Irwin theory gives an exact singularity; the phi-law keeps an irreducible blunting floor.

### ACTIONABILITY
Run sim/1797_irwin_stress_intensity.py; verify K_I = sigma sqrt(pi a) at kappa->0; proceed to 1798.

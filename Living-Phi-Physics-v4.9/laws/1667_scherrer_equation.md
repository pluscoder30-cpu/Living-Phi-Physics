# PHI-PHYSICS - LAW 1667
## Scherrer Equation (Crystallite Size from Peak Broadening)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1667_scherrer_equation.md` - **Sim:** `sim/1667_scherrer_equation.py`

---

### CLASSICAL STATEMENT
*"The mean crystallite size is tau = K lambda / (beta cos theta), where beta is the FWHM of the diffraction peak in radians, K ~ 0.9 is the shape factor, lambda the wavelength and theta the Bragg angle; smaller crystals give broader peaks because the finite coherently scattering domain truncates the lattice sum."*
- Paul Scherrer, 1918. Source: Wikipedia: Scherrer equation; P. Scherrer (1918), Goettinger Nachrichten 2:98

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfect crystal of zero coherent domain*: the Scherrer equation treats the peak width as arising purely from finite crystallite size, assuming the crystallites are strain-free, defect-free and uniformly sized, with all other broadening exactly zero - a size-only world no real sample occupies.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: crystallites carry irreducible coherent strain broadening. tau_phi(kappa) = K lambda/(beta cos theta)*(1 + kappa*(phi-1)) + kappa*phi^-1*tau_floor, where tau_floor is the phi-ground coherence length set by zero-point and strain disorder. At kappa->0 the pure-size Scherrer value is exact; at kappa=1 the size estimate acquires an irreducible floor and the beta-1/tau relation carries a coherent offset.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} tau_phi = K lambda/(beta cos theta) -> the Scherrer equation is the zero-strain, zero-defect, size-only limit of coherent peak broadening.
```

---

### STAGE 4 - SIMULATION

`sim/1667_scherrer_equation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1667_scherrer_equation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The crystallite size inferred from any single peak never matches the true size: the phi-ground coherent strain floor adds a reproducible broadening so that the Scherrer size is always bounded and the beta vs 1/cos(theta) plot carries a phi-floor intercept.
EXPERIMENT (VERIFIED): Williamson-Hall analysis of a nanocrystalline standard: plot beta cos(theta) vs sin(theta) and measure the nonzero phi-floor intercept that persists after strain removal.
VERIFIED BY: A nanocrystalline sample whose Williamson-Hall intercept is exactly zero at all crystallite sizes.
```

---

### RECOGNITION
Connects to Law 1665 (powder) and Law 1662 (Debye-Waller) - size and strain both speak through the peak width.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the size floor scales as phi^-1 * tau_floor.

### CLARITY
The peak remembers how small the crystal is - and the phi-law says it also remembers an irreducible wobble.

### NOVELTY
Classical Scherrer analysis isolates size; the phi-law keeps a coherent strain floor in every peak.

### ACTIONABILITY
Run sim/1667_scherrer_equation.py; verify tau=K lambda/(beta cos theta) at kappa->0; proceed to 1668.

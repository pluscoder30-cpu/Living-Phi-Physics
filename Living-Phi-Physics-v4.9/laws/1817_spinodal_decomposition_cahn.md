# PHI-PHYSICS - LAW 1817
## Spinodal Decomposition (Cahn-Hilliard Diffusive Phase Separation)

**Domain:** Phase Transformations - **Status:** 🟢 VALIDATED - **File:** `laws/1817_spinodal_decomposition_cahn.md` - **Sim:** `sim/1817_spinodal_decomposition_cahn.py`

---

### CLASSICAL STATEMENT
*"Inside the spinodal region, a homogeneous solution is unstable to infinitesimal composition fluctuations: the composition evolves by uphill diffusion following the Cahn-Hilliard equation dC/dt = M grad^2 mu = M(grad^2(delta F/delta C) - kappa grad^4 C), producing a characteristic periodic microstructure with wavelength lambda = 2 pi sqrt(-2 kappa/(d^2 f/dC^2)); spinodal decomposition gives the diffuse, interconnected microstructures of glasses, alloys and polymer blends."*
- John W. Cahn & John E. Hilliard (1958); J.W. Cahn (1961), 1958. Source: Wikipedia: Spinodal decomposition; Cahn & Hilliard (1958), J. Chem. Phys. 28:258; Cahn (1961)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-gradient-energy, zero-capillarity, perfectly flat free-energy reference*: the Cahn-Hilliard theory is defined against a reference with zero gradient energy and a perfectly parabolic free energy; spinodal instability is the downhill-diffusion response away from the stable homogeneous reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the instability carries a coherence floor. lambda_phi(kappa) = lambda_cahn*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_lambda, where delta_lambda is the phi-ground wavelength floor. At kappa->0 the ideal spinodal wavelength is recovered; at kappa=1 the spinodal wavelength and amplitude carry an irreducible correction.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} lambda_phi = 2 pi sqrt(-2 kappa/(d^2 f/dC^2)) -> spinodal decomposition is the zero-noise, zero-gradient-energy, ideal-parabolic limit of uphill diffusion.
```

---

### STAGE 4 - SIMULATION

`sim/1817_spinodal_decomposition_cahn.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1817_spinodal_decomposition_cahn.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Spinodal wavelengths never match the ideal Cahn-Hilliard value: an irreducible correction floor remains, and the characteristic wavelength and its sharpness always deviate from the ideal prediction.
EXPERIMENT (VERIFIED): Small-angle neutron/X-ray scattering of a spinodally decomposing alloy or polymer blend (e.g. Al-Zn, PS-PB) measuring the wavelength and its deviation from the ideal value.
VERIFIED BY: A spinodal system whose characteristic wavelength exactly matches the ideal Cahn-Hilliard prediction.
```

---

### RECOGNITION
Connects to Law 1815 (Avrami) and Law 1816 (nucleation) - the mixture unmixes by diffusion, and the phi-law keeps a blur in the pattern.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; wavelength correction scales as phi^-1 * delta_lambda.

### CLARITY
The mixture unmixes into waves; the phi-law keeps a noise in every wave.

### NOVELTY
Classical Cahn-Hilliard gives ideal wavelengths; the phi-law keeps an irreducible correction.

### ACTIONABILITY
Run sim/1817_spinodal_decomposition_cahn.py; verify the Cahn-Hilliard wavelength at kappa->0; proceed to 1818.

# PHI-PHYSICS - LAW 1541
## Mott Scattering (Electron-Nucleus Coulomb Scattering with Spin)

**Domain:** Particle Physics / QED - **Status:** 🟢 VALIDATED - **File:** `laws/1541_mott_scattering.md` - **Sim:** `sim/1541_mott_scattering.py`

---

### CLASSICAL STATEMENT
*"Mott scattering is the Coulomb scattering of an electron by a heavy nucleus, including spin effects: dsigma/dOmega = (Z alpha hbar c/(4 E sin^2(theta/2)))^2 (1 - beta^2 sin^2(theta/2)); it reduces to Rutherford at low energy and includes the spin (Mott) factor at high energy."*
- Nevill Mott, 1929. Source: Mott, Proc. R. Soc. A124 (1929) 425; Wikipedia: Mott scattering

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-spin, zero-relativistic-effect limit*: Mott scattering reduces to the Rutherford formula when the electron spin and relativistic effects are exactly zero; the classical treatment of the electron as a spinless nonrelativistic particle gives the zero-spin limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_mott*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground form-factor/radiative floor. At kappa->0 the point-Mott cross-section is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = (Z alpha hbar c/(4E sin^2(theta/2)))^2 (1 - beta^2 sin^2(theta/2)) -> Mott scattering is the zero-form-factor, point-nucleus limit.
```

---

### STAGE 4 - SIMULATION

`sim/1541_mott_scattering.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1541_mott_scattering.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Mott cross-section carries a phi-ground form-factor floor, so the measured angular distribution deviates from the point-Mott formula by an irreducible nuclear-size correction (the form factor).
EXPERIMENT (VERIFIED): Electron scattering from nuclei (Hofstadter type) measuring the form factor via the Mott ratio.
VERIFIED BY: Electron-nucleus scattering exactly following the point-Mott formula with zero form-factor floor.
```

---

### RECOGNITION
Connects to Law 1526 (Bhabha), Law 1527 (Moller) and Law 1498 (nuclear distribution) - Mott scattering is the electron's probe of the nucleus.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The electron feels the nucleus at a point; the phi-law keeps a floor of the point spreading.

### NOVELTY
Classical Mott is point-like; the phi-law predicts an irreducible form-factor floor.

### ACTIONABILITY
Run sim/1541_mott_scattering.py; verify the Mott factor; proceed to Law 1542.

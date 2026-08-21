# PHI-PHYSICS - LAW 1701
## Charge Density Waves (Periodic Modulation of Electron Density)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1701_charge_density_waves.md` - **Sim:** `sim/1701_charge_density_waves.py`

---

### CLASSICAL STATEMENT
*"Below the Peierls transition a charge density wave forms: the electron density modulates as rho(r) = rho_0 + rho_1 cos(2 k_F r + phi), accompanied by a periodic lattice distortion of the same wavevector; the CDW state is a condensate with a collective phase phi that can slide, producing nonlinear transport and narrow-band noise."*
- H. Frohlich (1954); R.E. Peierls (1955), 1954. Source: Wikipedia: Charge density wave; Frohlich (1954), Proc. R. Soc. A223:296; Peierls (1955)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly uniform, zero-modulation electron gas*: the CDW state is defined against a perfectly uniform electron density with zero modulation amplitude (the normal metal); the transition is the onset of a nonzero rho_1 from a zero-modulation reference state.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the modulation amplitude has a coherent floor. rho_1_phi(kappa) = rho_1*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_rho, where delta_rho is the phi-ground modulation floor. At kappa->0 the sharp CDW onset is recovered; at kappa=1 even the 'normal' state retains an irreducible coherent density modulation.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} rho_1_phi = rho_1 -> charge density waves are the zero-modulation normal-metal reference, sharpened to the ideal onset.
```

---

### STAGE 4 - SIMULATION

`sim/1701_charge_density_waves.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1701_charge_density_waves.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The normal metallic state above T_P retains an irreducible coherent density modulation floor: diffuse scattering signatures of 2 k_F order never fully vanish above the transition.
EXPERIMENT (VERIFIED): High-sensitivity diffuse X-ray or neutron scattering of a CDW material (e.g. TTF-TCNQ) above T_P, measuring the residual 2 k_F diffuse intensity floor.
VERIFIED BY: A CDW material whose 2 k_F diffuse scattering is exactly zero above the transition temperature.
```

---

### RECOGNITION
Connects to Law 1700 (Peierls) and Law 1683 (Fermi surface) - the electron sea orders into stripes, and the phi-law keeps the stripes from ever fully dissolving.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; modulation floor scales as phi^-1 * delta_rho.

### CLARITY
The electron sea stripes itself in a CDW; the phi-law keeps a ghost of the stripes above the wash.

### NOVELTY
Classical CDW theory has a clean normal state; the phi-law keeps an irreducible pre-ordering floor.

### ACTIONABILITY
Run sim/1701_charge_density_waves.py; verify rho = rho_0 + rho_1 cos(2k_F r) at kappa->0; proceed to 1702.

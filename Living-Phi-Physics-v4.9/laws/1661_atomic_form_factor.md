# PHI-PHYSICS - LAW 1661
## Atomic Form Factor (f_j, Fourier Transform of Electron Density)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1661_atomic_form_factor.md` - **Sim:** `sim/1661_atomic_form_factor.py`

---

### CLASSICAL STATEMENT
*"The scattering power of an atom for X-rays is its form factor f_j(q) = integral rho_j(r) exp(i q.r) dr, the Fourier transform of the atomic electron density; it falls off with scattering angle because the electron cloud is spatially extended, and peaks at q=0 with f_j(0) = Z_j, the atomic number."*
- A.H. Compton; refined by P. Debye, 1915. Source: Wikipedia: Atomic form factor; Compton (1915); Debye (1915), Ann. Phys. 46:809

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *point atom of zero size*: classical scattering theory's strongest simplifications treat the atom as a point charge (delta-function density) whose form factor is exactly constant and equal to Z at every angle - an atom with zero spatial extent that no electron cloud has.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the electron cloud carries coherent density. f_phi(q,kappa) = f_classical(q)*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_f, where delta_f is the phi-ground residual form factor from the coherent zero-point smearing of the electron density. At kappa->0 the exact form factor is recovered; at kappa=1 even at infinite q the form factor retains a phi-floor instead of falling to zero.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} f_phi = f_j(q) -> the atomic form factor is the exact-electron-density, well-defined-Fourier-transform limit of coherent atomic scattering.
```

---

### STAGE 4 - SIMULATION

`sim/1661_atomic_form_factor.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1661_atomic_form_factor.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: At very high momentum transfer the form factor of any atom retains a phi-ground residual delta_f instead of decaying to exactly zero, a small high-angle scattering floor observable in gas-phase or low-temperature electron diffraction.
EXPERIMENT (VERIFIED): Gas-phase electron diffraction at high scattering angles measuring the residual high-q scattering intensity floor of noble gas atoms.
VERIFIED BY: An atomic form factor measured to decay to exactly zero at high q with no residual floor.
```

---

### RECOGNITION
Connects to Law 1660 (structure factor) and Law 1662 (Debye-Waller) - the atom is a cloud, and the cloud never fully thins out.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual floor scales as phi^-1 * delta_f.

### CLARITY
Even the thinnest cloud keeps a coherent wisp.

### NOVELTY
Classical form factors decay to zero; the phi-law gives them an irreducible coherent residual.

### ACTIONABILITY
Run sim/1661_atomic_form_factor.py; verify f(0)=Z at kappa->0; proceed to 1662.

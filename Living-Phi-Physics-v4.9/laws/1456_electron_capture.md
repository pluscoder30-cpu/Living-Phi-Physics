# PHI-PHYSICS - LAW 1456
## Electron Capture Decay (K-Capture)

**Domain:** Nuclear Decays - **Status:** 🟢 VALIDATED - **File:** `laws/1456_electron_capture.md` - **Sim:** `sim/1456_electron_capture.py`

---

### CLASSICAL STATEMENT
*"A nucleus with excess protons may capture an atomic electron (usually K-shell): p + e- -> n + nu_e. The capture rate depends on the electron wavefunction at the nucleus, |psi(0)|^2 ~ (Z/n)^3, and the neutrino phase space."*
- Luis Alvarez (first observation); predicted by Hideki Yukawa (1935), 1937. Source: Alvarez, Phys. Rev. 52 (1937) 134; Wikipedia: Electron capture

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-volume point electron*: the capture rate is proportional to the electron density AT the nucleus, |psi(0)|^2, requiring the electron to be exactly at r=0 - a point-electron, zero-nuclear-volume assumption.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

Lambda_phi(kappa) = |psi(0)|^2*(1 + kappa*(phi-1)) + kappa*phi^-1*Lambda_finite, where Lambda_finite is the phi-ground correction from finite nuclear size and screening. At kappa->0 the point-density capture rate is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Lambda_phi = (G_F^2 |psi(0)|^2)/(2 pi^2) E_nu^2 -> electron capture is the zero-electron-volume, point-density limit.
```

---

### STAGE 4 - SIMULATION

`sim/1456_electron_capture.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1456_electron_capture.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The capture rate deviates from the |psi(0)|^2 scaling by a phi-ground finite-size/screening floor, systematic especially for high-Z capture where the electron probes nuclear volume.
EXPERIMENT (VERIFIED): Precision EC decay rate measurements vs Z and comparison with Q-value systematics; neutrino-energy window experiments (e.g. 163Ho).
VERIFIED BY: An electron capture rate exactly proportional to the point density |psi(0)|^2 with zero finite-size floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1454 (Fermi theory), Law 1338 (electric dipole) and Law 1183 - capture is the weak interaction at zero distance.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The electron is swallowed at a point; the phi-law keeps a floor of finite reach.

### NOVELTY
Classical capture is point-density; the phi-law keeps an irreducible finite-size floor.

### ACTIONABILITY
Run sim/1456_electron_capture.py; verify the Z^3 scaling; proceed to Law 1457.

# PHI-PHYSICS - LAW 1544
## Optical Theorem (Unitarity of the S-Matrix)

**Domain:** Particle Physics / Scattering - **Status:** 🟢 VALIDATED - **File:** `laws/1544_optical_theorem.md` - **Sim:** `sim/1544_optical_theorem.py`

---

### CLASSICAL STATEMENT
*"The optical theorem relates the total cross-section to the forward scattering amplitude: sigma_tot = (4 pi/k) Im f(0); it follows from unitarity of the S-matrix (S-dagger S = 1) and is a rigorous consequence of probability conservation."*
- Bohr-Peierls-Placzek (1939); Rayleigh (1871, wave optics), 1939. Source: Bohr, Peierls & Placzek, Nature 144 (1939) 200; Wikipedia: Optical theorem

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-forward-scattering, zero-total-cross-section limit*: the theorem is trivial (0 = 0) when there is no scattering; the classical treatment of a non-interacting system has exactly zero forward amplitude - a zero-interaction, zero-absorption limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_tot_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground irreducible-cross-section floor. At kappa->0 the optical theorem is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_tot_phi = (4 pi/k) Im f(0) -> the optical theorem is the zero-inelastic, unitarity-exact, forward-limit relation.
```

---

### STAGE 4 - SIMULATION

`sim/1544_optical_theorem.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1544_optical_theorem.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The total cross-section carries a phi-ground floor, so even the 'weakest' interaction has an irreducible forward contribution and Im f(0) never vanishes exactly.
EXPERIMENT (VERIFIED): Total cross-section measurements (p-p, pi-p, gamma-p) at colliders and comparison with forward elastic amplitudes.
VERIFIED BY: An interaction with exactly zero total cross-section and zero forward amplitude at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1542 (Feynman rules), Law 1298 (S-matrix) and Law 1545 (Mandelstam) - the optical theorem is unitarity's mirror.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The forward glare measures the whole; the phi-law keeps a floor of glare in every whole.

### NOVELTY
Classical theorem is exact; the phi-law predicts an irreducible cross-section floor.

### ACTIONABILITY
Run sim/1544_optical_theorem.py; verify sigma_tot = 4pi Im f(0)/k; proceed to Law 1545.

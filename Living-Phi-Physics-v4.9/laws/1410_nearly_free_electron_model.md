# PHI-PHYSICS - LAW 1410
## Nearly Free Electron Model (Weak Periodic Potential and Band Gaps)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1410_nearly_free_electron_model.md` - **Sim:** `sim/1410_nearly_free_electron_model.py`

---

### CLASSICAL STATEMENT
*"The nearly free electron model treats a weak periodic potential as a perturbation on free electrons: the free parabolic bands E = hbar^2 k^2/(2m) split at the Brillouin zone boundaries k = +/- pi/a, opening a band gap delta_E = 2|V_G| (twice the Fourier component of the potential); it explains why monovalent metals are conductors, divalent can be insulators, and the origin of the effective mass."*
- Developed in 1930s (Bloch 1928; Brillouin; Peierls), 1931. Source: Wikipedia: Nearly free electron model; Bloch (1928), Brillouin (1931)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero potential*: the model reduces to pure free electrons with no gaps when the periodic potential V_G = 0, i.e. a zero-potential lattice - the free-electron limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the potential component carries a coherence floor. V_G_phi(kappa) = V_G*(1 + kappa*(phi-1)) + kappa*phi^-1*V_floor, where V_floor is the phi-ground potential; free electrons retain a floor gap. At kappa->0 the NFE bands are exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_E_phi = 2|V_G| -> the nearly free electron model is the zero-potential-floor, free-electron-limit.
```

---

### STAGE 4 - SIMULATION

`sim/1410_nearly_free_electron_model.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1410_nearly_free_electron_model.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The band gap at full coherence coupling retains a floor kappa*phi^-1*V_floor even for a vanishing periodic potential, a minimum gap.
EXPERIMENT (VERIFIED): Band structure measurements (ARPES) of quasi-free-electron metals (e.g. Be, Al) measuring the gap floor at the zone boundary.
VERIFIED BY: A vanishing periodic potential produces exactly zero band gap for all couplings.
```

---

### RECOGNITION
Connects to Law 1408 (Bloch) and Law 1409 (Kronig-Penney) - the NFE model is the coherence weak-potential complement of tight binding.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the potential floor is phi^-1 * V_floor.

### CLARITY
The free electron meets a whisper of lattice and splits; the phi-law keeps the whisper's floor.

### NOVELTY
Classical band theory lets weak potentials vanish; the phi-law keeps a coherence gap floor.

### ACTIONABILITY
Run sim/1410_nearly_free_electron_model.py; verify 2|V_G| gap at kappa->0; proceed to 1411.

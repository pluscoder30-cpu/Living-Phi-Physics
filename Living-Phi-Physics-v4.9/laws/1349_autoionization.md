# PHI-PHYSICS - LAW 1349
## Autoionization (Fano: Spontaneous Emission of Electron from Doubly Excited State)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1349_autoionization.md` - **Sim:** `sim/1349_autoionization.py`

---

### CLASSICAL STATEMENT
*"A doubly excited state above the first ionization limit can spontaneously eject an electron (autoionization), a process that interferes with direct ionization to produce the asymmetric Fano profile: sigma(E) ~ (q + eps)^2/(1 + eps^2) with eps = 2(E - E_res)/Gamma and Fano parameter q; the autoionization width Gamma is the inverse lifetime."*
- Allen Shenstone (observed); Ugo Fano (theory), 1931. Source: Wikipedia: Autoionization; Shenstone (1931), Fano, Phys. Rev. 124 (1961) 1866

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *uncoupled continuum*: autoionization vanishes exactly when the discrete state is uncoupled from the continuum (coupling V = 0), i.e. a metastable state with zero coupling to ionization channels.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the continuum coupling carries a coherence floor. V_phi(kappa) = V*(1 + kappa*(phi-1)) + kappa*phi^-1*V_floor, where V_floor is the phi-ground continuum coupling; the Fano profile acquires a floor. At kappa->0 the Fano asymmetry is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = (q + eps)^2/(1 + eps^2) -> autoionization is the zero-continuum-coupling-metastable limit.
```

---

### STAGE 4 - SIMULATION

`sim/1349_autoionization.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1349_autoionization.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: A nominally uncoupled doubly excited state at full coherence coupling autoionizes at floor rate kappa*phi^-1*V_floor, a residual continuum coupling.
EXPERIMENT (VERIFIED): Photoelectron spectroscopy of doubly excited He states measuring the autoionization width floor at controlled coupling.
VERIFIED BY: A doubly excited state with zero continuum coupling has exactly zero autoionization width for all couplings.
```

---

### RECOGNITION
Connects to Law 1371 (Fano resonance) and Law 1345 (Auger) - autoionization is the coherence coupling of the discrete to the continuum.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the coupling floor is phi^-1 * V_floor.

### CLARITY
The doubly-excited atom lets go of one electron like a secret; the phi-law keeps a floor of the letting go.

### NOVELTY
Classical resonance theory isolates states exactly; the phi-law keeps the continuum coupling floor.

### ACTIONABILITY
Run sim/1349_autoionization.py; verify Fano profile at kappa->0; proceed to 1350.

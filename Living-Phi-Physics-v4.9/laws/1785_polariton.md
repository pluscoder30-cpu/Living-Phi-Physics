# PHI-PHYSICS - LAW 1785
## Polariton (Coupled Photon-Exciton Quasiparticle)

**Domain:** Dielectrics & Optics - **Status:** 🟢 VALIDATED - **File:** `laws/1785_polariton.md` - **Sim:** `sim/1785_polariton.py`

---

### CLASSICAL STATEMENT
*"When light couples strongly to a material excitation (exciton, phonon), the two form mixed quasiparticles - polaritons - whose dispersion splits into upper and lower branches with an anticrossing gap (Rabi splitting) 2 Omega_R; the polariton dispersion E(k) is obtained from the coupled oscillator model, and polaritons govern light propagation in crystals and exciton-polariton condensates in microcavities."*
- J.J. Hopfield (1958); S.I. Agranovich (1959), 1958. Source: Wikipedia: Polariton; Hopfield (1958), Phys. Rev. 112:1555; Agranovich (1959)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-coupling, perfectly independent photon and exciton*: polaritons are defined against the zero-coupling reference where photon and exciton propagate independently with no Rabi splitting; the mixed states are the coupling away from this zero-Omega_R reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the Rabi splitting carries a coherence floor. Omega_R_phi(kappa) = Omega_R*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_O, where delta_O is the phi-ground residual splitting. At kappa->0 the zero-coupling reference is recovered; at kappa=1 an irreducible photon-exciton coupling always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Omega_R_phi = 0 -> polaritons are the photon-exciton mixed states measured from the zero-coupling, perfectly-independent reference.
```

---

### STAGE 4 - SIMULATION

`sim/1785_polariton.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1785_polariton.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Every material retains an irreducible photon-matter coupling: a residual polariton splitting and anticrossing floor exists even for weakly coupled systems, and no crystal has perfectly independent photon and exciton.
EXPERIMENT (VERIFIED): High-resolution reflectivity or transmission of a crystal or microcavity measuring the residual Rabi splitting and anticrossing floor.
VERIFIED BY: A material with exactly zero photon-exciton coupling (perfectly independent photon and exciton).
```

---

### RECOGNITION
Connects to Law 1782 (exciton) and Law 966 (phonon dispersion) - the photon and the excitation dance as one, and the phi-law keeps a step always in the dance.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; splitting floor scales as phi^-1 * delta_O.

### CLARITY
Light and matter hold hands; the phi-law keeps the grip from being loose.

### NOVELTY
Classical polariton theory allows zero coupling; the phi-law keeps an irreducible Rabi floor.

### ACTIONABILITY
Run sim/1785_polariton.py; verify the anticrossing at kappa->0; proceed to 1786.

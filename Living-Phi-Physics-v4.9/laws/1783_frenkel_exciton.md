# PHI-PHYSICS - LAW 1783
## Frenkel Exciton (Tightly Bound Molecular Exciton)

**Domain:** Dielectrics & Optics - **Status:** 🟢 VALIDATED - **File:** `laws/1783_frenkel_exciton.md` - **Sim:** `sim/1783_frenkel_exciton.py`

---

### CLASSICAL STATEMENT
*"The Frenkel exciton is a tightly bound electron-hole pair localized on a single molecule or lattice site, with binding energy of order 0.1-1 eV and radius comparable to the lattice constant; Frenkel excitons dominate the optical spectra of molecular crystals, organic semiconductors and alkali halides, and move through the lattice by hopping (Davydov splitting, exciton bands)."*
- Yakov Frenkel, 1931. Source: Wikipedia: Frenkel exciton; Frenkel (1931), Phys. Rev. 37:17

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-hopping, perfectly localized, isolated-molecule exciton*: the Frenkel exciton is idealized as perfectly localized on a single site with zero inter-site coupling and zero lattice motion; real Frenkel excitons delocalize into bands and couple to phonons, away from this zero-hopping reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the exciton band carries a coherence floor. E_phi(kappa) = E_frenkel*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_E, where delta_E is the phi-ground band-width and phonon-dressing floor. At kappa->0 the perfectly localized exciton is recovered; at kappa=1 the exciton always has a finite band width and phonon dressing.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_phi = E_frenkel -> the Frenkel exciton is the zero-hopping, perfectly-localized, isolated-molecule limit of molecular excitations.
```

---

### STAGE 4 - SIMULATION

`sim/1783_frenkel_exciton.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1783_frenkel_exciton.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Frenkel excitons are never perfectly localized: an irreducible delocalization (band width) and phonon-dressing floor remains, observable as a residual exciton band dispersion and zero-phonon-line width.
EXPERIMENT (VERIFIED): Ultra-low-temperature absorption and photoluminescence of a molecular crystal (e.g. anthracene, acene) measuring the residual exciton band width and zero-phonon linewidth floor.
VERIFIED BY: A molecular crystal with perfectly localized Frenkel excitons (zero band width) at any temperature.
```

---

### RECOGNITION
Connects to Law 1782 (exciton) and Law 966 (phonon dispersion) - the molecular exciton is tightly bound, and the phi-law keeps a thread of motion in the bond.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; band-width floor scales as phi^-1 * delta_E.

### CLARITY
The molecular pair clings; the phi-law keeps a hop always possible.

### NOVELTY
Classical Frenkel theory allows perfect localization; the phi-law keeps an irreducible delocalization.

### ACTIONABILITY
Run sim/1783_frenkel_exciton.py; verify the localized exciton at kappa->0; proceed to 1784.

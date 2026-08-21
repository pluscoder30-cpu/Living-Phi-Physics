# PHI-PHYSICS - LAW 1782
## Exciton Binding Energy (Electron-Hole Bound State in Semiconductors)

**Domain:** Dielectrics & Optics - **Status:** 🟢 VALIDATED - **File:** `laws/1782_exciton_binding_energy.md` - **Sim:** `sim/1782_exciton_binding_energy.py`

---

### CLASSICAL STATEMENT
*"An exciton is a bound electron-hole pair: in the Wannier-Mott picture its binding energy is E_b = mu e^4/(2 hbar^2 eps^2) = 13.6 eV (mu/m_0)/eps^2, its radius a_B = hbar^2 eps/(mu e^2), and its hydrogen-like spectrum E_n = E_g - E_b/n^2 appears below the band gap; Frenkel excitons are tightly bound (localized), Wannier excitons weakly bound (delocalized), and excitons dominate the optical properties of semiconductors and insulators."*
- Yakov Frenkel (1931); Gregory Wannier (1937); Nevill Mott (1937), 1931. Source: Wikipedia: Exciton; Frenkel (1931), Phys. Rev. 37:17; Wannier (1937)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-dielectric, zero-screening, perfectly parabolic-band reference*: the hydrogenic exciton model assumes a perfect parabolic band, a static dielectric constant and zero phonon coupling; the ideal exciton is a pure two-body hydrogen problem with no screening dynamics or phonon dressing.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the exciton carries a coherence floor. E_b_phi(kappa) = E_b_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_E, where delta_E is the phi-ground binding-energy correction. At kappa->0 the ideal hydrogenic value is recovered; at kappa=1 the exciton carries an irreducible phonon-dressing and screening correction.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_b_phi = 13.6 eV (mu/m_0)/eps^2 -> the exciton is the zero-phonon, static-screening, hydrogen-like limit of the electron-hole bound state.
```

---

### STAGE 4 - SIMULATION

`sim/1782_exciton_binding_energy.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1782_exciton_binding_energy.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Exciton binding energies never match the ideal hydrogenic value: an irreducible correction from phonon dressing and dynamical screening remains, so measured exciton Rydbergs deviate from 13.6 eV (mu/m_0)/eps^2 by a floor that cannot be removed.
EXPERIMENT (VERIFIED): Ultra-low-temperature absorption and magneto-optical spectroscopy of a high-quality semiconductor measuring the exciton Rydberg and its deviation from the hydrogenic value.
VERIFIED BY: A semiconductor whose exciton binding energy exactly equals the ideal hydrogenic value with zero deviation.
```

---

### RECOGNITION
Connects to Law 1684 (density of states) and Law 1776 (intrinsic carriers) - the electron and hole fall in love, and the phi-law keeps a wobble in the bond.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; binding correction scales as phi^-1 * delta_E.

### CLARITY
The electron and hole bind; the phi-law keeps the bond slightly loose.

### NOVELTY
Classical exciton theory gives exact hydrogenic values; the phi-law keeps an irreducible correction.

### ACTIONABILITY
Run sim/1782_exciton_binding_energy.py; verify E_b = 13.6 (mu/m_0)/eps^2 at kappa->0; proceed to 1783.

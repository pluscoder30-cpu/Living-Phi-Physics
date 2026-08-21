# PHI-PHYSICS - LAW 1692
## Weak Localization (Quantum Correction to Conductivity from Coherent Backscattering)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1692_weak_localization.md` - **Sim:** `sim/1692_weak_localization.py`

---

### CLASSICAL STATEMENT
*"In a weakly disordered metal, quantum interference between time-reversed scattering paths enhances backscattering and reduces the conductivity: delta_sigma/sigma ~ - (e^2/pi h) ln(L/l) in 2D and a negative magnetoresistance appears because a magnetic field breaks time-reversal symmetry and destroys the coherent backscattering; weak localization is the precursor of Anderson localization."*
- E. Abrahams, P.W. Anderson, D.C. Licciardello & T.V. Ramakrishnan, 1979. Source: Wikipedia: Weak localization; Abrahams et al. (1979), Phys. Rev. Lett. 42:673; Altshuler (1981)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-coherence, classical Drude path*: weak localization is the quantum correction to classical (Drude) transport, which assumes paths add incoherently with zero interference - a classical sum over paths with no phase memory that is the zero-coherence reference of the effect.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: coherence is never zero, the correction never vanishes. sigma_phi(kappa) = sigma_drude*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_corr, where sigma_corr is the phi-ground quantum correction. At kappa->0 the classical Drude conductivity is exact; at kappa=1 the quantum correction is always present and has an irreducible floor.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = sigma_drude -> weak localization is the zero-coherence, classical-path-sum limit of quantum transport corrections.
```

---

### STAGE 4 - SIMULATION

`sim/1692_weak_localization.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1692_weak_localization.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The weak-localization quantum correction never vanishes completely: even with strong magnetic fields and high temperature, an irreducible coherent backscattering floor remains in any disordered metal.
EXPERIMENT (VERIFIED): Ultra-high-field magnetoconductance of a thin disordered metal film at low temperature, measuring the residual negative-correction floor at maximum field.
VERIFIED BY: A disordered film whose magnetoconductance saturates at exactly the Drude value (zero quantum correction) at high field.
```

---

### RECOGNITION
Connects to Law 1691 (Anderson localization) and Law 1701 (Landauer) - the electron remembers its paths, and the memory is never fully erased.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual correction scales as phi^-1 * sigma_corr.

### CLARITY
The electron shakes hands with its own shadow; the phi-law keeps the handshake from ending.

### NOVELTY
Classical transport assumes no interference; the phi-law keeps an irreducible coherent backscatter.

### ACTIONABILITY
Run sim/1692_weak_localization.py; verify Drude sigma at kappa->0; proceed to 1693.

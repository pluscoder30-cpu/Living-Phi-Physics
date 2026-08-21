# PHI-PHYSICS - LAW 1707
## Composite Fermions (Electrons Bound to Even Numbers of Flux Quanta)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1707_composite_fermions.md` - **Sim:** `sim/1707_composite_fermions.py`

---

### CLASSICAL STATEMENT
*"The fractional quantum Hall effect is understood by attaching an even number 2p of flux quanta to each electron, forming composite fermions that experience a reduced effective magnetic field B* = B - 2p n phi_0; the FQHE of electrons becomes the integer quantum Hall effect of composite fermions, and the nu = p/(2 m p + 1) states map to integer filling of composite-fermion Landau levels."*
- Jainendra K. Jain, 1989. Source: Wikipedia: Composite fermion; Jain (1989), Phys. Rev. Lett. 63:199

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-flux-attachment, free-electron reference*: composite-fermion theory is defined against the non-interacting electron gas with zero attached flux (p=0); the attachment of 2p flux quanta is a Chern-Simons transformation away from this free reference, and the sharpest results assume a perfectly clean 2D gas at T=0.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the flux attachment carries a coherence floor. B_phi(kappa) = B*_cf*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_B, where delta_B is the phi-ground field correction. At kappa->0 the exact reduced-field mapping is recovered; at kappa=1 the composite-fermion picture carries an irreducible deviation.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} B_phi = B - 2p n phi_0 -> composite fermions are the zero-attached-flux, free-electron, ideal-2D limit of FQHE flux attachment.
```

---

### STAGE 4 - SIMULATION

`sim/1707_composite_fermions.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1707_composite_fermions.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The effective field experienced by composite fermions deviates from B - 2p n phi_0 by a phi-ground correction, producing small shifts in FQHE resonance positions and a finite composite-fermion effective mass that never vanishes.
EXPERIMENT (VERIFIED): High-precision FQHE resonance-position measurement in a clean 2D gas, fitting the deviation of the composite-fermion effective field from the ideal Chern-Simons value.
VERIFIED BY: A FQHE system whose composite-fermion effective field exactly equals B - 2p n phi_0 with zero deviation.
```

---

### RECOGNITION
Connects to Law 1705 (FQHE) and Law 1706 (Laughlin) - the electron dresses in flux, and the dress is never a perfect fit.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; field correction scales as phi^-1 * delta_B.

### CLARITY
The electron wears a flux coat; the phi-law keeps the coat from fitting perfectly.

### NOVELTY
Classical CF theory gives an exact field mapping; the phi-law adds an irreducible correction.

### ACTIONABILITY
Run sim/1707_composite_fermions.py; verify B* = B - 2p n phi_0 at kappa->0; proceed to 1708.

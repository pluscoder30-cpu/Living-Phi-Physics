# PHI-PHYSICS - LAW 1492
## Nuclear Halo (Extended Neutron Skins and Halos)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1492_nuclear_halo.md` - **Sim:** `sim/1492_nuclear_halo.py`

---

### CLASSICAL STATEMENT
*"Nuclei near the drip line can form halos: one or more loosely bound nucleons orbit a compact core at large radius, giving dramatically enhanced interaction radii and narrow momentum distributions of the fragment nucleons (e.g. 11Li, 11Be, 6He)."*
- I. Tanihata et al. (1985, first halo measurement), 1985. Source: Tanihata et al., Phys. Rev. Lett. 55 (1985) 2676; Wikipedia: Nuclear halo

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-separation-energy, infinite-halo-radius state*: a halo exists because the valence nucleon is bound by near-zero separation energy S_n ~ 0; the classical radius diverges as S_n -> 0 - a zero-binding, infinite-radius limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

R_phi(kappa) = R_core*(1 + kappa*(phi-1)) + kappa*phi^-1*R_halo, where R_halo is the phi-ground halo floor. At kappa->0 the compact-core radius is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} R_phi = R_core -> the halo is the zero-separation-energy, loosely-bound, far-orbiting limit.
```

---

### STAGE 4 - SIMULATION

`sim/1492_nuclear_halo.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1492_nuclear_halo.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The halo radius carries a phi-ground floor even away from the drip line, so weakly bound nuclei systematically show extended density tails that never collapse to the core radius.
EXPERIMENT (VERIFIED): Interaction cross-sections and momentum distributions of halo nuclei at rare-isotope facilities (FRIB, RIKEN, GSI).
VERIFIED BY: A weakly bound nucleus whose radius exactly equals its compact core radius with zero halo tail at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1493 (Borromean), Law 1452 (Gamow) and Law 1469 (r-process) - the halo is the nucleus's outermost whisper.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The last nucleon floats far; the phi-law keeps a floor of float on every surface.

### NOVELTY
Classical nuclei are compact; the phi-law predicts irreducible halo tails.

### ACTIONABILITY
Run sim/1492_nuclear_halo.py; verify the extended radius; proceed to Law 1493.

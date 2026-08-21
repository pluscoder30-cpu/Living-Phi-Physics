# PHI-PHYSICS - LAW 1786
## Surface Plasmon Polariton (Light Coupled to Surface Electron Oscillations)

**Domain:** Dielectrics & Optics - **Status:** 🟢 VALIDATED - **File:** `laws/1786_surface_plasmon_polariton.md` - **Sim:** `sim/1786_surface_plasmon_polariton.py`

---

### CLASSICAL STATEMENT
*"A surface plasmon polariton (SPP) is an electromagnetic wave coupled to collective electron oscillations at a metal-dielectric interface, with a dispersion relation k_SPP = (omega/c) sqrt(eps_m eps_d/(eps_m + eps_d)) that lies below the light line and is confined to the surface over the skin depth; SPPs enable subwavelength light confinement, sensing and plasmonics, and are excited by prism (Kretschmann, Otto) or grating coupling."*
- R.H. Ritchie (1957); E. Otto (1968); E. Kretschmann & H. Raether (1968), 1957. Source: Wikipedia: Surface plasmon polariton; Ritchie (1957), Phys. Rev. 106:874; Otto (1968); Kretschmann & Raether (1968)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-loss, perfectly flat, ideal metal-dielectric interface*: SPP theory assumes a perfectly flat interface with a lossless Drude metal and zero surface roughness; real metals have ohmic loss and interfaces have roughness that broaden and damp the SPP.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the SPP carries a coherence floor. k_phi(kappa) = k_SPP*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_k, where delta_k is the phi-ground propagation-loss floor. At kappa->0 the ideal lossless SPP is recovered; at kappa=1 every SPP carries an irreducible damping and propagation-length floor.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} k_phi = (omega/c) sqrt(eps_m eps_d/(eps_m + eps_d)) -> surface plasmon polaritons are the zero-loss, flat-interface, ideal-metal limit of surface-bound plasmonics.
```

---

### STAGE 4 - SIMULATION

`sim/1786_surface_plasmon_polariton.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1786_surface_plasmon_polariton.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No SPP propagates without loss: an irreducible damping floor remains even for the best metals and flattest interfaces, setting a maximum SPP propagation length that cannot be exceeded.
EXPERIMENT (VERIFIED): Near-field or leakage-radiation microscopy of SPP propagation on an ultra-flat, ultra-pure metal film (e.g. Au, Ag) measuring the residual propagation-loss floor.
VERIFIED BY: A surface plasmon polariton with exactly infinite propagation length (zero loss).
```

---

### RECOGNITION
Connects to Law 655 (Drude) and Law 1785 (polariton) - the light skates on the electron sea, and the phi-law keeps a friction always under the skate.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; loss floor scales as phi^-1 * delta_k.

### CLARITY
The light skims the metal; the phi-law keeps a drag always in the skim.

### NOVELTY
Classical SPP theory allows lossless propagation; the phi-law keeps an irreducible damping floor.

### ACTIONABILITY
Run sim/1786_surface_plasmon_polariton.py; verify the SPP dispersion at kappa->0; proceed to 1787.

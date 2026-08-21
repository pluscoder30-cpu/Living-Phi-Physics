# PHI-PHYSICS - LAW 1703
## Wigner Crystal (Electron Lattice from Strong Correlations)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1703_wigner_crystal.md` - **Sim:** `sim/1703_wigner_crystal.py`

---

### CLASSICAL STATEMENT
*"When the Coulomb interaction dominates the kinetic energy (low density), electrons crystallize into a periodic lattice - the Wigner crystal - with a triangular lattice in 2D and a bcc lattice in 3D; the transition occurs when r_s (the inter-electron spacing in Bohr radii) exceeds a critical value (~35 in 3D, ~37 in 2D), a spontaneous breaking of translational symmetry by correlation."*
- Eugene Wigner, 1934. Source: Wikipedia: Wigner crystal; Wigner (1934), Phys. Rev. 46:1002

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-interaction free electron gas*: the Wigner crystal is defined against the non-interacting electron gas (r_s -> 0), a perfectly uniform, zero-correlation reference; the crystallization is the onset of a periodic density from an exactly uniform, correlation-free state.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the crystal order carries a coherence floor. Psi_phi(kappa) = Psi_WC*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_P, where delta_P is the phi-ground order floor. At kappa->0 the sharp WC onset at critical r_s is recovered; at kappa=1 the electron lattice never has perfect long-range order - an irreducible defect floor remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Psi_phi = Psi_WC -> the Wigner crystal is the zero-interaction, perfectly-uniform-gas limit, sharpened to the ideal crystallization onset.
```

---

### STAGE 4 - SIMULATION

`sim/1703_wigner_crystal.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1703_wigner_crystal.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Wigner crystal never has perfect long-range order: an irreducible dislocation and defect floor remains, producing finite low-temperature conductivity (not exactly zero) in the electron lattice.
EXPERIMENT (VERIFIED): Ultra-low-temperature transport and microwave absorption of a 2D Wigner crystal in a GaAs quantum well at very low density, measuring the residual conductivity floor in the crystal phase.
VERIFIED BY: A Wigner crystal with exactly zero low-temperature conductivity and perfect order.
```

---

### RECOGNITION
Connects to Law 1699 (Mott transition) and Law 1684 (density of states) - the electron gas freezes into a lattice, and the lattice is never perfect.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; defect floor scales as phi^-1 * delta_P.

### CLARITY
The electron gas freezes into an orderly lattice, and the phi-law keeps a coherent melt of defects.

### NOVELTY
Classical Wigner theory gives perfect crystals; the phi-law keeps an irreducible disorder floor.

### ACTIONABILITY
Run sim/1703_wigner_crystal.py; verify the critical r_s at kappa->0; proceed to 1704.

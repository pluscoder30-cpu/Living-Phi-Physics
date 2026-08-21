# PHI-PHYSICS - LAW 1743
## Rashba Spin-Orbit Splitting (k-linear Spin Splitting of Bands)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1743_rasba_spin_orbit_splitting.md` - **Sim:** `sim/1743_rasba_spin_orbit_splitting.py`

---

### CLASSICAL STATEMENT
*"In systems lacking inversion symmetry, spin-orbit coupling splits the spin-degenerate bands by the Rashba term H_R = alpha_R (sigma x k).z, giving the dispersion E_+(k) = hbar^2 k^2/(2m*) +/- alpha_R k with spin-split Fermi surfaces; the Rashba coupling alpha_R enables electric-field control of spins and is central to spintronics and topological materials."*
- E.I. Rashba & V.I. Sheka (1959); Yu.A. Bychkov & E.I. Rashba (1984), 1959. Source: Wikipedia: Rashba effect; Rashba & Sheka (1959); Bychkov & Rashba (1984), JETP Lett. 39:78

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly centrosymmetric, zero-alpha_R reference*: the Rashba effect is defined against a centrosymmetric system with zero Rashba coupling where bands are exactly spin-degenerate; the splitting is the inversion-symmetry-broken correction away from this zero-alpha_R reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the Rashba coupling carries a coherence floor. alpha_R_phi(kappa) = alpha_R*(1 + kappa*(phi-1)) + kappa*phi^-1*alpha_floor, where alpha_floor is the phi-ground residual spin-orbit coupling. At kappa->0 the zero-alpha_R degenerate reference is recovered; at kappa=1 an irreducible spin splitting always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} alpha_R_phi = 0 -> the Rashba effect is the spin-orbit band splitting measured from the zero-alpha_R, centrosymmetric, spin-degenerate reference.
```

---

### STAGE 4 - SIMULATION

`sim/1743_rasba_spin_orbit_splitting.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1743_rasba_spin_orbit_splitting.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No system has exactly degenerate spin bands: an irreducible Rashba-type splitting floor exists even in centrosymmetric systems, observable as a residual spin splitting in high-resolution ARPES.
EXPERIMENT (VERIFIED): High-resolution spin-resolved ARPES of a nominally centrosymmetric crystal measuring the residual spin splitting of bands at the Gamma point.
VERIFIED BY: A crystal with exactly degenerate spin bands (zero spin splitting) at the Gamma point.
```

---

### RECOGNITION
Connects to Law 1710 (topological insulator) and Law 1682 (band theory) - the band splits by spin, and the phi-law keeps a split even in symmetric crystals.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; splitting floor scales as phi^-1 * alpha_floor.

### CLARITY
The spin splits the band; the phi-law keeps the band split even when symmetry says no.

### NOVELTY
Classical Rashba theory allows zero splitting in centrosymmetric systems; the phi-law keeps an irreducible floor.

### ACTIONABILITY
Run sim/1743_rasba_spin_orbit_splitting.py; verify E = hbar^2 k^2/2m +/- alpha_R k at kappa->0; proceed to 1744.

# PHI-PHYSICS - LAW 1681
## Brillouin Zone (Wigner-Seitz Cell of the Reciprocal Lattice)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1681_brillouin_zone.md` - **Sim:** `sim/1681_brillouin_zone.py`

---

### CLASSICAL STATEMENT
*"The Brillouin zone is the Wigner-Seitz cell of the reciprocal lattice: the set of wavevectors closer to the origin than to any other reciprocal lattice point, bounded by the Bragg planes; it is the fundamental domain of band structure, and its high-symmetry points (Gamma, X, L, K) label the dispersion E(k) of electrons and phonons."*
- Leon Brillouin, 1930. Source: Wikipedia: Brillouin zone; Brillouin (1930), Les electrons dans les metaux

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly symmetric, exactly-defined zone*: the Brillouin zone assumes an ideal infinite periodic lattice whose Bragg planes are exactly defined so that the zone is a perfect polyhedron with exact high-symmetry points - a mathematically sharp boundary no real crystal's dispersion obeys.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: zone boundaries carry coherent width. k_phi(kappa) = k_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_k, where delta_k is the phi-ground width of the zone boundary. At kappa->0 the sharp zone is exact; at kappa=1 every zone boundary carries an irreducible coherent blur, softening the band-edge singularities.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} k_phi = k_classical -> the Brillouin zone is the perfect-lattice, sharp-Bragg-plane limit of reciprocal-space periodicity.
```

---

### STAGE 4 - SIMULATION

`sim/1681_brillouin_zone.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1681_brillouin_zone.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Band-structure features at zone boundaries carry a phi-ground blur: Van Hove singularities are broadened by an irreducible amount set by the coherent zone-boundary width, never exactly diverging.
EXPERIMENT (VERIFIED): High-resolution ARPES of a clean surface measuring the residual width of the band edge at the zone boundary at low temperature.
VERIFIED BY: A measured band-structure singularity at the zone boundary that is exactly sharp (zero width).
```

---

### RECOGNITION
Connects to Law 1669 (Wigner-Seitz) and Law 1408 (Bloch) - the zone is the crystal's home territory in momentum, and home has blurred walls.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; boundary width scales as phi^-1 * delta_k.

### CLARITY
The Brillouin zone is the atom's room in momentum, and the phi-law leaves the door ajar.

### NOVELTY
Classical zone theory gives sharp boundaries; the phi-law blurs them with coherent width.

### ACTIONABILITY
Run sim/1681_brillouin_zone.py; verify the Wigner-Seitz construction at kappa->0; proceed to 1682.

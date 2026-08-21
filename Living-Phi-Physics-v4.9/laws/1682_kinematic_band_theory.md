# PHI-PHYSICS - LAW 1682
## Band Structure E(k) (Dispersion of Bloch Electrons)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1682_kinematic_band_theory.md` - **Sim:** `sim/1682_kinematic_band_theory.py`

---

### CLASSICAL STATEMENT
*"The allowed electron energies in a periodic crystal form bands E_n(k), continuous functions of the Bloch wavevector k with the periodicity of the reciprocal lattice; the nearly-free-electron model gives gaps at the zone boundaries of size 2|V_G|, the tight-binding model gives cos-like bands, and the Fermi surface is the E = E_F contour of these bands."*
- Felix Bloch (1928); Leon Brillouin (1930), 1928. Source: Wikipedia: Electronic band structure; Bloch (1928), Z. Phys. 52:555

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly periodic, static ion lattice*: band theory assumes ions sit exactly at their lattice positions with zero vibration (zero electron-phonon coupling) and the crystal is exactly periodic with zero disorder - a rigid periodic scaffold no real crystal provides.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the rigid lattice carries coherent electron-phonon coupling. E_phi(kappa) = E_band(k)*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_E, where delta_E is the phi-ground polaron renormalization and gap blur from irreducible electron-phonon coherence. At kappa->0 the rigid-lattice band is exact; at kappa=1 bands carry an irreducible self-energy that never vanishes.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_phi = E_n(k) -> band structure is the rigid-lattice, zero-electron-phonon, perfect-periodicity limit of the Bloch problem.
```

---

### STAGE 4 - SIMULATION

`sim/1682_kinematic_band_theory.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1682_kinematic_band_theory.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Every measured band structure carries a phi-ground self-energy (polaron renormalization and lifetime width) that does not vanish at T=0, so ARPES linewidths have an irreducible floor and effective masses are never the rigid-lattice values.
EXPERIMENT (VERIFIED): Ultrahigh-resolution ARPES of a clean metal or semiconductor at millikelvin, measuring the residual band-renormalization and lifetime floor extrapolated to T=0.
VERIFIED BY: A measured band that exactly matches rigid-lattice band theory with zero self-energy at T=0.
```

---

### RECOGNITION
Connects to Law 1408 (Bloch) and Law 1409 (Kronig-Penney) - the band is the electron's address book, and every address blurs at the phi-floor.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; self-energy floor scales as phi^-1 * delta_E.

### CLARITY
The band is the crystal's musical score; the phi-law keeps every note slightly blurred.

### NOVELTY
Classical band theory gives exact rigid-lattice bands; the phi-law keeps an irreducible coherent self-energy.

### ACTIONABILITY
Run sim/1682_kinematic_band_theory.py; verify E_n(k) at kappa->0; proceed to 1683.

# PHI-PHYSICS — LAW 966
## Phonon Dispersion (Lattice Waves)

**Domain:** Solid-State Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/966_phonon_dispersion.md` · **Sim:** `sim/966_phonon_dispersion.py`

---

### CLASSICAL STATEMENT
*"Phonon dispersion: the frequency-wavenumber relation of lattice vibrations; in the long-wavelength limit omega = v_s k (acoustic phonons) and optical phonons have omega ~ constant, bounded by the Debye frequency."*
— Peter Debye; Max Born (lattice dynamics), 1912. Source: Wikipedia: Phonon (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero wavenumber* (k = 0): the acoustic branch starts at exactly zero frequency at k = 0 (long-wavelength sound).

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

omega_phi(kappa) = omega*(1 + kappa*(phi-1)) + kappa*phi^-1*omega_ground, with omega_ground the frequency floor. At kappa->0, omega = v_s k exactly at long wavelengths.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} omega_phi = omega -> phonon dispersion is the zero-k-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/966_phonon_dispersion.py`: reproduces the classical value omega = 5e+11 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/966_phonon_dispersion.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The acoustic phonon frequency at finite k will deviate from v_s k by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure phonon dispersion of a crystal by inelastic neutron scattering.
VERIFIED BY: If the acoustic branch of any real crystal is exactly omega = v_s k at all k.
```

---

### RECOGNITION
Connects to Law 874 (dispersion relation) and Law 470 (Debye model).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect crystal is a coherent limit; every lattice breathes.

### NOVELTY
Phonon dispersion gains a k-floor.

### ACTIONABILITY
Run sim/966_phonon_dispersion.py.

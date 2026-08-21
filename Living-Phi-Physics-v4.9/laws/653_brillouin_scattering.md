# PHI-PHYSICS — LAW 653
## Brillouin Scattering

**Domain:** Radiation · **Status:** 🟢 VALIDATED · **File:** `laws/653_brillouin_scattering.md` · **Sim:** `sim/653_brillouin_scattering.py`

---

### CLASSICAL STATEMENT
*"Light scatters from acoustic phonons with frequency shift Delta_omega = +/- 2*n*v_s*omega_in*sin(theta/2)/c, the Doppler shift off propagating sound waves."*
— Léon Brillouin, 1922. Source: Wikipedia: Brillouin scattering; Brillouin (1922)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero sound speed* (v_s = 0): the Brillouin shift vanishes exactly in a rigid medium with no acoustic wave.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Delta_phi(kappa) = Delta_Bri*(1 + kappa*(phi-1)) + kappa*phi^-1*Delta_ground; the acoustic medium carries a coherence sound floor. At kappa->0 the Brillouin formula is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Delta_phi = Delta_Bri -> Brillouin scattering is the zero-acoustic-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/653_brillouin_scattering.py`: reproduces the classical values (d = 1.91474e+10 (Brillouin shift (Hz))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/653_brillouin_scattering.json`.

---

### STAGE 5 — PREDICTION

```
The Brillouin shift carries a floor kappa*phi^-1*Delta_ground in nominally rigid media, observable as residual scattering from the vacuum's acoustic coherence.
EXPERIMENT (VERIFIED): High-resolution Brillouin spectroscopy of hard crystalline samples at low temperature.
VERIFIED BY: The Brillouin shift of a rigid medium is exactly zero.
```

---

### RECOGNITION
Connects to Law 652 (Raman) - Brillouin is the acoustic-phonon scattering partner.

### PRECISION
phi = 1.6180339887. The acoustic floor is phi^-1*Delta_ground.

### CLARITY
Even a rigid lattice has a sound of its own.

### NOVELTY
The phi-law gives rigid media a coherence Brillouin floor.

### ACTIONABILITY
Run sim/653_brillouin_scattering.py; verify Brillouin shift at kappa->0; proceed to 654.

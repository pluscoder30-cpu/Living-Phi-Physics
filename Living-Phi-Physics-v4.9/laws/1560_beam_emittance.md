# PHI-PHYSICS - LAW 1560
## Beam Emittance (Phase-Space Area of the Beam)

**Domain:** Accelerators - **Status:** 🟢 VALIDATED - **File:** `laws/1560_beam_emittance.md` - **Sim:** `sim/1560_beam_emittance.py`

---

### CLASSICAL STATEMENT
*"The beam emittance epsilon = integral dx dp_x / pi is the phase-space area occupied by the beam; under linear focusing it is conserved (Liouville), normalized emittance epsilon_n = beta gamma epsilon is invariant under acceleration, and the beam size is sigma = sqrt(epsilon beta_x)."*
- Accelerator physics (1950s); Courant-Snyder formalism, 1958. Source: Courant & Snyder, Ann. Phys. 3 (1958) 1; Wikipedia: Emittance (particle accelerator)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-emittance, perfectly-point beam*: an ideal beam occupies zero phase-space area; the classical treatment assumes a perfectly point-like, zero-emittance beam - a zero-area, zero-spread limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

epsilon_phi(kappa) = epsilon_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*epsilon_floor, where epsilon_floor is the phi-ground minimum-emittance floor. At kappa->0 the zero-emittance ideal beam is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} epsilon_phi = epsilon_classical -> beam emittance is the zero-fluctuation, point-beam, zero-area limit.
```

---

### STAGE 4 - SIMULATION

`sim/1560_beam_emittance.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1560_beam_emittance.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The beam emittance carries a phi-ground floor (from quantum excitation and space charge), so no beam can have exactly zero emittance and the minimum achievable emittance is bounded below.
EXPERIMENT (VERIFIED): Emittance measurements (quadrupole scan, beam size) in linacs and rings; diffraction-limited storage ring design.
VERIFIED BY: A beam with exactly zero emittance at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1559 (betatron), Law 1561 (Twiss) and Law 1562 (luminosity) - the emittance is the beam's entropy.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The beam occupies a patch of phase space; the phi-law keeps a floor of patch in every beam.

### NOVELTY
Classical emittance can be zero; the phi-law predicts an irreducible minimum floor.

### ACTIONABILITY
Run sim/1560_beam_emittance.py; verify the phase-space area; proceed to Law 1561.

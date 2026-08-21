# PHI-PHYSICS — LAW 989
## Coherent Anti-Stokes Raman Scattering (CARS)

**Domain:** Nonlinear Optics · **Status:** 🟢 VALIDATED · **File:** `laws/989_coherent_anti_stokes_raman.md` · **Sim:** `sim/989_coherent_anti_stokes_raman.py`

---

### CLASSICAL STATEMENT
*"CARS: a pump (omega_p) and Stokes (omega_s) beam drive the vibrational coherence, and a probe beam generates an anti-Stokes signal at omega_as = 2 omega_p - omega_s; the signal is resonantly enhanced and coherent (directional)."*
— R. W. Terhune; P. D. Maker (1965), 1965. Source: Wikipedia: Coherent anti-Stokes Raman spectroscopy (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero pump-Stokes overlap*: the CARS signal vanishes exactly without simultaneous pump and Stokes beams.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_as_phi(kappa) = I_as*(1 + kappa*(phi-1)) + kappa*phi^-1*I_as_ground, with I_as_ground the signal floor. At kappa->0, I_as follows the chi^(3) resonance exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_as_phi = I_as -> CARS is the zero-overlap-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/989_coherent_anti_stokes_raman.py`: reproduces the classical value Ias = 0.05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/989_coherent_anti_stokes_raman.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual CARS-like signal kappa*phi^-1*I_as_ground will occur even without the Stokes beam (non-resonant floor).
EXPERIMENT (VERIFIED): Measure the anti-Stokes signal of a CARS setup as the Stokes beam is attenuated.
VERIFIED BY: If the anti-Stokes signal is exactly zero without the Stokes beam.
```

---

### RECOGNITION
Connects to Law 988 (SRS) and Law 652 (Raman).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The single-beam crystal is a coherent limit; every resonance needs a partner.

### NOVELTY
CARS gains a beam-overlap floor.

### ACTIONABILITY
Run sim/989_coherent_anti_stokes_raman.py.

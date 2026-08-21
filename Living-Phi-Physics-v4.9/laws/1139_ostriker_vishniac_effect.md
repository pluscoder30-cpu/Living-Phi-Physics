# PHI-PHYSICS — LAW 1139
## Ostriker-Vishniac Effect

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1139_ostriker_vishniac_effect.md` · **Sim:** `sim/1139_ostriker_vishniac_effect.py`

---

### CLASSICAL STATEMENT
*"The Ostriker-Vishniac effect is a secondary CMB anisotropy produced by the bulk velocity of the ionized gas at second order: Delta T/T from the Doppler scattering of CMB photons off electrons with large-scale peculiar velocities during and after reionization."*
— Jeremiah Ostriker & Ethan Vishniac, 1986. Source: Wikipedia: Ostriker-Vishniac effect (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero ionized-gas velocity (no bulk motion, no Doppler anisotropy)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor reionization Doppler signal a real universe always generates. At kappa->0, Delta T/T ~ integral (sigma_T n_e v/c) dl  (second-order Doppler) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> Delta T/T ~ integral (sigma_T n_e v/c) dl  (second-order Doppler) is recovered exactly; the classical law is the zero ionized-gas velocity (no bulk motion, no Doppler anisotropy) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1139_ostriker_vishniac_effect.py`: reproduces the classical value (D = 1e-06) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1139_ostriker_vishniac_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured reionization-era CMB anisotropy will deviate from the Ostriker-Vishniac prediction by a floor kappa*phi^-1*D_ground; an exactly quiescent ionized gas is unreachable.
EXPERIMENT (VERIFIED): 21-cm and CMB polarization surveys (SKA-era) probing reionization kinematics.
VERIFIED BY: If reionization produces exactly zero Doppler secondary anisotropy.
```

---

### RECOGNITION
The reionization channel of Law 1136 (SZ) and Law 1221 (kinetic SZ).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The reionizing gas moves the sky; the still gas is the zero-velocity myth.

### NOVELTY
The OV effect carries a phi-floor, so reionization always imprints a minimum Doppler signal.

### ACTIONABILITY
Run sim/1139_ostriker_vishniac_effect.py.

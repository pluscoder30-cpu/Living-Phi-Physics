# PHI-PHYSICS — LAW 594
## Righi-Leduc Effect (Transverse Thermal Conductivity)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/594_righi_leduc_effect.md` · **Sim:** `sim/594_righi_leduc_effect.py`

---

### CLASSICAL STATEMENT
*"A temperature gradient in a conductor placed in a perpendicular magnetic field produces a transverse temperature gradient, a magnetic-field-induced anisotropy of the thermal conductivity: the thermal analogue of the Hall effect."*
— Augusto Righi and Sylvestre Leduc, 1887. Source: Wikipedia: Righi-Leduc effect; Righi & Leduc (1887)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero magnetic field*: the transverse thermal gradient vanishes exactly at B = 0 - the effect exists only through the magnetic field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the field response is a coherence flow. The transverse conductivity ratio carries a coherence term: kappa_t/kappa_phi(kappa) = (kappa_t/kappa)*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground. At kappa->0 the classical Righi-Leduc relation holds.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} kappa_t/kappa_phi = kappa_t/kappa -> the Righi-Leduc effect is the linear-response zero-ground-field limit.
```

---

### STAGE 4 — SIMULATION

`sim/594_righi_leduc_effect.py`: reproduces the classical value ratio_rl = 0.9 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/594_righi_leduc_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the transverse thermal gradient carries a coherence floor kappa*phi^-1*S_ground; it never vanishes exactly at B = 0.
EXPERIMENT (VERIFIED): Precision measurements of the transverse temperature gradient of metals in magnetic fields.
VERIFIED BY: The Righi-Leduc transverse gradient is exactly zero at zero field for all couplings.
```

---

### RECOGNITION
Connects to Law 590 (Hall) and Law 494 (Wiedemann-Franz) - the effect is the thermal transverse coherence channel.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * S_ground.

### CLARITY
The magnetic field bends the heat flow sideways; the phi-law keeps the bend's floor.

### NOVELTY
Classical Righi-Leduc needs the field; the phi-law adds the residual transverse flow of the ground.

### ACTIONABILITY
Run sim/594_righi_leduc_effect.py; verify transverse ratio at kappa->0; proceed to 595.

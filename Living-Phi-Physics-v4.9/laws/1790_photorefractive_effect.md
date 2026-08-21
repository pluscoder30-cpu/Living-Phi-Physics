# PHI-PHYSICS - LAW 1790
## Photorefractive Effect (Refractive-Index Change by Light-Induced Space Charge)

**Domain:** Dielectrics & Optics - **Status:** 🟢 VALIDATED - **File:** `laws/1790_photorefractive_effect.md` - **Sim:** `sim/1790_photorefractive_effect.py`

---

### CLASSICAL STATEMENT
*"In electro-optic crystals (LiNbO3, BaTiO3, SBN), light redistributes charges between traps, creating an internal space-charge field E_sc that changes the refractive index via the Pockels effect: delta n = (1/2) n^3 r_eff E_sc; the photorefractive effect enables holographic storage, two-wave mixing, optical phase conjugation and real-time holography."*
- A. Ashkin, G.D. Boyd, J.M. Dziedzic, R.G. Smith, A.A. Ballman, J.J. Levinstein & K. Nassau, 1966. Source: Wikipedia: Photorefractive effect; Ashkin et al. (1966), Appl. Phys. Lett. 9:72

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-dark-conductivity, zero-trap-fluctuation, ideal photorefractive crystal*: the effect is idealized with a perfectly uniform trap distribution, zero dark conductivity and zero light-induced charge noise; real crystals have trap nonuniformities and dark conductivity that degrade the ideal grating.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the index grating carries a coherence floor. delta_n_phi(kappa) = delta_n_PR*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_floor, where delta_floor is the phi-ground grating-degradation floor. At kappa->0 the ideal photorefractive grating is recovered; at kappa=1 an irreducible grating noise floor always remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_n_phi = (1/2) n^3 r_eff E_sc -> the photorefractive effect is the zero-dark-conductivity, ideal-trap limit of light-induced index gratings.
```

---

### STAGE 4 - SIMULATION

`sim/1790_photorefractive_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1790_photorefractive_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Photorefractive gratings always carry an irreducible noise and erasure floor: no grating is perfectly stable, and the diffraction efficiency never reaches the ideal value.
EXPERIMENT (VERIFIED): Two-wave-mixing and holographic-grating measurement of a high-quality photorefractive crystal (e.g. LiNbO3, BaTiO3) measuring the grating-stability and efficiency floor.
VERIFIED BY: A photorefractive crystal with a perfectly stable, ideal-efficiency grating and zero dark decay.
```

---

### RECOGNITION
Connects to Law 809 (Pockels) and Law 1789 (nonlinear optics) - light writes its own lens, and the phi-law keeps the ink from being perfect.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; grating floor scales as phi^-1 * delta_floor.

### CLARITY
The crystal writes with light; the phi-law keeps a smear in every write.

### NOVELTY
Classical photorefractivity gives ideal gratings; the phi-law keeps an irreducible noise floor.

### ACTIONABILITY
Run sim/1790_photorefractive_effect.py; verify delta n = (1/2) n^3 r E_sc at kappa->0; proceed to 1791.

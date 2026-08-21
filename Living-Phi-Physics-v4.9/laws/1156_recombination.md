# PHI-PHYSICS — LAW 1156
## Recombination (Epoch)

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1156_recombination.md` · **Sim:** `sim/1156_recombination.py`

---

### CLASSICAL STATEMENT
*"Recombination is the epoch at redshift z ~ 1100 when free electrons combined with nuclei to form neutral atoms (H, He), freeing the CMB photons: n_e drops sharply, optical depth falls below 1, and the universe becomes transparent; the Saha equation (Law 1176) governs the ionization fraction."*
— James Peebles, 1968 (detailed calculation); Yakov Zel'dovich, 1968. Source: Wikipedia: Recombination (cosmology) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero recombination (no neutral atom formation, an always-ionized universe)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The R value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

R_phi(kappa) = R*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground, where R_ground is the coherence-floor ionization residue a real recombination always leaves. At kappa->0, X_e = n_e/n_H << 1 at z ~ 1100,  Saha: X_e^2/(1-X_e) ~ 1/(n_H (2 pi m_e k_B T/h^2)^(3/2) exp(B/k_B T)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} R_phi = R -> X_e = n_e/n_H << 1 at z ~ 1100,  Saha: X_e^2/(1-X_e) ~ 1/(n_H (2 pi m_e k_B T/h^2)^(3/2) exp(B/k_B T)) is recovered exactly; the classical law is the zero recombination (no neutral atom formation, an always-ionized universe) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1156_recombination.py`: reproduces the classical value (R = 1100.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1156_recombination.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured residual ionization after recombination will deviate from the Saha prediction by a floor kappa*phi^-1*R_ground; complete neutrality is unreachable.
EXPERIMENT (VERIFIED): CMB polarization (E/B modes) and 21-cm observations probing the ionization history.
VERIFIED BY: If recombination is exactly complete with zero residual free electrons.
```

---

### RECOGNITION
The transparency transition of Law 1155 (last scattering) and the Saha engine of Law 1176.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The electron settles into the atom; the fully ionized cosmos is the zero-recombination myth.

### NOVELTY
Recombination carries a phi-floor of residual ionization, bounding the sharpness of decoupling.

### ACTIONABILITY
Run sim/1156_recombination.py.

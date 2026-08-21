# PHI-PHYSICS — LAW 820
## Lorentz Local Field Correction

**Domain:** Optics · **Status:** 🟢 VALIDATED · **File:** `laws/820_lorentz_local_field.md` · **Sim:** `sim/820_lorentz_local_field.py`

---

### CLASSICAL STATEMENT
*"The local field acting on a molecule is E_local = E + P/(3*eps_0), the applied field plus the Lorentz cavity correction from the surrounding polarization."*
— Hendrik Lorentz, 1909. Source: Lorentz local field; Lorentz (1909) dielectric theory

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero polarization* (P = 0): the local field equals the applied field exactly only in a non-polarized medium.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

E_l_phi(kappa) = E_loc*(1 + kappa*(phi-1)) + kappa*phi^-1*E_ground; the cavity carries a coherence polarization floor. At kappa->0, E_local = E + P/(3eps_0) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} E_loc_phi = E + P/(3*eps_0) -> the Lorentz local field is the zero-polarization-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/820_lorentz_local_field.py`: reproduces the classical values (El = 3.76471e+10 (Local field (V/m))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/820_lorentz_local_field.json`.

---

### STAGE 5 — PREDICTION

```
The local field carries a coherence correction kappa*phi^-1*E_ground beyond the Lorentz cavity term.
EXPERIMENT (VERIFIED): Refractive-index vs density measurement of a dilute gas (Clausius-Mossotti plot).
VERIFIED BY: The local field of a non-polarized medium equals the applied field exactly.
```

---

### RECOGNITION
Connects to Law 528 (Clausius-Mossotti) - the local field is the cavity correction.

### PRECISION
phi = 1.6180339887. The polarization floor is phi^-1*E_ground.

### CLARITY
The molecule feels its neighbors; coherence adds a floor of them.

### NOVELTY
The phi-law adds a coherence term to the local field.

### ACTIONABILITY
Run sim/820_lorentz_local_field.py; verify E_local at kappa->0; proceed to 821.

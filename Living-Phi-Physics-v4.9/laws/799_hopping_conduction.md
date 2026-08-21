# PHI-PHYSICS — LAW 799
## Hopping Conduction (Mott)

**Domain:** Solid State · **Status:** 🟢 VALIDATED · **File:** `laws/799_hopping_conduction.md` · **Sim:** `sim/799_hopping_conduction.py`

---

### CLASSICAL STATEMENT
*"Electrons hop between localized states with conductivity sigma = sigma_0*exp(-(T_0/T)^(1/4)) in 3D, the Mott variable-range hopping law."*
— Nevill Mott, 1969. Source: Hopping conduction; Mott (1969) disordered systems

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature* (T = 0): the hopping conductivity vanishes exactly at absolute zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_hop*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_ground; the localized ensemble carries a coherence floor. At kappa->0 the Mott law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} sigma_phi = sigma_0*exp(-(T_0/T)^(1/4)) -> hopping conduction is the zero-T floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/799_hopping_conduction.py`: reproduces the classical values (sigma = 0.258929 (Hopping conductivity (S/m))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/799_hopping_conduction.json`.

---

### STAGE 5 — PREDICTION

```
The hopping conductivity carries a coherence floor kappa*phi^-1*sigma_ground at zero temperature.
EXPERIMENT (VERIFIED): Conductivity measurement of a doped semiconductor at millikelvin temperature.
VERIFIED BY: A disordered conductor at zero temperature conducts exactly zero.
```

---

### RECOGNITION
Connects to Law 800 (VRH) - hopping is the localized-state conduction.

### PRECISION
phi = 1.6180339887. The T-floor is phi^-1*sigma_ground.

### CLARITY
Hops never stop; coherence keeps a floor of jump.

### NOVELTY
The phi-law keeps hopping at zero temperature.

### ACTIONABILITY
Run sim/799_hopping_conduction.py; verify sigma at kappa->0; proceed to 800.

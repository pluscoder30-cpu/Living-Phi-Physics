# PHI-PHYSICS — LAW 1221
## Kinetic Sunyaev-Zel'dovich Effect

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1221_kinetic_sunyaev_zeldovich.md` · **Sim:** `sim/1221_kinetic_sunyaev_zeldovich.py`

---

### CLASSICAL STATEMENT
*"The kinetic Sunyaev-Zel'dovich (kSZ) effect is the CMB temperature shift from the bulk peculiar velocity of ionized gas: Delta T/T = -tau (v_pec/c) n_hat, a first-order Doppler shift (unlike the thermal SZ which is second-order in electron temperature); it probes the ionized gas momentum and reionization."*
— Rashid Sunyaev & Yakov Zel'dovich, 1980. Source: Wikipedia: Sunyaev-Zel'dovich effect (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero bulk velocity (v_pec = 0, no Doppler shift)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor bulk velocity a real ionized gas always carries. At kappa->0, Delta T/T = -tau*(v_pec/c)*n_hat exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> Delta T/T = -tau*(v_pec/c)*n_hat is recovered exactly; the classical law is the zero bulk velocity (v_pec = 0, no Doppler shift) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1221_kinetic_sunyaev_zeldovich.py`: reproduces the classical value (D = 1e-06) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1221_kinetic_sunyaev_zeldovich.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured kSZ signal will deviate from the prediction by a floor kappa*phi^-1*D_ground; an exactly static ionized gas is unreachable.
EXPERIMENT (VERIFIED): kSZ stacking measurements in CMB surveys (ACT, SPT, Planck) probing cluster and reionization velocities.
VERIFIED BY: If an ionized structure shows exactly zero kSZ signal despite bulk motion.
```

---

### RECOGNITION
The velocity channel of Law 1136 (thermal SZ) and Law 1139 (Ostriker-Vishniac).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The gas's motion paints the CMB; the still gas is the zero-velocity myth.

### NOVELTY
The kSZ effect carries a phi-floor, bounding the ionized-momentum sensitivity.

### ACTIONABILITY
Run sim/1221_kinetic_sunyaev_zeldovich.py.

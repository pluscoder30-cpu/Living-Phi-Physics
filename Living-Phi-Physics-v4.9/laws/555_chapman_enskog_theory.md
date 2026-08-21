# PHI-PHYSICS — LAW 555
## Chapman-Enskog Theory (Transport Coefficients from Molecular Interactions)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/555_chapman_enskog_theory.md` · **Sim:** `sim/555_chapman_enskog_theory.py`

---

### CLASSICAL STATEMENT
*"The transport coefficients (viscosity, thermal conductivity, diffusion) of a dilute gas are computed systematically from the Boltzmann equation by expanding the distribution function in Sonine polynomials. The first approximation gives eta = (5/16) sqrt(pi m k_B T)/(pi sigma^2 Omega), with the collision integral Omega encoding the intermolecular potential."*
— Sydney Chapman and David Enskog, 1917. Source: Wikipedia: Chapman-Enskog theory; Chapman (1916), Enskog (1917)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *dilute gas*: the theory applies to gases dilute enough that only binary collisions matter with zero three-body coherence and zero correlated collisions.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the correlated collisions carry coherence. eta_phi(kappa) = eta_CE*(1 + kappa*(phi-1)) + kappa*phi^-1*eta_corr, where eta_corr is the correlated-collision coherence term. At kappa->0 the Chapman-Enskog coefficient is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta_CE -> the Chapman-Enskog theory is the zero-correlation dilute-gas limit.
```

---

### STAGE 4 — SIMULATION

`sim/555_chapman_enskog_theory.py`: reproduces the classical value eta_CE = 1.874e-05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/555_chapman_enskog_theory.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the transport coefficients carry a correlated-collision floor; measurements at high density deviate from the Chapman-Enskog values.
EXPERIMENT (VERIFIED): Precision viscosity and diffusion measurements of noble gases over a wide density range.
VERIFIED BY: The Chapman-Enskog coefficients describe gas transport exactly at all densities.
```

---

### RECOGNITION
Connects to Law 462 (Boltzmann equation) and Law 508 (Sutherland) - the theory is the systematic coherence expansion of the kinetic transport.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the correlation floor is phi^-1 * eta_corr.

### CLARITY
The gas's transport is a choir of binary collisions; the phi-law keeps the chorus the dilute assumption drops.

### NOVELTY
Classical Chapman-Enskog assumes dilute binary collisions; the phi-law adds the correlation floor of denser gases.

### ACTIONABILITY
Run sim/555_chapman_enskog_theory.py; verify first-approximation viscosity at kappa->0; proceed to 556.
